from fastapi import APIRouter, HTTPException, Depends
from app.models.assets import (
    AssetCreateRequest,
    AssetResponse,
    AssetDeleteResponse,
    AssetCreateResponse,
)
from app.services.asset_service import AssetService
from app.core.utils.auth import verify_role, get_current_user
from typing import List

router = APIRouter()
asset_service = AssetService()


@router.get("/", response_model=List[AssetResponse], tags=["Assets"])
def get_assets() -> List[AssetResponse]:
    """
    Retrieve all assets.

    **Response:**
    - List of `AssetResponse` objects.
    """
    try:
        return asset_service.get_assets()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{asset_id}", response_model=AssetResponse, tags=["Assets"])
def get_asset_by_id(asset_id: str) -> AssetResponse:
    """
    Retrieve details of a specific asset by ID.

    **Path Parameter:**
    - `asset_id`: Unique identifier of the asset.

    **Response:**
    - `AssetResponse`: Details of the asset.
    """
    try:
        return asset_service.get_asset_by_id(asset_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=AssetCreateResponse, tags=["Assets"])
def create_asset(asset_data: AssetCreateRequest) -> AssetCreateResponse:
    """
    Create a new asset.

    **Request Body:**
    - `AssetCreateRequest`: Asset details.

    **Response:**
    - `AssetResponse`: Details of the created asset.
    """
    try:
        # verify_role(token, "Admin")  # Only Admins can create assets
        print(f"Request for create asset:{asset_data}")
        return asset_service.create_asset(asset_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{asset_id}", response_model=AssetDeleteResponse, tags=["Assets"])
def delete_asset(asset_id: str) -> AssetDeleteResponse:
    """
    Delete an asset by ID.

    **Path Parameter:**
    - `asset_id`: Unique identifier of the asset.

    **Response:**
    - `AssetDeleteResponse`: Confirmation message.
    """
    try:
        return asset_service.delete_asset(asset_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
