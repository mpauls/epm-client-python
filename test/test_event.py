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

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.event import Event


class TestEvent(unittest.TestCase):
    """ Event unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEvent(self):
        """
        Test Event
        """
        model = swagger_client.models.event.Event()


if __name__ == '__main__':
    unittest.main()
