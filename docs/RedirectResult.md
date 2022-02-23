# RedirectResult

Indicates that a redirect has been triggered for a given query.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The redirect&#39;s ID. | [optional] 
**target** | **str** | The target to redirect the user to. | [optional] 
**token** | **str** | A redirect token.  Call SendEvent with this token to indicate that a redirect has been performed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


