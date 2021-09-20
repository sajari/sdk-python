# QueryResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | An object made up of field-value pairs that contains the record data. | [optional] 
**score** | **float** | The normalized score attributed to this record. Combines the index score and feature score. | [optional] 
**index_score** | **float** | Index score. | [optional] 
**token** | [**QueryResultToken**](QueryResultToken.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


