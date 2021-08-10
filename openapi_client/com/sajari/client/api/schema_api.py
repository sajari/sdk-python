"""
    Sajari API

    Sajari is a smart, highly-configurable, real-time search service that enables thousands of businesses worldwide to provide amazing search experiences on their websites, stores, and applications.  # noqa: E501

    The version of the OpenAPI document: v4
    Contact: support@sajari.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.batch_create_schema_fields_request import BatchCreateSchemaFieldsRequest
from openapi_client.model.batch_create_schema_fields_response import BatchCreateSchemaFieldsResponse
from openapi_client.model.error import Error
from openapi_client.model.list_schema_fields_response import ListSchemaFieldsResponse
from openapi_client.model.schema_field import SchemaField


class SchemaApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __batch_create_schema_fields(
            self,
            collection_id,
            batch_create_schema_fields_request,
            **kwargs
        ):
            """Batch create schema fields  # noqa: E501

            The batch version of the [CreateSchemaField](/api#operation/CreateSchemaField) call.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.batch_create_schema_fields(collection_id, batch_create_schema_fields_request, async_req=True)
            >>> result = thread.get()

            Args:
                collection_id (str): The collection to create the schema fields in, e.g. `my-collection`.
                batch_create_schema_fields_request (BatchCreateSchemaFieldsRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BatchCreateSchemaFieldsResponse
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['collection_id'] = \
                collection_id
            kwargs['batch_create_schema_fields_request'] = \
                batch_create_schema_fields_request
            return self.call_with_http_info(**kwargs)

        self.batch_create_schema_fields = _Endpoint(
            settings={
                'response_type': (BatchCreateSchemaFieldsResponse,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/schemaFields:batchCreate',
                'operation_id': 'batch_create_schema_fields',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'batch_create_schema_fields_request',
                ],
                'required': [
                    'collection_id',
                    'batch_create_schema_fields_request',
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
                    'batch_create_schema_fields_request':
                        (BatchCreateSchemaFieldsRequest,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'batch_create_schema_fields_request': 'body',
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
            api_client=api_client,
            callable=__batch_create_schema_fields
        )

        def __create_schema_field(
            self,
            collection_id,
            schema_field,
            **kwargs
        ):
            """Create schema field  # noqa: E501

            Create a new field in your collection's schema.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_schema_field(collection_id, schema_field, async_req=True)
            >>> result = thread.get()

            Args:
                collection_id (str): The collection to create a schema field in, e.g. `my-collection`.
                schema_field (SchemaField): The schema field to create.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SchemaField
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['collection_id'] = \
                collection_id
            kwargs['schema_field'] = \
                schema_field
            return self.call_with_http_info(**kwargs)

        self.create_schema_field = _Endpoint(
            settings={
                'response_type': (SchemaField,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/schemaFields',
                'operation_id': 'create_schema_field',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'schema_field',
                ],
                'required': [
                    'collection_id',
                    'schema_field',
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
                    'schema_field':
                        (SchemaField,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'schema_field': 'body',
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
            api_client=api_client,
            callable=__create_schema_field
        )

        def __list_schema_fields(
            self,
            collection_id,
            **kwargs
        ):
            """List schema fields  # noqa: E501

            Retrieve a list of schema fields in the collection.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_schema_fields(collection_id, async_req=True)
            >>> result = thread.get()

            Args:
                collection_id (str): The collection that owns this set of schema fields, e.g. `my-collection`.

            Keyword Args:
                page_size (int): The maximum number of schema fields to return. The service may return fewer than this value.  If unspecified, at most 50 schema fields are returned.  The maximum value is 1000; values above 1000 are coerced to 1000.. [optional]
                page_token (str): A page token, received from a previous [ListSchemaFields](/api#operation/ListSchemaFields) call.  Provide this to retrieve the subsequent page.  When paginating, all other parameters provided to [ListSchemaFields](/api#operation/ListSchemaFields) must match the call that provided the page token.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListSchemaFieldsResponse
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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['collection_id'] = \
                collection_id
            return self.call_with_http_info(**kwargs)

        self.list_schema_fields = _Endpoint(
            settings={
                'response_type': (ListSchemaFieldsResponse,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/schemaFields',
                'operation_id': 'list_schema_fields',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'page_size',
                    'page_token',
                ],
                'required': [
                    'collection_id',
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
                    'page_size':
                        (int,),
                    'page_token':
                        (str,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                    'page_size': 'page_size',
                    'page_token': 'page_token',
                },
                'location_map': {
                    'collection_id': 'path',
                    'page_size': 'query',
                    'page_token': 'query',
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
            api_client=api_client,
            callable=__list_schema_fields
        )
