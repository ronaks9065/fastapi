from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class DataAddressProperties(BaseModel):
    type: str = Field(
        ...,
        alias="https://w3id.org/edc/v0.0.1/ns/type",
        description="Type of the data address.",
    )
    baseUrl: str = Field(
        ...,
        alias="https://w3id.org/edc/v0.0.1/ns/baseUrl",
        description="Base URL of the data address.",
    )
    method: Optional[str] = Field(
        None, alias="https://w3id.org/edc/v0.0.1/ns/method", description="HTTP method."
    )
    queryParams: Optional[str] = Field(
        None,
        alias="https://w3id.org/edc/v0.0.1/ns/queryParams",
        description="Query parameters.",
    )

    class Config:
        allow_population_by_field_name = True


class HttpData(BaseModel):
    baseUrl: str = Field(..., description="Base URL for the HTTP data source.")


class DataSource(BaseModel):
    type: str = Field(..., description="Type of the data source.")
    httpData: Optional[HttpData] = Field(None, description="HTTP data details.")


class AssetCreateRequest(BaseModel):
    id: str = Field(..., description="Unique identifier for the asset.")
    title: str = Field(..., description="Title of the asset.")
    language: str = Field(..., description="Language of the asset.")
    description: str = Field(..., description="Description of the asset.")
    publisherHomepage: str = Field(..., description="Publisher's homepage URL.")
    licenseUrl: str = Field(..., description="License URL for the asset.")
    version: str = Field(..., description="Version of the asset.")
    keywords: List[str] = Field(..., description="Keywords associated with the asset.")
    mediaType: str = Field(..., description="Media type of the asset.")
    landingPageUrl: str = Field(..., description="Landing page URL for the asset.")
    dataAddressProperties: DataAddressProperties = Field(
        ..., description="Properties of the data address."
    )
    dataSource: DataSource = Field(..., description="Data source information.")


class AssetCreateResponse(BaseModel):
    id: str = Field(..., description="ID of the created asset.")
    lastUpdatedDate: str = Field(
        ..., description="Last updated timestamp of the asset."
    )


class AssetResponse(BaseModel):
    dataSourceAvailability: str = Field(
        ..., description="Availability of the data source."
    )
    assetId: str = Field(..., description="Unique identifier of the asset.")
    connectorEndpoint: str = Field(..., description="Endpoint of the connector.")
    participantId: str = Field(..., description="Participant ID of the connector.")
    title: str = Field(..., description="Title of the asset.")
    creatorOrganizationName: Optional[str] = Field(
        None, description="Name of the creator organization."
    )
    language: Optional[str] = Field(None, description="Language of the asset.")
    description: Optional[str] = Field(None, description="Description of the asset.")
    descriptionShortText: Optional[str] = Field(
        None, description="Short description of the asset."
    )
    isOwnConnector: Optional[bool] = Field(
        None, description="Indicates if this is the user's own connector."
    )
    publisherHomepage: Optional[str] = Field(
        None, description="Homepage of the publisher."
    )
    licenseUrl: Optional[str] = Field(None, description="License URL for the asset.")
    version: Optional[str] = Field(None, description="Version of the asset.")
    keywords: Optional[List[str]] = Field(
        None, description="Keywords associated with the asset."
    )
    mediaType: Optional[str] = Field(None, description="Media type of the asset.")
    landingPageUrl: Optional[str] = Field(
        None, description="Landing page URL for the asset."
    )
    httpDatasourceHintsProxyMethod: Optional[bool] = Field(
        None, description="Datasource proxy method hint."
    )
    httpDatasourceHintsProxyPath: Optional[bool] = Field(
        None, description="Datasource proxy path hint."
    )
    httpDatasourceHintsProxyQueryParams: Optional[bool] = Field(
        None, description="Datasource proxy query parameters hint."
    )
    httpDatasourceHintsProxyBody: Optional[bool] = Field(
        None, description="Datasource proxy body hint."
    )
    nutsLocations: Optional[List[str]] = Field(
        None, description="NUTS locations associated with the asset."
    )
    dataSampleUrls: Optional[List[str]] = Field(
        None, description="Sample data URLs for the asset."
    )
    referenceFileUrls: Optional[List[str]] = Field(
        None, description="Reference file URLs."
    )
    assetJsonLd: Optional[str] = Field(
        None, description="Asset details in JSON-LD format."
    )
    customJsonLdAsString: Optional[str] = Field(
        None, description="Custom JSON-LD as string."
    )
    privateCustomJsonLdAsString: Optional[str] = Field(
        None, description="Private custom JSON-LD as string."
    )


class AssetDeleteResponse(BaseModel):
    status: str = Field(..., description="Status of the deletion request.")
    message: str = Field(..., description="Message confirming the deletion.")
    deletedAssetId: str = Field(..., description="ID of the deleted asset.")
