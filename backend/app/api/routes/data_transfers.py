from fastapi import APIRouter, HTTPException
from app.models.data_transfer import DataTransferRequest, DataTransferResponse
from app.services.data_transfer_service import DataTransferService
from typing import List

router = APIRouter()
data_transfer_service = DataTransferService()


@router.post(
    "/data-transfers", response_model=DataTransferResponse, tags=["Data Transfers"]
)
def initiate_transfer(request: DataTransferRequest) -> DataTransferResponse:
    """
    Initiates a data transfer.
    """
    try:
        return data_transfer_service.initiate_transfer(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/data-transfers/history",
    response_model=List[DataTransferResponse],
    tags=["Data Transfers"],
)
def get_transfer_history() -> List[DataTransferResponse]:
    """
    Retrieves transfer history.
    """
    try:
        return data_transfer_service.get_transfer_history()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/data-transfers/{transfer_id}/asset",
    response_model=DataTransferResponse,
    tags=["Data Transfers"],
)
def get_transfer_asset(transfer_id: str) -> DataTransferResponse:
    """
    Retrieve the asset associated with a specific data transfer.
    """
    try:
        return data_transfer_service.get_transfer_asset(transfer_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
