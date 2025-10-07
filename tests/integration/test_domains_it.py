# flake8: noqa
# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import pytest

# from okta.models import Domain, DomainListResponse
from okta.models import DomainListResponse
from tests.mocks import MockOktaClient


class TestDomainResource:
    """
    Integration Tests for the Domain Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_domains(self, fs):
        client = MockOktaClient(fs)
        domain_list_resp, _, err = await client.list_custom_domains()
        assert isinstance(domain_list_resp, DomainListResponse)

    # @pytest.mark.vcr()
    # @pytest.mark.asyncio
    # async def test_create_and_delete_domain(self, fs):
    #     client = MockOktaClient(fs)
    #     domain_config = {
    #         "domain": "login.example.com",
    #         "certificateSourceType": "MANUAL"
    #     }
    #     domain, _, err = await client.create_email_domain(domain_config)
    #     assert err is None
    #     try:
    #         assert isinstance(domain, Domain)
    #         assert domain.id
    #     finally:
    #         _, err = await client.delete_domain(domain.id)

    # @pytest.mark.vcr()
    # @pytest.mark.asyncio
    # async def test_get_domain(self, fs):
    #     client = MockOktaClient(fs)
    #     domain_config = {
    #         "domain": "login.example.com",
    #         "certificateSourceType": "MANUAL"
    #     }
    #     domain, _, err = await client.create_domain(domain_config)
    #     assert err is None
    #     try:
    #         get_domain, _, err = await client.get_domain(domain.id)
    #         assert isinstance(domain, Domain)
    #         assert domain.id == get_domain.id
    #         assert domain.domain == get_domain.domain
    #     finally:
    #         _, err = await client.delete_domain(domain.id)
    #         assert err is None
