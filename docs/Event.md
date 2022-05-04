# Event

An analytics event that relates to a query made on a collection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_id** | **str** | The query identifier. | 
**type** | **str** | The type of event, e.g. &#x60;click&#x60;, &#x60;redirect&#x60;, &#x60;purchase&#x60;, &#x60;add_to_cart&#x60;. | 
**banner_id** | **str** | The identifier of the promotion banner the event is about. | [optional] 
**metadata** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | An object made up of field-value pairs that contains additional metadata to record with the event. | [optional] 
**redirect_id** | **str** | The identifier of the redirect the event is about. | [optional] 
**result_id** | **str** | The identifier of the result the event is about. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


