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


class VDU(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, compute_id=None, events=None, id=None, image_name=None, ip=None, metadata=None, name=None, net_name=None, po_p_name=None, status=None):
        """
        VDU - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'compute_id': 'str',
            'events': 'list[Event]',
            'id': 'str',
            'image_name': 'str',
            'ip': 'str',
            'metadata': 'list[KeyValuePair]',
            'name': 'str',
            'net_name': 'str',
            'po_p_name': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'compute_id': 'computeId',
            'events': 'events',
            'id': 'id',
            'image_name': 'imageName',
            'ip': 'ip',
            'metadata': 'metadata',
            'name': 'name',
            'net_name': 'netName',
            'po_p_name': 'poPName',
            'status': 'status'
        }

        self._compute_id = compute_id
        self._events = events
        self._id = id
        self._image_name = image_name
        self._ip = ip
        self._metadata = metadata
        self._name = name
        self._net_name = net_name
        self._po_p_name = po_p_name
        self._status = status

    @property
    def compute_id(self):
        """
        Gets the compute_id of this VDU.

        :return: The compute_id of this VDU.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        """
        Sets the compute_id of this VDU.

        :param compute_id: The compute_id of this VDU.
        :type: str
        """
        if compute_id is None:
            raise ValueError("Invalid value for `compute_id`, must not be `None`")

        self._compute_id = compute_id

    @property
    def events(self):
        """
        Gets the events of this VDU.

        :return: The events of this VDU.
        :rtype: list[Event]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this VDU.

        :param events: The events of this VDU.
        :type: list[Event]
        """

        self._events = events

    @property
    def id(self):
        """
        Gets the id of this VDU.

        :return: The id of this VDU.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VDU.

        :param id: The id of this VDU.
        :type: str
        """

        self._id = id

    @property
    def image_name(self):
        """
        Gets the image_name of this VDU.

        :return: The image_name of this VDU.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """
        Sets the image_name of this VDU.

        :param image_name: The image_name of this VDU.
        :type: str
        """
        if image_name is None:
            raise ValueError("Invalid value for `image_name`, must not be `None`")

        self._image_name = image_name

    @property
    def ip(self):
        """
        Gets the ip of this VDU.

        :return: The ip of this VDU.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this VDU.

        :param ip: The ip of this VDU.
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")

        self._ip = ip

    @property
    def metadata(self):
        """
        Gets the metadata of this VDU.

        :return: The metadata of this VDU.
        :rtype: list[KeyValuePair]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this VDU.

        :param metadata: The metadata of this VDU.
        :type: list[KeyValuePair]
        """

        self._metadata = metadata

    @property
    def name(self):
        """
        Gets the name of this VDU.

        :return: The name of this VDU.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VDU.

        :param name: The name of this VDU.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def net_name(self):
        """
        Gets the net_name of this VDU.

        :return: The net_name of this VDU.
        :rtype: str
        """
        return self._net_name

    @net_name.setter
    def net_name(self, net_name):
        """
        Sets the net_name of this VDU.

        :param net_name: The net_name of this VDU.
        :type: str
        """
        if net_name is None:
            raise ValueError("Invalid value for `net_name`, must not be `None`")

        self._net_name = net_name

    @property
    def po_p_name(self):
        """
        Gets the po_p_name of this VDU.

        :return: The po_p_name of this VDU.
        :rtype: str
        """
        return self._po_p_name

    @po_p_name.setter
    def po_p_name(self, po_p_name):
        """
        Sets the po_p_name of this VDU.

        :param po_p_name: The po_p_name of this VDU.
        :type: str
        """
        if po_p_name is None:
            raise ValueError("Invalid value for `po_p_name`, must not be `None`")

        self._po_p_name = po_p_name

    @property
    def status(self):
        """
        Gets the status of this VDU.

        :return: The status of this VDU.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this VDU.

        :param status: The status of this VDU.
        :type: str
        """
        allowed_values = ["initializing", "initialized", "deploying", "deployed", "running", "undeploying", "undeployed", "error"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, VDU):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
