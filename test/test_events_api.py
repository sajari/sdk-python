"""
    Sajari API

    Sajari is a smart, highly-configurable, real-time search service that enables thousands of businesses worldwide to provide amazing search experiences on their websites, stores, and applications.  # noqa: E501

    The version of the OpenAPI document: v4
    Contact: support@sajari.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import sajari_client
from sajari_client.api.events_api import EventsApi  # noqa: E501


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_send_event(self):
        """Test case for send_event

        Send event  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
