# Promotion

Promotion contains a trigger, determining which searches it should be active for, and a list of alterations that should be made to search results when it is active.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | A condition expression applied to a search request that determines which searches the promotion is active for.  For example, to apply the promotion&#39;s pins and boosts whenever a user searches for &#39;shoes&#39; set condition to &#x60;q &#x3D; &#39;shoes&#39;&#x60;. | 
**display_name** | **str** | The promotion&#39;s display name. | 
**banners** | [**[Banner]**](Banner.md) | The banners that are injected into the result set when the promotion is triggered. | [optional] 
**collection_id** | **str** | The ID of the collection that owns this promotion. | [optional] [readonly] 
**create_time** | **datetime** | The time the promotion was created. | [optional] [readonly] 
**disabled** | **bool** | If disabled, the promotion is never triggered. | [optional] 
**end_time** | **datetime** | If specified, the promotion is considered disabled after this time. | [optional] 
**exclusions** | [**[PromotionExclusion]**](PromotionExclusion.md) | The records to exclude from search results, if the promotion is enabled. | [optional] 
**filter_boosts** | [**[PromotionFilterBoost]**](PromotionFilterBoost.md) | The filter boosts to apply to searches, if the promotion is enabled. | [optional] 
**filter_conditions** | [**[PromotionFilterCondition]**](PromotionFilterCondition.md) | The conditions applied to the filters passed from the user. A query must match at least one of these in order to trigger the promotion. A filter condition is comprised of a set of filters of the form &#x60;field &#x3D; value&#x60; and matches a query if all of those filters are present in the query.  For example, a query with the filter &#x60;productType &#x3D; &#39;shirt&#39; AND size &#x3D; &#39;medium&#39;&#x60; triggers a promotion with the filter condition &#x60;productType &#x3D; &#39;shirt&#39;&#x60;, but not one with both &#x60;productType &#x3D; &#39;shirt&#39;, and &#x60;size &#x3D; &#39;small&#39;&#x60;. | [optional] 
**id** | **str** | The promotion&#39;s ID. | [optional] 
**pins** | [**[PromotionPin]**](PromotionPin.md) | The items to fix to specific positions in the search results. | [optional] 
**range_boosts** | [**[PromotionRangeBoost]**](PromotionRangeBoost.md) | The range boosts to apply to searches, if the promotion is enabled. | [optional] 
**start_time** | **datetime** | If specified, the promotion is considered disabled before this time. | [optional] 
**update_time** | **datetime** | The time the promotion was last updated. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


