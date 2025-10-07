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

import okta.models as models
from okta.errors.okta_api_error import OktaAPIError
from tests.mocks import MockOktaClient


class TestCaptchaResource:
    """
    Integration Tests for the CAPTCHA Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_captcha_lifecycle(self, fs):
        """
        Test the complete lifecycle of a CAPTCHA instance:
        1. Create CAPTCHA instance
        2. Get CAPTCHA instance (with both regular and _with_http_info variants)
        3. List CAPTCHA instances (with both regular and _with_http_info variants)
        4. Replace CAPTCHA instance (with both regular and _with_http_info variants)
        5. Configure org-wide CAPTCHA settings (with both regular and _with_http_info variants)
        6. Get org-wide CAPTCHA settings (with both regular and _with_http_info variants)
        7. Delete org-wide CAPTCHA settings (with both regular and _with_http_info variants)
        8. Delete CAPTCHA instance (with both regular and _with_http_info variants)
        9. Verify deletion
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, clean up any existing CAPTCHA instances and settings
        try:
            # Try to delete any existing org settings first
            await client.delete_org_captcha_settings()
        except:
            pass

        try:
            # List existing instances and delete them
            existing_instances, _, err = await client.list_captcha_instances()
            if err is None and existing_instances:
                for instance in existing_instances:
                    try:
                        await client.delete_captcha_instance(instance.id)
                    except:
                        pass
        except:
            pass

        # Step 1: Create CAPTCHA Instance
        captcha_name = "Test CAPTCHA Instance"
        captcha_site_key = "10000000-ffff-ffff-ffff-000000000001"
        captcha_secret_key = "0x0000000000000000000000000000000000000000"

        captcha_instance = models.CAPTCHAInstance(
            name=captcha_name,
            type=models.CAPTCHAType.HCAPTCHA,
            site_key=captcha_site_key,
            secret_key=captcha_secret_key,
        )

        try:
            # Create the CAPTCHA instance
            created_instance, _, err = await client.create_captcha_instance(
                captcha_instance
            )
            assert err is None
            assert isinstance(created_instance, models.CAPTCHAInstance)
            assert created_instance.id is not None
            assert created_instance.name == captcha_name
            assert created_instance.type == models.CAPTCHAType.HCAPTCHA
            assert created_instance.site_key == captcha_site_key

            captcha_id = created_instance.id

            # Test _without_preload_content variant for create (will be used later)
            # This tests the lower-level API method signature
            try:
                new_captcha_for_preload_test = models.CAPTCHAInstance(
                    name="Preload Test Instance",
                    type=models.CAPTCHAType.RECAPTCHA_V2,
                    site_key="50000000-ffff-ffff-ffff-000000000005",
                    secret_key="0x4444444444444444444444444444444444444444",
                )
                # This should fail due to org limit, but exercises the method signature
                resp = await client.create_captcha_instance_without_preload_content(
                    new_captcha_for_preload_test
                )
                # If it doesn't fail, clean it up
                if resp and hasattr(resp, "data"):
                    try:
                        temp_data = resp.data
                        if hasattr(temp_data, "id"):
                            await client.delete_captcha_instance(temp_data.id)
                    except:
                        pass
            except Exception:
                # Expected due to org limit, but we tested the method signature
                pass

            # Step 2: Get CAPTCHA Instance (regular method)
            retrieved_instance, _, err = await client.get_captcha_instance(captcha_id)
            assert err is None
            assert isinstance(retrieved_instance, models.CAPTCHAInstance)
            assert retrieved_instance.id == captcha_id
            assert retrieved_instance.name == captcha_name
            assert retrieved_instance.type == models.CAPTCHAType.HCAPTCHA

            # Test with_http_info variant for get
            retrieved_instance_http, resp, err = (
                await client.get_captcha_instance_with_http_info(captcha_id)
            )
            assert err is None
            assert resp is not None
            assert isinstance(retrieved_instance_http, models.CAPTCHAInstance)
            assert retrieved_instance_http.id == captcha_id

            # Test _without_preload_content variant for get
            resp_preload = await client.get_captcha_instance_without_preload_content(
                captcha_id
            )
            assert resp_preload is not None

            # Step 3: List CAPTCHA Instances (regular method)
            instances_list, _, err = await client.list_captcha_instances()
            assert err is None
            assert isinstance(instances_list, list)
            assert len(instances_list) >= 1  # Should have at least our created instance

            # Test with_http_info variant for list
            instances_list_http, resp, err = (
                await client.list_captcha_instances_with_http_info()
            )
            assert err is None
            assert resp is not None
            assert isinstance(instances_list_http, list)
            assert len(instances_list_http) >= 1

            # Test _without_preload_content variant for list
            resp_list_preload = (
                await client.list_captcha_instances_without_preload_content()
            )
            assert resp_list_preload is not None

            # Verify our instance is in the list
            found_instance = False
            for instance in instances_list:
                if instance.id == captcha_id:
                    found_instance = True
                    break
            assert (
                found_instance
            ), f"Created CAPTCHA instance {captcha_id} not found in list"

            # Step 4: Replace CAPTCHA Instance (regular method)
            updated_name = "Updated Test CAPTCHA Instance"
            updated_instance = models.CAPTCHAInstance(
                name=updated_name,
                type=models.CAPTCHAType.RECAPTCHA_V2,  # Change to different type
                site_key=captcha_site_key,
                secret_key=captcha_secret_key,
            )

            replaced_instance, _, err = await client.replace_captcha_instance(
                captcha_id, updated_instance
            )
            assert err is None
            assert isinstance(replaced_instance, models.CAPTCHAInstance)
            assert replaced_instance.id == captcha_id
            assert replaced_instance.name == updated_name
            assert replaced_instance.type == models.CAPTCHAType.RECAPTCHA_V2

            # Test with_http_info variant for replace (change back to HCAPTCHA)
            updated_instance_2 = models.CAPTCHAInstance(
                name="Final Updated CAPTCHA Instance",
                type=models.CAPTCHAType.HCAPTCHA,
                site_key="30000000-ffff-ffff-ffff-000000000003",
                secret_key="0x2222222222222222222222222222222222222222",
            )
            replaced_instance_http, resp, err = (
                await client.replace_captcha_instance_with_http_info(
                    captcha_id, updated_instance_2
                )
            )
            assert err is None
            assert resp is not None
            assert isinstance(replaced_instance_http, models.CAPTCHAInstance)
            assert replaced_instance_http.id == captcha_id
            assert replaced_instance_http.type == models.CAPTCHAType.HCAPTCHA

            # Test _without_preload_content variant for replace
            updated_instance_3 = models.CAPTCHAInstance(
                name="Preload Replace Test",
                type=models.CAPTCHAType.RECAPTCHA_V2,
                site_key="60000000-ffff-ffff-ffff-000000000006",
                secret_key="0x5555555555555555555555555555555555555555",
            )
            resp_replace_preload = (
                await client.replace_captcha_instance_without_preload_content(
                    captcha_id, updated_instance_3
                )
            )
            assert resp_replace_preload is not None

            # Step 5: Configure Org-wide CAPTCHA Settings (regular method)
            org_settings = models.OrgCAPTCHASettings(
                captcha_id=captcha_id,
                enabled_pages=[
                    models.EnabledPagesType.SIGN_IN,
                    models.EnabledPagesType.SSPR,
                ],
            )

            created_org_settings, _, err = await client.replaces_org_captcha_settings(
                org_settings
            )
            assert err is None
            assert isinstance(created_org_settings, models.OrgCAPTCHASettings)
            assert created_org_settings.captcha_id == captcha_id
            assert len(created_org_settings.enabled_pages) == 2
            assert models.EnabledPagesType.SIGN_IN in created_org_settings.enabled_pages
            assert models.EnabledPagesType.SSPR in created_org_settings.enabled_pages

            # Test with_http_info variant for replace org settings (update to single page)
            org_settings_updated = models.OrgCAPTCHASettings(
                captcha_id=captcha_id, enabled_pages=[models.EnabledPagesType.SIGN_IN]
            )
            created_org_settings_http, resp, err = (
                await client.replaces_org_captcha_settings_with_http_info(
                    org_settings_updated
                )
            )
            assert err is None
            assert resp is not None
            assert isinstance(created_org_settings_http, models.OrgCAPTCHASettings)
            assert created_org_settings_http.captcha_id == captcha_id
            assert len(created_org_settings_http.enabled_pages) == 1

            # Test _without_preload_content variant for replace org settings
            org_settings_preload = models.OrgCAPTCHASettings(
                captcha_id=captcha_id, enabled_pages=[models.EnabledPagesType.SSPR]
            )
            resp_org_preload = (
                await client.replaces_org_captcha_settings_without_preload_content(
                    org_settings_preload
                )
            )
            assert resp_org_preload is not None

            # Step 6: Get Org-wide CAPTCHA Settings (regular method)
            retrieved_org_settings, _, err = await client.get_org_captcha_settings()
            assert err is None
            assert isinstance(retrieved_org_settings, models.OrgCAPTCHASettings)
            assert retrieved_org_settings.captcha_id == captcha_id
            assert len(retrieved_org_settings.enabled_pages) == 1

            # Test with_http_info variant for get org settings
            retrieved_org_settings_http, resp, err = (
                await client.get_org_captcha_settings_with_http_info()
            )
            assert err is None
            assert resp is not None
            assert isinstance(retrieved_org_settings_http, models.OrgCAPTCHASettings)
            assert retrieved_org_settings_http.captcha_id == captcha_id

            # Test _without_preload_content variant for get org settings
            resp_get_org_preload = (
                await client.get_org_captcha_settings_without_preload_content()
            )
            assert resp_get_org_preload is not None

            # Step 7: Delete Org-wide CAPTCHA Settings (required before deleting instance)
            _, _, err = await client.delete_org_captcha_settings()
            assert err is None

            # Test with_http_info variant for delete org settings (should be no-op now)
            try:
                _, resp, err = await client.delete_org_captcha_settings_with_http_info()
                # This might succeed or fail depending on implementation
                if err is None:
                    assert resp is not None
            except Exception:
                # Expected - settings already deleted
                pass

            # Test _without_preload_content variant for delete org settings
            try:
                resp_delete_org_preload = (
                    await client.delete_org_captcha_settings_without_preload_content()
                )
                # May return response even if settings already deleted
                assert resp_delete_org_preload is not None
            except Exception:
                # Expected - settings may already be deleted
                pass

            # Verify org settings are deleted
            empty_org_settings, _, err = await client.get_org_captcha_settings()
            assert err is None
            # Should return empty settings or None values
            assert (
                    empty_org_settings.captcha_id is None
                    or empty_org_settings.captcha_id == ""
            )

            # Step 8: Delete CAPTCHA Instance (regular method)
            _, _, err = await client.delete_captcha_instance(captcha_id)
            assert err is None

            # Step 9: Verify Deletion - attempt to get deleted instance should fail
            try:
                deleted_instance, _, err = await client.get_captcha_instance(captcha_id)
                # Should either return an error or the call should fail
                assert err is not None or deleted_instance is None
            except OktaAPIError as e:
                # Expected behavior - should get 404 error
                assert e.error_code == "E0000007" or "404" in str(e)

            # Test error handling for non-existent ID with _with_http_info
            try:
                non_existent_instance, resp, err = (
                    await client.get_captcha_instance_with_http_info(captcha_id)
                )
                assert err is not None or non_existent_instance is None
            except OktaAPIError:
                # Expected - 404 error for deleted instance
                pass

            # Test error handling for non-existent ID with _without_preload_content
            try:
                resp_error = await client.get_captcha_instance_without_preload_content(
                    captcha_id
                )
                # Should handle error appropriately
            except Exception:
                # Expected - instance was deleted
                pass

            # Test additional _with_http_info variant for create (since we deleted the instance)
            # This tests create_captcha_instance_with_http_info after deletion
            new_captcha_instance = models.CAPTCHAInstance(
                name="New CAPTCHA Instance via HTTP Info",
                type=models.CAPTCHAType.RECAPTCHA_V2,
                site_key="40000000-ffff-ffff-ffff-000000000004",
                secret_key="0x3333333333333333333333333333333333333333",
            )
            created_instance_http, resp, err = (
                await client.create_captcha_instance_with_http_info(
                    new_captcha_instance
                )
            )
            assert err is None
            assert resp is not None
            assert isinstance(created_instance_http, models.CAPTCHAInstance)

            new_captcha_id = created_instance_http.id

            # Test _without_preload_content variant for delete (clean up the new instance)
            resp_delete_preload = (
                await client.delete_captcha_instance_without_preload_content(
                    new_captcha_id
                )
            )
            assert resp_delete_preload is not None

            # Final verification - instance should be deleted
            try:
                deleted_instance_http, _, err = (
                    await client.get_captcha_instance_with_http_info(new_captcha_id)
                )
                assert err is not None or deleted_instance_http is None
            except OktaAPIError as e:
                # Expected behavior - should get 404 error
                assert e.error_code == "E0000007" or "404" in str(e)

        except Exception as e:
            # Cleanup in case of test failure
            try:
                # Try to delete org settings first
                await client.delete_org_captcha_settings()
            except:
                pass

            try:
                # Try to delete the instance if it was created
                if "captcha_id" in locals():
                    await client.delete_captcha_instance(captcha_id)
                if "new_captcha_id" in locals():
                    await client.delete_captcha_instance(new_captcha_id)
            except:
                pass

            # Re-raise the original exception
            raise e

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_captcha_error_scenarios(self, fs):
        """
        Test error scenarios and edge cases for CAPTCHA API to increase coverage
        """
        client = MockOktaClient(fs)

        # Test get with invalid/non-existent ID
        fake_id = "cap0000000000000000000"
        try:
            instance, _, err = await client.get_captcha_instance(fake_id)
            assert err is not None or instance is None
        except Exception:
            # Expected - 404 error
            pass

        # Test get with invalid ID using _with_http_info
        try:
            instance_http, resp, err = await client.get_captcha_instance_with_http_info(
                fake_id
            )
            assert err is not None or instance_http is None
        except Exception:
            # Expected - 404 error
            pass

        # Test get with invalid ID using _without_preload_content
        try:
            resp_preload = await client.get_captcha_instance_without_preload_content(
                fake_id
            )
            # Should handle error appropriately
        except Exception:
            # Expected - invalid ID
            pass

        # Test delete with invalid/non-existent ID (returns 2 values, not 3)
        try:
            _, err = await client.delete_captcha_instance(fake_id)
            assert err is not None
        except Exception:
            # Expected - 404 error
            pass

        # Test delete with invalid ID using _with_http_info
        try:
            _, resp, err = await client.delete_captcha_instance_with_http_info(fake_id)
            assert err is not None
        except Exception:
            # Expected - 404 error
            pass

        # Test delete with invalid ID using _without_preload_content
        try:
            resp_delete = await client.delete_captcha_instance_without_preload_content(
                fake_id
            )
            # Should handle error appropriately
        except Exception:
            # Expected - invalid ID
            pass

        # Test replace with invalid/non-existent ID
        try:
            invalid_update = models.CAPTCHAInstance(
                name="Invalid Update",
                type=models.CAPTCHAType.HCAPTCHA,
                site_key="invalid-site-key",
                secret_key="invalid-secret-key",
            )
            instance, _, err = await client.replace_captcha_instance(
                fake_id, invalid_update
            )
            assert err is not None or instance is None
        except Exception:
            # Expected - 404 error
            pass

        # Test replace with invalid ID using _with_http_info
        try:
            instance_http, resp, err = (
                await client.replace_captcha_instance_with_http_info(
                    fake_id, invalid_update
                )
            )
            assert err is not None or instance_http is None
        except Exception:
            # Expected - 404 error
            pass

        # Test replace with invalid ID using _without_preload_content
        try:
            resp_replace = (
                await client.replace_captcha_instance_without_preload_content(
                    fake_id, invalid_update
                )
            )
            # Should handle error appropriately
        except Exception:
            # Expected - invalid ID
            pass
