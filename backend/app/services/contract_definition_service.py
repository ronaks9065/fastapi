"""
Contract Definition Service Module

This module provides functionality to manage contract definitions,
including creation, retrieval, and deletion.
"""

from pydantic import ValidationError
from app.models.contract_definitions import (
    ContractDefinitionCreateRequest,
    ContractDefinitionCreateResponse,
    ContractDefinitionGetResponse,
    ContractDefinitionItem,
    ContractDefinitionDeleteResponse,
)
from app.core.utils.request_handler import make_request

from app.core.config import settings

BASE_URL = settings.EDC_CE_URL


class ContractDefinitionService:
    """
    Service class to manage contract definitions.
    Provides methods to create, retrieve, and delete contract definitions.
    """

    @staticmethod
    def create_contract_definition(
        contract_definition_data: ContractDefinitionCreateRequest,
    ) -> ContractDefinitionCreateResponse:
        """
        Create a new contract definition.
        """
        url = (
            f"{BASE_URL}/wrapper/ui/pages/contract-definition-page/contract-definitions"
        )
        headers = {
            "X-Api-Key": "ApiKeyDefaultValue",
            "Content-Type": "application/json",
        }
        payload = contract_definition_data.dict()
        response = make_request("POST", url, headers=headers, json=payload)
        return ContractDefinitionCreateResponse(**response)

    @staticmethod
    def get_contract_definitions() -> ContractDefinitionGetResponse:
        """
        Retrieve all contract definitions.
        """
        url = f"{BASE_URL}/wrapper/ui/pages/contract-definition-page"
        headers = {
            "X-Api-Key": "ApiKeyDefaultValue",
            "Content-Type": "application/json",
        }
        response = make_request("GET", url, headers=headers)

        # Deserialize the response into ContractDefinitionItem objects
        try:
            # Deserialize the response into ContractDefinitionItem objects
            contract_definitions = [
                ContractDefinitionItem(**item)
                for item in response.get("contractDefinitions", [])
            ]
            return ContractDefinitionGetResponse(
                contractDefinitions=contract_definitions
            )
        except ValidationError as validation_error:
            print(
                f"ValidationError: {validation_error.json()}"
            )  # Log detailed validation errors
            # Return an empty ContractDefinitionGetResponse in case of an error
            return ContractDefinitionGetResponse(contractDefinitions=[])

    @staticmethod
    def delete_contract_definition(
        contract_definition_id: str,
    ) -> ContractDefinitionDeleteResponse:
        """
        Delete a contract definition by ID.
        """
        url = f"{BASE_URL}/v3/contract-definitions/{contract_definition_id}"
        headers = {"X-Api-Key": "ApiKeyDefaultValue"}
        make_request("DELETE", url, headers=headers)
        return ContractDefinitionDeleteResponse(
            message=f"Contract Definition with ID {contract_definition_id} deleted successfully."
        )
