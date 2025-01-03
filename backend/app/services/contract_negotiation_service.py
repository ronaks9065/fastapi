from typing import Dict

from app.models.contract_negotiation import (
    NegotiationStartRequest,
    NegotiationStatusResponse,
)
from app.core.utils.request_handler import make_request

from app.core.config import settings

BASE_URL = settings.EDC_CE_URL


class ContractNegotiationService:
    def start_negotiation(
        self, request: NegotiationStartRequest
    ) -> NegotiationStatusResponse:
        url = f"{BASE_URL}/v3/contract-negotiations"
        headers: Dict[str, str] = {
            "Authorization": "Bearer <token>",
            "Content-Type": "application/json",
        }
        payload = request.dict()
        response = make_request("POST", url, headers=headers, json=payload)
        return NegotiationStatusResponse(**response)

    def get_negotiation_status(self, negotiation_id: str) -> NegotiationStatusResponse:
        url = f"{BASE_URL}/v3/contract-negotiations/{negotiation_id}"
        headers: Dict[str, str] = {"Authorization": "Bearer <token>"}
        response = make_request("GET", url, headers=headers)
        return NegotiationStatusResponse(**response)
