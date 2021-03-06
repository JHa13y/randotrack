# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Message(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, unix_time: str=None, message_type: str=None, lat: float=None, long: float=None, message: str=None, date_time: str=None):  # noqa: E501
        """Message - a model defined in Swagger

        :param id: The id of this Message.  # noqa: E501
        :type id: int
        :param unix_time: The unix_time of this Message.  # noqa: E501
        :type unix_time: str
        :param message_type: The message_type of this Message.  # noqa: E501
        :type message_type: str
        :param lat: The lat of this Message.  # noqa: E501
        :type lat: float
        :param long: The long of this Message.  # noqa: E501
        :type long: float
        :param message: The message of this Message.  # noqa: E501
        :type message: str
        :param date_time: The date_time of this Message.  # noqa: E501
        :type date_time: str
        """
        self.swagger_types = {
            'id': int,
            'unix_time': str,
            'message_type': str,
            'lat': float,
            'long': float,
            'message': str,
            'date_time': str
        }

        self.attribute_map = {
            'id': 'id',
            'unix_time': 'unixTime',
            'message_type': 'messageType',
            'lat': 'lat',
            'long': 'long',
            'message': 'message',
            'date_time': 'dateTime'
        }

        self._id = id
        self._unix_time = unix_time
        self._message_type = message_type
        self._lat = lat
        self._long = long
        self._message = message
        self._date_time = date_time

    @classmethod
    def from_dict(cls, dikt) -> 'Message':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Message of this Message.  # noqa: E501
        :rtype: Message
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Message.


        :return: The id of this Message.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Message.


        :param id: The id of this Message.
        :type id: int
        """

        self._id = id

    @property
    def unix_time(self) -> str:
        """Gets the unix_time of this Message.


        :return: The unix_time of this Message.
        :rtype: str
        """
        return self._unix_time

    @unix_time.setter
    def unix_time(self, unix_time: str):
        """Sets the unix_time of this Message.


        :param unix_time: The unix_time of this Message.
        :type unix_time: str
        """

        self._unix_time = unix_time

    @property
    def message_type(self) -> str:
        """Gets the message_type of this Message.


        :return: The message_type of this Message.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type: str):
        """Sets the message_type of this Message.


        :param message_type: The message_type of this Message.
        :type message_type: str
        """

        self._message_type = message_type

    @property
    def lat(self) -> float:
        """Gets the lat of this Message.


        :return: The lat of this Message.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat: float):
        """Sets the lat of this Message.


        :param lat: The lat of this Message.
        :type lat: float
        """

        self._lat = lat

    @property
    def long(self) -> float:
        """Gets the long of this Message.


        :return: The long of this Message.
        :rtype: float
        """
        return self._long

    @long.setter
    def long(self, long: float):
        """Sets the long of this Message.


        :param long: The long of this Message.
        :type long: float
        """

        self._long = long

    @property
    def message(self) -> str:
        """Gets the message of this Message.


        :return: The message of this Message.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Message.


        :param message: The message of this Message.
        :type message: str
        """

        self._message = message

    @property
    def date_time(self) -> str:
        """Gets the date_time of this Message.


        :return: The date_time of this Message.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time: str):
        """Sets the date_time of this Message.


        :param date_time: The date_time of this Message.
        :type date_time: str
        """

        self._date_time = date_time
