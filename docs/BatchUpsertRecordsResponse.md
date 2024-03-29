# BatchUpsertRecordsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[BatchUpsertRecordsResponseError]**](BatchUpsertRecordsResponseError.md) | Errors that occurred. | [optional] 
**keys** | [**[BatchUpsertRecordsResponseKey]**](BatchUpsertRecordsResponseKey.md) | A list of keys of the records that were inserted.  If a record was inserted, keys contains an entry containing the index of the inserted record from &#x60;records&#x60; and the key. You can use the key if you need to retrieve or delete the record.  If a record was updated, keys contains no such entry for the updated record. | [optional] 
**variables** | [**[BatchUpsertRecordsResponseVariables]**](BatchUpsertRecordsResponseVariables.md) | A list of modified variables returned by the pipeline after it has finished processing each record. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


