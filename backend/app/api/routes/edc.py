from fastapi import APIRouter, HTTPException
from app.models.edc import EDCRequest, EDCResponse, EDCDeleteResponse
from app.services.edc_service import EDCService

router = APIRouter()
edc_service = EDCService()


@router.post("/edc", response_model=EDCResponse, tags=["EDC"])
def create_edc(edc_request: EDCRequest) -> EDCResponse:
    """
    Create a new EDC instance for the user.
    """
    try:
        return edc_service.create_edc_instance(edc_request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/edc/{instance_id}", response_model=EDCDeleteResponse, tags=["EDC"])
def delete_edc(instance_id: str) -> EDCDeleteResponse:
    """
    Delete an allocated EDC instance.
    """
    try:
        return edc_service.delete_edc_instance(instance_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/edc/{instance_id}/deallocate", response_model=EDCResponse, tags=["EDC"])
def deallocate_edc(instance_id: str) -> EDCResponse:
    """
    Deallocate an EDC instance (stop it).
    """
    try:
        return edc_service.deallocate_edc_instance(instance_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
