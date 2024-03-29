"""
    Search.io API

    The version of the OpenAPI document: 4.0.0
    Contact: support@search.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from sajari_client.api_client import ApiClient, Endpoint as _Endpoint
from sajari_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from sajari_client.model.error import Error
from sajari_client.model.list_promotions_response import ListPromotionsResponse
from sajari_client.model.promotion import Promotion


class PromotionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_promotion_endpoint = _Endpoint(
            settings={
                'response_type': (Promotion,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/promotions',
                'operation_id': 'create_promotion',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'promotion',
                    'account_id',
                ],
                'required': [
                    'collection_id',
                    'promotion',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'collection_id':
                        (str,),
                    'promotion':
                        (Promotion,),
                    'account_id':
                        (str,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                    'account_id': 'Account-Id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'promotion': 'body',
                    'account_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_promotion_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/promotions/{promotion_id}',
                'operation_id': 'delete_promotion',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'promotion_id',
                    'account_id',
                ],
                'required': [
                    'collection_id',
                    'promotion_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'collection_id':
                        (str,),
                    'promotion_id':
                        (str,),
                    'account_id':
                        (str,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                    'promotion_id': 'promotion_id',
                    'account_id': 'Account-Id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'promotion_id': 'path',
                    'account_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_promotion_endpoint = _Endpoint(
            settings={
                'response_type': (Promotion,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/promotions/{promotion_id}',
                'operation_id': 'get_promotion',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'promotion_id',
                    'account_id',
                ],
                'required': [
                    'collection_id',
                    'promotion_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'collection_id':
                        (str,),
                    'promotion_id':
                        (str,),
                    'account_id':
                        (str,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                    'promotion_id': 'promotion_id',
                    'account_id': 'Account-Id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'promotion_id': 'path',
                    'account_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_promotions_endpoint = _Endpoint(
            settings={
                'response_type': (ListPromotionsResponse,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/promotions',
                'operation_id': 'list_promotions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'account_id',
                    'page_size',
                    'page_token',
                    'view',
                ],
                'required': [
                    'collection_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'view',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('view',): {

                        "PROMOTION_VIEW_UNSPECIFIED": "PROMOTION_VIEW_UNSPECIFIED",
                        "BASIC": "BASIC",
                        "FULL": "FULL"
                    },
                },
                'openapi_types': {
                    'collection_id':
                        (str,),
                    'account_id':
                        (str,),
                    'page_size':
                        (int,),
                    'page_token':
                        (str,),
                    'view':
                        (str,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                    'account_id': 'Account-Id',
                    'page_size': 'page_size',
                    'page_token': 'page_token',
                    'view': 'view',
                },
                'location_map': {
                    'collection_id': 'path',
                    'account_id': 'header',
                    'page_size': 'query',
                    'page_token': 'query',
                    'view': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_promotion_endpoint = _Endpoint(
            settings={
                'response_type': (Promotion,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/promotions/{promotion_id}',
                'operation_id': 'update_promotion',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'promotion_id',
                    'update_mask',
                    'promotion',
                    'account_id',
                ],
                'required': [
                    'collection_id',
                    'promotion_id',
                    'update_mask',
                    'promotion',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'collection_id':
                        (str,),
                    'promotion_id':
                        (str,),
                    'update_mask':
                        (str,),
                    'promotion':
                        (Promotion,),
                    'account_id':
                        (str,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                    'promotion_id': 'promotion_id',
                    'update_mask': 'update_mask',
                    'account_id': 'Account-Id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'promotion_id': 'path',
                    'update_mask': 'query',
                    'promotion': 'body',
                    'account_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_promotion(
        self,
        collection_id,
        promotion,
        **kwargs
    ):
        """Create promotion  # noqa: E501

        Create a new promotion in a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_promotion(collection_id, promotion, async_req=True)
        >>> result = thread.get()

        Args:
            collection_id (str): The collection to create a promotion in, e.g. `my-collection`.
            promotion (Promotion): The promotion to create.

        Keyword Args:
            account_id (str): The account that owns the collection, e.g. `1618535966441231024`.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Promotion
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['collection_id'] = \
            collection_id
        kwargs['promotion'] = \
            promotion
        return self.create_promotion_endpoint.call_with_http_info(**kwargs)

    def delete_promotion(
        self,
        collection_id,
        promotion_id,
        **kwargs
    ):
        """Delete promotion  # noqa: E501

        Delete a promotion and all of its associated data.  > Note: This operation cannot be reversed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_promotion(collection_id, promotion_id, async_req=True)
        >>> result = thread.get()

        Args:
            collection_id (str): The collection the promotion belongs to, e.g. `my-collection`.
            promotion_id (str): The promotion to delete, e.g. `1234`.

        Keyword Args:
            account_id (str): The account that owns the collection, e.g. `1618535966441231024`.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['collection_id'] = \
            collection_id
        kwargs['promotion_id'] = \
            promotion_id
        return self.delete_promotion_endpoint.call_with_http_info(**kwargs)

    def get_promotion(
        self,
        collection_id,
        promotion_id,
        **kwargs
    ):
        """Get promotion  # noqa: E501

        Retrieve the details of a promotion.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_promotion(collection_id, promotion_id, async_req=True)
        >>> result = thread.get()

        Args:
            collection_id (str): The collection that owns the promotion, e.g. `my-collection`.
            promotion_id (str): The promotion to retrieve, e.g. `1234`.

        Keyword Args:
            account_id (str): The account that owns the collection, e.g. `1618535966441231024`.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Promotion
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['collection_id'] = \
            collection_id
        kwargs['promotion_id'] = \
            promotion_id
        return self.get_promotion_endpoint.call_with_http_info(**kwargs)

    def list_promotions(
        self,
        collection_id,
        **kwargs
    ):
        """List promotions  # noqa: E501

        Retrieve a list of promotions in a collection.  Promotion pins, exclusions and filter boosts are not returned in this call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_promotions(collection_id, async_req=True)
        >>> result = thread.get()

        Args:
            collection_id (str): The collection that owns this set of promotions, e.g. `my-collection`.

        Keyword Args:
            account_id (str): The account that owns the collection, e.g. `1618535966441231024`.. [optional]
            page_size (int): The maximum number of promotions to return. The service may return fewer than this value.  If unspecified, at most 50 promotions are returned.  The maximum value is 1000; values above 1000 are coerced to 1000.. [optional]
            page_token (str): A page token, received from a previous [ListPromotions](/docs/api#operation/ListPromotions) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListPromotions](/docs/api#operation/ListPromotions) must match the call that provided the page token.. [optional]
            view (str): The amount of information to include in each retrieved promotion.   - BASIC: Include basic information including name, start time and end time, but not detailed information about the promotion effects.  - FULL: Returns all information about a promotion. This is the default value.. [optional] if omitted the server will use the default value of "PROMOTION_VIEW_UNSPECIFIED"
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ListPromotionsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['collection_id'] = \
            collection_id
        return self.list_promotions_endpoint.call_with_http_info(**kwargs)

    def update_promotion(
        self,
        collection_id,
        promotion_id,
        update_mask,
        promotion,
        **kwargs
    ):
        """Update promotion  # noqa: E501

        Update the details of a promotion.  Pass each field that you want to update in the request body. Also specify the name of each field that you want to update in the `update_mask` in the request URL query string. Separate multiple fields with a comma. Fields included in the request body, but not included in the field mask are not updated.  For example, to update the `display_name` and `start_time` fields, make a `PATCH` request to the URL:  ``` /v4/collections/{collection_id}/promotions/{promotion_id}?update_mask=display_name,start_time ```  With the JSON body:  ``` {   \"display_name\": \"new value\",   \"start_time\": \"2006-01-02T15:04:05Z07:00\",   \"end_time\": \"2006-01-02T15:04:05Z07:00\" } ```  > Note: In this example `end_time` is not updated because it is not specified in the `update_mask`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_promotion(collection_id, promotion_id, update_mask, promotion, async_req=True)
        >>> result = thread.get()

        Args:
            collection_id (str): The collection the promotion belongs to, e.g. `my-collection`.
            promotion_id (str): The promotion to update, e.g. `1234`.
            update_mask (str): The list of fields to be updated, separated by a comma, e.g. `field1,field2`.  Each field should be in snake case, e.g. `display_name`, `filter_boosts`.  For each field that you want to update, provide a corresponding value in the promotion object containing the new value.
            promotion (Promotion): Details of the promotion to update.

        Keyword Args:
            account_id (str): The account that owns the collection, e.g. `1618535966441231024`.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Promotion
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['collection_id'] = \
            collection_id
        kwargs['promotion_id'] = \
            promotion_id
        kwargs['update_mask'] = \
            update_mask
        kwargs['promotion'] = \
            promotion
        return self.update_promotion_endpoint.call_with_http_info(**kwargs)

