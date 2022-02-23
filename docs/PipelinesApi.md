# sajari_client.PipelinesApi

All URIs are relative to *https://api.search.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pipeline**](PipelinesApi.md#create_pipeline) | **POST** /v4/collections/{collection_id}/pipelines | Create pipeline
[**generate_pipelines**](PipelinesApi.md#generate_pipelines) | **POST** /v4/collections/{collection_id}:generatePipelines | Generate pipelines
[**get_default_pipeline**](PipelinesApi.md#get_default_pipeline) | **GET** /v4/collections/{collection_id}:getDefaultPipeline | Get default pipeline
[**get_default_version**](PipelinesApi.md#get_default_version) | **GET** /v4/collections/{collection_id}/pipelines/{type}/{name}:getDefaultVersion | Get default pipeline version
[**get_pipeline**](PipelinesApi.md#get_pipeline) | **GET** /v4/collections/{collection_id}/pipelines/{type}/{name}/{version} | Get pipeline
[**list_pipelines**](PipelinesApi.md#list_pipelines) | **GET** /v4/collections/{collection_id}/pipelines | List pipelines
[**set_default_pipeline**](PipelinesApi.md#set_default_pipeline) | **POST** /v4/collections/{collection_id}:setDefaultPipeline | Set default pipeline
[**set_default_version**](PipelinesApi.md#set_default_version) | **POST** /v4/collections/{collection_id}/pipelines/{type}/{name}:setDefaultVersion | Set default pipeline version


# **create_pipeline**
> Pipeline create_pipeline(collection_id, pipeline)

Create pipeline

Create a new pipeline.  Pipelines are immutable once created. If you want to change a pipeline e.g. to add or change some steps, you need to create a new version of that pipeline.  To start using a new pipeline you need to update your record ingestion calls and/or your query calls to specify the new pipeline.  To create the pipeline from YAML, set the request's `Content-Type` header to `application/yaml` and submit the pipeline's YAML in the request body.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import pipelines_api
from sajari_client.model.error import Error
from sajari_client.model.pipeline import Pipeline
from pprint import pprint
# Defining the host is optional and defaults to https://api.search.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api.search.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = sajari_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sajari_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipelines_api.PipelinesApi(api_client)
    collection_id = "collection_id_example" # str | The collection to create the pipeline in, e.g. `my-collection`.
    pipeline = Pipeline(
        description="description_example",
        name="name_example",
        post_steps=[
            PipelineStep(
                annotations=[
                    "annotations_example",
                ],
                condition="condition_example",
                description="description_example",
                id="id_example",
                params={
                    "key": PipelineStepParamBinding(
                        bind="bind_example",
                        constant="constant_example",
                        default_value="default_value_example",
                        description="description_example",
                    ),
                },
                title="title_example",
            ),
        ],
        pre_steps=[
            PipelineStep(
                annotations=[
                    "annotations_example",
                ],
                condition="condition_example",
                description="description_example",
                id="id_example",
                params={
                    "key": PipelineStepParamBinding(
                        bind="bind_example",
                        constant="constant_example",
                        default_value="default_value_example",
                        description="description_example",
                    ),
                },
                title="title_example",
            ),
        ],
        type=PipelineType("TYPE_UNSPECIFIED"),
        version="version_example",
    ) # Pipeline | The pipeline to create.

    # example passing only required values which don't have defaults set
    try:
        # Create pipeline
        api_response = api_instance.create_pipeline(collection_id, pipeline)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->create_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to create the pipeline in, e.g. &#x60;my-collection&#x60;. |
 **pipeline** | [**Pipeline**](Pipeline.md)| The pipeline to create. |

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pipelines**
> GeneratePipelinesResponse generate_pipelines(collection_id, generate_pipelines_request)

Generate pipelines

Generate basic record, query and autocomplete pipeline templates. Use these templates as a starting point for your collection's pipelines.  This call returns a set of pipelines that you can pass directly to the create pipeline call.  The generated templates can be returned in JSON, the default, or YAML. To return the generated pipelines in YAML, set the request's `Accept` header to `application/yaml`. The three pipelines in the YAML response are separated by three dashes (`---`).

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import pipelines_api
from sajari_client.model.generate_pipelines_response import GeneratePipelinesResponse
from sajari_client.model.error import Error
from sajari_client.model.generate_pipelines_request import GeneratePipelinesRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.search.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api.search.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = sajari_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sajari_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipelines_api.PipelinesApi(api_client)
    collection_id = "collection_id_example" # str | The collection, e.g. `my-collection`.
    generate_pipelines_request = GeneratePipelinesRequest(
        query_training_fields=[
            "query_training_fields_example",
        ],
        searchable_fields=[
            "searchable_fields_example",
        ],
    ) # GeneratePipelinesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Generate pipelines
        api_response = api_instance.generate_pipelines(collection_id, generate_pipelines_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->generate_pipelines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection, e.g. &#x60;my-collection&#x60;. |
 **generate_pipelines_request** | [**GeneratePipelinesRequest**](GeneratePipelinesRequest.md)|  |

### Return type

[**GeneratePipelinesResponse**](GeneratePipelinesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_pipeline**
> GetDefaultPipelineResponse get_default_pipeline(collection_id, )

Get default pipeline

Get the default pipeline for a collection.  Every collection has a default record pipeline and a default query pipeline.  When a pipeline is required to complete an operation, it can be omitted from the request if a default pipeline has been set. When adding a record to a collection, the default record pipeline is used if none is provided. When querying a collection, the default query pipeline is used if none is provided.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import pipelines_api
from sajari_client.model.get_default_pipeline_response import GetDefaultPipelineResponse
from sajari_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.search.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api.search.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = sajari_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sajari_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipelines_api.PipelinesApi(api_client)
    collection_id = "collection_id_example" # str | The collection to get the default query pipeline of, e.g. `my-collection`.

    # example passing only required values which don't have defaults set
    try:
        # Get default pipeline
        api_response = api_instance.get_default_pipeline(collection_id, )
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->get_default_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to get the default query pipeline of, e.g. &#x60;my-collection&#x60;. |
 **type** | **str**| The type of the pipeline to get.   - TYPE_UNSPECIFIED: Pipeline type not specified.  - RECORD: Record pipeline.  - QUERY: Query pipeline. | defaults to "TYPE_UNSPECIFIED"

### Return type

[**GetDefaultPipelineResponse**](GetDefaultPipelineResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_version**
> Pipeline get_default_version(collection_id, type, name)

Get default pipeline version

Get the default version for a given pipeline.  The default version of a pipeline is used when a pipeline is referred to without specifying a version.  This allows you to change the pipeline version used for requests without having to change your code.  To retrieve the pipeline in YAML, set the request's `Accept` header to `application/yaml`.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import pipelines_api
from sajari_client.model.error import Error
from sajari_client.model.pipeline import Pipeline
from pprint import pprint
# Defining the host is optional and defaults to https://api.search.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api.search.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = sajari_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sajari_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipelines_api.PipelinesApi(api_client)
    collection_id = "collection_id_example" # str | The collection that owns the pipeline to get the default version of, e.g. `my-collection`.
    type = "TYPE_UNSPECIFIED" # str | The type of the pipeline to get the default version of.
    name = "name_example" # str | The name of the pipeline to get the default version of, e.g. `my-pipeline`.
    view = "VIEW_UNSPECIFIED" # str | The amount of information to include in the retrieved pipeline.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the `BASIC` view.  - BASIC: Include basic information including type, name, version and description but not the full step configuration. This is the default value (for both [ListPipelines](/docs/api#operation/ListPipelines) and [GetPipeline](/docs/api#operation/GetPipeline)).  - FULL: Include the information from `BASIC`, plus full step configuration. (optional) if omitted the server will use the default value of "VIEW_UNSPECIFIED"

    # example passing only required values which don't have defaults set
    try:
        # Get default pipeline version
        api_response = api_instance.get_default_version(collection_id, type, name)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->get_default_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get default pipeline version
        api_response = api_instance.get_default_version(collection_id, type, name, view=view)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->get_default_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that owns the pipeline to get the default version of, e.g. &#x60;my-collection&#x60;. |
 **type** | **str**| The type of the pipeline to get the default version of. |
 **name** | **str**| The name of the pipeline to get the default version of, e.g. &#x60;my-pipeline&#x60;. |
 **view** | **str**| The amount of information to include in the retrieved pipeline.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the &#x60;BASIC&#x60; view.  - BASIC: Include basic information including type, name, version and description but not the full step configuration. This is the default value (for both [ListPipelines](/docs/api#operation/ListPipelines) and [GetPipeline](/docs/api#operation/GetPipeline)).  - FULL: Include the information from &#x60;BASIC&#x60;, plus full step configuration. | [optional] if omitted the server will use the default value of "VIEW_UNSPECIFIED"

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the pipeline does not have a default version. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline**
> Pipeline get_pipeline(collection_id, type, name, version)

Get pipeline

Retrieve the details of a pipeline. Supply the type, name and version.  To retrieve the pipeline in YAML, set the request's `Accept` header to `application/yaml`.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import pipelines_api
from sajari_client.model.error import Error
from sajari_client.model.pipeline import Pipeline
from pprint import pprint
# Defining the host is optional and defaults to https://api.search.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api.search.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = sajari_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sajari_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipelines_api.PipelinesApi(api_client)
    collection_id = "collection_id_example" # str | The collection that owns the pipeline, e.g. `my-collection`.
    type = "TYPE_UNSPECIFIED" # str | The type of the pipeline to retrieve.
    name = "name_example" # str | The name of the pipeline to retrieve, e.g. `my-pipeline`.
    version = "version_example" # str | The version of the pipeline to retrieve, e.g. `42`.
    view = "VIEW_UNSPECIFIED" # str | The amount of information to include in the retrieved pipeline.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the `BASIC` view.  - BASIC: Include basic information including type, name, version and description but not the full step configuration. This is the default value (for both [ListPipelines](/docs/api#operation/ListPipelines) and [GetPipeline](/docs/api#operation/GetPipeline)).  - FULL: Include the information from `BASIC`, plus full step configuration. (optional) if omitted the server will use the default value of "VIEW_UNSPECIFIED"

    # example passing only required values which don't have defaults set
    try:
        # Get pipeline
        api_response = api_instance.get_pipeline(collection_id, type, name, version)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->get_pipeline: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get pipeline
        api_response = api_instance.get_pipeline(collection_id, type, name, version, view=view)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->get_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that owns the pipeline, e.g. &#x60;my-collection&#x60;. |
 **type** | **str**| The type of the pipeline to retrieve. |
 **name** | **str**| The name of the pipeline to retrieve, e.g. &#x60;my-pipeline&#x60;. |
 **version** | **str**| The version of the pipeline to retrieve, e.g. &#x60;42&#x60;. |
 **view** | **str**| The amount of information to include in the retrieved pipeline.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the &#x60;BASIC&#x60; view.  - BASIC: Include basic information including type, name, version and description but not the full step configuration. This is the default value (for both [ListPipelines](/docs/api#operation/ListPipelines) and [GetPipeline](/docs/api#operation/GetPipeline)).  - FULL: Include the information from &#x60;BASIC&#x60;, plus full step configuration. | [optional] if omitted the server will use the default value of "VIEW_UNSPECIFIED"

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipelines**
> ListPipelinesResponse list_pipelines(collection_id)

List pipelines

Retrieve a list of pipelines in a collection.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import pipelines_api
from sajari_client.model.error import Error
from sajari_client.model.list_pipelines_response import ListPipelinesResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.search.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api.search.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = sajari_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sajari_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipelines_api.PipelinesApi(api_client)
    collection_id = "collection_id_example" # str | The collection that owns this set of pipelines, e.g. `my-collection`.
    page_size = 1 # int | The maximum number of pipelines to return. The service may return fewer than this value.  If unspecified, at most 50 pipelines are returned.  The maximum value is 1000; values above 1000 are coerced to 1000. (optional)
    page_token = "page_token_example" # str | A page token, received from a previous [ListPipelines](/docs/api#operation/ListPipelines) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListPipelines](/docs/api#operation/ListPipelines) must match the call that provided the page token. (optional)
    view = "VIEW_UNSPECIFIED" # str | The amount of information to include in each retrieved pipeline.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the `BASIC` view.  - BASIC: Include basic information including type, name, version and description but not the full step configuration. This is the default value (for both [ListPipelines](/docs/api#operation/ListPipelines) and [GetPipeline](/docs/api#operation/GetPipeline)).  - FULL: Include the information from `BASIC`, plus full step configuration. (optional) if omitted the server will use the default value of "VIEW_UNSPECIFIED"

    # example passing only required values which don't have defaults set
    try:
        # List pipelines
        api_response = api_instance.list_pipelines(collection_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->list_pipelines: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List pipelines
        api_response = api_instance.list_pipelines(collection_id, page_size=page_size, page_token=page_token, view=view)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->list_pipelines: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that owns this set of pipelines, e.g. &#x60;my-collection&#x60;. |
 **page_size** | **int**| The maximum number of pipelines to return. The service may return fewer than this value.  If unspecified, at most 50 pipelines are returned.  The maximum value is 1000; values above 1000 are coerced to 1000. | [optional]
 **page_token** | **str**| A page token, received from a previous [ListPipelines](/docs/api#operation/ListPipelines) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListPipelines](/docs/api#operation/ListPipelines) must match the call that provided the page token. | [optional]
 **view** | **str**| The amount of information to include in each retrieved pipeline.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the &#x60;BASIC&#x60; view.  - BASIC: Include basic information including type, name, version and description but not the full step configuration. This is the default value (for both [ListPipelines](/docs/api#operation/ListPipelines) and [GetPipeline](/docs/api#operation/GetPipeline)).  - FULL: Include the information from &#x60;BASIC&#x60;, plus full step configuration. | [optional] if omitted the server will use the default value of "VIEW_UNSPECIFIED"

### Return type

[**ListPipelinesResponse**](ListPipelinesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_pipeline**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_default_pipeline(collection_id, set_default_pipeline_request)

Set default pipeline

Set the default pipeline for a collection.  Every collection has a default record pipeline and a default query pipeline.  When a pipeline is required to complete an operation, it can be omitted from the request if a default pipeline has been set. When adding a record to a collection, the default record pipeline is used if none is provided. When querying a collection, the default query pipeline is used if none is provided.  Once a default pipeline has been set it cannot be cleared, only set to another pipeline.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import pipelines_api
from sajari_client.model.set_default_pipeline_request import SetDefaultPipelineRequest
from sajari_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.search.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api.search.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = sajari_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sajari_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipelines_api.PipelinesApi(api_client)
    collection_id = "collection_id_example" # str | The collection to set the default query pipeline of, e.g. `my-collection`.
    set_default_pipeline_request = SetDefaultPipelineRequest(
        pipeline="pipeline_example",
        type=PipelineType("TYPE_UNSPECIFIED"),
    ) # SetDefaultPipelineRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set default pipeline
        api_response = api_instance.set_default_pipeline(collection_id, set_default_pipeline_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->set_default_pipeline: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to set the default query pipeline of, e.g. &#x60;my-collection&#x60;. |
 **set_default_pipeline_request** | [**SetDefaultPipelineRequest**](SetDefaultPipelineRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_version**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} set_default_version(collection_id, type, name, set_default_version_request)

Set default pipeline version

Set the default version for a given pipeline.  The default version of a pipeline is used when a pipeline is referred to without specifying a version.  This allows you to change the pipeline version used for requests without having to change your code.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import pipelines_api
from sajari_client.model.set_default_version_request import SetDefaultVersionRequest
from sajari_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.search.io
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api.search.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = sajari_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with sajari_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipelines_api.PipelinesApi(api_client)
    collection_id = "collection_id_example" # str | The collection that owns the pipeline to set the default version of, e.g. `my-collection`.
    type = "TYPE_UNSPECIFIED" # str | The type of the pipeline to set the default version of.
    name = "name_example" # str | The name of the pipeline to set the default version of, e.g. `my-pipeline`.
    set_default_version_request = SetDefaultVersionRequest(
        version="version_example",
    ) # SetDefaultVersionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Set default pipeline version
        api_response = api_instance.set_default_version(collection_id, type, name, set_default_version_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PipelinesApi->set_default_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that owns the pipeline to set the default version of, e.g. &#x60;my-collection&#x60;. |
 **type** | **str**| The type of the pipeline to set the default version of. |
 **name** | **str**| The name of the pipeline to set the default version of, e.g. &#x60;my-pipeline&#x60;. |
 **set_default_version_request** | [**SetDefaultVersionRequest**](SetDefaultVersionRequest.md)|  |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

