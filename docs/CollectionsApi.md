# sajari_client.CollectionsApi

All URIs are relative to *https://api-gateway.sajari.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collection**](CollectionsApi.md#create_collection) | **POST** /v4/collections | Create collection
[**delete_collection**](CollectionsApi.md#delete_collection) | **DELETE** /v4/collections/{collection_id} | Delete collection
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /v4/collections/{collection_id} | Get collection
[**list_collections**](CollectionsApi.md#list_collections) | **GET** /v4/collections | List collections
[**query_collection**](CollectionsApi.md#query_collection) | **POST** /v4/collections/{collection_id}:queryCollection | Query collection
[**update_collection**](CollectionsApi.md#update_collection) | **PATCH** /v4/collections/{collection_id} | Update collection


# **create_collection**
> Collection create_collection(collection_id, collection)

Create collection

Create an empty collection.  Before records can be added to a collection, the schema and pipelines for the collection have to be set up. Consider setting up new collections via the Sajari Console, which handles the creation of the schema and pipelines for you.

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.collection import Collection
from sajari_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api-gateway.sajari.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api-gateway.sajari.com"
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The ID to use for the collection.  This must start with an alphanumeric character followed by one or more alphanumeric or `-` characters. Strictly speaking, it must match the regular expression: `^[A-Za-z][A-Za-z0-9\\-]*$`.
    collection = Collection(
        display_name="display_name_example",
        authorized_query_domains=[
            "authorized_query_domains_example",
        ],
    ) # Collection | Details of the collection to create.

    # example passing only required values which don't have defaults set
    try:
        # Create collection
        api_response = api_instance.create_collection(collection_id, collection)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->create_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID to use for the collection.  This must start with an alphanumeric character followed by one or more alphanumeric or &#x60;-&#x60; characters. Strictly speaking, it must match the regular expression: &#x60;^[A-Za-z][A-Za-z0-9\\-]*$&#x60;. |
 **collection** | [**Collection**](Collection.md)| Details of the collection to create. |

### Return type

[**Collection**](Collection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Returned when the request contains violations for one or more fields. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**409** | Returned when the collection already exists. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection**
> bool, date, datetime, dict, float, int, list, str, none_type delete_collection(collection_id)

Delete collection

Delete a collection and all of its associated data.  > Note: This operation cannot be reversed.

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api-gateway.sajari.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api-gateway.sajari.com"
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to delete, e.g. `my-collection`.

    # example passing only required values which don't have defaults set
    try:
        # Delete collection
        api_response = api_instance.delete_collection(collection_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to delete, e.g. &#x60;my-collection&#x60;. |

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
**404** | Returned when the collection was not found. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection**
> Collection get_collection(collection_id)

Get collection

Retrieve the details of a collection.

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.collection import Collection
from sajari_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api-gateway.sajari.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api-gateway.sajari.com"
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to retrieve, e.g. `my-collection`.

    # example passing only required values which don't have defaults set
    try:
        # Get collection
        api_response = api_instance.get_collection(collection_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to retrieve, e.g. &#x60;my-collection&#x60;. |

### Return type

[**Collection**](Collection.md)

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
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collections**
> ListCollectionsResponse list_collections()

List collections

Retrieve a list of collections in the account.

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.list_collections_response import ListCollectionsResponse
from sajari_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api-gateway.sajari.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api-gateway.sajari.com"
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
    api_instance = collections_api.CollectionsApi(api_client)
    page_size = 1 # int | The maximum number of collections to return. The service may return fewer than this value.  If unspecified, at most 50 collections are returned.  The maximum value is 100; values above 100 are coerced to 100. (optional)
    page_token = "page_token_example" # str | A page token, received from a previous [ListCollections](/api#operation/ListCollections) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListCollections](/api#operation/ListCollections) must match the call that provided the page token. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List collections
        api_response = api_instance.list_collections(page_size=page_size, page_token=page_token)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->list_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The maximum number of collections to return. The service may return fewer than this value.  If unspecified, at most 50 collections are returned.  The maximum value is 100; values above 100 are coerced to 100. | [optional]
 **page_token** | **str**| A page token, received from a previous [ListCollections](/api#operation/ListCollections) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListCollections](/api#operation/ListCollections) must match the call that provided the page token. | [optional]

### Return type

[**ListCollectionsResponse**](ListCollectionsResponse.md)

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
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_collection**
> QueryCollectionResponse query_collection(collection_id, query_collection_request)

Query collection

Query the collection to search for records.  The following example demonstrates how to run a simple search for a particular string:  ```json {   \"variables\": { \"q\": \"search terms\" } } ```  For more information:  - See [filtering content](https://docs.sajari.com/user-guide/integrating-search/filters/) - See [tracking in the Go SDK](https://github.com/sajari/sdk-go/blob/v2/session.go) - See [tracking in the JS SDK](https://github.com/sajari/sajari-sdk-js/blob/master/src/session.ts)

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.query_collection_response import QueryCollectionResponse
from sajari_client.model.query_collection_request import QueryCollectionRequest
from sajari_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api-gateway.sajari.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api-gateway.sajari.com"
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to query, e.g. `my-collection`.
    query_collection_request = QueryCollectionRequest(
        pipeline=QueryCollectionRequestPipeline(
            name="name_example",
            version="version_example",
        ),
        variables={},
        tracking=QueryCollectionRequestTracking(
            type=QueryCollectionRequestTrackingType("TYPE_UNSPECIFIED"),
            query_id="query_id_example",
            sequence=1,
            field="field_example",
            data={
                "key": "key_example",
            },
        ),
    ) # QueryCollectionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Query collection
        api_response = api_instance.query_collection(collection_id, query_collection_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->query_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to query, e.g. &#x60;my-collection&#x60;. |
 **query_collection_request** | [**QueryCollectionRequest**](QueryCollectionRequest.md)|  |

### Return type

[**QueryCollectionResponse**](QueryCollectionResponse.md)

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
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection**
> Collection update_collection(collection_id, collection)

Update collection

Update the details of a collection.

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.collection import Collection
from sajari_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api-gateway.sajari.com
# See configuration.py for a list of all supported configuration parameters.
configuration = sajari_client.Configuration(
    host = "https://api-gateway.sajari.com"
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to update, e.g. `my-collection`.
    collection = Collection(
        display_name="display_name_example",
        authorized_query_domains=[
            "authorized_query_domains_example",
        ],
    ) # Collection | Details of the collection to update.
    update_mask = "update_mask_example" # str | The list of fields to be updated, separated by a comma, e.g. `field1,field2`.  Each field should be in snake case, e.g. `display_name`.  For each field that you want to update, provide a corresponding value in the collection object containing the new value. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update collection
        api_response = api_instance.update_collection(collection_id, collection)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->update_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update collection
        api_response = api_instance.update_collection(collection_id, collection, update_mask=update_mask)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->update_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to update, e.g. &#x60;my-collection&#x60;. |
 **collection** | [**Collection**](Collection.md)| Details of the collection to update. |
 **update_mask** | **str**| The list of fields to be updated, separated by a comma, e.g. &#x60;field1,field2&#x60;.  Each field should be in snake case, e.g. &#x60;display_name&#x60;.  For each field that you want to update, provide a corresponding value in the collection object containing the new value. | [optional]

### Return type

[**Collection**](Collection.md)

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
**404** | Returned when the collection was not found. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

