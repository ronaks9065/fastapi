from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class CatalogRequest(BaseModel):
    connectorEndpoint: str = Field(
        ...,
        description=(
            "The full URL to the connector's DSP endpoint. "
            "Example: 'http://provider.edc.com/api/dsp'"
        ),
    )


class AssetProperty(BaseModel):
    key: str
    value: str


class DataOffer(BaseModel):
    asset_id: str = Field(..., description="Identifier of the asset.")
    asset_name: Optional[str] = Field(None, description="Name of the asset.")
    description: Optional[str] = Field(None, description="Description of the asset.")
    version: Optional[str] = Field(None, description="Version of the asset.")
    properties: Optional[Dict[str, str]] = Field(
        None, description="Additional properties of the asset."
    )


class CatalogResponse(BaseModel):
    connector_id: str = Field(..., description="Identifier of the connector.")
    data_offers: List[DataOffer] = Field(..., description="List of data offers.")
