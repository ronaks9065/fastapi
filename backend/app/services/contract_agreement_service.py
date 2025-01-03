"""
Contract Agreement Service Module

This module provides services for managing contract agreements, including retrieval and termination.
"""

from typing import List, Any
from app.models.contract_agreement import (
    ContractAgreementResponse,
    TerminateAgreementRequest,
)
from app.core.utils.request_handler import make_request
from app.core.config import settings

BASE_URL = settings.EDC_CE_URL


class ContractAgreementService:
    """
    Service class for managing contract agreements.
    Provides methods for retrieving, terminating, and fetching agreement details.
    """

    @staticmethod
    def get_contract_agreements() -> List[ContractAgreementResponse]:
        """
        Retrieve all contract agreements.
        """
        url = f"{BASE_URL}/v3/contract-agreements"
        headers = {"Authorization": "Bearer <token>"}
        response = make_request("GET", url, headers=headers)
        return [ContractAgreementResponse(**item) for item in response]

    @staticmethod
    def terminate_agreement(
        agreement_id: str, termination_request: TerminateAgreementRequest
    ) -> Any:
        """
        Terminate a specific contract agreement by ID.
        """
        url = f"{BASE_URL}/v3/contract-agreements/{agreement_id}/terminate"
        headers = {
            "Authorization": "Bearer <token>",
            "Content-Type": "application/json",
        }
        payload = termination_request.dict()
        make_request("POST", url, headers=headers, json=payload)
        return {
            "message": f"Contract agreement {agreement_id} terminated successfully."
        }

    @staticmethod
    def get_agreement_by_id(agreement_id: str) -> ContractAgreementResponse:
        """
        Fetch details of a specific contract agreement by ID.
        """
        url = f"{BASE_URL}/v3/contract-agreements/{agreement_id}"
        headers = {"Authorization": "Bearer <token>"}
        response = make_request("GET", url, headers=headers)
        return ContractAgreementResponse(**response)
