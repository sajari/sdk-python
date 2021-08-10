# sajari_client.RecordsApi

All URIs are relative to *https://api-gateway.sajari.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_upsert_records**](RecordsApi.md#batch_upsert_records) | **POST** /v4/collections/{collection_id}/records:batchUpsert | Batch upsert records
[**delete_record**](RecordsApi.md#delete_record) | **POST** /v4/collections/{collection_id}/records:delete | Delete record
[**get_record**](RecordsApi.md#get_record) | **POST** /v4/collections/{collection_id}/records:get | Get record
[**upsert_record**](RecordsApi.md#upsert_record) | **POST** /v4/collections/{collection_id}/records:upsert | Upsert record


# **batch_upsert_records**
> BatchUpsertRecordsResponse batch_upsert_records(collection_id, batch_upsert_records_request)

Batch upsert records

The batch version of the [UpsertRecord](/api#operation/UpsertRecord) call.

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from com.sajari.client.api import records_api
from sajari_client.model.batch_upsert_records_request import BatchUpsertRecordsRequest
from sajari_client.model.batch_upsert_records_response import BatchUpsertRecordsResponse
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
    api_instance = records_api.RecordsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to upsert the records in, e.g. `my-collection`.
    batch_upsert_records_request = BatchUpsertRecordsRequest(
        pipeline=BatchUpsertRecordsRequestPipeline(
            name="name_example",
            version="version_example",
        ),
        records=[
            {},
        ],
        variables={},
    ) # BatchUpsertRecordsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Batch upsert records
        api_response = api_instance.batch_upsert_records(collection_id, batch_upsert_records_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RecordsApi->batch_upsert_records: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to upsert the records in, e.g. &#x60;my-collection&#x60;. |
 **batch_upsert_records_request** | [**BatchUpsertRecordsRequest**](BatchUpsertRecordsRequest.md)|  |

### Return type

[**BatchUpsertRecordsResponse**](BatchUpsertRecordsResponse.md)

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

# **delete_record**
> bool, date, datetime, dict, float, int, list, str, none_type delete_record(collection_id, delete_record_request)

Delete record

Delete a record with the given key.

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from com.sajari.client.api import records_api
from sajari_client.model.delete_record_request import DeleteRecordRequest
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
    api_instance = records_api.RecordsApi(api_client)
    collection_id = "collection_id_example" # str | The collection that contains the record to delete, e.g. `my-collection`.
    delete_record_request = DeleteRecordRequest(
        key=RecordKey(
            field="field_example",
            value="value_example",
        ),
    ) # DeleteRecordRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Delete record
        api_response = api_instance.delete_record(collection_id, delete_record_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RecordsApi->delete_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that contains the record to delete, e.g. &#x60;my-collection&#x60;. |
 **delete_record_request** | [**DeleteRecordRequest**](DeleteRecordRequest.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

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

# **get_record**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_record(collection_id, get_record_request)

Get record

Retrieve a record with the given key.

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from com.sajari.client.api import records_api
from sajari_client.model.get_record_request import GetRecordRequest
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
    api_instance = records_api.RecordsApi(api_client)
    collection_id = "collection_id_example" # str | The collection that contains the record to retrieve, e.g. `my-collection`.
    get_record_request = GetRecordRequest(
        key=RecordKey(
            field="field_example",
            value="value_example",
        ),
    ) # GetRecordRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get record
        api_response = api_instance.get_record(collection_id, get_record_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RecordsApi->get_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that contains the record to retrieve, e.g. &#x60;my-collection&#x60;. |
 **get_record_request** | [**GetRecordRequest**](GetRecordRequest.md)|  |

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
**0** | An unexpected error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_record**
> UpsertRecordResponse upsert_record(collection_id, upsert_record_request)

Upsert record

If the record does not exist in your collection it is inserted. If it does exist it is updated.  If no pipeline is specified, the default record pipeline is used to process the record.  If the record is inserted, the response contains the key of the inserted record. You can use this if you need to retrieve or delete the record. If the record is updated, the response does not contain a key. Callers can use this as a signal to determine if the record is inserted/created or updated.  For example, to add a single product from your ecommerce store to a collection, use the following call:  ```json {   \"pipeline\": {     \"name\": \"my-pipeline\",     \"version\": \"1\"   },   \"record\": {     \"id\": \"54hdc7h2334h\",     \"name\": \"Smart TV\",     \"price\": 1999,     \"brand\": \"Acme\",     \"description\": \"...\",     \"in_stock\": true   } } ```

### Example

* Basic Authentication (BasicAuth):
```python
import time
import sajari_client
from com.sajari.client.api import records_api
from sajari_client.model.upsert_record_request import UpsertRecordRequest
from sajari_client.model.upsert_record_response import UpsertRecordResponse
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
    api_instance = records_api.RecordsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to upsert the record in, e.g. `my-collection`.
    upsert_record_request = UpsertRecordRequest(
        pipeline=UpsertRecordRequestPipeline(
            name="name_example",
            version="version_example",
        ),
        record={},
        variables={},
    ) # UpsertRecordRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Upsert record
        api_response = api_instance.upsert_record(collection_id, upsert_record_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RecordsApi->upsert_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to upsert the record in, e.g. &#x60;my-collection&#x60;. |
 **upsert_record_request** | [**UpsertRecordRequest**](UpsertRecordRequest.md)|  |

### Return type

[**UpsertRecordResponse**](UpsertRecordResponse.md)

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

