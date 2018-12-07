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


class ClusterFromResourceGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, resource_group_id=None, master_id=None):
        """
        ClusterFromResourceGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'list[str]',
            'resource_group_id': 'str',
            'master_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'resource_group_id': 'resourceGroupId',
            'master_id': 'masterId'
        }

        self._type = type
        self._resource_group_id = resource_group_id
        self._master_id = master_id

    @property
    def type(self):
        """
        Gets the type of this ClusterFromResourceGroup.
        The types of the worker.

        :return: The type of this ClusterFromResourceGroup.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ClusterFromResourceGroup.
        The types of the worker.

        :param type: The type of this ClusterFromResourceGroup.
        :type: list[str]
        """

        self._type = type

    @property
    def resource_group_id(self):
        """
        Gets the resource_group_id of this ClusterFromResourceGroup.
        The id of vdu from which to create the worker.

        :return: The resource_group_id of this ClusterFromResourceGroup.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """
        Sets the resource_group_id of this ClusterFromResourceGroup.
        The id of vdu from which to create the worker.

        :param resource_group_id: The resource_group_id of this ClusterFromResourceGroup.
        :type: str
        """

        self._resource_group_id = resource_group_id

    @property
    def master_id(self):
        """
        Gets the master_id of this ClusterFromResourceGroup.
        The ID of the VDU which will serve as the master node. This should be an ID of a VDU which belongs to the specified Ressource Group.

        :return: The master_id of this ClusterFromResourceGroup.
        :rtype: str
        """
        return self._master_id

    @master_id.setter
    def master_id(self, master_id):
        """
        Sets the master_id of this ClusterFromResourceGroup.
        The ID of the VDU which will serve as the master node. This should be an ID of a VDU which belongs to the specified Ressource Group.

        :param master_id: The master_id of this ClusterFromResourceGroup.
        :type: str
        """

        self._master_id = master_id

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
