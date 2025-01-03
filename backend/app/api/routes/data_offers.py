from typing import Any

from fastapi import APIRouter, HTTPException
from app.models.data_offer import DataOfferRequest, DataOfferResponse
from app.services.data_offer_service import DataOfferService

router = APIRouter()
data_offer_service = DataOfferService()


@router.post("/data-offers", response_model=DataOfferResponse, tags=["Data Offers"])
def create_data_offer(request: DataOfferRequest) -> DataOfferResponse:
    """
    Create a new data offer.
    """
    try:
        return data_offer_service.create_data_offer(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/data-offers/policies/{policy_id}/validate", tags=["Data Offers"])
def validate_policy_id(policy_id: str) -> Any:
    """
    Validate a policy ID.
    """
    try:
        valid = data_offer_service.validate_policy_id(policy_id)
        return {"policy_id": policy_id, "valid": valid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/data-offers/assets/{asset_id}/validate", tags=["Data Offers"])
def validate_asset_id(asset_id: str) -> Any:
    """
    Validate an asset ID.
    """
    try:
        valid = data_offer_service.validate_asset_id(asset_id)
        return {"asset_id": asset_id, "valid": valid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/data-offers/contracts/{contract_definition_id}/validate", tags=["Data Offers"]
)
def validate_contract_definition_id(contract_definition_id: str) -> Any:
    """
    Validate a contract definition ID.
    """
    try:
        valid = data_offer_service.validate_contract_definition_id(
            contract_definition_id
        )
        return {"contract_definition_id": contract_definition_id, "valid": valid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
