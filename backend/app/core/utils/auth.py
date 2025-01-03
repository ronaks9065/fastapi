from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from typing import Dict, Any, List

# Set up OAuth2 scheme for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Secret key and algorithms for token decoding (Replace these with actual values)
JWT_SECRET = "your_jwt_secret"  # Replace with your JWT secret (if using AWS Cognito, this can be a public key URL)
JWT_ALGORITHM = "HS256"  # Replace with RS256 for asymmetric encryption, if required


def get_current_user(token: str = Depends(oauth2_scheme)) -> Any:
    """
    Decodes the JWT token and returns the payload.

    Args:
        token (str): JWT access token.

    Returns:
        dict: Decoded token payload.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    try:
        # Decode the token (use public keys for RS256 if needed)
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def verify_role(token_payload: Dict[str, str], required_role: str) -> None:
    """
    Verifies that the user has the required role.

    Args:
        token_payload (dict): Decoded token payload.
        required_role (str): Role required to access the resource.

    Raises:
        HTTPException: If the user does not have the required role.
    """
    user_roles: Any = token_payload.get("roles", [])
    if required_role not in user_roles:
        raise HTTPException(
            status_code=403, detail=f"Access Denied. Required role: {required_role}"
        )
