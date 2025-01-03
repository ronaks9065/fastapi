# mypy: disable-error-code="return-value, no-untyped-def, no-any-return, attr-defined"
# Standard Library imports
from typing import Any

# Local application imports
from app.auth.cognito_auth import CognitoAuth

# Third-party imports
from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()


# Define request body schema
class AuthRequest(BaseModel):
    username: str
    password: str


@router.post("/login", response_model=dict[str, str])
async def login(
    auth_request: AuthRequest, auth: CognitoAuth = Depends(CognitoAuth)
) -> dict[str, str]:
    tokens = auth.authenticate_user(auth_request.username, auth_request.password)
    return tokens
