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


class TestDeviceAssuranceResource:
    """
    Integration Tests for the Device Assurance Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_windows_device_assurance_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Windows Device Assurance Policy Object
        POLICY_NAME = "Test Windows Device Assurance Policy"

        # Create OS version constraint
        os_version = models.OSVersion(**{"minimum": "10.0.19041"})

        # Create disk encryption type constraint - Windows uses ALL_INTERNAL_VOLUMES
        disk_encryption_type = (
            models.DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType(
                **{"include": [models.DiskEncryptionType.ALL_INTERNAL_VOLUMES]}
            )
        )

        # Create screen lock type constraint
        screen_lock_type = models.DeviceAssuranceAndroidPlatformAllOfScreenLockType(
            **{"include": [models.ScreenLockType.BIOMETRIC]}
        )

        # Create Windows Device Assurance Policy - jailbreak is not supported for Windows
        windows_policy = models.DeviceAssuranceWindowsPlatform(
            **{
                "name": POLICY_NAME,
                "platform": models.Platform.WINDOWS,
                "osVersion": os_version,
                "diskEncryptionType": disk_encryption_type,
                "screenLockType": screen_lock_type,
                "secureHardwarePresent": True,
            }
        )

        policy = None
        try:
            # Create Device Assurance Policy
            policy, _, err = await client.create_device_assurance_policy(windows_policy)
            assert err is None
            assert isinstance(policy, models.DeviceAssurance)
            assert policy.name == POLICY_NAME
            assert policy.platform == models.Platform.WINDOWS

            # Get policy and verify details
            found_policy, _, err = await client.get_device_assurance_policy(policy.id)
            assert err is None
            assert found_policy.name == POLICY_NAME
            assert found_policy.platform == models.Platform.WINDOWS
            assert found_policy.os_version.minimum == "10.0.19041"

        finally:
            errors = []
            # Delete created policy
            if policy:
                try:
                    _, _, err = await client.delete_device_assurance_policy(policy.id)
                    if err is not None:
                        errors.append(err)
                except Exception as exc:
                    errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_macos_device_assurance_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create macOS Device Assurance Policy Object
        POLICY_NAME = "Test macOS Device Assurance Policy"

        # Create OS version constraint
        os_version = models.OSVersion(**{"minimum": "12.0"})

        # Create disk encryption type constraint - macOS uses ALL_INTERNAL_VOLUMES
        disk_encryption_type = (
            models.DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType(
                **{"include": [models.DiskEncryptionType.ALL_INTERNAL_VOLUMES]}
            )
        )

        # Create macOS Device Assurance Policy - jailbreak is not supported for macOS
        macos_policy = models.DeviceAssuranceMacOSPlatform(
            **{
                "name": POLICY_NAME,
                "platform": models.Platform.MACOS,
                "osVersion": os_version,
                "diskEncryptionType": disk_encryption_type,
                "secureHardwarePresent": True,
            }
        )

        policy = None
        try:
            # Create Device Assurance Policy
            policy, _, err = await client.create_device_assurance_policy(macos_policy)
            assert err is None
            assert isinstance(policy, models.DeviceAssurance)
            assert policy.name == POLICY_NAME
            assert policy.platform == models.Platform.MACOS

            # Get policy and verify details
            found_policy, _, err = await client.get_device_assurance_policy(policy.id)
            assert err is None
            assert found_policy.name == POLICY_NAME
            assert found_policy.platform == models.Platform.MACOS

        finally:
            errors = []
            # Delete created policy
            if policy:
                try:
                    _, _, err = await client.delete_device_assurance_policy(policy.id)
                    if err is not None:
                        errors.append(err)
                except Exception as exc:
                    errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_android_device_assurance_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Android Device Assurance Policy Object
        POLICY_NAME = "Test Android Device Assurance Policy"

        # Create OS version constraint - Android uses different version format
        os_version = models.OSVersion(**{"minimum": "11"})

        # Create Android Device Assurance Policy with minimal required fields first
        android_policy = models.DeviceAssuranceAndroidPlatform(
            **{
                "name": POLICY_NAME,
                "platform": models.Platform.ANDROID,
                "osVersion": os_version,
                "jailbreak": False,
            }
        )

        policy = None
        try:
            # Create Device Assurance Policy
            policy, _, err = await client.create_device_assurance_policy(android_policy)
            assert err is None
            assert isinstance(policy, models.DeviceAssurance)
            assert policy.name == POLICY_NAME
            assert policy.platform == models.Platform.ANDROID

            # Get policy and verify details
            found_policy, _, err = await client.get_device_assurance_policy(policy.id)
            assert err is None
            assert found_policy.name == POLICY_NAME
            assert found_policy.platform == models.Platform.ANDROID

        finally:
            errors = []
            # Delete created policy
            if policy:
                try:
                    _, _, err = await client.delete_device_assurance_policy(policy.id)
                    if err is not None:
                        errors.append(err)
                except Exception as exc:
                    errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_ios_device_assurance_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create iOS Device Assurance Policy Object
        POLICY_NAME = "Test iOS Device Assurance Policy"

        # Create OS version constraint
        os_version = models.OSVersion(**{"minimum": "15.0"})

        # Create screen lock type constraint
        screen_lock_type = models.DeviceAssuranceAndroidPlatformAllOfScreenLockType(
            **{"include": [models.ScreenLockType.BIOMETRIC]}
        )

        # Create iOS Device Assurance Policy
        ios_policy = models.DeviceAssuranceIOSPlatform(
            **{
                "name": POLICY_NAME,
                "platform": models.Platform.IOS,
                "osVersion": os_version,
                "screenLockType": screen_lock_type,
                "jailbreak": False,
            }
        )

        policy = None
        try:
            # Create Device Assurance Policy
            policy, _, err = await client.create_device_assurance_policy(ios_policy)
            assert err is None
            assert isinstance(policy, models.DeviceAssurance)
            assert policy.name == POLICY_NAME
            assert policy.platform == models.Platform.IOS

            # Get policy and verify details
            found_policy, _, err = await client.get_device_assurance_policy(policy.id)
            assert err is None
            assert found_policy.name == POLICY_NAME
            assert found_policy.platform == models.Platform.IOS

        finally:
            errors = []
            # Delete created policy
            if policy:
                try:
                    _, _, err = await client.delete_device_assurance_policy(policy.id)
                    if err is not None:
                        errors.append(err)
                except Exception as exc:
                    errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr(record_mode="all")
    @pytest.mark.asyncio
    async def atest_create_chromeos_device_assurance_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create ChromeOS Device Assurance Policy Object
        POLICY_NAME = "Test ChromeOS Device Assurance Policy"

        # Create OS version constraint
        os_version = models.OSVersion(**{"minimum": "100.0"})

        # Create ChromeOS Device Assurance Policy with minimal setup
        # Note: ChromeOS may require Device Trust to be enabled in the org
        chromeos_policy = models.DeviceAssuranceChromeOSPlatform(
            **{
                "name": POLICY_NAME,
                "platform": models.Platform.CHROMEOS,
                "osVersion": os_version,
            }
        )

        policy = None
        try:
            # Create Device Assurance Policy
            policy, _, err = await client.create_device_assurance_policy(
                chromeos_policy
            )

            # ChromeOS has specific requirements that may not be enabled in all orgs
            if err is not None:
                error_message = str(err)
                if "Chrome Device Trust" in error_message:
                    # Skip if ChromeOS Device Trust is not enabled in the org
                    import pytest

                    pytest.skip(
                        "ChromeOS Device Trust feature is not enabled in this Okta org"
                    )
                elif "device condition" in error_message:
                    # Skip if the org requires specific device conditions that we can't easily satisfy
                    import pytest

                    pytest.skip(
                        "ChromeOS device assurance requires specific device conditions not available in this test org"
                    )

            assert err is None
            assert isinstance(policy, models.DeviceAssurance)
            assert policy.name == POLICY_NAME
            assert policy.platform == models.Platform.CHROMEOS

            # Get policy and verify details
            found_policy, _, err = await client.get_device_assurance_policy(policy.id)
            assert err is None
            assert found_policy.name == POLICY_NAME
            assert found_policy.platform == models.Platform.CHROMEOS

        finally:
            errors = []
            # Delete created policy
            if policy:
                try:
                    _, _, err = await client.delete_device_assurance_policy(policy.id)
                    if err is not None:
                        errors.append(err)
                except Exception as exc:
                    errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_device_assurance_policies(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create a test policy first
        POLICY_NAME = "Test List Device Assurance Policy"

        os_version = models.OSVersion(**{"minimum": "10.0"})

        test_policy = models.DeviceAssuranceWindowsPlatform(
            **{
                "name": POLICY_NAME,
                "platform": models.Platform.WINDOWS,
                "osVersion": os_version,
            }
        )

        created_policy = None
        try:
            # Create Device Assurance Policy
            created_policy, _, err = await client.create_device_assurance_policy(
                test_policy
            )
            assert err is None

            # List all policies
            policies, _, err = await client.list_device_assurance_policies()
            assert err is None
            assert isinstance(policies, list)
            assert len(policies) >= 1

            # Verify our created policy is in the list
            policy_names = [policy.name for policy in policies]
            assert POLICY_NAME in policy_names

        finally:
            errors = []
            # Clean up - delete created policy
            if created_policy:
                try:
                    _, _, err = await client.delete_device_assurance_policy(
                        created_policy.id
                    )
                    if err is not None:
                        errors.append(err)
                except Exception as exc:
                    errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_device_assurance_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create initial policy
        ORIGINAL_NAME = "Original Device Assurance Policy"
        UPDATED_NAME = "Updated Device Assurance Policy"

        os_version = models.OSVersion(**{"minimum": "10.0"})

        # Create original policy - secureHardwarePresent only accepts true as valid value
        original_policy = models.DeviceAssuranceWindowsPlatform(
            **{
                "name": ORIGINAL_NAME,
                "platform": models.Platform.WINDOWS,
                "osVersion": os_version,
                "secureHardwarePresent": True,
            }
        )

        created_policy = None
        try:
            # Create Device Assurance Policy
            created_policy, _, err = await client.create_device_assurance_policy(
                original_policy
            )
            assert err is None
            assert created_policy.name == ORIGINAL_NAME

            # Update the policy with different OS version and name
            updated_os_version = models.OSVersion(**{"minimum": "11.0"})

            # Create disk encryption type constraint for the update
            disk_encryption_type = (
                models.DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType(
                    **{"include": [models.DiskEncryptionType.ALL_INTERNAL_VOLUMES]}
                )
            )

            updated_policy = models.DeviceAssuranceWindowsPlatform(
                **{
                    "name": UPDATED_NAME,
                    "platform": models.Platform.WINDOWS,
                    "osVersion": updated_os_version,
                    "diskEncryptionType": disk_encryption_type,
                    "secureHardwarePresent": True,  # Keep as true since it's the only valid value
                }
            )

            # Replace the policy
            replaced_policy, _, err = await client.replace_device_assurance_policy(
                created_policy.id, updated_policy
            )
            assert err is None
            assert replaced_policy.name == UPDATED_NAME
            assert replaced_policy.secure_hardware_present is True

            # Verify the update by fetching the policy
            fetched_policy, _, err = await client.get_device_assurance_policy(
                created_policy.id
            )
            assert err is None
            assert fetched_policy.name == UPDATED_NAME
            assert fetched_policy.os_version.minimum == "11.0"

        finally:
            errors = []
            # Delete created policy
            if created_policy:
                try:
                    _, _, err = await client.delete_device_assurance_policy(
                        created_policy.id
                    )
                    if err is not None:
                        errors.append(err)
                except Exception as exc:
                    errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_nonexistent_device_assurance_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Try to get a non-existent policy
        FAKE_ID = "fake-device-assurance-policy-id"

        try:
            policy, _, err = await client.get_device_assurance_policy(FAKE_ID)
            # Should get an error for non-existent policy
            assert err is not None
            assert isinstance(err, OktaAPIError)
            assert "404" in str(err) or "Not Found" in str(err)
        except Exception as e:
            # If an exception is thrown instead of returning an error
            assert "404" in str(e) or "Not Found" in str(e)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_nonexistent_device_assurance_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Try to delete a non-existent policy
        FAKE_ID = "fake-device-assurance-policy-id"

        try:
            resp, err = await client.delete_device_assurance_policy(FAKE_ID)
            # Should get an error for non-existent policy
            assert err is not None
            assert isinstance(err, OktaAPIError)
            assert "404" in str(err) or "Not Found" in str(err)
        except Exception as e:
            # If an exception is thrown instead of returning an error
            assert "404" in str(e) or "Not Found" in str(e)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_device_assurance_policy_crud_flow(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Complete CRUD flow test
        POLICY_NAME = "CRUD Test Device Assurance Policy"
        UPDATED_POLICY_NAME = "CRUD Updated Device Assurance Policy"

        # CREATE
        os_version = models.OSVersion(**{"minimum": "10.0"})

        disk_encryption = models.DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType(
            **{
                "include": [
                    models.DiskEncryptionType.ALL_INTERNAL_VOLUMES
                ]  # Use correct disk encryption type for Windows
            }
        )

        policy = models.DeviceAssuranceWindowsPlatform(
            **{
                "name": POLICY_NAME,
                "platform": models.Platform.WINDOWS,
                "osVersion": os_version,
                "diskEncryptionType": disk_encryption,
                "secureHardwarePresent": True,
            }
        )

        created_policy = None
        try:
            # CREATE - Create Device Assurance Policy
            created_policy, _, err = await client.create_device_assurance_policy(policy)
            assert err is None
            assert isinstance(created_policy, models.DeviceAssurance)
            assert created_policy.name == POLICY_NAME
            policy_id = created_policy.id

            # READ - Get the created policy
            read_policy, _, err = await client.get_device_assurance_policy(policy_id)
            assert err is None
            assert read_policy.id == policy_id
            assert read_policy.name == POLICY_NAME

            # UPDATE - Replace the policy
            updated_os_version = models.OSVersion(**{"minimum": "11.0"})

            updated_policy = models.DeviceAssuranceWindowsPlatform(
                **{
                    "name": UPDATED_POLICY_NAME,
                    "platform": models.Platform.WINDOWS,
                    "osVersion": updated_os_version,
                    "diskEncryptionType": disk_encryption,
                    "secureHardwarePresent": True,  # Keep as true since it's the only valid value
                }
            )

            replaced_policy, _, err = await client.replace_device_assurance_policy(
                policy_id, updated_policy
            )
            assert err is None
            assert replaced_policy.name == UPDATED_POLICY_NAME
            assert replaced_policy.secure_hardware_present is True

            # READ - Verify the update
            updated_read_policy, _, err = await client.get_device_assurance_policy(
                policy_id
            )
            assert err is None
            assert updated_read_policy.name == UPDATED_POLICY_NAME
            assert updated_read_policy.os_version.minimum == "11.0"

            # LIST - Verify policy appears in list
            policies, _, err = await client.list_device_assurance_policies()
            assert err is None
            policy_ids = [p.id for p in policies]
            assert policy_id in policy_ids

            # DELETE - Delete the policy
            _, _, err = await client.delete_device_assurance_policy(policy_id)
            assert err is None

            # Verify deletion - should get 404 when trying to fetch
            try:
                deleted_policy, _, err = await client.get_device_assurance_policy(
                    policy_id
                )
                assert err is not None
                assert "404" in str(err) or "Not Found" in str(err)
            except Exception as e:
                assert "404" in str(e) or "Not Found" in str(e)

        except Exception as e:
            # Clean up in case of test failure
            if created_policy and created_policy.id:
                try:
                    await client.delete_device_assurance_policy(created_policy.id)
                except:
                    pass  # Ignore cleanup errors
            raise e
