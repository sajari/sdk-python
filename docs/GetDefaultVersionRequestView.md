# GetDefaultVersionRequestView

 - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the `BASIC` view.  - BASIC: Include basic information including type, name, version and description but not the full step configuration. This is the default value (for both [ListPipelines](/api#operation/ListPipelines) and [GetPipeline](/api#operation/GetPipeline)).  - FULL: Include the information from `BASIC`, plus full step configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the &#x60;BASIC&#x60; view.  - BASIC: Include basic information including type, name, version and description but not the full step configuration. This is the default value (for both [ListPipelines](/api#operation/ListPipelines) and [GetPipeline](/api#operation/GetPipeline)).  - FULL: Include the information from &#x60;BASIC&#x60;, plus full step configuration. | defaults to "VIEW_UNSPECIFIED",  must be one of ["VIEW_UNSPECIFIED", "BASIC", "FULL", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


