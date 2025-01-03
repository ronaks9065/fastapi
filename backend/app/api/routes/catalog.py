from fastapi import APIRouter, HTTPException
from app.models.catalog import CatalogRequest, CatalogResponse
from app.services.catalog_service import CatalogService

router = APIRouter()
catalog_service = CatalogService()


@router.post("/catalog", response_model=CatalogResponse)
def request_catalog(catalog_request: CatalogRequest) -> CatalogResponse:
    """
    Request catalog data.
    """
    try:
        return catalog_service.request_catalog(catalog_request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
