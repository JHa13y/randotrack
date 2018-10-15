import connexion
import six

from swagger_server.models.messages import Messages  # noqa: E501
from swagger_server.models.rider import Rider  # noqa: E501
from swagger_server import util


def get_rider_by_id(riderID):  # noqa: E501
    """Find a rider by ID

    Returns a single rider # noqa: E501

    :param riderID: ID of rider to return
    :type riderID: int

    :rtype: Rider
    """
    return 'do some magic!'


def get_rider_messages_by_id(riderID):  # noqa: E501
    """Find last spot messages for rider

    Returns spot messages for a single rider # noqa: E501

    :param riderID: ID of rider we are getting the events for
    :type riderID: int

    :rtype: Messages
    """
    return 'do some magic!'
