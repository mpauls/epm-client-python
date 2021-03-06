# coding: utf-8

"""
    EPM REST API

    REST API description of the ElasTest Platform Manager Module.

    OpenAPI spec version: 0.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CommandExecutionBody(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, command=None, await_completion=None):
        """
        CommandExecutionBody - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'command': 'str',
            'await_completion': 'bool'
        }

        self.attribute_map = {
            'command': 'command',
            'await_completion': 'awaitCompletion'
        }

        self._command = command
        self._await_completion = await_completion

    @property
    def command(self):
        """
        Gets the command of this CommandExecutionBody.

        :return: The command of this CommandExecutionBody.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this CommandExecutionBody.

        :param command: The command of this CommandExecutionBody.
        :type: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")

        self._command = command

    @property
    def await_completion(self):
        """
        Gets the await_completion of this CommandExecutionBody.

        :return: The await_completion of this CommandExecutionBody.
        :rtype: bool
        """
        return self._await_completion

    @await_completion.setter
    def await_completion(self, await_completion):
        """
        Sets the await_completion of this CommandExecutionBody.

        :param await_completion: The await_completion of this CommandExecutionBody.
        :type: bool
        """
        if await_completion is None:
            raise ValueError("Invalid value for `await_completion`, must not be `None`")

        self._await_completion = await_completion

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CommandExecutionBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
