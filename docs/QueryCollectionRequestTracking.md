# QueryCollectionRequestTracking


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**QueryCollectionRequestTrackingType**](QueryCollectionRequestTrackingType.md) |  | [optional] 
**query_id** | **str** | Query ID of the query. If this is empty, then one is generated. | [optional] 
**sequence** | **int** | Sequence number of query. | [optional] 
**field** | **str** | Tracking field used to identify records in the collection.  Must be unique schema field. | [optional] 
**data** | **{str: (str,)}** | Custom values to be included in tracking data. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


