from __future__ import absolute_import

import os
import sys
import unittest
import json
from time import sleep
import tarfile
from typing import List

import epm_client
from epm_client.rest import ApiException
from epm_client.apis.key_api import KeyApi
from epm_client.api_client import ApiClient
from epm_client.models import PoP
from epm_client.models import CommandExecutionBody
from epm_client.models import WorkerFromVDU


class FullTest(unittest.TestCase):
    """ KeyApi unit test stubs """

    def setUp(self):
        api_client = ApiClient(host="http://elastest-epm:8180/v1")
        self.key_api = epm_client.apis.key_api.KeyApi(api_client=api_client)
        self.worker_api = epm_client.apis.worker_api.WorkerApi(api_client=api_client)
        self.package_api = epm_client.apis.PackageApi(api_client=api_client)
        self.runtime_api = epm_client.apis.RuntimeApi(api_client=api_client)
        self.adapter_api = epm_client.apis.AdapterApi(api_client=api_client)
        self.pop_api = epm_client.apis.PoPApi(api_client=api_client)
        self.default_api = epm_client.apis.DefaultApi(api_client=api_client)
        self.cluster_api = epm_client.apis.ClusterApi(api_client=api_client)

        os_pop = PoP(interface_endpoint="<REPLACE>",
                     interface_info=[{"key": "type", "value": "openstack"},
                                     {"key": "username",
                                      "value": "<REPLACE>"},
                                     {"key": "password",
                                      "value": "<REPLACE>"},
                                     {"key": "project_name",
                                      "value": "<REPLACE>"},
                                     {"key": "auth_url",
                                      "value": "<REPLACE>"}], name="os-dc1")
        self.pop_api.register_po_p(os_pop)

    #@unittest.skip
    def test(self):
        #sleep(120)
        adapters = self.adapter_api.get_all_adapters()
        ansible_found = False
        for a in adapters:
            if a.type == "ansible":
                ansible_found = True
        assert ansible_found

        ansible_package = self.package_api.receive_package(file='resources/ansible-package.tar')
        print(ansible_package)

        sleep(15)
        type = List[str]
        worker_from_vdu = WorkerFromVDU(type=[], vdu_id=ansible_package.vdus[0].id)
        w = self.default_api.create_worker(worker_from_vdu=worker_from_vdu)

        self.worker_api.install_adapter(w.id, "docker-compose")

        # LAUNCH COMPOSE PACKAGE
        sleep(10)
        compose_package = self.package_api.receive_package('resources/compose-package.tar')
        assert len(compose_package.vdus) > 0
        command = CommandExecutionBody(command="ls /", await_completion=True)
        self.runtime_api.execute_on_instance(id=compose_package.vdus[0].id, command_execution_body=command)

        # CLEAN
        self.package_api.delete_package(compose_package.id)
        self.worker_api.delete_worker(w.id)
        self.package_api.delete_package(ansible_package.id)

        print("Test completed :)")


if __name__ == '__main__':
    unittest.main()

