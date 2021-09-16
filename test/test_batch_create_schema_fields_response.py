"""
    Sajari API

    Sajari is a smart, highly-configurable, real-time search service that enables thousands of businesses worldwide to provide amazing search experiences on their websites, stores, and applications.  # noqa: E501

    The version of the OpenAPI document: v4
    Contact: support@sajari.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import sajari_client
from sajari_client.model.batch_create_schema_fields_response_error import (
    BatchCreateSchemaFieldsResponseError,
)
from sajari_client.model.schema_field import SchemaField

globals()["BatchCreateSchemaFieldsResponseError"] = BatchCreateSchemaFieldsResponseError
globals()["SchemaField"] = SchemaField
from sajari_client.model.batch_create_schema_fields_response import (
    BatchCreateSchemaFieldsResponse,
)


class TestBatchCreateSchemaFieldsResponse(unittest.TestCase):
    """BatchCreateSchemaFieldsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBatchCreateSchemaFieldsResponse(self):
        """Test BatchCreateSchemaFieldsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BatchCreateSchemaFieldsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
