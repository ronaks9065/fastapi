from app.models.data_transfer import DataTransferRequest, DataTransferResponse
from app.core.utils.request_handler import make_request
from typing import List

from app.core.config import settings

BASE_URL = settings.EDC_CE_URL


class DataTransferService:
    def initiate_transfer(self, request: DataTransferRequest) -> DataTransferResponse:
        """
        Initiates a data transfer.
        """
        url = f"{BASE_URL}/v3/data-transfers"
        headers = {
            "Authorization": "Bearer <token>",
            "Content-Type": "application/json",
        }
        payload = request.dict()
        response = make_request("POST", url, headers=headers, json=payload)
        return DataTransferResponse(**response)

    def get_transfer_history(self) -> List[DataTransferResponse]:
        """
        Retrieves transfer history.
        """
        url = f"{BASE_URL}/v3/data-transfers/history"
        headers = {"Authorization": "Bearer <token>"}
        response = make_request("GET", url, headers=headers)
        return [DataTransferResponse(**item) for item in response]

    def get_transfer_asset(self, transfer_id: str) -> DataTransferResponse:
        """
        Retrieve the asset associated with a specific data transfer.
        """
        url = f"{BASE_URL}/v3/data-transfers/{transfer_id}/asset"
        headers = {"Authorization": "Bearer <token>"}
        response = make_request("GET", url, headers=headers)
        return DataTransferResponse(**response)
