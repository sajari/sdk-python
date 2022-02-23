# PromotionRangeBoost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boost** | **float** | Number that determines the size of the boost that is applied to matching records. Must be greater than or equal to 0 and less than or equal to 1. | [optional] 
**end** | **float** | The end value to apply 1 boost to. | [optional] 
**field** | **str** | The field to apply the boost to. | [optional] 
**null_boost** | **float** | The boost given to null/empty values. Must be greater than or equal to 0 and less than or equal to 1. The default value is 0. | [optional] 
**start** | **float** | The start value to apply 0 boost to. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


