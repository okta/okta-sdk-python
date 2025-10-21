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
from tests.mocks import MockOktaClient


class TestRateLimitSettingsResource:
    """
    Integration Tests for the Rate Limit Settings Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_rate_limit_admin_notifications(self, fs):
        """Test retrieving rate limit admin notification settings"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Get current admin notification settings
        admin_notifications, _, err = (
            await client.get_rate_limit_settings_admin_notifications()
        )
        assert err is None
        assert isinstance(admin_notifications, models.RateLimitAdminNotifications)
        assert admin_notifications.notifications_enabled is not None
        assert isinstance(admin_notifications.notifications_enabled, bool)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_replace_rate_limit_admin_notifications(self, fs):
        """Test updating rate limit admin notification settings"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Get current settings first to restore later
        original_settings, _, err = (
            await client.get_rate_limit_settings_admin_notifications()
        )
        assert err is None
        original_enabled = original_settings.notifications_enabled

        try:
            # Create notification settings object with opposite value
            new_enabled = not original_enabled
            notification_settings = models.RateLimitAdminNotifications(
                notifications_enabled=new_enabled
            )

            # Update admin notification settings
            updated_settings, _, err = (
                await client.replace_rate_limit_settings_admin_notifications(
                    notification_settings
                )
            )
            assert err is None
            assert isinstance(updated_settings, models.RateLimitAdminNotifications)
            assert updated_settings.notifications_enabled == new_enabled

            # Verify the change by getting settings again
            retrieved_settings, _, err = (
                await client.get_rate_limit_settings_admin_notifications()
            )
            assert err is None
            assert retrieved_settings.notifications_enabled == new_enabled

        finally:
            # Restore original settings
            restore_settings = models.RateLimitAdminNotifications(
                notifications_enabled=original_enabled
            )
            _, _, err = await client.replace_rate_limit_settings_admin_notifications(
                restore_settings
            )
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_rate_limit_per_client_settings(self, fs):
        """Test retrieving per-client rate limit settings"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Get current per-client rate limit settings
        per_client_settings, _, err = await client.get_rate_limit_settings_per_client()
        assert err is None
        assert isinstance(per_client_settings, models.PerClientRateLimitSettings)
        assert per_client_settings.default_mode is not None
        assert isinstance(
            per_client_settings.default_mode, models.PerClientRateLimitMode
        )
        assert per_client_settings.default_mode in [
            models.PerClientRateLimitMode.DISABLE,
            models.PerClientRateLimitMode.ENFORCE,
            models.PerClientRateLimitMode.PREVIEW,
        ]

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_replace_rate_limit_per_client_settings(self, fs):
        """Test updating per-client rate limit settings"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Get current settings first to restore later
        original_settings, _, err = await client.get_rate_limit_settings_per_client()
        assert err is None
        original_mode = original_settings.default_mode

        try:
            # Choose a different mode for testing
            new_mode = models.PerClientRateLimitMode.PREVIEW
            if original_mode == models.PerClientRateLimitMode.PREVIEW:
                new_mode = models.PerClientRateLimitMode.DISABLE

            # Create per-client settings object
            per_client_settings = models.PerClientRateLimitSettings(
                default_mode=new_mode
            )

            # Update per-client rate limit settings
            updated_settings, _, err = (
                await client.replace_rate_limit_settings_per_client(per_client_settings)
            )
            assert err is None
            assert isinstance(updated_settings, models.PerClientRateLimitSettings)
            assert updated_settings.default_mode == new_mode

            # Verify the change by getting settings again
            retrieved_settings, _, err = (
                await client.get_rate_limit_settings_per_client()
            )
            assert err is None
            assert retrieved_settings.default_mode == new_mode

        finally:
            # Restore original settings
            restore_settings = models.PerClientRateLimitSettings(
                default_mode=original_mode,
                use_case_mode_overrides=original_settings.use_case_mode_overrides,
            )
            _, _, err = await client.replace_rate_limit_settings_per_client(
                restore_settings
            )
            assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_rate_limit_warning_threshold(self, fs):
        """Test retrieving rate limit warning threshold"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Get current warning threshold settings
        threshold_response, _, err = (
            await client.get_rate_limit_settings_warning_threshold()
        )
        assert err is None
        assert isinstance(threshold_response, models.RateLimitWarningThresholdResponse)

        # Warning threshold may be None if not set, or should be between 30-90
        if threshold_response.warning_threshold is not None:
            assert 30 <= threshold_response.warning_threshold <= 90

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_replace_rate_limit_warning_threshold(self, fs):
        """Test updating rate limit warning threshold"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Get current settings first to restore later
        original_response, _, err = (
            await client.get_rate_limit_settings_warning_threshold()
        )
        assert err is None
        original_threshold = original_response.warning_threshold

        try:
            # Set a new threshold value (between 30-90)
            new_threshold = 75
            if original_threshold == 75:
                new_threshold = 80

            # Create warning threshold request object
            threshold_request = models.RateLimitWarningThresholdRequest(
                warning_threshold=new_threshold
            )

            # Update warning threshold settings
            updated_response, _, err = (
                await client.replace_rate_limit_settings_warning_threshold(
                    threshold_request
                )
            )
            assert err is None
            assert isinstance(
                updated_response, models.RateLimitWarningThresholdResponse
            )
            assert updated_response.warning_threshold == new_threshold

            # Verify the change by getting settings again
            retrieved_response, _, err = (
                await client.get_rate_limit_settings_warning_threshold()
            )
            assert err is None
            assert retrieved_response.warning_threshold == new_threshold

        finally:
            # Restore original settings if they were set
            if original_threshold is not None:
                restore_request = models.RateLimitWarningThresholdRequest(
                    warning_threshold=original_threshold
                )
                _, _, err = await client.replace_rate_limit_settings_warning_threshold(
                    restore_request
                )
                assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_rate_limit_settings_crud_workflow(self, fs):
        """Test complete CRUD workflow for rate limit settings"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Step 1: Get all current settings to store as backup
        admin_notifications, _, err = (
            await client.get_rate_limit_settings_admin_notifications()
        )
        assert err is None
        original_admin_enabled = admin_notifications.notifications_enabled

        per_client_settings, _, err = await client.get_rate_limit_settings_per_client()
        assert err is None
        original_per_client_mode = per_client_settings.default_mode

        warning_threshold, _, err = (
            await client.get_rate_limit_settings_warning_threshold()
        )
        assert err is None
        original_warning_threshold = warning_threshold.warning_threshold

        try:
            # Step 2: Update admin notifications
            new_admin_notifications = models.RateLimitAdminNotifications(
                notifications_enabled=True
            )
            updated_admin, _, err = (
                await client.replace_rate_limit_settings_admin_notifications(
                    new_admin_notifications
                )
            )
            assert err is None
            assert updated_admin.notifications_enabled is True

            # Step 3: Update per-client settings
            new_per_client = models.PerClientRateLimitSettings(
                default_mode=models.PerClientRateLimitMode.PREVIEW
            )
            updated_per_client, _, err = (
                await client.replace_rate_limit_settings_per_client(new_per_client)
            )
            assert err is None
            assert (
                    updated_per_client.default_mode == models.PerClientRateLimitMode.PREVIEW
            )

            # Step 4: Update warning threshold
            new_threshold_request = models.RateLimitWarningThresholdRequest(
                warning_threshold=85
            )
            updated_threshold, _, err = (
                await client.replace_rate_limit_settings_warning_threshold(
                    new_threshold_request
                )
            )
            assert err is None
            assert updated_threshold.warning_threshold == 85

            # Step 5: Verify all settings are updated
            verify_admin, _, err = (
                await client.get_rate_limit_settings_admin_notifications()
            )
            assert err is None
            assert verify_admin.notifications_enabled is True

            verify_per_client, _, err = (
                await client.get_rate_limit_settings_per_client()
            )
            assert err is None
            assert (
                    verify_per_client.default_mode == models.PerClientRateLimitMode.PREVIEW
            )

            verify_threshold, _, err = (
                await client.get_rate_limit_settings_warning_threshold()
            )
            assert err is None
            assert verify_threshold.warning_threshold == 85

        finally:
            # Restore all original settings
            errors = []

            try:
                restore_admin = models.RateLimitAdminNotifications(
                    notifications_enabled=original_admin_enabled
                )
                _, _, err = (
                    await client.replace_rate_limit_settings_admin_notifications(
                        restore_admin
                    )
                )
                if err:
                    errors.append(f"Failed to restore admin notifications: {err}")
            except Exception as exc:
                errors.append(f"Exception restoring admin notifications: {exc}")

            try:
                restore_per_client = models.PerClientRateLimitSettings(
                    default_mode=original_per_client_mode,
                    use_case_mode_overrides=per_client_settings.use_case_mode_overrides,
                )
                _, _, err = await client.replace_rate_limit_settings_per_client(
                    restore_per_client
                )
                if err:
                    errors.append(f"Failed to restore per-client settings: {err}")
            except Exception as exc:
                errors.append(f"Exception restoring per-client settings: {exc}")

            try:
                if original_warning_threshold is not None:
                    restore_threshold = models.RateLimitWarningThresholdRequest(
                        warning_threshold=original_warning_threshold
                    )
                    _, _, err = (
                        await client.replace_rate_limit_settings_warning_threshold(
                            restore_threshold
                        )
                    )
                    if err:
                        errors.append(f"Failed to restore warning threshold: {err}")
            except Exception as exc:
                errors.append(f"Exception restoring warning threshold: {exc}")

            # Assert no errors occurred during cleanup
            assert len(errors) == 0, f"Cleanup errors: {errors}"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_rate_limit_settings_with_http_info(self, fs):
        """Test rate limit settings APIs with HTTP info"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Test admin notifications with HTTP info
        admin_notifications, response, err = (
            await client.get_rate_limit_settings_admin_notifications_with_http_info()
        )
        assert err is None
        assert isinstance(admin_notifications, models.RateLimitAdminNotifications)
        assert response is not None
        assert response.status_code == 200

        # Test per-client settings with HTTP info
        per_client_settings, response, err = (
            await client.get_rate_limit_settings_per_client_with_http_info()
        )
        assert err is None
        assert isinstance(per_client_settings, models.PerClientRateLimitSettings)
        assert response is not None
        assert response.status_code == 200

        # Test warning threshold with HTTP info
        warning_threshold, response, err = (
            await client.get_rate_limit_settings_warning_threshold_with_http_info()
        )
        assert err is None
        assert isinstance(warning_threshold, models.RateLimitWarningThresholdResponse)
        assert response is not None
        assert response.status_code == 200

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_rate_limit_settings_boundary_values(self, fs):
        """Test rate limit settings with boundary values"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Get current warning threshold to restore later
        original_response, _, err = (
            await client.get_rate_limit_settings_warning_threshold()
        )
        assert err is None
        original_threshold = original_response.warning_threshold

        try:
            # Test minimum threshold value (30)
            min_threshold_request = models.RateLimitWarningThresholdRequest(
                warning_threshold=30
            )
            min_response, _, err = (
                await client.replace_rate_limit_settings_warning_threshold(
                    min_threshold_request
                )
            )
            assert err is None
            assert min_response.warning_threshold == 30

            # Test maximum threshold value (90)
            max_threshold_request = models.RateLimitWarningThresholdRequest(
                warning_threshold=90
            )
            max_response, _, err = (
                await client.replace_rate_limit_settings_warning_threshold(
                    max_threshold_request
                )
            )
            assert err is None
            assert max_response.warning_threshold == 90

        finally:
            # Restore original threshold if it was set
            if original_threshold is not None:
                restore_request = models.RateLimitWarningThresholdRequest(
                    warning_threshold=original_threshold
                )
                _, _, err = await client.replace_rate_limit_settings_warning_threshold(
                    restore_request
                )
                assert err is None
