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

import copy

import pytest

import okta.models as models
from tests.mocks import MockOktaClient


class TestAuthenticatorsResource:
    """
    Integration Tests for the Authenticators Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_authenticators(self, fs):
        client = MockOktaClient(fs)
        resp, _, err = await client.list_authenticators()
        assert err is None
        assert len(resp) > 0
        assert all([isinstance(elem, models.Authenticator) for elem in resp])
        assert all([isinstance(elem.type, models.AuthenticatorType) for elem in resp])

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_authenticator(self, fs):
        client = MockOktaClient(fs)
        authenticators_list, _, err = await client.list_authenticators()
        assert err is None

        resp, _, err = await client.get_authenticator(authenticators_list[0].id)
        assert err is None
        assert isinstance(resp, models.Authenticator)
        assert resp.to_dict() == authenticators_list[0].to_dict()

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_and_deactivate_authenticator(self, fs):
        client = MockOktaClient(fs)
        authenticators_list, _, err = await client.list_authenticators()
        assert err is None

        app_authenticator = [a for a in authenticators_list if a.type == "phone"][0]
        try:
            resp, _, err = await client.activate_authenticator(app_authenticator.id)
            assert err is None
            assert isinstance(resp, models.Authenticator)
            assert resp.status == "ACTIVE"
        finally:
            resp, _, err = await client.deactivate_authenticator(app_authenticator.id)
            assert err is None
            assert isinstance(resp, models.Authenticator)
            assert resp.status == "INACTIVE"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_authenticator(self, fs):
        client = MockOktaClient(fs)
        authenticators_list, _, err = await client.list_authenticators()
        assert err is None

        app_authenticator = [a for a in authenticators_list if a.type == "phone"][0]
        new_authenticator = copy.deepcopy(app_authenticator)
        new_authenticator.settings.allowed_for = models.AllowedForEnum.RECOVERY.value
        try:
            updated_authenticator, _, err = await client.replace_authenticator(
                app_authenticator.id, new_authenticator
            )
            assert err is None
            assert isinstance(updated_authenticator, models.Authenticator)
            assert (
                    updated_authenticator.settings.allowed_for
                    == models.AllowedForEnum.RECOVERY.value
            )
        finally:
            updated_authenticator, _, err = await client.replace_authenticator(
                app_authenticator.id, app_authenticator
            )
            assert err is None
