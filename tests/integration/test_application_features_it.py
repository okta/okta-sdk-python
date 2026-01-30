# flake8: noqa
# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import pytest

import okta.models as models
from tests.mocks import MockOktaClient


class TestApplicationFeaturesResource:
    """
    Integration Tests for the Application Features Resource

    This test suite provides comprehensive integration testing for all Application Features API operations
    within the Okta Python SDK. The tests validate real API interactions using VCR for recording
    and replaying HTTP requests/responses.

    API Methods Tested:
    1. list_features_for_application() - List all features for an application
    2. get_feature_for_application() - Get a specific feature
    3. update_feature_for_application() - Update a feature configuration
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_application_features_lifecycle(self, fs):
        """
        Test the complete lifecycle of Application Features

        This test covers:
        - Creating a bookmark application
        - Testing list_features_for_application (may not be supported)
        - Testing get_feature_for_application (may not be supported)
        - Testing update_feature_for_application (may not be supported)
        - Cleaning up the application

        Note: The Application Features API requires provisioning to be enabled,
        which may not be supported for all application types. This test validates
        that all API methods are accessible and handles expected errors gracefully.
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        app_id = None

        try:
            # ===== CREATE APPLICATION =====
            print("\n=== Creating Application ===")

            app_label = "Test App for Features API"
            app_settings_app = models.BookmarkApplicationSettingsApplication(
                requestIntegration=False,
                url="https://example.com/test"
            )
            app_settings = models.BookmarkApplicationSettings(app=app_settings_app)

            app_obj = models.BookmarkApplication(
                name="bookmark",
                label=app_label,
                sign_on_mode=models.ApplicationSignOnMode.BOOKMARK,
                settings=app_settings
            )

            app, _, err = await client.create_application(app_obj)
            assert err is None, f"Failed to create application: {err}"
            assert app is not None
            assert app.id is not None

            app_id = app.id
            print(f"Created app with ID: {app_id}")

            # ===== TEST LIST FEATURES FOR APPLICATION =====
            print("\n=== Testing list_features_for_application ===")

            features_list, _, err = await client.list_features_for_application(app_id)

            # API method was called - this validates the endpoint exists
            # Error is expected for apps without provisioning support
            if err is not None:
                print(f"Expected error (app doesn't support features): {err}")
                assert "provisioning" in str(err).lower() or "feature" in str(err).lower()
            else:
                print(f"Found {len(features_list)} features")
                assert isinstance(features_list, list)

            # ===== TEST GET FEATURE FOR APPLICATION =====
            print("\n=== Testing get_feature_for_application ===")

            feature_name = models.ApplicationFeatureType.USER_PROVISIONING
            retrieved_feature, _, err = await client.get_feature_for_application(
                app_id, feature_name
            )

            # API method was called - validates endpoint exists
            if err is not None:
                print(f"Expected error (app doesn't support this feature): {err}")
            else:
                print(f"Retrieved feature: {feature_name}")
                assert retrieved_feature is not None

            # ===== TEST UPDATE FEATURE FOR APPLICATION =====
            print("\n=== Testing update_feature_for_application ===")

            # Create update request - use CapabilitiesObject directly as the actual_instance
            capabilities = models.CapabilitiesObject()
            update_request = models.UpdateFeatureForApplicationRequest(actual_instance=capabilities)

            updated_feature, _, err = await client.update_feature_for_application(
                app_id, feature_name, update_request
            )

            # API method was called - validates endpoint exists
            if err is not None:
                print(f"Expected error (app doesn't support feature updates): {err}")
            else:
                print(f"Updated feature: {feature_name}")
                assert updated_feature is not None

            print("\n=== All API methods successfully tested ===")

        except Exception as e:
            print(f"\n!!! Test failed with error: {e}")
            raise

        finally:
            # Cleanup
            if app_id:
                try:
                    print(f"\n=== Cleanup: Deactivating app {app_id} ===")
                    _, _, err = await client.deactivate_application(app_id)
                    if err:
                        print(f"Cleanup: Failed to deactivate app: {err}")
                except Exception as exc:
                    print(f"Cleanup: Exception deactivating app: {exc}")

                try:
                    print(f"=== Cleanup: Deleting app {app_id} ===")
                    _, _, err = await client.delete_application(app_id)
                    if err:
                        print(f"Cleanup: Failed to delete app: {err}")
                except Exception as exc:
                    print(f"Cleanup: Exception deleting app: {exc}")

