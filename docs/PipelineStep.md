# PipelineStep

Step creates a pipeline step.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the step template. | 
**annotations** | **[str]** | Annotations added to the request when the step is run. | [optional] 
**condition** | **str** | A condition expression to determine if the step should be run.  This is a filter expression much like the query filter expression, but it acts upon the pipeline variables.  For example, to only run the step if the pipeline &#x60;q&#x60; variable is not empty, set this to &#x60;q !&#x3D; &#39;&#39;&#x60;. | [optional] 
**description** | **str** | Description for the step. Overrides the default description. | [optional] 
**params** | [**{str: (PipelineStepParamBinding,)}**](PipelineStepParamBinding.md) | Bindings for the step parameters. | [optional] 
**title** | **str** | Title for the step. Overrides the default title. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


