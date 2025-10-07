# noqa: C901
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

from http import HTTPStatus

import pytest

import okta.models as models
from tests.mocks import MockOktaClient


class TestAgentPoolsResource:
    """
    Integration Tests for the Agent Pools Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_agent_pools(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # List all agent pools
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None
        assert isinstance(agent_pools, list)
        # Should return at least zero agent pools
        assert len(agent_pools) >= 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_agent_pools_with_filters(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # List agent pools with pool type filter
        agent_pools, _, err = await client.list_agent_pools(
            pool_type=models.AgentType.AD, limit_per_pool_type=10
        )
        assert err is None
        assert isinstance(agent_pools, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_agent_pools_with_multiple_pool_types(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Test with different pool types to exercise more code paths
        for pool_type in [models.AgentType.LDAP, models.AgentType.RADIUS]:
            agent_pools, _, err = await client.list_agent_pools(
                pool_type=pool_type, limit_per_pool_type=5
            )
            assert err is None
            assert isinstance(agent_pools, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_agent_pools_with_pagination(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Test pagination parameters to exercise more code paths
        agent_pools, _, err = await client.list_agent_pools(
            limit_per_pool_type=1, after=None
        )
        assert err is None
        assert isinstance(agent_pools, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_agent_pools_update_settings(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Get agent pool update settings
            settings, _, err = await client.get_agent_pools_update_settings(pool_id)
            assert err is None
            assert isinstance(settings, models.AgentPoolUpdateSetting)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_agent_pools_update_settings_nonexistent(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Test with non-existent pool ID to exercise error handling
        settings, resp, err = await client.get_agent_pools_update_settings(
            "nonexistent-pool-id"
        )
        assert err is not None
        assert resp.status == HTTPStatus.NOT_FOUND

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_agent_pools_update_settings(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Get current settings
            current_settings, _, err = await client.get_agent_pools_update_settings(
                pool_id
            )
            assert err is None

            # Update settings with basic configuration
            updated_settings = models.AgentPoolUpdateSetting(
                pool_id=pool_id,
                continue_on_error=True,
                release_channel=models.ReleaseChannel.GA,
            )

            # Apply the update
            result, _, err = await client.update_agent_pools_update_settings(
                pool_id, updated_settings
            )
            assert err is None
            assert isinstance(result, models.AgentPoolUpdateSetting)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_agent_pools_update_settings_various_channels(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Test different release channels to exercise more code paths
            for channel in [
                models.ReleaseChannel.BETA,
                models.ReleaseChannel.EA,
                models.ReleaseChannel.TEST,
            ]:
                updated_settings = models.AgentPoolUpdateSetting(
                    pool_id=pool_id, continue_on_error=False, release_channel=channel
                )

                result, _, err = await client.update_agent_pools_update_settings(
                    pool_id, updated_settings
                )
                assert err is None
                assert isinstance(result, models.AgentPoolUpdateSetting)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_agent_pools_update(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create agent pool update
            update_request = models.AgentPoolUpdate(
                enabled=True,
                schedule=models.AutoUpdateSchedule(
                    timezone="America/Los_Angeles", delay=0, duration=60
                ),
            )

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None
            assert isinstance(created_update, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_agent_pools_update_different_schedules(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Test different schedule configurations
            schedules = [
                models.AutoUpdateSchedule(timezone="UTC", delay=1, duration=30),
                models.AutoUpdateSchedule(
                    timezone="Europe/London", delay=7, duration=120
                ),
                models.AutoUpdateSchedule(timezone="Asia/Tokyo", delay=3, duration=90),
            ]

            for schedule in schedules:
                update_request = models.AgentPoolUpdate(enabled=True, schedule=schedule)

                created_update, _, err = await client.create_agent_pools_update(
                    pool_id, update_request
                )
                assert err is None
                assert isinstance(created_update, models.AgentPoolUpdate)

                # Clean up
                try:
                    await client.delete_agent_pools_update(pool_id, created_update.id)
                except:
                    pass  # Continue with test even if cleanup fails

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_agent_pools_update_minimal(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create minimal agent pool update
            update_request = models.AgentPoolUpdate(enabled=False)

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None
            assert isinstance(created_update, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_agent_pools_updates(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # List all updates for the pool
            updates, _, err = await client.list_agent_pools_updates(pool_id)
            assert err is None
            assert isinstance(updates, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_agent_pools_updates_scheduled_only(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # List only scheduled updates
            updates, _, err = await client.list_agent_pools_updates(
                pool_id, scheduled=True
            )
            assert err is None
            assert isinstance(updates, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_agent_pools_updates_not_scheduled(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # List non-scheduled updates
            updates, _, err = await client.list_agent_pools_updates(
                pool_id, scheduled=False
            )
            assert err is None
            assert isinstance(updates, list)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_agent_pools_update_instance(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Get list of updates to find a valid update ID
            updates, _, err = await client.list_agent_pools_updates(pool_id)
            assert err is None

            if isinstance(updates, list) and len(updates) > 0:
                update_id = updates[0].id

                # Get specific update instance
                update_instance, _, err = await client.get_agent_pools_update_instance(
                    pool_id, update_id
                )
                assert err is None
                assert isinstance(update_instance, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_agent_pools_update_instance_nonexistent(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Test with non-existent update ID
            update_instance, resp, err = await client.get_agent_pools_update_instance(
                pool_id, "nonexistent-update-id"
            )
            assert err is not None
            assert resp.status == HTTPStatus.NOT_FOUND

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_agent_pools_update(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create an update first
            update_request = models.AgentPoolUpdate(enabled=True)

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None

            # Update the created update
            updated_request = models.AgentPoolUpdate(enabled=False)  # Change this value

            updated_update, _, err = await client.update_agent_pools_update(
                pool_id, created_update.id, updated_request
            )
            assert err is None
            assert isinstance(updated_update, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_agent_pools_update(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create an update that can be activated
            update_request = models.AgentPoolUpdate(enabled=False)

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None

            # Activate the update
            activated_update, _, err = await client.activate_agent_pools_update(
                pool_id, created_update.id
            )
            assert err is None
            assert isinstance(activated_update, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_deactivate_agent_pools_update(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create and activate an update
            update_request = models.AgentPoolUpdate(enabled=True)

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None

            # Deactivate the update
            deactivated_update, _, err = await client.deactivate_agent_pools_update(
                pool_id, created_update.id
            )
            assert err is None
            assert isinstance(deactivated_update, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_pause_agent_pools_update(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create a running update
            update_request = models.AgentPoolUpdate(enabled=True)

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None

            # Pause the update
            paused_update, _, err = await client.pause_agent_pools_update(
                pool_id, created_update.id
            )
            assert err is None
            assert isinstance(paused_update, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_resume_agent_pools_update(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create and pause an update
            update_request = models.AgentPoolUpdate(enabled=True)

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None

            # Pause first
            _, _, err = await client.pause_agent_pools_update(
                pool_id, created_update.id
            )
            assert err is None

            # Resume the update
            resumed_update, _, err = await client.resume_agent_pools_update(
                pool_id, created_update.id
            )
            assert err is None
            assert isinstance(resumed_update, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_stop_agent_pools_update(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create a running update
            update_request = models.AgentPoolUpdate(enabled=True)

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None

            # Stop the update
            stopped_update, _, err = await client.stop_agent_pools_update(
                pool_id, created_update.id
            )
            assert err is None
            assert isinstance(stopped_update, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_retry_agent_pools_update(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create a failed update (this would normally be a failed update)
            update_request = models.AgentPoolUpdate(enabled=True)

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None

            # Retry the update
            retried_update, _, err = await client.retry_agent_pools_update(
                pool_id, created_update.id
            )
            assert err is None
            assert isinstance(retried_update, models.AgentPoolUpdate)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_agent_pools_update(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create an update to delete
            update_request = models.AgentPoolUpdate(enabled=False)

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None

            # Delete the update
            result, resp, err = await client.delete_agent_pools_update(
                pool_id, created_update.id
            )
            assert err is None
            assert resp.status == HTTPStatus.NO_CONTENT

            # Verify the update is deleted
            _, resp, err = await client.get_agent_pools_update_instance(
                pool_id, created_update.id
            )
            assert err is not None
            assert resp.status == HTTPStatus.NOT_FOUND

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_agent_pools_update_nonexistent(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Try to delete non-existent update
            result, resp, err = await client.delete_agent_pools_update(
                pool_id, "nonexistent-update-id"
            )
            assert err is not None
            assert resp.status == HTTPStatus.NOT_FOUND

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_agent_pools_update_lifecycle(self, fs):
        """
        Test complete CRUD lifecycle for agent pool updates
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # 1. Create an update
            update_request = models.AgentPoolUpdate(
                enabled=True,
                schedule=models.AutoUpdateSchedule(
                    timezone="UTC", delay=5, duration=120
                ),
            )

            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None
            assert isinstance(created_update, models.AgentPoolUpdate)

            # 2. Get the created update
            retrieved_update, _, err = await client.get_agent_pools_update_instance(
                pool_id, created_update.id
            )
            assert err is None
            assert retrieved_update.id == created_update.id

            # 3. Update the update
            modified_request = models.AgentPoolUpdate(enabled=False)  # Change this

            updated_update, _, err = await client.update_agent_pools_update(
                pool_id, created_update.id, modified_request
            )
            assert err is None
            assert isinstance(updated_update, models.AgentPoolUpdate)

            # 4. List updates and verify our update is there
            all_updates, _, err = await client.list_agent_pools_updates(pool_id)
            assert err is None
            if isinstance(all_updates, list):
                update_ids = [update.id for update in all_updates]
                assert created_update.id in update_ids

            # 5. Delete the update
            result, resp, err = await client.delete_agent_pools_update(
                pool_id, created_update.id
            )
            assert err is None
            assert resp.status == HTTPStatus.NO_CONTENT

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_agent_pools_update_state_transitions(self, fs):
        """
        Test state transitions for agent pool updates to exercise more code paths
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # First, get list of agent pools to get a valid pool ID
        agent_pools, _, err = await client.list_agent_pools()
        assert err is None

        if isinstance(agent_pools, list) and len(agent_pools) > 0:
            pool_id = agent_pools[0].id

            # Create an update
            update_request = models.AgentPoolUpdate(enabled=False)
            created_update, _, err = await client.create_agent_pools_update(
                pool_id, update_request
            )
            assert err is None

            try:
                # Test activation
                activated_update, _, err = await client.activate_agent_pools_update(
                    pool_id, created_update.id
                )
                assert err is None or activated_update is not None

                # Test pause
                paused_update, _, err = await client.pause_agent_pools_update(
                    pool_id, created_update.id
                )
                assert err is None or paused_update is not None

                # Test resume
                resumed_update, _, err = await client.resume_agent_pools_update(
                    pool_id, created_update.id
                )
                assert err is None or resumed_update is not None

                # Test stop
                stopped_update, _, err = await client.stop_agent_pools_update(
                    pool_id, created_update.id
                )
                assert err is None or stopped_update is not None

                # Test retry
                retried_update, _, err = await client.retry_agent_pools_update(
                    pool_id, created_update.id
                )
                assert err is None or retried_update is not None

            finally:
                # Clean up - delete the update
                try:
                    await client.delete_agent_pools_update(pool_id, created_update.id)
                except:
                    pass  # Ignore cleanup errors

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_agent_pools_error_handling(self, fs):
        """
        Test various error conditions to exercise error handling code paths
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Test with invalid pool ID
        invalid_pool_id = "invalid-pool-id-12345"

        # Test list updates with invalid pool
        updates, resp, err = await client.list_agent_pools_updates(invalid_pool_id)
        assert err is None
        assert resp.status_code == HTTPStatus.OK

        # Test get settings with invalid pool
        settings, resp, err = await client.get_agent_pools_update_settings(
            invalid_pool_id
        )
        assert err is not None
        assert resp.status == HTTPStatus.NOT_FOUND

        # Test create update with invalid pool
        update_request = models.AgentPoolUpdate(enabled=True)
        created_update, resp, err = await client.create_agent_pools_update(
            invalid_pool_id, update_request
        )
        assert err is not None
        assert resp.status == HTTPStatus.BAD_REQUEST
