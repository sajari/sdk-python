# sajari_client.SchemaApi

All URIs are relative to *https://api.search.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_schema_fields**](SchemaApi.md#batch_create_schema_fields) | **POST** /v4/collections/{collection_id}/schemaFields:batchCreate | Batch create schema fields
[**create_schema_field**](SchemaApi.md#create_schema_field) | **POST** /v4/collections/{collection_id}/schemaFields | Create schema field
[**delete_schema_field**](SchemaApi.md#delete_schema_field) | **DELETE** /v4/collections/{collection_id}/schemaFields/{schema_field_name} | Delete schema field
[**list_schema_fields**](SchemaApi.md#list_schema_fields) | **GET** /v4/collections/{collection_id}/schemaFields | List schema fields
[**update_schema_field**](SchemaApi.md#update_schema_field) | **PATCH** /v4/collections/{collection_id}/schemaFields/{schema_field_name} | Update schema field


# **batch_create_schema_fields**
> BatchCreateSchemaFieldsResponse batch_create_schema_fields(collection_id, batch_create_schema_fields_request)

Batch create schema fields

The batch version of the [CreateSchemaField](/docs/api#operation/CreateSchemaField) call.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import schema_api
from sajari_client.model.batch_create_schema_fields_request import BatchCreateSchemaFieldsRequest
from sajari_client.model.batch_create_schema_fields_response import BatchCreateSchemaFieldsResponse
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
    api_instance = schema_api.SchemaApi(api_client)
    collection_id = "collection_id_example" # str | The collection to create the schema fields in, e.g. `my-collection`.
    batch_create_schema_fields_request = BatchCreateSchemaFieldsRequest(
        fields=[
            SchemaField(
                array=True,
                array_length=1,
                description="description_example",
                mode=SchemaFieldMode("MODE_UNSPECIFIED"),
                name="name_example",
                type=SchemaFieldType("TYPE_UNSPECIFIED"),
            ),
        ],
    ) # BatchCreateSchemaFieldsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Batch create schema fields
        api_response = api_instance.batch_create_schema_fields(collection_id, batch_create_schema_fields_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling SchemaApi->batch_create_schema_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to create the schema fields in, e.g. &#x60;my-collection&#x60;. |
 **batch_create_schema_fields_request** | [**BatchCreateSchemaFieldsRequest**](BatchCreateSchemaFieldsRequest.md)|  |

### Return type

[**BatchCreateSchemaFieldsResponse**](BatchCreateSchemaFieldsResponse.md)

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

# **create_schema_field**
> SchemaField create_schema_field(collection_id, schema_field)

Create schema field

Create a new field in a collection's schema.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import schema_api
from sajari_client.model.schema_field import SchemaField
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
    api_instance = schema_api.SchemaApi(api_client)
    collection_id = "collection_id_example" # str | The collection to create a schema field in, e.g. `my-collection`.
    schema_field = SchemaField(
        array=True,
        array_length=1,
        description="description_example",
        mode=SchemaFieldMode("MODE_UNSPECIFIED"),
        name="name_example",
        type=SchemaFieldType("TYPE_UNSPECIFIED"),
    ) # SchemaField | The schema field to create.

    # example passing only required values which don't have defaults set
    try:
        # Create schema field
        api_response = api_instance.create_schema_field(collection_id, schema_field)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling SchemaApi->create_schema_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to create a schema field in, e.g. &#x60;my-collection&#x60;. |
 **schema_field** | [**SchemaField**](SchemaField.md)| The schema field to create. |

### Return type

[**SchemaField**](SchemaField.md)

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

# **delete_schema_field**
> bool, date, datetime, dict, float, int, list, str, none_type delete_schema_field(collection_id, schema_field_name)

Delete schema field

Deleting a schema field removes it from all records within the collection, however, references to the schema field in pipelines are not removed.  > Note: This operation cannot be reversed.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import schema_api
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
    api_instance = schema_api.SchemaApi(api_client)
    collection_id = "collection_id_example" # str | The collection the schema field belongs to, e.g. `my-collection`.
    schema_field_name = "schema_field_name_example" # str | The name of the schema field to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete schema field
        api_response = api_instance.delete_schema_field(collection_id, schema_field_name)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling SchemaApi->delete_schema_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection the schema field belongs to, e.g. &#x60;my-collection&#x60;. |
 **schema_field_name** | **str**| The name of the schema field to delete. |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **list_schema_fields**
> ListSchemaFieldsResponse list_schema_fields(collection_id)

List schema fields

Retrieve a list of schema fields in a collection.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import schema_api
from sajari_client.model.list_schema_fields_response import ListSchemaFieldsResponse
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
    api_instance = schema_api.SchemaApi(api_client)
    collection_id = "collection_id_example" # str | The collection that owns this set of schema fields, e.g. `my-collection`.
    page_size = 1 # int | The maximum number of schema fields to return. The service may return fewer than this value.  If unspecified, at most 50 schema fields are returned.  The maximum value is 1000; values above 1000 are coerced to 1000. (optional)
    page_token = "page_token_example" # str | A page token, received from a previous [ListSchemaFields](/docs/api#operation/ListSchemaFields) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListSchemaFields](/docs/api#operation/ListSchemaFields) must match the call that provided the page token. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List schema fields
        api_response = api_instance.list_schema_fields(collection_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling SchemaApi->list_schema_fields: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List schema fields
        api_response = api_instance.list_schema_fields(collection_id, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling SchemaApi->list_schema_fields: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that owns this set of schema fields, e.g. &#x60;my-collection&#x60;. |
 **page_size** | **int**| The maximum number of schema fields to return. The service may return fewer than this value.  If unspecified, at most 50 schema fields are returned.  The maximum value is 1000; values above 1000 are coerced to 1000. | [optional]
 **page_token** | **str**| A page token, received from a previous [ListSchemaFields](/docs/api#operation/ListSchemaFields) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListSchemaFields](/docs/api#operation/ListSchemaFields) must match the call that provided the page token. | [optional]

### Return type

[**ListSchemaFieldsResponse**](ListSchemaFieldsResponse.md)

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

# **update_schema_field**
> SchemaField update_schema_field(collection_id, schema_field_name, schema_field)

Update schema field

Update the details of a schema field.  Only `name` and `description` can be updated.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import schema_api
from sajari_client.model.schema_field import SchemaField
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
    api_instance = schema_api.SchemaApi(api_client)
    collection_id = "collection_id_example" # str | The collection the schema field belongs to, e.g. `my-collection`.
    schema_field_name = "schema_field_name_example" # str | The name of the schema field to update.
    schema_field = SchemaField(
        array=True,
        array_length=1,
        description="description_example",
        mode=SchemaFieldMode("MODE_UNSPECIFIED"),
        name="name_example",
        type=SchemaFieldType("TYPE_UNSPECIFIED"),
    ) # SchemaField | The schema field details to update.
    update_mask = "update_mask_example" # str | The list of fields to update, separated by a comma, e.g. `name,description`.  Each field should be in snake case.  For each field that you want to update, provide a corresponding value in the schema field object containing the new value. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update schema field
        api_response = api_instance.update_schema_field(collection_id, schema_field_name, schema_field)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling SchemaApi->update_schema_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update schema field
        api_response = api_instance.update_schema_field(collection_id, schema_field_name, schema_field, update_mask=update_mask)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling SchemaApi->update_schema_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection the schema field belongs to, e.g. &#x60;my-collection&#x60;. |
 **schema_field_name** | **str**| The name of the schema field to update. |
 **schema_field** | [**SchemaField**](SchemaField.md)| The schema field details to update. |
 **update_mask** | **str**| The list of fields to update, separated by a comma, e.g. &#x60;name,description&#x60;.  Each field should be in snake case.  For each field that you want to update, provide a corresponding value in the schema field object containing the new value. | [optional]

### Return type

[**SchemaField**](SchemaField.md)

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

