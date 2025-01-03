from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict
from app.models.contract_negotiation import (
    NegotiationStartRequest,
    NegotiationStatusResponse,
)
from app.services.contract_negotiation_service import ContractNegotiationService
from app.core.utils.auth import get_current_user, verify_role

router = APIRouter()
contract_negotiation_service = ContractNegotiationService()


@router.post(
    "/start", response_model=NegotiationStatusResponse, tags=["Contract Negotiations"]
)
def start_negotiation(
    negotiation_request: NegotiationStartRequest,
    token: Dict[str, str] = Depends(get_current_user),
) -> NegotiationStatusResponse:
    """
    Start a new contract negotiation.

    **Request Body:**
    - `NegotiationStartRequest`: Contains the required fields to start a negotiation:
        - `counterPartyAddress`: Address of the counterparty.
        - `contractOfferId`: The ID of the contract offer.
        - `assetId`: The ID of the asset involved in the negotiation.

    **Response:**
    - `NegotiationStatusResponse`: Returns the status and details of the started negotiation.
    """
    try:
        verify_role(token, "User")  # Ensure the user has the 'User' role
        return contract_negotiation_service.start_negotiation(negotiation_request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/{negotiation_id}",
    response_model=NegotiationStatusResponse,
    tags=["Contract Negotiations"],
)
def get_negotiation_status(
    negotiation_id: str, token: Dict[str, str] = Depends(get_current_user)
) -> NegotiationStatusResponse:
    """
    Get the status of a specific contract negotiation.

    **Path Parameter:**
    - `negotiation_id`: Unique identifier of the negotiation.

    **Response:**
    - `NegotiationStatusResponse`: Returns the current status and details of the negotiation.
    """
    try:
        verify_role(token, "User")  # Ensure the user has the 'User' role
        return contract_negotiation_service.get_negotiation_status(negotiation_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
