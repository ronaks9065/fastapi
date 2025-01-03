from pydantic import BaseModel, Field
from typing import Optional


class ContractAgreementResponse(BaseModel):
    id: str = Field(..., description="Unique identifier for the contract agreement.")
    state: str = Field(..., description="Current state of the agreement.")
    asset_id: str = Field(
        ..., description="ID of the asset associated with this agreement."
    )
    policy_id: Optional[str] = Field(
        None, description="Policy ID linked to this agreement."
    )


class TerminateAgreementRequest(BaseModel):
    reason: str = Field(..., description="Reason for terminating the agreement.")
    details: Optional[str] = Field(
        None, description="Additional details for termination."
    )
