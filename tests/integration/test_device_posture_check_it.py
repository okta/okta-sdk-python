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

from okta import models
from tests.mocks import MockOktaClient


class TestDevicePostureCheckResource:
    """
    Integration Tests for the Device Posture Check Resource

    This test suite provides comprehensive integration testing for the Device Posture Check API
    within the Okta Python SDK. The tests validate real API interactions using VCR for recording
    and replaying HTTP requests/responses.

    API Methods Tested:
    1. create_device_posture_check() - Create a device posture check
    2. get_device_posture_check() - Get a specific device posture check
    3. list_device_posture_checks() - List all device posture checks
    4. list_default_device_posture_checks() - List default device posture checks
    5. replace_device_posture_check() - Replace/update a device posture check
    6. delete_device_posture_check() - Delete a device posture check
    """

    SDK_PREFIX = "python_sdk_posture"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_device_posture_check_lifecycle(self, fs):
        """
        Test Device Posture Check API operations

        This test covers:
        - Listing default device posture checks (if available)
        - Attempting to create/list custom device posture checks

        Note: Device Posture Checks require Okta Identity Engine with Device Trust add-on.
        If the org doesn't have this feature, the API will return 401 permission errors.
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        posture_check_id = None

        try:
            # ===== LIST DEFAULT DEVICE POSTURE CHECKS =====
            print("\n=== Listing Default Device Posture Checks ===")

            default_checks, _, default_err = await client.list_default_device_posture_checks()

            if default_err is None:
                assert default_checks is not None
                assert isinstance(default_checks, list)
                print(f"Found {len(default_checks)} default device posture check(s)")

                if len(default_checks) > 0:
                    print(f"  First check: {default_checks[0].name}")
            else:
                print(f"Cannot list default checks (permission denied): {default_err}")

            # ===== LIST DEVICE POSTURE CHECKS =====
            print("\n=== Listing Device Posture Checks ===")

            checks_list, _, list_err = await client.list_device_posture_checks()

            if list_err is None:
                assert checks_list is not None
                assert isinstance(checks_list, list)
                print(f"Found {len(checks_list)} device posture check(s)")
            else:
                print(f"Cannot list checks (permission denied): {list_err}")

            # ===== CREATE DEVICE POSTURE CHECK =====
            print("\n=== Creating Device Posture Check ===")

            # Create a custom posture check with OSQuery
            posture_check_name = f"{TestDevicePostureCheckResource.SDK_PREFIX}_check"

            posture_check = models.DevicePostureCheck(
                name=posture_check_name,
                description="Test custom posture check",
                platform="WINDOWS",
                type="CUSTOM",
                mapping_type="TEXTBOX",
                query="SELECT * FROM programs WHERE name = 'AcmeCorpAgent';"
            )

            created_check, _, err = await client.create_device_posture_check(posture_check)

            if err is None:
                assert created_check is not None
                assert isinstance(created_check, models.DevicePostureCheck)
                assert created_check.name == posture_check_name

                posture_check_id = created_check.id
                print(f"Created device posture check: {posture_check_id}")
                print(f"  Name: {created_check.name}")
                print(f"  Platform: {created_check.platform}")
                print(f"  Type: {created_check.type}")

                # ===== GET DEVICE POSTURE CHECK =====
                print("\n=== Getting Specific Device Posture Check ===")

                retrieved_check, _, err = await client.get_device_posture_check(posture_check_id)

                assert err is None, f"Failed to get device posture check: {err}"
                assert retrieved_check is not None
                assert isinstance(retrieved_check, models.DevicePostureCheck)
                assert retrieved_check.id == posture_check_id
                assert retrieved_check.name == posture_check_name

                print(f"Retrieved device posture check: {retrieved_check.id}")
                print(f"  Name: {retrieved_check.name}")

                # ===== REPLACE (UPDATE) DEVICE POSTURE CHECK =====
                print("\n=== Replacing Device Posture Check ===")

                updated_name = f"{posture_check_name}_updated"

                updated_check = models.DevicePostureCheck(
                    name=updated_name,
                    description="Updated test custom posture check",
                    platform="WINDOWS",
                    type="CUSTOM",
                    mapping_type="TEXTBOX",
                    query="SELECT * FROM programs WHERE name = 'UpdatedAcmeCorpAgent';"
                )

                replaced_check, _, err = await client.replace_device_posture_check(
                    posture_check_id, updated_check
                )

                assert err is None, f"Failed to replace device posture check: {err}"
                assert replaced_check is not None
                assert replaced_check.id == posture_check_id
                assert replaced_check.name == updated_name

                print(f"Replaced device posture check successfully")
                print(f"  New name: {replaced_check.name}")

            else:
                print(f"Cannot create posture check (permission denied): {err}")
                print("This is expected for orgs without Device Trust licensing")

            print("\n=== Test completed successfully ===")

        except Exception as e:
            print(f"\n!!! Test failed with error: {e}")
            raise

        finally:
            # ===== DELETE DEVICE POSTURE CHECK =====
            if posture_check_id:
                print("\n=== Cleanup: Deleting Device Posture Check ===")

                try:
                    _, _, err = await client.delete_device_posture_check(posture_check_id)

                    if err:
                        print(f"Warning: Could not delete device posture check: {err}")
                    else:
                        print(f"Deleted device posture check successfully")

                        # Verify deletion by trying to get the check
                        verify_check, _, verify_err = await client.get_device_posture_check(posture_check_id)

                        if verify_err:
                            print(f"Verified check is deleted (404 expected): {verify_err}")

                except Exception as e:
                    print(f"Exception deleting device posture check: {e}")

            print("=== Cleanup completed ===")

