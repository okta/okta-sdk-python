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
from okta.errors.okta_api_error import OktaAPIError
from tests.mocks import MockOktaClient


class TestApplicationCrossAppAccessConnectionsResource:
    """
    Integration Tests for the Application Cross App Access Connections Resource

    This test suite provides comprehensive integration testing for all Application Cross App Access Connections API operations
    within the Okta Python SDK. The tests validate real API interactions using VCR for recording
    and replaying HTTP requests/responses.

    API Methods Tested:
    1. create_cross_app_access_connection() - Create a cross app access connection
    2. get_cross_app_access_connection() - Get a specific connection
    3. get_all_cross_app_access_connections() - List all connections for an app
    4. update_cross_app_access_connection() - Update a connection
    5. delete_cross_app_access_connection() - Delete a connection
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_cross_app_access_connection_lifecycle(self, fs):
        """
        Test the complete lifecycle of Cross App Access Connections

        This test covers:
        - Creating two OIDC applications (requesting and resource apps)
        - Creating a cross app access connection
        - Retrieving the connection
        - Listing connections
        - Updating the connection status
        - Deleting the connection
        - Cleaning up applications
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        requesting_app_id = None
        resource_app_id = None
        connection_id = None

        try:
            # ===== CREATE REQUESTING APPLICATION (Bookmark) =====
            print("\n=== Creating Requesting Application ===")

            requesting_app_label = "Test Requesting App for CWO"
            requesting_app_settings_app = models.BookmarkApplicationSettingsApplication(
                requestIntegration=False,
                url="https://example.com/requesting"
            )
            requesting_app_settings = models.BookmarkApplicationSettings(
                app=requesting_app_settings_app
            )

            requesting_app_obj = models.BookmarkApplication(
                name="bookmark",
                label=requesting_app_label,
                sign_on_mode=models.ApplicationSignOnMode.BOOKMARK,
                settings=requesting_app_settings
            )

            requesting_app, _, err = await client.create_application(requesting_app_obj)
            assert err is None, f"Failed to create requesting application: {err}"
            assert requesting_app is not None
            assert requesting_app.id is not None

            requesting_app_id = requesting_app.id
            print(f"Created requesting app with ID: {requesting_app_id}")

            # ===== USE SAME APP AS RESOURCE (due to app instance limits) =====
            print("\n=== Using same app as resource app (to avoid instance limits) ===")

            # Use the same app as both requesting and resource for testing purposes
            resource_app_id = requesting_app_id
            print(f"Using resource app with ID: {resource_app_id}")

            # ===== CREATE CROSS APP ACCESS CONNECTION =====
            print("\n=== Creating Cross App Access Connection ===")

            # Create connection object - only specify resource app
            # The requesting app is specified in the URL path
            connection_obj = models.OrgCrossAppAccessConnection(
                resource_app_instance_id=resource_app_id
            )

            # Create the connection
            connection, _, err = await client.create_cross_app_access_connection(
                app_id=requesting_app_id,
                org_cross_app_access_connection=connection_obj
            )

            assert err is None, f"Failed to create cross app access connection: {err}"
            assert connection is not None
            assert isinstance(connection, models.OrgCrossAppAccessConnection)
            assert connection.id is not None
            assert connection.requesting_app_instance_id == requesting_app_id
            assert connection.resource_app_instance_id == resource_app_id
            assert connection.status in ["ACTIVE", "PENDING"]

            connection_id = connection.id
            print(f"Created connection with ID: {connection_id}, status: {connection.status}")

            # ===== GET CROSS APP ACCESS CONNECTION =====
            print("\n=== Getting Cross App Access Connection ===")

            retrieved_connection, _, err = await client.get_cross_app_access_connection(
                app_id=requesting_app_id,
                connection_id=connection_id
            )

            assert err is None, f"Failed to get cross app access connection: {err}"
            assert retrieved_connection is not None
            assert isinstance(retrieved_connection, models.OrgCrossAppAccessConnection)
            assert retrieved_connection.id == connection_id
            assert retrieved_connection.requesting_app_instance_id == requesting_app_id
            assert retrieved_connection.resource_app_instance_id == resource_app_id
            print(f"Retrieved connection: {retrieved_connection.id}")

            # ===== LIST CROSS APP ACCESS CONNECTIONS =====
            print("\n=== Listing Cross App Access Connections ===")

            connections_list, _, err = await client.get_all_cross_app_access_connections(
                app_id=requesting_app_id
            )

            assert err is None, f"Failed to list cross app access connections: {err}"
            assert isinstance(connections_list, list)
            assert len(connections_list) > 0

            # Verify our created connection is in the list
            found_in_list = any(conn.id == connection_id for conn in connections_list)
            assert found_in_list, f"Created connection {connection_id} not found in list"
            print(f"Found {len(connections_list)} connections, including our new connection")

            # ===== UPDATE CROSS APP ACCESS CONNECTION =====
            print("\n=== Updating Cross App Access Connection ===")

            # Create patch request to change status
            # If currently ACTIVE, set to INACTIVE, and vice versa
            new_status = "INACTIVE" if connection.status == "ACTIVE" else "ACTIVE"
            patch_request = models.OrgCrossAppAccessConnectionPatchRequest(
                status=new_status
            )

            updated_connection, _, err = await client.update_cross_app_access_connection(
                app_id=requesting_app_id,
                connection_id=connection_id,
                org_cross_app_access_connection_patch_request=patch_request
            )

            assert err is None, f"Failed to update cross app access connection: {err}"
            assert updated_connection is not None
            assert isinstance(updated_connection, models.OrgCrossAppAccessConnection)
            assert updated_connection.id == connection_id
            assert updated_connection.status == new_status
            print(f"Updated connection status to: {updated_connection.status}")

            # ===== DELETE CROSS APP ACCESS CONNECTION =====
            print("\n=== Deleting Cross App Access Connection ===")

            delete_result, _, err = await client.delete_cross_app_access_connection(
                app_id=requesting_app_id,
                connection_id=connection_id
            )

            assert err is None, f"Failed to delete cross app access connection: {err}"
            print(f"Successfully deleted connection {connection_id}")

            # Verify connection is deleted - trying to get it should fail
            try:
                deleted_connection, _, get_err = await client.get_cross_app_access_connection(
                    app_id=requesting_app_id,
                    connection_id=connection_id
                )
                # If no error, the connection should be None or we should have an error
                assert get_err is not None or deleted_connection is None, \
                    f"Connection {connection_id} should be deleted but still exists"
            except OktaAPIError as e:
                # Expected - connection not found
                print(f"Verified connection is deleted (got expected 404)")

            # Reset for cleanup
            connection_id = None

        except Exception as e:
            print(f"\n!!! Test failed with error: {e}")
            raise

        finally:
            # Cleanup in case of test failure
            errors = []

            # Delete connection if it still exists
            if connection_id and requesting_app_id:
                try:
                    print(f"\n=== Cleanup: Deleting connection {connection_id} ===")
                    _, _, err = await client.delete_cross_app_access_connection(
                        app_id=requesting_app_id,
                        connection_id=connection_id
                    )
                    if err:
                        print(f"Cleanup: Failed to delete connection: {err}")
                except Exception as exc:
                    errors.append(exc)
                    print(f"Cleanup: Exception deleting connection: {exc}")

            # Deactivate and delete requesting app (which was also used as resource app)
            if requesting_app_id:
                try:
                    print(f"\n=== Cleanup: Deactivating app {requesting_app_id} ===")
                    _, _, err = await client.deactivate_application(requesting_app_id)
                    if err:
                        print(f"Cleanup: Failed to deactivate app: {err}")
                except Exception as exc:
                    errors.append(exc)
                    print(f"Cleanup: Exception deactivating app: {exc}")

                try:
                    print(f"=== Cleanup: Deleting app {requesting_app_id} ===")
                    _, _, err = await client.delete_application(requesting_app_id)
                    if err:
                        print(f"Cleanup: Failed to delete app: {err}")
                except Exception as exc:
                    errors.append(exc)
                    print(f"Cleanup: Exception deleting app: {exc}")

            # Don't fail the test on cleanup errors, just log them
            if errors:
                print(f"\n=== Cleanup completed with {len(errors)} error(s) ===")

