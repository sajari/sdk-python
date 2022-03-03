# UpsertRecordRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | An object made up of field-value pairs that contains the record data. | 
**pipeline** | [**UpsertRecordRequestPipeline**](UpsertRecordRequestPipeline.md) |  | [optional] 
**variables** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | The initial values for the variables the pipeline operates on and transforms throughout its steps. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


