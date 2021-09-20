# Pipeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PipelineType**](PipelineType.md) |  | 
**name** | **str** | The pipeline&#39;s name.  Must start with an alphanumeric character followed by one or more alphanumeric, &#x60;_&#x60;, &#x60;-&#x60; or &#x60;.&#x60; characters. Strictly speaking, it must match the regular expression: &#x60;^[a-zA-Z0-9][a-zA-Z0-9_\\-\\.]+$&#x60;. | 
**version** | **str** | The pipeline&#39;s version.  Must start with an alphanumeric character followed by one or more alphanumeric, &#x60;_&#x60;, &#x60;-&#x60; or &#x60;.&#x60; characters. Strictly speaking, it must match the regular expression: &#x60;^[a-zA-Z0-9][a-zA-Z0-9_\\-\\.]+$&#x60;. | 
**create_time** | **datetime** | Output only. Creation time of the pipeline. | [optional] [readonly] 
**description** | **str** | Description of the pipeline. | [optional] 
**pre_steps** | [**[PipelineStep]**](PipelineStep.md) | Pre-steps are run before an indexing operation or query request is sent to the search index. | [optional] 
**post_steps** | [**[PipelineStep]**](PipelineStep.md) | Post-steps are run after an indexing operation or query request has been sent to the search index.  For indexing operations, the post-steps only run when creating new records. They do not run when updating records.  For querying, the post-steps have access to the result-set. This makes it possible to act on the results before sending them back to the caller. | [optional] 
**collection_default** | **bool** | Output only. Indicates if the pipeline is the collection default pipeline. | [optional] [readonly] 
**default_version** | **bool** | Output only. Indicates if the pipeline is the default version. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


