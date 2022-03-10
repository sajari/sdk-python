# QueryCollectionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_promotions** | [**[ActivePromotion]**](ActivePromotion.md) | A list of the promotions activated when running the query. | [optional] 
**aggregate_filters** | [**{str: (QueryAggregateResult,)}**](QueryAggregateResult.md) | The aggregates run with filters. | [optional] 
**aggregates** | [**{str: (QueryAggregateResult,)}**](QueryAggregateResult.md) | The aggregates returned by the query. | [optional] 
**banners** | [**[Banner]**](Banner.md) | Banners associated with this query. | [optional] 
**feature_score_weight** | **float** | The weight applied to the features in the query, used for analyzing the index, neural and feature components for results.  For each result:  &#x60;&#x60;&#x60; score &#x3D; max(index_score, neural_score) * (1 - feature_score_weight) +         feature_score * feature_score_weight &#x60;&#x60;&#x60; | [optional] 
**pipeline** | [**QueryCollectionResponsePipeline**](QueryCollectionResponsePipeline.md) |  | [optional] 
**processing_duration** | **str** | The total time taken to perform the query. | [optional] 
**query_id** | **str** | The query identifier.  This uniqely identifies the specific query it was returned on. This is used to link user interactions with a query. | [optional] 
**redirects** | [**{str: (RedirectResult,)}**](RedirectResult.md) | A mapping of redirects triggered for all possible variations of the query. | [optional] 
**results** | [**[QueryResult]**](QueryResult.md) | The results returned by the query. | [optional] 
**total_size** | **str** | The total number of results that match the query. | [optional] 
**variables** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | The modified variables returned by the pipeline after it has finished processing. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


