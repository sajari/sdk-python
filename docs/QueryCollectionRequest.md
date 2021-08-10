# QueryCollectionRequest

A request to perform a search using a pipeline.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variables** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The initial values for the variables the pipeline operates on and transforms throughout its steps.  A typical variable is &#x60;q&#x60; which is the query the user entered, for example:  &#x60;&#x60;&#x60;json { \&quot;q\&quot;: \&quot;search terms\&quot; } &#x60;&#x60;&#x60; | 
**pipeline** | [**QueryCollectionRequestPipeline**](QueryCollectionRequestPipeline.md) |  | [optional] 
**tracking** | [**QueryCollectionRequestTracking**](QueryCollectionRequestTracking.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


