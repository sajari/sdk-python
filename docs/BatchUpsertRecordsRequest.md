# BatchUpsertRecordsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | A list of records to upsert.  A maximum of 200 records can be upserted in a batch. | 
**pipeline** | [**BatchUpsertRecordsRequestPipeline**](BatchUpsertRecordsRequestPipeline.md) |  | [optional] 
**variables** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | The initial values for the variables the pipeline operates on and transforms throughout its steps. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


