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

from okta.models import (
    NetworkZone,
    NetworkZoneType,
    NetworkZoneStatus,
    NetworkZoneUsage,
    NetworkZoneAddress,
    NetworkZoneAddressType,
)
from tests.mocks import MockOktaClient


class TestNetworkZoneResource:
    """
    Integration Tests for the NetworkZone Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_network_zones(self, fs):
        client = MockOktaClient(fs)
        resp, _, err = await client.list_network_zones()
        for network_zone in resp:
            assert isinstance(network_zone, NetworkZone)
            assert isinstance(network_zone.type, NetworkZoneType)
            assert isinstance(network_zone.status, NetworkZoneStatus)
            assert isinstance(network_zone.usage, NetworkZoneUsage)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_and_delete_network_zone(self, fs):
        client = MockOktaClient(fs)
        network_zone_config = {
            "type": "IP",
            "id": None,
            "name": "testNetworkZone",
            "status": "ACTIVE",
            "created": None,
            "lastUpdated": None,
            "gateways": [{"type": "CIDR", "value": "1.2.3.4/24"}],
            "proxies": [{"type": "CIDR", "value": "2.2.3.4/24"}],
        }
        resp, _, err = await client.create_network_zone(network_zone_config)
        assert err is None
        try:
            assert resp.name == "testNetworkZone"
            assert isinstance(resp.gateways[0], NetworkZoneAddress)
            assert resp.gateways[0].value == "1.2.3.4/24"
            assert isinstance(resp.proxies[0], NetworkZoneAddress)
            assert resp.proxies[0].value == "2.2.3.4/24"
        finally:
            errors = []
            try:
                _, _, err = await client.deactivate_network_zone(resp.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            try:
                _, _, err = await client.delete_network_zone(resp.id)
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_network_zone(self, fs):
        client = MockOktaClient(fs)
        network_zone_config = {
            "type": "IP",
            "id": None,
            "name": "testNetworkZone",
            "status": "ACTIVE",
            "created": None,
            "lastUpdated": None,
            "gateways": [{"type": "CIDR", "value": "1.2.3.4/24"}],
            "proxies": [{"type": "CIDR", "value": "2.2.3.4/24"}],
        }
        resp, _, err = await client.create_network_zone(network_zone_config)
        assert err is None
        try:
            new_gateway = NetworkZoneAddress(
                **{"type": NetworkZoneAddressType("CIDR"), "value": "2.3.4.5/24"}
            )
            resp.gateways.append(new_gateway)
            resp, _, err = await client.replace_network_zone(resp.id, resp)
            assert len(resp.gateways) == 2
            assert resp.gateways[1].value == "2.3.4.5/24"
        finally:
            errors = []
            try:
                _, _, err = await client.deactivate_network_zone(resp.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            try:
                _, _, err = await client.delete_network_zone(resp.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0
