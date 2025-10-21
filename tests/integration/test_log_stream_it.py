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

import datetime

import pytest

import okta.models as models
from okta.errors.okta_api_error import OktaAPIError
from tests.mocks import MockOktaClient


class TestLogStreamResource:
    """
    Integration Tests for the Log Stream Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_aws_log_stream(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create AWS Log Stream Settings
        log_stream_settings_aws = models.LogStreamSettingsAws(
            **{
                "accountId": "123456789012",
                "eventSourceName": "p",
                "region": "us-east-1",
            }
        )

        # Create AWS Log Stream Object
        STREAM_NAME = "Test AWS Log Stream"

        # Create minimal _links object
        self_link = models.LogStreamSelfLink(
            href=f"/api/v1/logStreams/dummy", method="GET"
        )
        links = models.LogStreamLinksSelfAndLifecycle(var_self=self_link)

        log_stream_obj = models.LogStreamAws(
            **{
                "name": STREAM_NAME,
                "type": models.LogStreamType.AWS_EVENTBRIDGE,
                "settings": log_stream_settings_aws,
                "created": datetime.datetime.now(),
                "id": "dummy-id",
                "lastUpdated": datetime.datetime.now(),
                "status": "ACTIVE",
                "links": links,
            }
        )

        try:
            # Create Log Stream in org
            log_stream, _, err = await client.create_log_stream(log_stream_obj)
            assert err is None
            assert isinstance(log_stream, models.LogStream)
            assert isinstance(log_stream, models.LogStreamAws)
            assert log_stream.name == STREAM_NAME
            assert log_stream.type == models.LogStreamType.AWS_EVENTBRIDGE
            assert log_stream.status == "ACTIVE"
            assert log_stream.settings.account_id == "123456789012"
            assert log_stream.settings.event_source_name == "p"
            assert log_stream.settings.region == "us-east-1"

            # Get log stream and verify details
            found_log_stream, _, err = await client.get_log_stream(log_stream.id)
            assert err is None
            assert found_log_stream.name == STREAM_NAME
            assert found_log_stream.type == models.LogStreamType.AWS_EVENTBRIDGE
            assert found_log_stream.settings.account_id == "123456789012"

        finally:
            # Clean up - delete the log stream
            if "log_stream" in locals() and log_stream:
                try:
                    _, _, err = await client.deactivate_log_stream(log_stream.id)
                    assert err is None

                    _, _, err = await client.delete_log_stream(log_stream.id)
                    assert err is None
                except OktaAPIError:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_log_stream(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create a log stream first
        log_stream_settings_aws = models.LogStreamSettingsAws(
            **{
                "accountId": "123456789012",
                "eventSourceName": "p",
                "region": "us-west-2",
            }
        )

        STREAM_NAME = "Test Get Log Stream"

        # Create minimal _links object
        self_link = models.LogStreamSelfLink(
            href=f"/api/v1/logStreams/dummy", method="GET"
        )
        links = models.LogStreamLinksSelfAndLifecycle(var_self=self_link)

        log_stream_obj = models.LogStreamAws(
            **{
                "name": STREAM_NAME,
                "type": models.LogStreamType.AWS_EVENTBRIDGE,
                "settings": log_stream_settings_aws,
                "created": datetime.datetime.now(),
                "id": "dummy-id",
                "lastUpdated": datetime.datetime.now(),
                "status": "INACTIVE",
                "links": links,
            }
        )

        try:
            # Create Log Stream
            created_log_stream, _, err = await client.create_log_stream(log_stream_obj)
            assert err is None

            # Get the created log stream
            retrieved_log_stream, _, err = await client.get_log_stream(
                created_log_stream.id
            )
            assert err is None
            assert isinstance(retrieved_log_stream, models.LogStream)
            assert isinstance(retrieved_log_stream, models.LogStreamAws)
            assert retrieved_log_stream.id == created_log_stream.id
            assert retrieved_log_stream.name == STREAM_NAME
            assert retrieved_log_stream.type == models.LogStreamType.AWS_EVENTBRIDGE
            assert retrieved_log_stream.settings.account_id == "123456789012"
            assert retrieved_log_stream.settings.region == "us-west-2"

        finally:
            # Clean up
            if "created_log_stream" in locals() and created_log_stream:
                try:
                    _, _, err = await client.deactivate_log_stream(
                        created_log_stream.id
                    )
                    assert err is None

                    _, _, err = await client.delete_log_stream(created_log_stream.id)
                    assert err is None
                except OktaAPIError:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_log_stream(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create a log stream first
        log_stream_settings_aws = models.LogStreamSettingsAws(
            **{
                "accountId": "123456789012",
                "eventSourceName": "p",
                "region": "us-east-1",
            }
        )

        STREAM_NAME = "Test Activate Log Stream"

        # Create minimal _links object
        self_link = models.LogStreamSelfLink(
            href=f"/api/v1/logStreams/dummy", method="GET"
        )
        links = models.LogStreamLinksSelfAndLifecycle(var_self=self_link)

        log_stream_obj = models.LogStreamAws(
            **{
                "name": STREAM_NAME,
                "type": models.LogStreamType.AWS_EVENTBRIDGE,
                "settings": log_stream_settings_aws,
                "created": datetime.datetime.now(),
                "id": "dummy-id",
                "lastUpdated": datetime.datetime.now(),
                "status": "INACTIVE",
                "links": links,
            }
        )

        try:
            # Create Log Stream
            created_log_stream, _, err = await client.create_log_stream(log_stream_obj)
            assert err is None
            assert created_log_stream.status == "ACTIVE"

            # Activate the log stream
            _, _, err = await client.activate_log_stream(created_log_stream.id)
            assert err is None

            # Verify the log stream is active by getting it
            retrieved_log_stream, _, err = await client.get_log_stream(
                created_log_stream.id
            )
            assert err is None
            assert retrieved_log_stream.status == "ACTIVE"

        finally:
            # Clean up
            if "created_log_stream" in locals() and created_log_stream:
                try:
                    # Deactivate first, then delete
                    _, _, err = await client.deactivate_log_stream(
                        created_log_stream.id
                    )
                    assert err is None

                    _, _, err = await client.delete_log_stream(created_log_stream.id)
                    assert err is None
                except OktaAPIError:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_deactivate_log_stream(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create a log stream first
        log_stream_settings_aws = models.LogStreamSettingsAws(
            **{
                "accountId": "123456789012",
                "eventSourceName": "p",
                "region": "us-east-1",
            }
        )

        STREAM_NAME = "Test Deactivate Log Stream"

        # Create minimal _links object
        self_link = models.LogStreamSelfLink(
            href=f"/api/v1/logStreams/dummy", method="GET"
        )
        links = models.LogStreamLinksSelfAndLifecycle(var_self=self_link)

        log_stream_obj = models.LogStreamAws(
            **{
                "name": STREAM_NAME,
                "type": models.LogStreamType.AWS_EVENTBRIDGE,
                "settings": log_stream_settings_aws,
                "created": datetime.datetime.now(),
                "id": "dummy-id",
                "lastUpdated": datetime.datetime.now(),
                "status": "INACTIVE",
                "links": links,
            }
        )

        try:
            # Create Log Stream
            created_log_stream, _, err = await client.create_log_stream(log_stream_obj)
            assert err is None

            # Deactivate the log stream
            _, _, err = await client.deactivate_log_stream(created_log_stream.id)
            assert err is None

            # Verify the log stream is inactive by getting it
            retrieved_log_stream, _, err = await client.get_log_stream(
                created_log_stream.id
            )
            assert err is None
            assert retrieved_log_stream.status == "INACTIVE"

        finally:
            # Clean up
            if "created_log_stream" in locals() and created_log_stream:
                try:
                    _, _, err = await client.delete_log_stream(created_log_stream.id)
                    assert err is None
                except OktaAPIError:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_log_stream(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create a log stream first
        log_stream_settings_aws = models.LogStreamSettingsAws(
            **{
                "accountId": "123456789012",
                "eventSourceName": "p",
                "region": "us-east-1",
            }
        )

        STREAM_NAME = "Test Delete Log Stream"

        # Create minimal _links object
        self_link = models.LogStreamSelfLink(
            href=f"/api/v1/logStreams/dummy", method="GET"
        )
        links = models.LogStreamLinksSelfAndLifecycle(var_self=self_link)

        log_stream_obj = models.LogStreamAws(
            **{
                "name": STREAM_NAME,
                "type": models.LogStreamType.AWS_EVENTBRIDGE,
                "settings": log_stream_settings_aws,
                "created": datetime.datetime.now(),
                "id": "dummy-id",
                "lastUpdated": datetime.datetime.now(),
                "status": "INACTIVE",
                "links": links,
            }
        )

        # Create Log Stream
        created_log_stream, _, err = await client.create_log_stream(log_stream_obj)
        assert err is None
        assert created_log_stream.name == STREAM_NAME

        _, _, err = await client.deactivate_log_stream(created_log_stream.id)
        assert err is None

        # Delete the log stream
        _, _, err = await client.delete_log_stream(created_log_stream.id)
        assert err is None

        # Verify the log stream is deleted by trying to get it
        try:
            _, _, err = await client.get_log_stream(created_log_stream.id)
            # Should get a 404 error when trying to get a deleted log stream
            assert err is not None
            assert "404" in str(err) or "Not Found" in str(err)
        except OktaAPIError as e:
            # Expected - log stream should not be found
            assert e.status == 404

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_log_streams(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create a few log streams for testing list functionality
        log_streams_created = []

        try:
            # Create AWS Log Stream
            aws_settings = models.LogStreamSettingsAws(
                **{
                    "accountId": "123456789012",
                    "eventSourceName": "p",
                    "region": "us-east-1",
                }
            )
            # Create minimal _links object
            self_link = models.LogStreamSelfLink(
                href=f"/api/v1/logStreams/dummy", method="GET"
            )
            links = models.LogStreamLinksSelfAndLifecycle(var_self=self_link)

            aws_log_stream = models.LogStreamAws(
                **{
                    "name": "Test List AWS Log Stream",
                    "type": models.LogStreamType.AWS_EVENTBRIDGE,
                    "settings": aws_settings,
                    "created": datetime.datetime.now(),
                    "id": "dummy-id",
                    "lastUpdated": datetime.datetime.now(),
                    "status": "INACTIVE",
                    "links": links,
                }
            )
            created_aws, _, err = await client.create_log_stream(aws_log_stream)
            assert err is None
            log_streams_created.append(created_aws)

            # List all log streams
            log_streams, _, err = await client.list_log_streams()
            assert err is None
            assert isinstance(log_streams, list)
            assert len(log_streams) >= 1  # At least the one we created

            # Verify our created log streams are in the list
            created_ids = {ls.id for ls in log_streams_created}
            listed_ids = {ls.id for ls in log_streams}
            assert created_ids.issubset(listed_ids)

            # Verify different types are present
            types_in_list = {ls.type for ls in log_streams}
            assert (
                    models.LogStreamType.AWS_EVENTBRIDGE in types_in_list
                    or models.LogStreamType.SPLUNK_CLOUD_LOGSTREAMING in types_in_list
            )

        finally:
            # Clean up all created log streams
            for log_stream in log_streams_created:
                try:
                    # Deactivate if active, then delete
                    if log_stream.status == "ACTIVE":
                        _, _, err = await client.deactivate_log_stream(log_stream.id)
                    _, _, err = await client.delete_log_stream(log_stream.id)
                except OktaAPIError:
                    pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_log_stream_lifecycle_complete_flow(self, fs):
        """Test complete CRUD lifecycle for a log stream"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create AWS Log Stream Settings
        log_stream_settings_aws = models.LogStreamSettingsAws(
            **{
                "accountId": "123456789012",
                "eventSourceName": "p",
                "region": "us-west-1",
            }
        )

        # Create AWS Log Stream Object
        STREAM_NAME = "Test Lifecycle Log Stream"

        # Create minimal _links object
        self_link = models.LogStreamSelfLink(
            href=f"/api/v1/logStreams/dummy", method="GET"
        )
        links = models.LogStreamLinksSelfAndLifecycle(var_self=self_link)

        log_stream_obj = models.LogStreamAws(
            **{
                "name": STREAM_NAME,
                "type": models.LogStreamType.AWS_EVENTBRIDGE,
                "settings": log_stream_settings_aws,
                "created": datetime.datetime.now(),
                "id": "dummy-id",
                "lastUpdated": datetime.datetime.now(),
                "status": "ACTIVE",
                "links": links,
            }
        )

        try:
            # Step 1: Create Log Stream
            created_log_stream, _, err = await client.create_log_stream(log_stream_obj)
            assert err is None
            assert created_log_stream.status == "ACTIVE"
            assert created_log_stream.name == STREAM_NAME

            # Step 2: Get Log Stream
            retrieved_log_stream, _, err = await client.get_log_stream(
                created_log_stream.id
            )
            assert err is None
            assert retrieved_log_stream.id == created_log_stream.id
            assert retrieved_log_stream.status == "ACTIVE"

            # Step 3: Activate Log Stream
            activated_log_stream, _, err = await client.activate_log_stream(
                created_log_stream.id
            )
            assert err is None

            # Step 4: Verify activation by getting again
            active_log_stream, _, err = await client.get_log_stream(
                created_log_stream.id
            )
            assert err is None
            assert active_log_stream.status == "ACTIVE"

            # Step 5: Deactivate Log Stream
            deactivated_log_stream, _, err = await client.deactivate_log_stream(
                created_log_stream.id
            )
            assert err is None

            # Step 6: Verify deactivation by getting again
            inactive_log_stream, _, err = await client.get_log_stream(
                created_log_stream.id
            )
            assert err is None
            assert inactive_log_stream.status == "INACTIVE"

            # Step 7: Delete Log Stream
            _, _, err = await client.delete_log_stream(created_log_stream.id)
            assert err is None

            # Step 8: Verify deletion by trying to get
            try:
                _, _, err = await client.get_log_stream(created_log_stream.id)
                assert err is not None
            except OktaAPIError as e:
                assert e.status == 404

        except Exception:
            # Clean up on any failure
            if "created_log_stream" in locals() and created_log_stream:
                try:
                    # Try to deactivate first, then delete
                    _, _, err = await client.deactivate_log_stream(
                        created_log_stream.id
                    )
                    _, _, err = await client.delete_log_stream(created_log_stream.id)
                except OktaAPIError:
                    pass
            raise

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_log_stream_error_handling(self, fs):
        """Test error handling for invalid operations"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Test getting non-existent log stream
        try:
            _, _, err = await client.get_log_stream("non-existent-id")
            assert err is not None
        except OktaAPIError as e:
            assert e.status == 404

        # Test activating non-existent log stream
        try:
            _, _, err = await client.activate_log_stream("non-existent-id")
            assert err is not None
        except OktaAPIError as e:
            assert e.status == 404

        # Test deactivating non-existent log stream
        try:
            _, _, err = await client.deactivate_log_stream("non-existent-id")
            assert err is not None
        except OktaAPIError as e:
            assert e.status == 404
