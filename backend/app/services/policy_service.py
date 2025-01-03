from typing import List, Dict, Any
from app.models.policies import (
    PolicyCreateRequest,
    PolicyCreateResponse,
    PolicyGetResponse,
    PolicyDeleteResponse,
)
from app.core.utils.request_handler import make_request

from app.models.policies import PolicyItem

from app.core.config import settings

BASE_URL = settings.EDC_CE_URL


class PolicyService:
    @staticmethod
    def get_policies() -> Dict[str, Any]:
        """
        Retrieve all policies.
        """
        url = f"{BASE_URL}/wrapper/ui/pages/policy-page"
        headers = {
            "X-Api-Key": "ApiKeyDefaultValue",
            "Content-Type": "application/json",
        }
        response = make_request("GET", url, headers=headers)
        # Serialize policies into dictionaries
        policies = [PolicyItem(**policy) for policy in response.get("policies", [])]
        return PolicyGetResponse(
            policies=policies
        ).dict()  # Return a list of serialized policies

    @staticmethod
    def create_policy(policy_data: PolicyCreateRequest) -> PolicyCreateResponse:
        """
        Create a new policy.
        """
        url = f"{BASE_URL}/wrapper/ui/pages/policy-page/policy-definitions"
        headers = {
            "X-API-KEY": "ApiKeyDefaultValue",
            "Content-Type": "application/json",
        }
        payload = policy_data.dict()
        response = make_request("POST", url, headers=headers, json=payload)
        return PolicyCreateResponse(**response)

    @staticmethod
    def delete_policy(policy_id: str) -> PolicyDeleteResponse:
        """
        Delete a policy by ID.
        """
        url = f"{BASE_URL}/v3/policies/{policy_id}"
        headers = {"Authorization": "Bearer <token>"}
        response = make_request("DELETE", url, headers=headers)
        return PolicyDeleteResponse(
            status=response.get("status", "success"),  # Default status to "success"
            deletedPolicyId=policy_id,
            message=f"Policy with ID {policy_id} deleted successfully.",
        )

    @staticmethod
    def update_policy(
        policy_id: str, policy_data: PolicyCreateRequest
    ) -> PolicyCreateResponse:
        """
        Update an existing policy by ID.
        """
        url = f"{BASE_URL}/v3/policies/{policy_id}"
        headers = {
            "Authorization": "Bearer <token>",
            "Content-Type": "application/json",
        }
        payload = policy_data.dict()
        response = make_request("PUT", url, headers=headers, json=payload)
        return PolicyCreateResponse(**response)
