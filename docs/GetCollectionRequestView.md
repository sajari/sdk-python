# GetCollectionRequestView

 - BASIC: Include basic information including display name and domains. This is the default value (for both [ListCollections](/docs/api#operation/ListCollections) and [GetCollection](/docs/api#operation/GetCollection)).  - FULL: Include the information from `BASIC`, plus full collection details like disk usage.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  - BASIC: Include basic information including display name and domains. This is the default value (for both [ListCollections](/docs/api#operation/ListCollections) and [GetCollection](/docs/api#operation/GetCollection)).  - FULL: Include the information from &#x60;BASIC&#x60;, plus full collection details like disk usage. | defaults to "VIEW_UNSPECIFIED",  must be one of ["VIEW_UNSPECIFIED", "BASIC", "FULL", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


