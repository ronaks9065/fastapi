from fastapi import APIRouter, HTTPException
from app.models.contract_definitions import (
    ContractDefinitionCreateRequest,
    ContractDefinitionCreateResponse,
    ContractDefinitionGetResponse,
    ContractDefinitionDeleteResponse,
)
from app.services.contract_definition_service import ContractDefinitionService

router = APIRouter()
contract_definition_service = ContractDefinitionService()


@router.post(
    "/contract-definitions",
    response_model=ContractDefinitionCreateResponse,
    tags=["Contract Definitions"],
    summary="Create a new contract definition",
    description="This endpoint creates a new contract definition by accepting a JSON payload with details.",
    response_description="Details of the created contract definition.",
)
def create_contract_definition(
    contract_definition_data: ContractDefinitionCreateRequest,
) -> ContractDefinitionCreateResponse:
    """
    Create a new contract definition.
    """
    try:
        return contract_definition_service.create_contract_definition(
            contract_definition_data
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/contract-definitions",
    response_model=ContractDefinitionGetResponse,
    tags=["Contract Definitions"],
    summary="Retrieve all contract definitions",
    description="This endpoint retrieves all contract definitions available in the system.",
    response_description="List of all contract definitions.",
)
def get_contract_definitions() -> ContractDefinitionGetResponse:
    """
    Retrieve all contract definitions.
    """
    try:
        return contract_definition_service.get_contract_definitions()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/contract-definitions/{contract_definition_id}",
    response_model=ContractDefinitionDeleteResponse,
    tags=["Contract Definitions"],
    summary="Delete a contract definition",
    description="This endpoint deletes a contract definition by ID.",
    response_description="Confirmation message for the deletion.",
)
def delete_contract_definition(
    contract_definition_id: str,
) -> ContractDefinitionDeleteResponse:
    """
    Delete a contract definition by ID.
    """
    try:
        return contract_definition_service.delete_contract_definition(
            contract_definition_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
