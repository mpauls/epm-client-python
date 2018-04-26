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
from epm_client.apis.adapter_api import AdapterApi


class TestAdapterApi(unittest.TestCase):
    """ AdapterApi unit test stubs """

    def setUp(self):
        self.api = epm_client.apis.adapter_api.AdapterApi()

    def tearDown(self):
        pass

    def test_get_all_adapters(self):
        """
        Test case for get_all_adapters

        Returns all registered adapters
        """
        print(self.api.get_all_adapters())
        pass


if __name__ == '__main__':
    unittest.main()