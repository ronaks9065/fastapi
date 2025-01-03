from pydantic import BaseModel, Field, root_validator, model_validator
from typing import List, Optional, Dict, Any
from enum import Enum


class ExpressionType(str, Enum):
    CONSTRAINT = "CONSTRAINT"
    EMPTY = "EMPTY"


class Right(BaseModel):
    type: str = Field(..., description="Type of the right operand (e.g., STRING).")
    value: str = Field(..., description="Value of the right operand.")


class Constraint(BaseModel):
    left: str = Field(
        ..., description="Left operand of the constraint (e.g., REFERRING_CONNECTOR)."
    )
    operator: str = Field(..., description="Operator of the constraint (e.g., EQ).")
    right: Right = Field(..., description="Right operand of the constraint.")


class Expression(BaseModel):
    type: ExpressionType = Field(
        ..., description="Type of the expression (e.g., CONSTRAINT or EMPTY)."
    )
    constraint: Optional[Constraint] = Field(
        None, description="Details of the constraint if applicable."
    )


class PolicyDetails(BaseModel):
    policyJsonLd: str = Field(..., description="Policy details in JSON-LD format.")
    expression: Expression = Field(
        ..., description="Expression associated with the policy."
    )
    errors: List[str] = Field(..., description="List of errors, if any.")


class PolicyItem(BaseModel):
    policyDefinitionId: str = Field(
        ..., description="Unique identifier for the policy definition."
    )
    policy: PolicyDetails = Field(..., description="Details of the policy.")


class PolicyGetResponse(BaseModel):
    policies: List[PolicyItem] = Field(..., description="List of policy items.")


class PolicyCreateRequest(BaseModel):
    policyDefinitionId: str = Field(
        ..., description="Unique identifier for the policy."
    )
    policy: Dict[str, List[Constraint]] = Field(
        ..., description="Constraints defining the policy."
    )

    @model_validator(mode="before")
    def validate_policy(cls, values: Any) -> Any:
        policy = values.get("policy")
        if not policy or not isinstance(policy, dict):
            raise ValueError("The 'policy' field must be a non-empty dictionary.")
        for key, constraints in policy.items():
            if not isinstance(constraints, list) or not all(
                isinstance(c, Constraint) for c in constraints
            ):
                raise ValueError(
                    f"Each key in 'policy' must map to a list of Constraint objects. Issue with key: {key}"
                )
        return values


class PolicyCreateResponse(BaseModel):
    id: str = Field(..., description="Unique identifier of the created policy.")
    lastUpdatedDate: str = Field(
        ..., description="Last updated timestamp for the policy."
    )


class PolicyDeleteResponse(BaseModel):
    status: str = Field(..., description="Status of the deletion request.")
    message: str = Field(..., description="Message confirming the deletion.")
    deletedPolicyId: str = Field(..., description="ID of the deleted policy.")
