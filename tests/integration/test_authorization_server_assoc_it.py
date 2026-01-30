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


class TestAuthorizationServerAssocResource:
    """
    Integration Tests for the Authorization Server Association Resource

    This test suite provides comprehensive integration testing for the Authorization Server Association API
    within the Okta Python SDK. The tests validate real API interactions using VCR for recording
    and replaying HTTP requests/responses.

    API Methods Tested:
    1. create_associated_servers() - Create trusted relationships between authorization servers
    2. list_associated_servers_by_trusted_type() - List associated authorization servers
    3. delete_associated_server() - Delete an association between authorization servers
    """

    SDK_PREFIX = "python_sdk_assoc"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_associated_server_lifecycle(self, fs):
        """
        Test the complete lifecycle of Authorization Server Association operations

        This test covers:
        - Creating two temporary authorization servers
        - Creating an association between them
        - Listing associated servers
        - Deleting the association
        - Cleaning up the temporary servers
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        primary_server_id = None
        associated_server_id = None

        try:
            # ===== CREATE PRIMARY AUTHORIZATION SERVER =====
            print("\n=== Creating Primary Authorization Server ===")

            primary_name = f"{TestAuthorizationServerAssocResource.SDK_PREFIX}_primary"
            primary_server = models.AuthorizationServer(
                name=primary_name,
                description="Primary Auth Server for Association Test",
                audiences=["api://primary"]
            )

            created_primary, _, err = await client.create_authorization_server(primary_server)

            assert err is None, f"Failed to create primary server: {err}"
            assert created_primary is not None
            assert isinstance(created_primary, models.AuthorizationServer)

            primary_server_id = created_primary.id
            print(f"Created primary server: {primary_server_id}")

            # ===== CREATE ASSOCIATED AUTHORIZATION SERVER =====
            print("\n=== Creating Associated Authorization Server ===")

            associated_name = f"{TestAuthorizationServerAssocResource.SDK_PREFIX}_associated"
            associated_server = models.AuthorizationServer(
                name=associated_name,
                description="Associated Auth Server for Association Test",
                audiences=["api://associated"]
            )

            created_associated, _, err = await client.create_authorization_server(associated_server)

            assert err is None, f"Failed to create associated server: {err}"
            assert created_associated is not None
            assert isinstance(created_associated, models.AuthorizationServer)

            associated_server_id = created_associated.id
            print(f"Created associated server: {associated_server_id}")

            # ===== CREATE ASSOCIATION =====
            print("\n=== Creating Association Between Servers ===")

            # Create the association payload
            association_payload = models.AssociatedServerMediated(
                trusted=[associated_server_id]
            )

            associated_servers, _, err = await client.create_associated_servers(
                primary_server_id,
                association_payload
            )

            assert err is None, f"Failed to create association: {err}"
            assert associated_servers is not None
            assert isinstance(associated_servers, list)
            assert len(associated_servers) > 0

            # Verify the associated server is in the response
            associated_ids = [server.id for server in associated_servers]
            assert associated_server_id in associated_ids, \
                f"Associated server {associated_server_id} not found in response"

            print(f"Successfully created association")
            print(f"  Primary server: {primary_server_id}")
            print(f"  Associated server: {associated_server_id}")

            # ===== LIST ASSOCIATED SERVERS =====
            print("\n=== Listing Associated Servers (Trusted) ===")

            listed_servers, _, err = await client.list_associated_servers_by_trusted_type(
                primary_server_id,
                trusted=True
            )

            assert err is None, f"Failed to list associated servers: {err}"
            assert listed_servers is not None
            assert isinstance(listed_servers, list)
            assert len(listed_servers) > 0

            # Verify the associated server is in the list
            listed_ids = [server.id for server in listed_servers]
            assert associated_server_id in listed_ids, \
                f"Associated server {associated_server_id} not found in list"

            print(f"Found {len(listed_servers)} associated server(s)")

            # ===== LIST ASSOCIATED SERVERS (with pagination) =====
            print("\n=== Testing List with Pagination Parameters ===")

            listed_with_limit, _, err = await client.list_associated_servers_by_trusted_type(
                primary_server_id,
                trusted=True,
                limit=10
            )

            assert err is None, f"Failed to list with limit: {err}"
            assert listed_with_limit is not None
            assert isinstance(listed_with_limit, list)
            print(f"List with limit returned {len(listed_with_limit)} server(s)")

            # ===== DELETE ASSOCIATION =====
            print("\n=== Deleting Association ===")

            result, resp, err = await client.delete_associated_server(
                primary_server_id,
                associated_server_id
            )

            assert err is None, f"Failed to delete association: {err}"
            # DELETE typically returns None/204 No Content
            assert result is None or resp.status == 204

            print(f"Successfully deleted association")

            # ===== VERIFY ASSOCIATION IS DELETED =====
            print("\n=== Verifying Association is Deleted ===")

            verify_list, _, err = await client.list_associated_servers_by_trusted_type(
                primary_server_id,
                trusted=True
            )

            # Should either be empty or not contain the associated server
            if verify_list:
                verify_ids = [server.id for server in verify_list]
                assert associated_server_id not in verify_ids, \
                    f"Associated server {associated_server_id} still in list after deletion"

            print(f"Verified association is deleted")

            print("\n=== Test completed successfully ===")

        except Exception as e:
            print(f"\n!!! Test failed with error: {e}")
            raise

        finally:
            # ===== CLEANUP: DELETE AUTHORIZATION SERVERS =====
            print("\n=== Cleanup: Deleting Authorization Servers ===")

            if associated_server_id:
                try:
                    print(f"Deleting associated server: {associated_server_id}")
                    _, _, err = await client.delete_authorization_server(associated_server_id)
                    if err:
                        print(f"Warning: Could not delete associated server: {err}")
                    else:
                        print(f"Deleted associated server successfully")
                except Exception as e:
                    print(f"Exception deleting associated server: {e}")

            if primary_server_id:
                try:
                    print(f"Deleting primary server: {primary_server_id}")
                    _, _, err = await client.delete_authorization_server(primary_server_id)
                    if err:
                        print(f"Warning: Could not delete primary server: {err}")
                    else:
                        print(f"Deleted primary server successfully")
                except Exception as e:
                    print(f"Exception deleting primary server: {e}")

            print("=== Cleanup completed ===")

