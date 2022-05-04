# sajari_client.PromotionsApi

All URIs are relative to *https://api.search.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_promotion**](PromotionsApi.md#create_promotion) | **POST** /v4/collections/{collection_id}/promotions | Create promotion
[**delete_promotion**](PromotionsApi.md#delete_promotion) | **DELETE** /v4/collections/{collection_id}/promotions/{promotion_id} | Delete promotion
[**get_promotion**](PromotionsApi.md#get_promotion) | **GET** /v4/collections/{collection_id}/promotions/{promotion_id} | Get promotion
[**list_promotions**](PromotionsApi.md#list_promotions) | **GET** /v4/collections/{collection_id}/promotions | List promotions
[**update_promotion**](PromotionsApi.md#update_promotion) | **PATCH** /v4/collections/{collection_id}/promotions/{promotion_id} | Update promotion


# **create_promotion**
> Promotion create_promotion(collection_id, promotion)

Create promotion

Create a new promotion in a collection.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import promotions_api
from sajari_client.model.promotion import Promotion
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
    api_instance = promotions_api.PromotionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection to create a promotion in, e.g. `my-collection`.
    promotion = Promotion(
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
    ) # Promotion | The promotion to create.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create promotion
        api_response = api_instance.create_promotion(collection_id, promotion)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->create_promotion: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create promotion
        api_response = api_instance.create_promotion(collection_id, promotion, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->create_promotion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection to create a promotion in, e.g. &#x60;my-collection&#x60;. |
 **promotion** | [**Promotion**](Promotion.md)| The promotion to create. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]

### Return type

[**Promotion**](Promotion.md)

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

# **delete_promotion**
> bool, date, datetime, dict, float, int, list, str, none_type delete_promotion(collection_id, promotion_id)

Delete promotion

Delete a promotion and all of its associated data.  > Note: This operation cannot be reversed.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import promotions_api
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
    api_instance = promotions_api.PromotionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection the promotion belongs to, e.g. `my-collection`.
    promotion_id = "promotion_id_example" # str | The promotion to delete, e.g. `1234`.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete promotion
        api_response = api_instance.delete_promotion(collection_id, promotion_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->delete_promotion: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete promotion
        api_response = api_instance.delete_promotion(collection_id, promotion_id, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->delete_promotion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection the promotion belongs to, e.g. &#x60;my-collection&#x60;. |
 **promotion_id** | **str**| The promotion to delete, e.g. &#x60;1234&#x60;. |
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
**404** | Returned when the promotion was not found. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_promotion**
> Promotion get_promotion(collection_id, promotion_id)

Get promotion

Retrieve the details of a promotion.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import promotions_api
from sajari_client.model.promotion import Promotion
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
    api_instance = promotions_api.PromotionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection that owns the promotion, e.g. `my-collection`.
    promotion_id = "promotion_id_example" # str | The promotion to retrieve, e.g. `1234`.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get promotion
        api_response = api_instance.get_promotion(collection_id, promotion_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->get_promotion: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get promotion
        api_response = api_instance.get_promotion(collection_id, promotion_id, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->get_promotion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that owns the promotion, e.g. &#x60;my-collection&#x60;. |
 **promotion_id** | **str**| The promotion to retrieve, e.g. &#x60;1234&#x60;. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]

### Return type

[**Promotion**](Promotion.md)

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

# **list_promotions**
> ListPromotionsResponse list_promotions(collection_id)

List promotions

Retrieve a list of promotions in a collection.  Promotion pins, exclusions and filter boosts are not returned in this call.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import promotions_api
from sajari_client.model.error import Error
from sajari_client.model.list_promotions_response import ListPromotionsResponse
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
    api_instance = promotions_api.PromotionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection that owns this set of promotions, e.g. `my-collection`.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)
    page_size = 1 # int | The maximum number of promotions to return. The service may return fewer than this value.  If unspecified, at most 50 promotions are returned.  The maximum value is 1000; values above 1000 are coerced to 1000. (optional)
    page_token = "page_token_example" # str | A page token, received from a previous [ListPromotions](/docs/api#operation/ListPromotions) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListPromotions](/docs/api#operation/ListPromotions) must match the call that provided the page token. (optional)
    view = "PROMOTION_VIEW_UNSPECIFIED" # str | The amount of information to include in each retrieved promotion.   - PROMOTION_VIEW_UNSPECIFIED: The default / unset value. The API defaults to the `FULL` view.  - BASIC: Include basic information including name, start time and end time, but not detailed information about the promotion effects.  - FULL: Returns all information about a promotion. This is the default value. (optional) if omitted the server will use the default value of "PROMOTION_VIEW_UNSPECIFIED"

    # example passing only required values which don't have defaults set
    try:
        # List promotions
        api_response = api_instance.list_promotions(collection_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->list_promotions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List promotions
        api_response = api_instance.list_promotions(collection_id, account_id=account_id, page_size=page_size, page_token=page_token, view=view)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->list_promotions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection that owns this set of promotions, e.g. &#x60;my-collection&#x60;. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]
 **page_size** | **int**| The maximum number of promotions to return. The service may return fewer than this value.  If unspecified, at most 50 promotions are returned.  The maximum value is 1000; values above 1000 are coerced to 1000. | [optional]
 **page_token** | **str**| A page token, received from a previous [ListPromotions](/docs/api#operation/ListPromotions) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListPromotions](/docs/api#operation/ListPromotions) must match the call that provided the page token. | [optional]
 **view** | **str**| The amount of information to include in each retrieved promotion.   - PROMOTION_VIEW_UNSPECIFIED: The default / unset value. The API defaults to the &#x60;FULL&#x60; view.  - BASIC: Include basic information including name, start time and end time, but not detailed information about the promotion effects.  - FULL: Returns all information about a promotion. This is the default value. | [optional] if omitted the server will use the default value of "PROMOTION_VIEW_UNSPECIFIED"

### Return type

[**ListPromotionsResponse**](ListPromotionsResponse.md)

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

# **update_promotion**
> Promotion update_promotion(collection_id, promotion_id, update_mask, promotion)

Update promotion

Update the details of a promotion.  Pass each field that you want to update in the request body. Also specify the name of each field that you want to update in the `update_mask` in the request URL query string. Separate multiple fields with a comma. Fields included in the request body, but not included in the field mask are not updated.  For example, to update the `display_name` and `start_time` fields, make a `PATCH` request to the URL:  ``` /v4/collections/{collection_id}/promotions/{promotion_id}?update_mask=display_name,start_time ```  With the JSON body:  ``` {   \"display_name\": \"new value\",   \"start_time\": \"2006-01-02T15:04:05Z07:00\",   \"end_time\": \"2006-01-02T15:04:05Z07:00\" } ```  > Note: In this example `end_time` is not updated because it is not specified in the `update_mask`.

### Example

* Basic Authentication (BasicAuth):

```python
import time
import sajari_client
from sajari_client.api import promotions_api
from sajari_client.model.promotion import Promotion
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
    api_instance = promotions_api.PromotionsApi(api_client)
    collection_id = "collection_id_example" # str | The collection the promotion belongs to, e.g. `my-collection`.
    promotion_id = "promotion_id_example" # str | The promotion to update, e.g. `1234`.
    update_mask = "update_mask_example" # str | The list of fields to be updated, separated by a comma, e.g. `field1,field2`.  Each field should be in snake case, e.g. `display_name`, `filter_boosts`.  For each field that you want to update, provide a corresponding value in the promotion object containing the new value.
    promotion = Promotion(
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
    ) # Promotion | Details of the promotion to update.
    account_id = "Account-Id_example" # str | The account that owns the collection, e.g. `1618535966441231024`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update promotion
        api_response = api_instance.update_promotion(collection_id, promotion_id, update_mask, promotion)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->update_promotion: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update promotion
        api_response = api_instance.update_promotion(collection_id, promotion_id, update_mask, promotion, account_id=account_id)
        pprint(api_response)
    except sajari_client.ApiException as e:
        print("Exception when calling PromotionsApi->update_promotion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| The collection the promotion belongs to, e.g. &#x60;my-collection&#x60;. |
 **promotion_id** | **str**| The promotion to update, e.g. &#x60;1234&#x60;. |
 **update_mask** | **str**| The list of fields to be updated, separated by a comma, e.g. &#x60;field1,field2&#x60;.  Each field should be in snake case, e.g. &#x60;display_name&#x60;, &#x60;filter_boosts&#x60;.  For each field that you want to update, provide a corresponding value in the promotion object containing the new value. |
 **promotion** | [**Promotion**](Promotion.md)| Details of the promotion to update. |
 **account_id** | **str**| The account that owns the collection, e.g. &#x60;1618535966441231024&#x60;. | [optional]

### Return type

[**Promotion**](Promotion.md)

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
**404** | Returned when the promotion was not found. |  -  |
**500** | Returned when the API encounters an internal error. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

