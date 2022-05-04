# PromotionFilterCondition

A set of filters of the form `field = 'value'`. Matches a query if all filters are present in that query.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **[str]** | A filter of the form &#x60;field &#x3D; &#39;value&#39;&#x60;. All of these filters must be present in a query&#39;s filter in order for the promotion to be considered active. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


