# UpdateRecordRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**RecordKey**](RecordKey.md) |  | 
**record** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | The record to update. | 
**update_mask** | **str** | The list of fields to be updated, separated by a comma, e.g. &#x60;field1,field2&#x60;.  For each field that you want to update, provide a corresponding value in the record object containing the new value. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


