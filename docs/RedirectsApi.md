# sajari_client.RedirectsApi

All URIs are relative to *https://api.search.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_redirect**](RedirectsApi.md#create_redirect) | **POST** /v4/collections/{collection_id}/redirects | Create redirect
[**delete_redirect**](RedirectsApi.md#delete_redirect) | **DELETE** /v4/collections/{collection_id}/redirects/{redirect_id} | Delete redirect
[**get_redirect**](RedirectsApi.md#get_redirect) | **GET** /v4/collections/{collection_id}/redirects/{redirect_id} | Get redirect
[**list_redirects**](RedirectsApi.md#list_redirects) | **GET** /v4/collections/{collection_id}/redirects | List redirects
[**update_redirect**](RedirectsApi.md#update_redirect) | **PATCH** /v4/collections/{collection_id}/redirects/{redirect_id} | Update redirect


# **create_redirect**
> Redirect create_redirect(collection_id, redirect)

Create redirect

Create a new redirect in a collection.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import redirects_api
from sajari_client.model.redirect import Redirect
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
    api_instance = redirects_api.RedirectsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to create a redirect in, e.g. `my-collection`.
    redirect = Redirect(
        condition="condition_example",
        disabled=True,
        target="target_example",
    ) # Redirect | The redirect to create.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create redirect
        api_response = api_instance.create_redirect(collection_id, redirect)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->create_redirect: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create redirect
        api_response = api_instance.create_redirect(collection_id, redirect, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->create_redirect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to create a redirect in, e.g. &#x60;my-collection&#x60;. |
 **redirect** | [**Redirect**](Redirect.md)| The redirect to create. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]

### Return type

[**Redirect**](Redirect.md)

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

# **delete_redirect**
> bool, date, datetime, dict, float, int, list, str, none_type delete_redirect(collection_id, redirect_id)

Delete redirect

Delete a redirect and all of its associated data.  > Note: This operation cannot be reversed.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import redirects_api
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
    api_instance = redirects_api.RedirectsApi(api_client)
    collection_id = "collection_id_example" # str | The collection the redirect belongs to, e.g. `my-collection`.
    redirect_id = "redirect_id_example" # str | The redirect to delete, e.g. `1234`.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete redirect
        api_response = api_instance.delete_redirect(collection_id, redirect_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->delete_redirect: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete redirect
        api_response = api_instance.delete_redirect(collection_id, redirect_id, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->delete_redirect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection the redirect belongs to, e.g. &#x60;my-collection&#x60;. |
 **redirect_id** | **str**| The redirect to delete, e.g. &#x60;1234&#x60;. |
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
**404** | Returned when the redirect was not found. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redirect**
> Redirect get_redirect(collection_id, redirect_id)

Get redirect

Retrieve the details of a redirect.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import redirects_api
from sajari_client.model.redirect import Redirect
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
    api_instance = redirects_api.RedirectsApi(api_client)
    collection_id = "collection_id_example" # str | The collection that owns the redirect, e.g. `my-collection`.
    redirect_id = "redirect_id_example" # str | The redirect to retrieve, e.g. `1234`.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get redirect
        api_response = api_instance.get_redirect(collection_id, redirect_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->get_redirect: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get redirect
        api_response = api_instance.get_redirect(collection_id, redirect_id, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->get_redirect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that owns the redirect, e.g. &#x60;my-collection&#x60;. |
 **redirect_id** | **str**| The redirect to retrieve, e.g. &#x60;1234&#x60;. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]

### Return type

[**Redirect**](Redirect.md)

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

# **list_redirects**
> ListRedirectsResponse list_redirects(collection_id)

List redirects

Retrieve a list of redirects in a collection.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import redirects_api
from sajari_client.model.error import Error
from sajari_client.model.list_redirects_response import ListRedirectsResponse
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
    api_instance = redirects_api.RedirectsApi(api_client)
    collection_id = "collection_id_example" # str | The collection that owns this set of redirects, e.g. `my-collection`.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)
    page_size = 1 # int | The maximum number of redirects to return. The service may return fewer than this value.  If unspecified, at most 50 redirects are returned.  The maximum value is 1000; values above 1000 are coerced to 1000. (optional)
    page_token = "page_token_example" # str | A page token, received from a previous [ListRedirects](/docs/api#operation/ListRedirects) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListRedirects](/docs/api#operation/ListRedirects) must match the call that provided the page token. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List redirects
        api_response = api_instance.list_redirects(collection_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->list_redirects: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List redirects
        api_response = api_instance.list_redirects(collection_id, account_id=account_id, page_size=page_size, page_token=page_token)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->list_redirects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that owns this set of redirects, e.g. &#x60;my-collection&#x60;. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]
 **page_size** | **int**| The maximum number of redirects to return. The service may return fewer than this value.  If unspecified, at most 50 redirects are returned.  The maximum value is 1000; values above 1000 are coerced to 1000. | [optional]
 **page_token** | **str**| A page token, received from a previous [ListRedirects](/docs/api#operation/ListRedirects) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListRedirects](/docs/api#operation/ListRedirects) must match the call that provided the page token. | [optional]

### Return type

[**ListRedirectsResponse**](ListRedirectsResponse.md)

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

# **update_redirect**
> Redirect update_redirect(collection_id, redirect_id, update_mask, redirect)

Update redirect

Update the details of a redirect.  Pass each field that you want to update in the request body. Also specify the name of each field that you want to update in the `update_mask` in the request URL query string. Separate multiple fields with a comma. Fields included in the request body, but not included in the field mask are not updated.  For example, to update the `condition` field, make a `PATCH` request to the URL:  ``` /v4/collections/{collection_id}/redirects/{redirect_id}?update_mask=condition ```  With the JSON body:  ``` {   \"condition\": \"new value\",   \"target\": \"...\" } ```  > Note: In this example `target` is not updated because it is not specified in the `update_mask`.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import redirects_api
from sajari_client.model.redirect import Redirect
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
    api_instance = redirects_api.RedirectsApi(api_client)
    collection_id = "collection_id_example" # str | The collection the redirect belongs to, e.g. `my-collection`.
    redirect_id = "redirect_id_example" # str | The redirect to update, e.g. `1234`.
    update_mask = "update_mask_example" # str | The list of fields to be updated, separated by a comma, e.g. `field1,field2`.  Each field should be in snake case, e.g. `condition`, `target`.  For each field that you want to update, provide a corresponding value in the redirect object containing the new value.
    redirect = Redirect(
        condition="condition_example",
        disabled=True,
        target="target_example",
    ) # Redirect | Details of the redirect to update.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update redirect
        api_response = api_instance.update_redirect(collection_id, redirect_id, update_mask, redirect)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->update_redirect: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update redirect
        api_response = api_instance.update_redirect(collection_id, redirect_id, update_mask, redirect, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling RedirectsApi->update_redirect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection the redirect belongs to, e.g. &#x60;my-collection&#x60;. |
 **redirect_id** | **str**| The redirect to update, e.g. &#x60;1234&#x60;. |
 **update_mask** | **str**| The list of fields to be updated, separated by a comma, e.g. &#x60;field1,field2&#x60;.  Each field should be in snake case, e.g. &#x60;condition&#x60;, &#x60;target&#x60;.  For each field that you want to update, provide a corresponding value in the redirect object containing the new value. |
 **redirect** | [**Redirect**](Redirect.md)| Details of the redirect to update. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]

### Return type

[**Redirect**](Redirect.md)

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
**404** | Returned when the redirect was not found. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

