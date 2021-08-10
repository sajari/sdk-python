# QueryCollectionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline** | [**QueryCollectionResponsePipeline**](QueryCollectionResponsePipeline.md) |  | [optional] 
**variables** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The modified variables returned by the pipeline after it has finished processing. | [optional] 
**results** | [**[QueryResult]**](QueryResult.md) | The results returned by the query. | [optional] 
**total_size** | **str** | The total number of results that match the query. | [optional] 
**processing_duration** | **str** | The total time taken to perform the query. | [optional] 
**aggregates** | [**{str: (QueryAggregateResult,)}**](QueryAggregateResult.md) | The aggregates returned by the query. | [optional] 
**aggregate_filters** | [**{str: (QueryAggregateResult,)}**](QueryAggregateResult.md) | The aggregates run with filters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


