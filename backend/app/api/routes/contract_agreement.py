from fastapi import APIRouter, HTTPException
from app.models.contract_agreement import (
    ContractAgreementResponse,
    TerminateAgreementRequest,
)
from app.services.contract_agreement_service import ContractAgreementService
from typing import List, Any

router = APIRouter()
contract_service = ContractAgreementService()


@router.get(
    "/agreements",
    response_model=List[ContractAgreementResponse],
    tags=["Contract Agreements"],
)
def get_contract_agreements() -> List[ContractAgreementResponse]:
    try:
        return contract_service.get_contract_agreements()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/agreements/{agreement_id}/terminate", tags=["Contract Agreements"])
def terminate_agreement(agreement_id: str, request: TerminateAgreementRequest) -> Any:
    try:
        return contract_service.terminate_agreement(agreement_id, request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/agreements/{agreement_id}",
    response_model=ContractAgreementResponse,
    tags=["Contract Agreements"],
)
def get_agreement_by_id(agreement_id: str) -> Any:
    """
    Fetch details of a specific contract agreement by ID.
    """
    try:
        return contract_service.get_agreement_by_id(agreement_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
