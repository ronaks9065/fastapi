from pydantic import BaseModel, Field
from typing import Optional, Dict


class DataOfferRequest(BaseModel):
    asset_id: str = Field(
        ..., description="The unique ID of the asset for the data offer."
    )
    policy_id: Optional[str] = Field(
        None, description="Optional policy ID for the data offer."
    )


class DataOfferResponse(BaseModel):
    offer_id: str = Field(..., description="Unique ID of the created data offer.")
    asset_id: str = Field(..., description="The unique ID of the asset for this offer.")
    policy_id: Optional[str] = Field(
        None, description="The policy ID associated with the offer."
    )
