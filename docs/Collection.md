# Collection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The collection&#39;s display name. You can change this at any time. | 
**account_id** | **str** | Output only. The ID of the account that owns this collection. | [optional] [readonly] 
**authorized_query_domains** | **[str]** | The list of authorized query domains for the collection.  Client-side / browser requests to the [QueryCollection](/docs/api#operation/QueryCollection) call can be made by any authorized query domain or any of its subdomains. This allows your interface to make search requests without having to provide an API key in the client-side request. | [optional] 
**create_time** | **datetime** | Output only. Time the collection was created. | [optional] [readonly] 
**id** | **str** | Output only. The collection&#39;s ID. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


