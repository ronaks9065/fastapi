from typing import Any

from app.models.data_offer import DataOfferRequest, DataOfferResponse
from app.core.utils.request_handler import make_request

from app.core.config import settings

BASE_URL = settings.EDC_CE_URL


class DataOfferService:
    def create_data_offer(self, request: DataOfferRequest) -> DataOfferResponse:
        """
        Create a new data offer.
        """
        url = f"{BASE_URL}/v3/data-offers"
        headers = {
            "Authorization": "Bearer <token>",
            "Content-Type": "application/json",
        }
        payload = request.dict()
        response = make_request("POST", url, headers=headers, json=payload)
        return DataOfferResponse(**response)

    def validate_policy_id(self, policy_id: str) -> Any:
        """
        Validate if a policy ID is valid.
        """
        url = f"{BASE_URL}/v3/policies/{policy_id}/validate"
        headers = {"Authorization": "Bearer <token>"}
        response = make_request("GET", url, headers=headers)
        return response.get("valid", False)

    def validate_asset_id(self, asset_id: str) -> Any:
        """
        Validate if an asset ID is valid.
        """
        url = f"{BASE_URL}/v3/assets/{asset_id}/validate"
        headers = {"Authorization": "Bearer <token>"}
        response = make_request("GET", url, headers=headers)
        return response.get("valid", False)

    def validate_contract_definition_id(self, contract_definition_id: str) -> Any:
        """
        Validate if a contract definition ID is valid.
        """
        url = f"{BASE_URL}/v3/contracts/{contract_definition_id}/validate"
        headers = {"Authorization": "Bearer <token>"}
        response = make_request("GET", url, headers=headers)
        return response.get("valid", False)
