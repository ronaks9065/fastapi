from pydantic import BaseModel, Field


class NegotiationStartRequest(BaseModel):
    counterPartyAddress: str = Field(..., description="Address of the counterparty.")
    contractOfferId: str = Field(..., description="ID of the contract offer.")
    assetId: str = Field(..., description="Asset ID linked to the negotiation.")


class NegotiationStatusResponse(BaseModel):
    id: str = Field(..., description="Negotiation ID.")
    state: str = Field(..., description="Current state of the negotiation.")
