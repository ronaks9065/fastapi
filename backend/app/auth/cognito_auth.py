# mypy: disable-error-code="return-value, no-untyped-def, no-any-return, attr-defined"
# Standard Library imports
import base64
import hashlib
import hmac
import os
from typing import Any, Dict, List

# Third-party imports
import boto3
import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer

os.environ["AWS_ACCESS_KEY_ID"] = "3sllvv4gajsd1ur47bm6hbu3bn"
os.environ["AWS_SECRET_ACCESS_KEY"] = (
    "4tudmms91t1l7t7dgrgoj5kpulb37jlnm2c8h2efkkkqm9k6red"
)


def calculate_secret_hash(client_id: str, client_secret: str, username: str) -> str:
    message = username + client_id
    digest = hmac.new(
        client_secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha256
    ).digest()
    return base64.b64encode(digest).decode("utf-8")


class CognitoAuth:
    def __init__(self) -> None:
        self.region = "eu-central-1"  # e.g., "us-west-2"
        self.user_pool_id = "eu-central-1_z8ZARPcVu"
        self.app_client_id = "3sllvv4gajsd1ur47bm6hbu3bn"
        self.cognito_issuer = (
            f"https://cognito-idp.{self.region}.amazonaws.com/{self.user_pool_id}"
        )
        self.jwks_url = "https://cognito-idp.eu-central-1.amazonaws.com/eu-central-1_z8ZARPcVu/.well-known/jwks.json"

        # self.jwks = requests.get(self.jwks_url, proxies=None).json()
        self.jwks = {
            "keys": [
                {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "KI9NQ6VhFyQTv8lfpEPFJ107IqDPePYlxUnJxFj4MpY=",
                    "kty": "RSA",
                    "n": "zKAsJEpHh52ZAa7AwUBWmMlkirUfAkpMM9GIDb9jRQ4sI0WqjWxWAMvkb6Kuyrda66TwjHC8naSJPEzhKfifmW91gw7caqilKWG35F68UHpsALfCV8uZK5dP6doDJWhPDqjXDh07xiuDbGH0IDBKmrcquFm5Wi1UHl4leB5IAxskQPvivp88heFoFNC1-QVhSa81PBaXhVV4iw7hiC8McluGhYd6-gMB5hqp8aBiFDfQlztcp9iD1aUmHEFvKM1b0qeTCceD7NkHNJw5CjTAEVDMv5z1rqxata6LqcsutWZz0CTtgbA9L46DUo8FnuPIrpQcMtO3YCTCB_ioAaPrKw",
                    "use": "sig",
                },
                {
                    "alg": "RS256",
                    "e": "AQAB",
                    "kid": "9oAyDC7E3abWqCHcqxzdMTV3M2vkV5Klr40T1KmBakQ=",
                    "kty": "RSA",
                    "n": "2zo5wkNXuIWGWFlU-eJYugdyjnOzwNybVsp6R5e4wYAQWxpr0nE8PwayRc2ahF_BXe5boWJmOyJk0p6v5cDrY1a7WNt4vgx_NE1ezL8FA-a-za_dKLhRnpR4ZKulJfkpU5TktcjBvGyFKJHolzNKRxIdvRpGJmepnJhauoOeVf3PX3GHx-hJoSoS_4yVJpVDpNV6TgpqkDPyD8AhERx7jexhvZA7JIR78svcdTMTTWnGKDplXiWJwUckKcFopXdcTwlUAaDy3Dq5FtiuBCz8BFqW-HiZV-92BnaEREH_F-OBPiux8dLc_Yj-VUM5xwYZkDlM_ssIb8h1z4jnZdJ9qQ",
                    "use": "sig",
                },
            ]
        }

        self.client = boto3.client("cognito-idp", region_name=self.region)

    def verify_access_token(self, token: str) -> Dict[str, Any]:
        try:
            headers = jwt.get_unverified_header(token)
            key = next(
                item for item in self.jwks["keys"] if item["kid"] == headers["kid"]
            )
            decoded_token = jwt.decode(
                token,
                jwt.algorithms.RSAAlgorithm.from_jwk(key),
                algorithms=["RS256"],
                audience=self.app_client_id,  # Access Token must match the client_id.
                issuer=self.cognito_issuer,  # Verify the token issuer.
                options={"verify_exp": True},
            )
            return decoded_token
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid access token") from e

    def verify_token(self, token: str) -> Dict[str, Any]:
        try:
            headers = jwt.get_unverified_header(token)
            key = next(
                item for item in self.jwks["keys"] if item["kid"] == headers["kid"]
            )
            decoded_token = jwt.decode(
                token,
                key,
                audience=self.app_client_id,
                issuer=self.cognito_issuer,
                options={"verify_exp": True},
            )
            return decoded_token
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid token") from e

    def role_dependency(
        self, token: str = Security(HTTPBearer()), required_roles: List[str] = []
    ):
        decoded_token = self.verify_access_token(token.credentials)
        user_roles = decoded_token.get("cognito:groups", [])
        if not any(role in user_roles for role in required_roles):
            raise HTTPException(status_code=403, detail="Not enough permissions")
        return decoded_token

    def has_role(self, required_roles: List[str]):
        """
        Dependency function to check if the token's user has any of the required roles.
        This can be used directly as a dependency.
        """

        def role_dependency(
            token: str = Security(HTTPBearer()), required_roles: List[str] = []
        ) -> Dict[str, Any]:
            decoded_token = self.verify_token(token.credentials)
            user_roles = decoded_token.get("cognito:groups", [])
            if not any(role in user_roles for role in required_roles):
                raise HTTPException(status_code=403, detail="Not enough permissions")
            return decoded_token

        return role_dependency

    def authenticate_user(self, username: str, password: str) -> Dict[str, Any]:
        try:
            print("Initiating Cognito authentication for user:", username)
            print("Client Id:", self.app_client_id)
            client_secret = "4tudmms91t1l7t7dgrgoj5kpulb37jlnm2c8h2efkkkqm9k6red"
            secret_hash = calculate_secret_hash(
                self.app_client_id, client_secret, username
            )
            response = self.client.initiate_auth(
                ClientId=self.app_client_id,
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": username,
                    "PASSWORD": password,
                    "SECRET_HASH": secret_hash,
                },
            )
            print("Authentication response:", response)

            id_token = response["AuthenticationResult"]["IdToken"]
            access_token = response["AuthenticationResult"]["AccessToken"]
            refresh_token = response["AuthenticationResult"]["RefreshToken"]
            expires_in = response["AuthenticationResult"]["ExpiresIn"]

            return {
                "id_token": id_token,
                "access_token": access_token,
                "refresh_token": refresh_token,
                "expires_in": expires_in,
            }
        except self.client.exceptions.NotAuthorizedException as e:
            print("Invalid username or password", e.response)
            raise HTTPException(status_code=401, detail="Invalid username or password")
        except self.client.exceptions.UserNotFoundException as e:
            print("User not found", e.response)
            raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            print("Unexpected error during Cognito authentication:", e)
            raise HTTPException(status_code=500, detail="Authentication failed") from e
