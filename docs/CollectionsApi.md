# sajari_client.CollectionsApi

All URIs are relative to *https://api.search.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collection**](CollectionsApi.md#create_collection) | **POST** /v4/collections | Create collection
[**delete_collection**](CollectionsApi.md#delete_collection) | **DELETE** /v4/collections/{collection_id} | Delete collection
[**experiment**](CollectionsApi.md#experiment) | **POST** /v4/collections/{collection_id}:experiment | Experiment
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /v4/collections/{collection_id} | Get collection
[**list_collections**](CollectionsApi.md#list_collections) | **GET** /v4/collections | List collections
[**query_collection**](CollectionsApi.md#query_collection) | **POST** /v4/collections/{collection_id}:query | Query collection
[**query_collection2**](CollectionsApi.md#query_collection2) | **POST** /v4/collections/{collection_id}:queryCollection | Query collection
[**track_event**](CollectionsApi.md#track_event) | **POST** /v4/collections/{collection_id}:trackEvent | Track event
[**update_collection**](CollectionsApi.md#update_collection) | **PATCH** /v4/collections/{collection_id} | Update collection


# **create_collection**
> Collection create_collection(collection_id, collection)

Create collection

Create an empty collection.  Before records can be added to a collection, the schema and pipelines for the collection have to be set up. Consider setting up new collections via the Search.io Console, which handles the creation of the schema and pipelines for you.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.collection import Collection
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The ID to use for the collection.  This must start with an alphanumeric character followed by one or more alphanumeric or `-` characters. Strictly speaking, it must match the regular expression: `^[A-Za-z][A-Za-z0-9\\-]*$`.
    collection = Collection(
        authorized_query_domains=[
            "authorized_query_domains_example",
        ],
        display_name="display_name_example",
    ) # Collection | Details of the collection to create.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create collection
        api_response = api_instance.create_collection(collection_id, collection)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->create_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create collection
        api_response = api_instance.create_collection(collection_id, collection, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->create_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The ID to use for the collection.  This must start with an alphanumeric character followed by one or more alphanumeric or &#x60;-&#x60; characters. Strictly speaking, it must match the regular expression: &#x60;^[A-Za-z][A-Za-z0-9\\-]*$&#x60;. |
 **collection** | [**Collection**](Collection.md)| Details of the collection to create. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]

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
**0** | An unexpected error response. |  -  |

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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to delete, e.g. `my-collection`.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete collection
        api_response = api_instance.delete_collection(collection_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete collection
        api_response = api_instance.delete_collection(collection_id, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to delete, e.g. &#x60;my-collection&#x60;. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]

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
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiment**
> ExperimentResponse experiment(collection_id, experiment_request)

Experiment

Run a query on a collection with a hypothetical configuration to see what kinds of results it produces.  Saved promotions with a start date in the future are enabled during the experiment, unless they are explicitly disabled.  The following example demonstrates how to run a simple experiment for a string, against a pipeline and with a proposed promotion:  ```json {   \"pipeline\": { \"name\": \"my-pipeline\" },   \"variables\": { \"q\": \"search terms\" },   \"promotions\": [{     \"id\": \"1234\",     \"condition\": \"q = 'search terms'\",     \"pins\": [{       \"key\": { \"field\": \"id\", \"value\": \"54hdc7h2334h\" },       \"position\": 1     }]   }] } ```

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.error import Error
from sajari_client.model.experiment_response import ExperimentResponse
from sajari_client.model.experiment_request import ExperimentRequest
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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to query, e.g. `my-collection`.
    experiment_request = ExperimentRequest(
        custom_pipeline=Pipeline(
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
        ),
        pipeline=ExperimentRequestPipeline(
            name="name_example",
            version="version_example",
        ),
        promotions=[
            Promotion(
                banners=[
                    Banner(
                        description="description_example",
                        height=1,
                        id="id_example",
                        image_url="image_url_example",
                        position=1,
                        target_url="target_url_example",
                        text_color="text_color_example",
                        text_position=TextPosition("TEXT_POSITION_UNSPECIFIED"),
                        title="title_example",
                        width=1,
                    ),
                ],
                condition="condition_example",
                disabled=True,
                display_name="display_name_example",
                end_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                exclusions=[
                    PromotionExclusion(
                        key=RecordKey(
                            field="field_example",
                            value="value_example",
                        ),
                    ),
                ],
                filter_boosts=[
                    PromotionFilterBoost(
                        boost=3.14,
                        filter="filter_example",
                    ),
                ],
                filter_conditions=[
                    PromotionFilterCondition(
                        filter=[
                            "filter_example",
                        ],
                    ),
                ],
                id="id_example",
                pins=[
                    PromotionPin(
                        key=RecordKey(
                            field="field_example",
                            value="value_example",
                        ),
                        mode=PromotionPinMode("PIN"),
                        position=1,
                    ),
                ],
                range_boosts=[
                    PromotionRangeBoost(
                        boost=3.14,
                        end=3.14,
                        field="field_example",
                        null_boost=3.14,
                        start=3.14,
                    ),
                ],
                start_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        variables={
            "key": {},
        },
    ) # ExperimentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Experiment
        api_response = api_instance.experiment(collection_id, experiment_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->experiment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to query, e.g. &#x60;my-collection&#x60;. |
 **experiment_request** | [**ExperimentRequest**](ExperimentRequest.md)|  |

### Return type

[**ExperimentResponse**](ExperimentResponse.md)

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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to retrieve, e.g. `my-collection`.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)
    view = "VIEW_UNSPECIFIED" # str | The amount of information to include in the retrieved pipeline.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the `BASIC` view.  - BASIC: Include basic information including display name and domains. This is the default value (for both [ListCollections](/docs/api#operation/ListCollections) and [GetCollection](/docs/api#operation/GetCollection)).  - FULL: Include the information from `BASIC`, plus full collection details like disk usage. (optional) if omitted the server will use the default value of "VIEW_UNSPECIFIED"

    # example passing only required values which don't have defaults set
    try:
        # Get collection
        api_response = api_instance.get_collection(collection_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get collection
        api_response = api_instance.get_collection(collection_id, account_id=account_id, view=view)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to retrieve, e.g. &#x60;my-collection&#x60;. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]
 **view** | **str**| The amount of information to include in the retrieved pipeline.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the &#x60;BASIC&#x60; view.  - BASIC: Include basic information including display name and domains. This is the default value (for both [ListCollections](/docs/api#operation/ListCollections) and [GetCollection](/docs/api#operation/GetCollection)).  - FULL: Include the information from &#x60;BASIC&#x60;, plus full collection details like disk usage. | [optional] if omitted the server will use the default value of "VIEW_UNSPECIFIED"

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
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collections**
> ListCollectionsResponse list_collections()

List collections

Retrieve a list of collections in an account.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.list_collections_response import ListCollectionsResponse
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
    api_instance = collections_api.CollectionsApi(api_client)
    account_id = "Account-Id_example" # str | The account that owns this set of collections, e.g. `1618535966441231024`. (optional)
    page_size = 1 # int | The maximum number of collections to return. The service may return fewer than this value.  If unspecified, at most 50 collections are returned.  The maximum value is 100; values above 100 are coerced to 100. (optional)
    page_token = "page_token_example" # str | A page token, received from a previous [ListCollections](/docs/api#operation/ListCollections) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListCollections](/docs/api#operation/ListCollections) must match the call that provided the page token. (optional)
    view = "VIEW_UNSPECIFIED" # str | The amount of information to include in each retrieved collection.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the `BASIC` view.  - BASIC: Include basic information including display name and domains. This is the default value (for both [ListCollections](/docs/api#operation/ListCollections) and [GetCollection](/docs/api#operation/GetCollection)).  - FULL: Include the information from `BASIC`, plus full collection details like disk usage. (optional) if omitted the server will use the default value of "VIEW_UNSPECIFIED"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List collections
        api_response = api_instance.list_collections(account_id=account_id, page_size=page_size, page_token=page_token, view=view)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->list_collections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account that owns this set of collections, e.g. &#x60;1618535966441231024&#x60;. | [optional]
 **page_size** | **int**| The maximum number of collections to return. The service may return fewer than this value.  If unspecified, at most 50 collections are returned.  The maximum value is 100; values above 100 are coerced to 100. | [optional]
 **page_token** | **str**| A page token, received from a previous [ListCollections](/docs/api#operation/ListCollections) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListCollections](/docs/api#operation/ListCollections) must match the call that provided the page token. | [optional]
 **view** | **str**| The amount of information to include in each retrieved collection.   - VIEW_UNSPECIFIED: The default / unset value. The API defaults to the &#x60;BASIC&#x60; view.  - BASIC: Include basic information including display name and domains. This is the default value (for both [ListCollections](/docs/api#operation/ListCollections) and [GetCollection](/docs/api#operation/GetCollection)).  - FULL: Include the information from &#x60;BASIC&#x60;, plus full collection details like disk usage. | [optional] if omitted the server will use the default value of "VIEW_UNSPECIFIED"

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
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_collection**
> QueryCollectionResponse query_collection(collection_id, query_collection_request)

Query collection

Query the collection to search for records.  The following example demonstrates how to run a simple search for a particular string:  ```json {   \"variables\": { \"q\": \"search terms\" } } ```  For more information:  - See [filtering content](https://docs.search.io/documentation/fundamentals/integrating-search/filters-and-sort-options) - See [tracking in the Go SDK](https://github.com/sajari/sdk-go/blob/v2/session.go) - See [tracking in the JS SDK](https://github.com/sajari/sdk-js/blob/554e182e77d3ba99a9c100b208ebf3be414d2067/src/index.ts#L881)  Note: Unlike other API calls, the `QueryCollection` call can be called from a browser. When called from a browser, the `Account-Id` header must be set to your account ID.

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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to query, e.g. `my-collection`.
    query_collection_request = QueryCollectionRequest(
        pipeline=QueryCollectionRequestPipeline(
            name="name_example",
            version="version_example",
        ),
        tracking=QueryCollectionRequestTracking(
            data={
                "key": "key_example",
            },
            field="field_example",
            query_id="query_id_example",
            sequence=1,
            type=QueryCollectionRequestTrackingType("TYPE_UNSPECIFIED"),
        ),
        variables={
            "key": {},
        },
    ) # QueryCollectionRequest | 
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`.  Unlike other API calls, the `QueryCollection` call can be called from a browser. When called from a browser, the `Account-Id` header must be set to your account ID. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Query collection
        api_response = api_instance.query_collection(collection_id, query_collection_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->query_collection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Query collection
        api_response = api_instance.query_collection(collection_id, query_collection_request, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->query_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to query, e.g. &#x60;my-collection&#x60;. |
 **query_collection_request** | [**QueryCollectionRequest**](QueryCollectionRequest.md)|  |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;.  Unlike other API calls, the &#x60;QueryCollection&#x60; call can be called from a browser. When called from a browser, the &#x60;Account-Id&#x60; header must be set to your account ID. | [optional]

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
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_collection2**
> QueryCollectionResponse query_collection2(collection_id, query_collection_request)

Query collection

Query the collection to search for records.  The following example demonstrates how to run a simple search for a particular string:  ```json {   \"variables\": { \"q\": \"search terms\" } } ```  For more information:  - See [filtering content](https://docs.search.io/documentation/fundamentals/integrating-search/filters-and-sort-options) - See [tracking in the Go SDK](https://github.com/sajari/sdk-go/blob/v2/session.go) - See [tracking in the JS SDK](https://github.com/sajari/sdk-js/blob/554e182e77d3ba99a9c100b208ebf3be414d2067/src/index.ts#L881)  Note: Unlike other API calls, the `QueryCollection` call can be called from a browser. When called from a browser, the `Account-Id` header must be set to your account ID.

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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to query, e.g. `my-collection`.
    query_collection_request = QueryCollectionRequest(
        pipeline=QueryCollectionRequestPipeline(
            name="name_example",
            version="version_example",
        ),
        tracking=QueryCollectionRequestTracking(
            data={
                "key": "key_example",
            },
            field="field_example",
            query_id="query_id_example",
            sequence=1,
            type=QueryCollectionRequestTrackingType("TYPE_UNSPECIFIED"),
        ),
        variables={
            "key": {},
        },
    ) # QueryCollectionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Query collection
        api_response = api_instance.query_collection2(collection_id, query_collection_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->query_collection2: %s\n" % e)
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
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_event**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} track_event(account_id, collection_id, event)

Track event

Track an analytics event when a user interacts with an object returned by a [QueryCollection](/docs/api/#operation/QueryCollection) request.  An analytics event can be tracked for the following objects:  - Results - Promotion banners - Redirects  When tracking redirect events, set `type` to `redirect`.  Note: You must pass an `Account-Id` header.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import collections_api
from sajari_client.model.error import Error
from sajari_client.model.event import Event
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
    api_instance = collections_api.CollectionsApi(api_client)
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`.
    collection_id = "collection_id_example" # str | The collection to track the event against, e.g. `my-collection`.
    event = Event(
        banner_id="banner_id_example",
        metadata={
            "key": {},
        },
        query_id="query_id_example",
        redirect_id="redirect_id_example",
        result_id="result_id_example",
        type="type_example",
    ) # Event | The details of the event to track.

    # example passing only required values which don't have defaults set
    try:
        # Track event
        api_response = api_instance.track_event(account_id, collection_id, event)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->track_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. |
 **collection_id** | **str**| The collection to track the event against, e.g. &#x60;my-collection&#x60;. |
 **event** | [**Event**](Event.md)| The details of the event to track. |

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
    api_instance = collections_api.CollectionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to update, e.g. `my-collection`.
    collection = Collection(
        authorized_query_domains=[
            "authorized_query_domains_example",
        ],
        display_name="display_name_example",
    ) # Collection | The details of the collection to update.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)
    update_mask = "update_mask_example" # str | The list of fields to update, separated by a comma, e.g. `authorized_query_domains,display_name`.  Each field should be in snake case.  For each field that you want to update, provide a corresponding value in the collection object containing the new value. (optional)

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
        api_response = api_instance.update_collection(collection_id, collection, account_id=account_id, update_mask=update_mask)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling CollectionsApi->update_collection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to update, e.g. &#x60;my-collection&#x60;. |
 **collection** | [**Collection**](Collection.md)| The details of the collection to update. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]
 **update_mask** | **str**| The list of fields to update, separated by a comma, e.g. &#x60;authorized_query_domains,display_name&#x60;.  Each field should be in snake case.  For each field that you want to update, provide a corresponding value in the collection object containing the new value. | [optional]

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
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

