# sajari_client.EventsApi

All URIs are relative to *https://api.search.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_event**](EventsApi.md#send_event) | **POST** /v4/events:send | Send event
[**send_event2**](EventsApi.md#send_event2) | **POST** /v4/events:sendEvent | Send event


# **send_event**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} send_event(account_id, send_event_request)

Send event

Send an event to the ranking system after a user interacts with a search result.  When querying a collection, you can set the tracking type of the query request. When it is `CLICK` or `POS_NEG`, a token is generated for each result in the query response. You can use this token to provide feedback to the ranking system. Each time you want to record an event on a particular search result, use the send event call and provide:  - The `name` of the event, e.g. `click`, `purchase`. - The `token` from the search result. - The `weight` to assign to the event, e.g. `1`. - An object containing any additional `metadata`.  For example, to send an event where a customer purchased a product, use the following call:  ```json {   \"name\": \"purchase\",   \"token\": \"eyJ...\",   \"weight\": 1,   \"metadata\": {     \"discount\": 0.2,     \"margin\": 30.0,     \"customer_id\": \"12345\",     \"ui_test_segment\": \"A\"   } } ```  Note: Unlike other API calls, the `SendEvent` call requires the `Account-Id` header to be set to your account ID. This is because other API calls infer the account ID from your API key.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import events_api
from sajari_client.model.send_event_request import SendEventRequest
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
    api_instance = events_api.EventsApi(api_client)
    account_id = "Account-Id_example" # str | Unlike other API calls, the `SendEvent` call requires the `Account-Id` header to be set to your account ID. This is because other API calls infer the account ID from your API key.
    send_event_request = SendEventRequest(
        metadata={
            "key": {},
        },
        name="name_example",
        token="token_example",
        weight=1,
    ) # SendEventRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Send event
        api_response = api_instance.send_event(account_id, send_event_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling EventsApi->send_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Unlike other API calls, the &#x60;SendEvent&#x60; call requires the &#x60;Account-Id&#x60; header to be set to your account ID. This is because other API calls infer the account ID from your API key. |
 **send_event_request** | [**SendEventRequest**](SendEventRequest.md)|  |

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
**400** | Returned when the request contains violations for one or more fields. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_event2**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} send_event2(send_event_request)

Send event

Send an event to the ranking system after a user interacts with a search result.  When querying a collection, you can set the tracking type of the query request. When it is `CLICK` or `POS_NEG`, a token is generated for each result in the query response. You can use this token to provide feedback to the ranking system. Each time you want to record an event on a particular search result, use the send event call and provide:  - The `name` of the event, e.g. `click`, `purchase`. - The `token` from the search result. - The `weight` to assign to the event, e.g. `1`. - An object containing any additional `metadata`.  For example, to send an event where a customer purchased a product, use the following call:  ```json {   \"name\": \"purchase\",   \"token\": \"eyJ...\",   \"weight\": 1,   \"metadata\": {     \"discount\": 0.2,     \"margin\": 30.0,     \"customer_id\": \"12345\",     \"ui_test_segment\": \"A\"   } } ```  Note: Unlike other API calls, the `SendEvent` call requires the `Account-Id` header to be set to your account ID. This is because other API calls infer the account ID from your API key.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import events_api
from sajari_client.model.send_event_request import SendEventRequest
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
    api_instance = events_api.EventsApi(api_client)
    send_event_request = SendEventRequest(
        metadata={
            "key": {},
        },
        name="name_example",
        token="token_example",
        weight=1,
    ) # SendEventRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Send event
        api_response = api_instance.send_event2(send_event_request)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling EventsApi->send_event2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_event_request** | [**SendEventRequest**](SendEventRequest.md)|  |

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
**400** | Returned when the request contains violations for one or more fields. |  -  |
**401** | Returned when the request does not have valid authentication credentials. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

