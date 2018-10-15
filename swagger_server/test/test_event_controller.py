# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.event import Event  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEventController(BaseTestCase):
    """EventController integration test stubs"""

    def test_delete_event(self):
        """Test case for delete_event

        Deletes a event
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/JHa13y/randotrack/1.0.0/event/{eventId}'.format(eventId=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_event_by_id(self):
        """Test case for get_event_by_id

        Find event by ID
        """
        response = self.client.open(
            '/JHa13y/randotrack/1.0.0/event/{eventId}'.format(eventId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_event_with_form(self):
        """Test case for update_event_with_form

        Updates a event in the with form data
        """
        data = dict(name='name_example',
                    status='status_example')
        response = self.client.open(
            '/JHa13y/randotrack/1.0.0/event/{eventId}'.format(eventId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
