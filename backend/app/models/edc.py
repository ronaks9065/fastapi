from pydantic import BaseModel, Field
from typing import Optional


class EDCRequest(BaseModel):
    user_id: str = Field(..., description="Unique identifier for the user.")
    instance_type: str = Field(
        ..., description="Type of EC2 instance (e.g., t2.micro)."
    )
    region: str = Field(..., description="AWS region for the EC2 instance.")
    key_name: str = Field(
        ..., description="Key pair name for SSH access to the instance."
    )


class EDCResponse(BaseModel):
    instance_id: str = Field(..., description="The ID of the allocated EC2 instance.")
    public_ip: Optional[str] = Field(
        None, description="Public IP address of the EC2 instance."
    )
    state: str = Field(
        ..., description="State of the EC2 instance (e.g., running, stopped)."
    )


class EDCDeleteResponse(BaseModel):
    instance_id: str = Field(..., description="The ID of the deleted EC2 instance.")
    status: str = Field(..., description="Status of the deletion request.")
