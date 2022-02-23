# SendEventRequest

A request to send an event to the ranking system after a user interacts with a search result.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of event, e.g. &#x60;click&#x60;, &#x60;purchase&#x60;. | 
**token** | **str** | The token corresponding to the search result that was interacted with, e.g. &#x60;eyJ...&#x60;. | 
**metadata** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | An object made up of field-value pairs that contains additional metadata to record with the event.  Every value in the object must be one of the following primitive types:  - boolean - number - string | [optional] 
**weight** | **int** | The weight assigned to the event.  Generally a sensible weight is 1. If you want to weight an event in a certain way you can use a value other than 1. For example, if you want to capture profit in an event, you could set the weight to a value that represents the profit. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


