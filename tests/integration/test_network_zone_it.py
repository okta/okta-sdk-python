import pytest
from tests.mocks import MockOktaClient
from okta.models import (
                            NetworkZone,
                            NetworkZoneType,
                            NetworkZoneStatus,
                            NetworkZoneUsage,
                            NetworkZoneAddress,
                            NetworkZoneAddressType
                        )


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
            "gateways": [
              {
                "type": "CIDR",
                "value": "1.2.3.4/24"
              }
            ],
            "proxies": [
              {
                "type": "CIDR",
                "value": "2.2.3.4/24"
              }
            ]
        }
        resp, _, err = await client.create_network_zone(network_zone_config)
        assert err is None
        try:
            assert resp.name == 'testNetworkZone'
            assert isinstance(resp.gateways[0], NetworkZoneAddress)
            assert resp.gateways[0].value == '1.2.3.4/24'
            assert isinstance(resp.proxies[0], NetworkZoneAddress)
            assert resp.proxies[0].value == '2.2.3.4/24'
        finally:
            errors = []
            try:
                _, _, err = await client.deactivate_network_zone(resp.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            try:
                _, err = await client.delete_network_zone(resp.id)
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
            "gateways": [
              {
                "type": "CIDR",
                "value": "1.2.3.4/24"
              }
            ],
            "proxies": [
              {
                "type": "CIDR",
                "value": "2.2.3.4/24"
              }
            ]
        }
        resp, _, err = await client.create_network_zone(network_zone_config)
        assert err is None
        try:
            new_gateway = NetworkZoneAddress({'type': NetworkZoneAddressType('CIDR'),
                                              'value': '2.3.4.5/24'})
            resp.gateways.append(new_gateway)
            resp, _, err = await client.update_network_zone(resp.id, resp)
            assert len(resp.gateways) == 2
            assert resp.gateways[1].value == '2.3.4.5/24'
        finally:
            errors = []
            try:
                _, _, err = await client.deactivate_network_zone(resp.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            try:
                _, err = await client.delete_network_zone(resp.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0
