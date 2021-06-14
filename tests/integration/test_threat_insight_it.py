import pytest
from tests.mocks import MockOktaClient
from okta.models import ThreatInsightConfiguration


class TestThreatInsightConfiguration:
    """
    Integration Tests for the Threat Insight Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_threat_insight_configuration(self, fs):
        client = MockOktaClient(fs)
        resp, _, err = await client.get_current_configuration()
        assert isinstance(resp, ThreatInsightConfiguration)
        assert '_links' in resp.as_dict().keys()
        assert 'action' in resp.as_dict().keys()
        assert 'excludeZones' in resp.as_dict().keys()

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_threat_insight_configuration(self, fs):
        client = MockOktaClient(fs)
        old_config, _, err = await client.get_current_configuration()
        new_config = old_config
        new_config.action = 'audit'
        try:
            updated_config, _, err = await client.update_configuration(new_config)
            assert updated_config.action == 'audit'
        finally:
            _, _, err = await client.update_configuration(old_config)
            assert err is None
