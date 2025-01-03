from pydantic import BaseModel, Field, root_validator, model_validator
from typing import List, Optional, Any


class OperandRight(BaseModel):
    type: str = Field(
        ..., description="Type of the operand right (e.g., VALUE, VALUE_LIST)."
    )
    value: Optional[str] = Field(
        None, description="The value for single VALUE type operand right."
    )
    valueList: Optional[List[str]] = Field(
        None, description="The value list for VALUE_LIST type operand right."
    )

    @model_validator(mode="before")
    def validate_operand_right(cls, values: Any) -> Any:
        print(f"DEBUG - OperandRight Values: {values}")
        type_ = values.get("type")
        value = values.get("value")
        value_list = values.get("valueList")

        if type_ == "VALUE" and not value:
            raise ValueError("For type 'VALUE', the 'value' field is required.")
        if type_ == "VALUE_LIST" and not value_list:
            raise ValueError(
                "For type 'VALUE_LIST', the 'valueList' field is required."
            )
        return values


class AssetSelector(BaseModel):
    operandLeft: str = Field(..., description="The left operand of the selector.")
    operator: str = Field(
        ..., description="The operator for the selector (e.g., EQ, IN)."
    )
    operandRight: OperandRight = Field(
        ..., description="The right operand of the selector."
    )


class ContractDefinitionCreateRequest(BaseModel):
    contractDefinitionId: str = Field(
        ..., description="Unique identifier for the contract definition."
    )
    contractPolicyId: str = Field(..., description="ID of the contract policy.")
    accessPolicyId: str = Field(..., description="ID of the access policy.")
    assetSelector: List[AssetSelector] = Field(
        ..., description="Asset selector for the contract definition."
    )


class ContractDefinitionCreateResponse(BaseModel):
    id: str = Field(..., description="ID of the created contract definition.")
    lastUpdatedDate: str = Field(
        ..., description="Timestamp when the contract definition was last updated."
    )


class ContractDefinitionItem(BaseModel):
    contractDefinitionId: str = Field(
        ..., description="Unique identifier for the contract definition."
    )
    accessPolicyId: str = Field(..., description="ID of the access policy.")
    contractPolicyId: str = Field(..., description="ID of the contract policy.")
    assetSelector: List[AssetSelector] = Field(
        ..., description="Asset selector for the contract definition."
    )


class ContractDefinitionGetResponse(BaseModel):
    contractDefinitions: List[ContractDefinitionItem] = Field(
        ..., description="List of contract definitions."
    )


class ContractDefinitionDeleteResponse(BaseModel):
    message: str = Field(..., description="Message confirming the deletion.")
