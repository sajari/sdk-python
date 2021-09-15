"""
    Sajari API

    Sajari is a smart, highly-configurable, real-time search service that enables thousands of businesses worldwide to provide amazing search experiences on their websites, stores, and applications.  # noqa: E501

    The version of the OpenAPI document: v4
    Contact: support@sajari.com
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from sajari_client.api_client import ApiClient, Endpoint as _Endpoint
from sajari_client.model.batch_upsert_records_request import BatchUpsertRecordsRequest
from sajari_client.model.batch_upsert_records_response import BatchUpsertRecordsResponse
from sajari_client.model.delete_record_request import DeleteRecordRequest
from sajari_client.model.get_record_request import GetRecordRequest
from sajari_client.model.upsert_record_request import UpsertRecordRequest
from sajari_client.model.upsert_record_response import UpsertRecordResponse
from sajari_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class RecordsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __batch_upsert_records(
                self,
                collection_id,
                batch_upsert_records_request,
                **kwargs
        ):
            """Batch upsert records  # noqa: E501

            The batch version of the [UpsertRecord](/api#operation/UpsertRecord) call.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.batch_upsert_records(collection_id, batch_upsert_records_request, async_req=True)
            >>> result = thread.get()

            Args:
                collection_id (str): The collection to upsert the records in, e.g. `my-collection`.
                batch_upsert_records_request (BatchUpsertRecordsRequest):

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
                BatchUpsertRecordsResponse
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
            kwargs['batch_upsert_records_request'] = \
                batch_upsert_records_request
            return self.call_with_http_info(**kwargs)

        self.batch_upsert_records = _Endpoint(
            settings={
                'response_type': (BatchUpsertRecordsResponse,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/records:batchUpsert',
                'operation_id': 'batch_upsert_records',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'batch_upsert_records_request',
                ],
                'required': [
                    'collection_id',
                    'batch_upsert_records_request',
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
                    'batch_upsert_records_request':
                        (BatchUpsertRecordsRequest,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'batch_upsert_records_request': 'body',
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
            callable=__batch_upsert_records
        )

        def __delete_record(
                self,
                collection_id,
                delete_record_request,
                **kwargs
        ):
            """Delete record  # noqa: E501

            Delete a record with the given key.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_record(collection_id, delete_record_request, async_req=True)
            >>> result = thread.get()

            Args:
                collection_id (str): The collection that contains the record to delete, e.g. `my-collection`.
                delete_record_request (DeleteRecordRequest):

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
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['collection_id'] = \
                collection_id
            kwargs['delete_record_request'] = \
                delete_record_request
            return self.call_with_http_info(**kwargs)

        self.delete_record = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/records:delete',
                'operation_id': 'delete_record',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'delete_record_request',
                ],
                'required': [
                    'collection_id',
                    'delete_record_request',
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
                    'delete_record_request':
                        (DeleteRecordRequest,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'delete_record_request': 'body',
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
            callable=__delete_record
        )

        def __get_record(
                self,
                collection_id,
                get_record_request,
                **kwargs
        ):
            """Get record  # noqa: E501

            Retrieve a record with the given key.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_record(collection_id, get_record_request, async_req=True)
            >>> result = thread.get()

            Args:
                collection_id (str): The collection that contains the record to retrieve, e.g. `my-collection`.
                get_record_request (GetRecordRequest):

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
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
            kwargs['get_record_request'] = \
                get_record_request
            return self.call_with_http_info(**kwargs)

        self.get_record = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/records:get',
                'operation_id': 'get_record',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'get_record_request',
                ],
                'required': [
                    'collection_id',
                    'get_record_request',
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
                    'get_record_request':
                        (GetRecordRequest,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'get_record_request': 'body',
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
            callable=__get_record
        )

        def __upsert_record(
                self,
                collection_id,
                upsert_record_request,
                **kwargs
        ):
            """Upsert record  # noqa: E501

            If the record does not exist in your collection it is inserted. If it does exist it is updated.  If no pipeline is specified, the default record pipeline is used to process the record.  If the record is inserted, the response contains the key of the inserted record. You can use this if you need to retrieve or delete the record. If the record is updated, the response does not contain a key. Callers can use this as a signal to determine if the record is inserted/created or updated.  For example, to add a single product from your ecommerce store to a collection, use the following call:  ```json {   \"pipeline\": {     \"name\": \"my-pipeline\",     \"version\": \"1\"   },   \"record\": {     \"id\": \"54hdc7h2334h\",     \"name\": \"Smart TV\",     \"price\": 1999,     \"brand\": \"Acme\",     \"description\": \"...\",     \"in_stock\": true   } } ```  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.upsert_record(collection_id, upsert_record_request, async_req=True)
            >>> result = thread.get()

            Args:
                collection_id (str): The collection to upsert the record in, e.g. `my-collection`.
                upsert_record_request (UpsertRecordRequest):

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
                UpsertRecordResponse
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
            kwargs['upsert_record_request'] = \
                upsert_record_request
            return self.call_with_http_info(**kwargs)

        self.upsert_record = _Endpoint(
            settings={
                'response_type': (UpsertRecordResponse,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/v4/collections/{collection_id}/records:upsert',
                'operation_id': 'upsert_record',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'collection_id',
                    'upsert_record_request',
                ],
                'required': [
                    'collection_id',
                    'upsert_record_request',
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
                    'upsert_record_request':
                        (UpsertRecordRequest,),
                },
                'attribute_map': {
                    'collection_id': 'collection_id',
                },
                'location_map': {
                    'collection_id': 'path',
                    'upsert_record_request': 'body',
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
            callable=__upsert_record
        )
