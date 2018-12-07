# coding: utf-8

"""
    EPM REST API

    REST API description of the ElasTest Platform Manager Module.

    OpenAPI spec version: 0.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class AuthCredentials(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, key=None, user=None, passphrase=None, password=None, port=None):
        """
        AuthCredentials - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'key': 'str',
            'user': 'str',
            'passphrase': 'str',
            'password': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'key': 'key',
            'user': 'user',
            'passphrase': 'passphrase',
            'password': 'password',
            'port': 'port'
        }

        self._id = id
        self._key = key
        self._user = user
        self._passphrase = passphrase
        self._password = password
        self._port = port

    @property
    def id(self):
        """
        Gets the id of this AuthCredentials.


        :return: The id of this AuthCredentials.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuthCredentials.


        :param id: The id of this AuthCredentials.
        :type: str
        """

        self._id = id

    @property
    def key(self):
        """
        Gets the key of this AuthCredentials.
        The name of the key saved in EPM, which can be used to execute runtime operations on this VDU.

        :return: The key of this AuthCredentials.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this AuthCredentials.
        The name of the key saved in EPM, which can be used to execute runtime operations on this VDU.

        :param key: The key of this AuthCredentials.
        :type: str
        """

        self._key = key

    @property
    def user(self):
        """
        Gets the user of this AuthCredentials.
        This is the user, which the EPM will use when trying to ssh in to the Worker.

        :return: The user of this AuthCredentials.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this AuthCredentials.
        This is the user, which the EPM will use when trying to ssh in to the Worker.

        :param user: The user of this AuthCredentials.
        :type: str
        """

        self._user = user

    @property
    def passphrase(self):
        """
        Gets the passphrase of this AuthCredentials.
        This is the Passphrase of the Key provided for connecting to the Worker.

        :return: The passphrase of this AuthCredentials.
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """
        Sets the passphrase of this AuthCredentials.
        This is the Passphrase of the Key provided for connecting to the Worker.

        :param passphrase: The passphrase of this AuthCredentials.
        :type: str
        """

        self._passphrase = passphrase

    @property
    def password(self):
        """
        Gets the password of this AuthCredentials.
        This is the password of the user, which can be left blank if no password is needed.

        :return: The password of this AuthCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this AuthCredentials.
        This is the password of the user, which can be left blank if no password is needed.

        :param password: The password of this AuthCredentials.
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """
        Gets the port of this AuthCredentials.
        The ssh port of the worker, where the EPM can reach it.

        :return: The port of this AuthCredentials.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this AuthCredentials.
        The ssh port of the worker, where the EPM can reach it.

        :param port: The port of this AuthCredentials.
        :type: int
        """

        self._port = port

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
