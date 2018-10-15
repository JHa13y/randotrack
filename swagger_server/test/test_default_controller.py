# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.messages import Messages  # noqa: E501
from swagger_server.models.rider import Rider  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_rider_by_id(self):
        """Test case for get_rider_by_id

        Find a rider by ID
        """
        response = self.client.open(
            '/JHa13y/randotrack/1.0.0/riders/{riderID}'.format(riderID=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_rider_messages_by_id(self):
        """Test case for get_rider_messages_by_id

        Find last spot messages for rider
        """
        response = self.client.open(
            '/JHa13y/randotrack/1.0.0/riders/{riderID}/messages'.format(riderID=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
