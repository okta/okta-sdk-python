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

from okta.models import ThreatInsightConfiguration
from tests.mocks import MockOktaClient


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
        assert "_links" in resp.to_dict().keys()
        assert "action" in resp.to_dict().keys()
        assert "excludeZones" in resp.to_dict().keys()

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_threat_insight_configuration(self, fs):
        client = MockOktaClient(fs)
        old_config, _, err = await client.get_current_configuration()
        new_config = old_config
        new_config.action = "audit"
        try:
            updated_config, _, err = await client.update_configuration(new_config)
            assert updated_config.action == "audit"
        finally:
            _, _, err = await client.update_configuration(old_config)
            assert err is None
