from pydantic import BaseModel, Field
from typing import Optional


class DataTransferRequest(BaseModel):
    asset_id: str = Field(..., description="The unique ID of the asset to transfer.")
    destination_connector: str = Field(
        ..., description="The endpoint of the destination connector."
    )
    contract_agreement_id: str = Field(
        ..., description="The ID of the associated contract agreement."
    )


class DataTransferResponse(BaseModel):
    transfer_id: str = Field(
        ..., description="Unique ID of the initiated data transfer."
    )
    status: str = Field(..., description="Current status of the data transfer.")
