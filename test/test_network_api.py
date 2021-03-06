# coding: utf-8

"""
    EPM REST API

    REST API description of the ElasTest Platform Manager Module.

    OpenAPI spec version: 0.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import epm_client
from epm_client.rest import ApiException
from epm_client.apis.network_api import NetworkApi
from epm_client.models import Network


class TestNetworkApi(unittest.TestCase):
    """ NetworkApi unit test stubs """

    def setUp(self):
        self.api = epm_client.apis.network_api.NetworkApi()

    def tearDown(self):
        pass

    @unittest.skip
    def test_create_network(self):
        """
        Test case for create_network

        Creates a new network.
        """
        network = Network(name="test-network",cidr="192.168.5.1/24",po_p_name="test")
        self.api.create_network(network)
        pass

    @unittest.skip
    def test_delete_network(self):
        """
        Test case for delete_network

        Deletes a network.
        """
        self.api.delete_network("7f5ebaf0-13a4-4c82-a905-f563c7815b92")
        pass

    @unittest.skip
    def test_get_all_networks(self):
        """
        Test case for get_all_networks

        Returns all existing networks.
        """
        self.api.get_all_networks()
        pass

    @unittest.skip
    def test_get_network_by_id(self):
        """
        Test case for get_network_by_id

        Returns a network.
        """
        self.api.get_network_by_id("36255e82-f536-4bf0-8af5-a04c9ed37fc3")
        pass

    @unittest.skip
    def test_update_network(self):
        """
        Test case for update_network

        Updates a Network.
        """
        network = Network(name="test-network2",cidr="192.168.5.1/24",po_p_name="test")
        self.api.update_network("36255e82-f536-4bf0-8af5-a04c9ed37fc3", network.to_dict())
        pass


if __name__ == '__main__':
    unittest.main()
