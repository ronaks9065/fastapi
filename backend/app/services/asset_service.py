"""
Asset Service Module

This module provides services for managing assets, including retrieval, creation, and deletion.
"""

from typing import List
from app.models.assets import (
    AssetCreateRequest,
    AssetResponse,
    AssetDeleteResponse,
    AssetCreateResponse,
)
from app.core.utils.request_handler import make_request
from app.core.config import settings

BASE_URL = settings.EDC_CE_URL


class AssetService:
    """
    A service class to manage assets,
    providing methods for retrieving, creating, and deleting assets.
    """

    @staticmethod
    def get_assets() -> List[AssetResponse]:
        """
        Retrieve all assets.
        """
        url = f"{BASE_URL}/wrapper/ui/pages/asset-page"
        headers = {
            "X-Api-Key": "ApiKeyDefaultValue",
            "Content-Type": "application/json",
        }
        response = make_request("GET", url, headers=headers)
        print("pointing inside Asset Service")
        # if not isinstance(response.assets, list):  # Ensure the response is a list of assets
        #     raise ValueError("API response is not a list of assets.")
        assets = response.get("assets", [])
        print(f"got assets:{assets}")

        return [AssetResponse(**asset) for asset in assets]

    @staticmethod
    def get_asset_by_id(asset_id: str) -> AssetResponse:
        """
        Retrieve details of a specific asset by ID. This is not
        """
        url = f"{BASE_URL}/wrapper/ui/pages/asset-page/{asset_id}"
        headers = {
            "X-API-KEY": "ApiKeyDefaultValue",
            "Content-Type": "application/json",
        }
        response = make_request("GET", url, headers=headers)
        return AssetResponse(**response)

    @staticmethod
    def create_asset(asset_data: AssetCreateRequest) -> AssetCreateResponse:
        """
        Create a new asset.
        """
        url = f"{BASE_URL}/wrapper/ui/pages/asset-page/assets"
        headers = {
            "X-API-KEY": "ApiKeyDefaultValue",
            "Content-Type": "application/json",
        }
        print("pointing inside Asset Service")

        payload = asset_data.dict(by_alias=True)
        print(f"payload:{payload}")
        response = make_request("POST", url, headers=headers, json=payload)
        return AssetCreateResponse(**response)

    @staticmethod
    def delete_asset(asset_id: str) -> AssetDeleteResponse:
        """
        Delete an asset by ID.
        """
        url = f"{BASE_URL}/wrapper/ui/pages/asset-page/assets/{asset_id}"
        headers = {"Authorization": f"Bearer {settings.API_KEY}"}
        response = make_request("DELETE", url, headers=headers)
        return AssetDeleteResponse(
            status=response.get("status", "success"),
            deletedAssetId=response.get("deletedAssetId", asset_id),
            message=f"Asset with ID {asset_id} deleted successfully.",
        )
