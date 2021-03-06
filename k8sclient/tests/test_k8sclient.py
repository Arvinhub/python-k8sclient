# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
test_k8sclient
----------------------------------

Tests for `k8sclient` module. Deploy Kubernetes using:
http://kubernetes.io/docs/getting-started-guides/docker/

and then run this test.
"""

from testtools.testcase import unittest
import urllib3

from k8sclient.client import api_client
from k8sclient.client.apis import apiv_api
from k8sclient.tests import base


def _is_k8s_running():
    try:
        urllib3.PoolManager().request('GET', '127.0.0.1:8080')
        return True
    except urllib3.exceptions.HTTPError:
        return False


class TestK8sclient(base.TestCase):
    @unittest.skipUnless(
            _is_k8s_running(), "Kubernetes is not available")
    def test_list_nodes_and_endpoints(self):
        client = api_client.ApiClient('http://127.0.0.1:8080/')
        api = apiv_api.ApivApi(client)

        pod = api.list_pod()
        self.assertEquals(3, len(pod.items))

        endpoints = api.list_endpoints()
        self.assertEquals(1, len(endpoints.items))
