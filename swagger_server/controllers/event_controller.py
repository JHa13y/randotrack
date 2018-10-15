import connexion
import six

from swagger_server.models import Event  # noqa: E501
from swagger_server import util


def delete_event(eventId, api_key=None):  # noqa: E501
    """Deletes a event

     # noqa: E501

    :param eventId: event id to delete
    :type eventId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_event_by_id(eventId):  # noqa: E501
    """Find event by ID

    Returns a single event # noqa: E501

    :param eventId: ID of eventId to return
    :type eventId: int

    :rtype: Event
    """
    return 'do some magic!'


def update_event_with_form(eventId, name=None, status=None):  # noqa: E501
    """Updates a event in the with form data

     # noqa: E501

    :param eventId: ID of event that needs to be updated
    :type eventId: int
    :param name: Updated name of the event
    :type name: str
    :param status: Updated status of the event
    :type status: str

    :rtype: None
    """
    return 'do some magic!'
