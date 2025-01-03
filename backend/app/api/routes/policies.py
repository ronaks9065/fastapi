from fastapi import APIRouter, HTTPException, Depends
from app.models.policies import (
    PolicyCreateRequest,
    PolicyDeleteResponse,
    PolicyGetResponse,
    PolicyCreateResponse,
)
from app.services.policy_service import PolicyService
from app.core.utils.auth import verify_role, get_current_user
from typing import List, Dict, Any

router = APIRouter()
policy_service = PolicyService()


@router.get("/policies", response_model=PolicyGetResponse, tags=["Policies"])
def get_policies() -> Dict[str, Any]:
    """
    Retrieve all policies.
    """
    try:
        policies = policy_service.get_policies()
        print(f"DEBUG - Response: {policies}")  # Debugging output
        return policies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/policies", response_model=PolicyCreateResponse, tags=["Policies"])
def create_policy(policy_data: PolicyCreateRequest) -> PolicyCreateResponse:
    """
    Create a new policy.
    """
    try:
        # verify_role(token, "Admin")  # Ensure only Admins can create policies
        return policy_service.create_policy(policy_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/policies/{policy_id}", response_model=PolicyDeleteResponse, tags=["Policies"]
)
def delete_policy(policy_id: str) -> PolicyDeleteResponse:
    """
    Delete a policy by ID.
    """
    try:
        return policy_service.delete_policy(policy_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put(
    "/policies/{policy_id}", response_model=PolicyCreateResponse, tags=["Policies"]
)
def update_policy(
    policy_id: str, policy_data: PolicyCreateRequest
) -> PolicyCreateResponse:
    """
    Update an existing policy by ID.
    """
    try:
        return policy_service.update_policy(policy_id, policy_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
