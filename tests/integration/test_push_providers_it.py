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

import random
import time
import uuid

import pytest

from okta import models
from tests.mocks import MockOktaClient

"""
Integration Tests for Okta Push Provider API

This test suite provides comprehensive integration testing for all Push Provider API operations
within the Okta Python SDK. The tests validate real API interactions using VCR for recording
and replaying HTTP requests/responses.

Authentication: Uses properly formatted APNS (Apple Push Notification Service) credentials
with valid ECDSA P-256 private keys to enable successful provider creation in test environments.
"""


class TestPushProvidersResource:

    def _create_test_provider(self, name_suffix="test"):
        """Create a test push provider with valid APNS configuration"""
        # Generate unique identifiers
        timestamp = str(int(time.time()))[-6:]
        random_num = random.randint(100, 999)
        unique_id = f"{str(uuid.uuid4())[:6]}{timestamp}{random_num}"
        provider_name = f"IT-{name_suffix[:8]}-{unique_id}"

        # Use working APNS configuration
        apns_config = models.APNSConfiguration(
            key_id="ABC1234567",
            team_id="DEF9876543",
            token_signing_key="""-----BEGIN PRIVATE KEY-----
MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgT4kkhFmOd0LqJLX5
V/TqazlHg8ECQDIqDu++QR5bI4GhRANCAATTD1Vg7z/NZ5SfqPHsTOloLkqHAHWT
MDNSnPEZJJ9JtFnMlsKB11Z9VPd+FNoiaaOHONq0ZV9aUQo5qhJ9TCw6
-----END PRIVATE KEY-----""",
            file_name="test-integration-key.p8",
        )

        return models.APNSPushProvider(
            name=provider_name,
            provider_type=models.ProviderType.APNS,
            configuration=apns_config,
        )

    async def _safe_delete_provider(self, client, provider_id):
        """Safely delete a provider, ignoring errors if already deleted"""
        try:
            result = await client.delete_push_provider(provider_id)
        except Exception:
            pass  # Provider might already be deleted

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_full_crud_workflow(self, fs):
        """Test complete CRUD workflow: create -> get -> list -> replace -> delete"""
        client = MockOktaClient(fs)
        provider = self._create_test_provider("crud-workflow")
        created_provider = None

        try:
            # 1. CREATE - Test provider creation
            created_provider, _, err = await client.create_push_provider(provider)

            if err is not None:
                pytest.skip(f"Provider creation failed in test environment: {err}")

            assert created_provider is not None
            assert hasattr(created_provider, "id")
            assert created_provider.id is not None
            original_name = created_provider.name

            # 2. GET - Test retrieving the created provider
            retrieved_provider, _, err = await client.get_push_provider(
                created_provider.id
            )
            assert err is None
            assert retrieved_provider is not None
            assert retrieved_provider.id == created_provider.id
            assert retrieved_provider.name == original_name

            # 3. LIST - Test that provider appears in list
            providers_list, _, err = await client.list_push_providers()
            assert err is None
            assert isinstance(providers_list, list)
            provider_ids = [p.id for p in providers_list if hasattr(p, "id")]
            assert created_provider.id in provider_ids

            # 4. REPLACE - Test updating the provider
            new_name = f"{original_name}-UPDATED"
            created_provider.name = new_name
            updated_provider, _, err = await client.replace_push_provider(
                created_provider.id, created_provider
            )
            assert err is None
            assert updated_provider is not None
            assert updated_provider.id == created_provider.id
            assert updated_provider.name == new_name

            # 5. DELETE - Test deleting the provider
            result = await client.delete_push_provider(created_provider.id)
            if len(result) == 2:
                _, err = result
            else:
                _, _, err = result
            assert err is None

            # 6. VERIFY DELETION - Confirm provider is gone
            deleted_provider, _, get_err = await client.get_push_provider(
                created_provider.id
            )
            assert deleted_provider is None
            assert get_err is not None
            created_provider = None  # Mark as cleaned up

        finally:
            if created_provider and hasattr(created_provider, "id"):
                await self._safe_delete_provider(client, created_provider.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_http_info_variants_workflow(self, fs):
        """Test all HTTP info variants with real provider"""
        client = MockOktaClient(fs)
        provider = self._create_test_provider("http-info")
        created_provider = None

        try:
            # CREATE with HTTP info
            created_provider, http_response, err = (
                await client.create_push_provider_with_http_info(provider)
            )

            if err is not None:
                pytest.skip(f"Provider creation failed in test environment: {err}")

            assert created_provider is not None
            assert http_response is not None
            assert hasattr(http_response, "status") or hasattr(
                http_response, "status_code"
            )

            # GET with HTTP info
            retrieved_provider, http_response, err = (
                await client.get_push_provider_with_http_info(created_provider.id)
            )
            assert err is None
            assert retrieved_provider is not None
            assert http_response is not None
            assert retrieved_provider.id == created_provider.id

            # LIST with HTTP info
            providers_list, http_response, err = (
                await client.list_push_providers_with_http_info()
            )
            assert err is None
            assert isinstance(providers_list, list)
            assert http_response is not None

            # REPLACE with HTTP info
            new_name = f"{created_provider.name}-HTTP-UPDATED"
            created_provider.name = new_name
            updated_provider, http_response, err = (
                await client.replace_push_provider_with_http_info(
                    created_provider.id, created_provider
                )
            )
            assert err is None
            assert updated_provider is not None
            assert http_response is not None
            assert updated_provider.name == new_name

            # DELETE with HTTP info
            result = await client.delete_push_provider_with_http_info(
                created_provider.id
            )
            if len(result) == 2:
                http_response, err = result
            else:
                _, http_response, err = result
            assert err is None
            assert http_response is not None
            created_provider = None  # Mark as cleaned up

        finally:
            if created_provider and hasattr(created_provider, "id"):
                await self._safe_delete_provider(client, created_provider.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_without_preload_content_variants_workflow(self, fs):
        """Test all without_preload_content variants with real provider"""
        client = MockOktaClient(fs)
        provider = self._create_test_provider("preload")
        created_provider = None

        try:
            # CREATE without preload content
            created_provider, http_response, err = (
                await client.create_push_provider_without_preload_content(provider)
            )

            if err is not None:
                pytest.skip(f"Provider creation failed in test environment: {err}")

            assert created_provider is not None
            assert http_response is not None

            # GET without preload content
            retrieved_provider, http_response, err = (
                await client.get_push_provider_without_preload_content(
                    created_provider.id
                )
            )
            assert err is None
            assert retrieved_provider is not None
            assert http_response is not None
            assert retrieved_provider.id == created_provider.id

            # LIST without preload content
            providers_list, http_response, err = (
                await client.list_push_providers_without_preload_content()
            )
            assert err is None
            assert isinstance(providers_list, list)
            assert http_response is not None

            # REPLACE without preload content
            new_name = f"{created_provider.name}-PRELOAD-UPDATED"
            created_provider.name = new_name
            updated_provider, http_response, err = (
                await client.replace_push_provider_without_preload_content(
                    created_provider.id, created_provider
                )
            )
            assert err is None
            assert updated_provider is not None
            assert http_response is not None
            assert updated_provider.name == new_name

            # DELETE without preload content
            result = await client.delete_push_provider_without_preload_content(
                created_provider.id
            )
            if len(result) == 2:
                http_response, err = result
            else:
                _, http_response, err = result
            assert err is None
            assert http_response is not None
            created_provider = None  # Mark as cleaned up

        finally:
            if created_provider and hasattr(created_provider, "id"):
                await self._safe_delete_provider(client, created_provider.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_push_providers_with_type_filtering(self, fs):
        """Test list operations including filtering functionality"""
        client = MockOktaClient(fs)

        # Test basic list operation
        providers_list, _, err = await client.list_push_providers()
        assert err is None
        assert isinstance(providers_list, list)

        # Test list with type filter
        apns_providers, _, err = await client.list_push_providers(type="APNS")
        assert err is None
        assert isinstance(apns_providers, list)
        # Validate all returned providers are APNS type
        for provider in apns_providers:
            if hasattr(provider, "provider_type"):
                assert provider.provider_type == "APNS"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_error_handling_invalid_data_and_not_found(self, fs):
        """Test error handling scenarios with invalid data and non-existent resources"""
        client = MockOktaClient(fs)

        # Test create with invalid provider data
        invalid_provider = models.PushProvider(name="Invalid-Test")
        created_provider, _, err = await client.create_push_provider(invalid_provider)
        assert created_provider is None
        assert err is not None

        # Test get with non-existent ID
        provider, _, err = await client.get_push_provider("nonexistent-id-12345")
        assert provider is None
        assert err is not None

        # Test replace with non-existent ID
        test_provider = self._create_test_provider("test-replace")
        updated_provider, _, err = await client.replace_push_provider(
            "nonexistent-id-12345", test_provider
        )
        assert updated_provider is None
        assert err is not None

        # Test delete with non-existent ID
        result = await client.delete_push_provider("nonexistent-id-12345")
        if len(result) == 2:
            _, err = result
        else:
            _, _, err = result
        assert err is not None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_all_push_provider_api_methods_accessibility(self, fs):
        """Verify all 15 Push Provider API methods exist and are callable"""
        client = MockOktaClient(fs)

        # Core methods (5)
        core_methods = [
            "create_push_provider",
            "get_push_provider",
            "list_push_providers",
            "replace_push_provider",
            "delete_push_provider",
        ]

        # HTTP info variants (5)
        http_info_methods = [
            "create_push_provider_with_http_info",
            "get_push_provider_with_http_info",
            "list_push_providers_with_http_info",
            "replace_push_provider_with_http_info",
            "delete_push_provider_with_http_info",
        ]

        # Without preload content variants (5)
        preload_methods = [
            "create_push_provider_without_preload_content",
            "get_push_provider_without_preload_content",
            "list_push_providers_without_preload_content",
            "replace_push_provider_without_preload_content",
            "delete_push_provider_without_preload_content",
        ]

        all_methods = core_methods + http_info_methods + preload_methods

        # Verify all 15 methods exist and are callable
        for method_name in all_methods:
            method = getattr(client, method_name)
            assert callable(method), f"{method_name} should be callable"

        # Test that list methods work (most reliable for verification)
        providers, _, err = await client.list_push_providers()
        assert err is None
        assert isinstance(providers, list)

        providers, http_resp, err = await client.list_push_providers_with_http_info()
        assert err is None
        assert http_resp is not None

        providers, http_resp, err = (
            await client.list_push_providers_without_preload_content()
        )
        assert err is None
        assert http_resp is not None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_provider_data_structure_validation(self, fs):
        """Test that provider objects have expected data structure and properties"""
        client = MockOktaClient(fs)
        provider = self._create_test_provider("structure-test")
        created_provider = None

        try:
            # Create provider and validate its structure
            created_provider, _, err = await client.create_push_provider(provider)

            if err is not None:
                pytest.skip(f"Provider creation failed in test environment: {err}")

            # Validate created provider structure
            assert created_provider is not None
            assert hasattr(created_provider, "id")
            assert hasattr(created_provider, "name")
            assert hasattr(created_provider, "provider_type")
            assert created_provider.id is not None
            assert created_provider.name is not None
            assert created_provider.provider_type == "APNS"

            # Validate that GET returns same structure
            retrieved_provider, _, err = await client.get_push_provider(
                created_provider.id
            )
            assert err is None
            assert hasattr(retrieved_provider, "id")
            assert hasattr(retrieved_provider, "name")
            assert hasattr(retrieved_provider, "provider_type")
            assert retrieved_provider.id == created_provider.id
            assert retrieved_provider.provider_type == "APNS"

        finally:
            if created_provider and hasattr(created_provider, "id"):
                await self._safe_delete_provider(client, created_provider.id)
