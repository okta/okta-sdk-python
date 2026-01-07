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


class TestApiServiceIntegrationsResource:
    """
    Integration Tests for the API Service Integrations Resource

    This test suite provides comprehensive integration testing for all API Service Integrations API operations
    within the Okta Python SDK. The tests validate real API interactions using VCR for recording
    and replaying HTTP requests/responses.

    API Methods Tested:
    1. create_api_service_integration_instance() - Create an API service integration instance
    2. get_api_service_integration_instance() - Get a specific instance
    3. list_api_service_integration_instances() - List all instances
    4. create_api_service_integration_instance_secret() - Create a secret for an instance
    5. list_api_service_integration_instance_secrets() - List secrets for an instance
    6. deactivate_api_service_integration_instance_secret() - Deactivate a secret
    7. activate_api_service_integration_instance_secret() - Activate a secret
    8. delete_api_service_integration_instance_secret() - Delete a secret
    9. delete_api_service_integration_instance() - Delete an instance
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_api_service_integration_lifecycle(self, fs):
        """
        Test the complete lifecycle of API Service Integration Instance and Secrets

        This test covers:
        - Creating an API service integration instance
        - Retrieving the instance
        - Listing instances
        - Creating a secret
        - Listing secrets
        - Deactivating a secret
        - Activating a secret
        - Deleting a secret
        - Deleting the instance
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        instance_id = None
        secret_id = None

        try:
            # ===== CREATE API Service Integration Instance =====
            # Create request object with required fields
            # Using 'cerbos' as an example API Service Integration type from the OIN catalog
            create_request = models.PostAPIServiceIntegrationInstanceRequest(
                type="cerbos",
                granted_scopes=[
                    "okta.apps.read",
                    "okta.users.read"
                ]
            )

            # Create the instance
            instance, _, err = await client.create_api_service_integration_instance(
                post_api_service_integration_instance_request=create_request
            )

            assert err is None, f"Failed to create API service integration instance: {err}"
            assert instance is not None
            assert isinstance(instance, models.PostAPIServiceIntegrationInstance)
            assert instance.id is not None
            assert instance.name is not None

            instance_id = instance.id

            # Verify granted scopes
            assert "okta.apps.read" in instance.granted_scopes
            assert "okta.users.read" in instance.granted_scopes

            # ===== GET API Service Integration Instance =====
            retrieved_instance, _, err = await client.get_api_service_integration_instance(
                instance_id
            )

            assert err is None, f"Failed to get API service integration instance: {err}"
            assert retrieved_instance is not None
            assert isinstance(retrieved_instance, models.APIServiceIntegrationInstance)
            assert retrieved_instance.id == instance_id
            assert retrieved_instance.name == instance.name

            # ===== LIST API Service Integration Instances =====
            instances_list, _, err = await client.list_api_service_integration_instances()

            assert err is None, f"Failed to list API service integration instances: {err}"
            assert isinstance(instances_list, list)
            assert len(instances_list) > 0

            # Verify our created instance is in the list
            found_in_list = any(inst.id == instance_id for inst in instances_list)
            assert found_in_list, f"Created instance {instance_id} not found in list"

            # ===== CREATE Secret =====
            secret, _, err = await client.create_api_service_integration_instance_secret(
                instance_id
            )

            assert err is None, f"Failed to create secret: {err}"
            assert secret is not None
            assert isinstance(secret, models.APIServiceIntegrationInstanceSecret)
            assert secret.id is not None
            assert secret.status == "ACTIVE"

            secret_id = secret.id

            # ===== LIST Secrets =====
            secrets_list, _, err = await client.list_api_service_integration_instance_secrets(
                instance_id
            )

            assert err is None, f"Failed to list secrets: {err}"
            assert isinstance(secrets_list, list)
            assert len(secrets_list) > 0

            # Verify our created secret is in the list
            found_secret = any(s.id == secret_id for s in secrets_list)
            assert found_secret, f"Created secret {secret_id} not found in list"

            # ===== DEACTIVATE Secret =====
            deactivated_secret, _, err = await client.deactivate_api_service_integration_instance_secret(
                instance_id, secret_id
            )

            assert err is None, f"Failed to deactivate secret: {err}"
            assert deactivated_secret is not None
            assert deactivated_secret.status == "INACTIVE"

            # ===== ACTIVATE Secret =====
            activated_secret, _, err = await client.activate_api_service_integration_instance_secret(
                instance_id, secret_id
            )

            assert err is None, f"Failed to activate secret: {err}"
            assert activated_secret is not None
            assert activated_secret.status == "ACTIVE"

            # ===== DEACTIVATE Secret Again (required before deletion) =====
            deactivated_secret2, _, err = await client.deactivate_api_service_integration_instance_secret(
                instance_id, secret_id
            )

            assert err is None, f"Failed to deactivate secret for deletion: {err}"
            assert deactivated_secret2.status == "INACTIVE"

            # ===== DELETE Secret =====
            delete_result, _, err = await client.delete_api_service_integration_instance_secret(
                instance_id, secret_id
            )

            assert err is None, f"Failed to delete secret: {err}"

            # Verify secret is deleted by listing again
            secrets_after_delete, _, err = await client.list_api_service_integration_instance_secrets(
                instance_id
            )
            assert err is None
            deleted_secret_found = any(s.id == secret_id for s in secrets_after_delete)
            assert not deleted_secret_found, f"Secret {secret_id} should be deleted but still exists"

            # ===== DELETE Instance =====
            delete_instance_result, _, err = await client.delete_api_service_integration_instance(
                instance_id
            )

            assert err is None, f"Failed to delete instance: {err}"

            # Verify instance is deleted - trying to get it should fail
            try:
                deleted_instance, _, get_err = await client.get_api_service_integration_instance(
                    instance_id
                )
                # If we get here, check if there's an error or the instance is None
                assert get_err is not None or deleted_instance is None, \
                    f"Instance {instance_id} should be deleted but still exists"
            except OktaAPIError as e:
                # Expected - instance not found
                assert e.status_code == 404, f"Expected 404 but got {e.status_code}"

            # Reset for cleanup
            instance_id = None
            secret_id = None

        finally:
            # Cleanup in case of test failure
            if secret_id and instance_id:
                try:
                    # Try to deactivate first
                    try:
                        await client.deactivate_api_service_integration_instance_secret(
                            instance_id, secret_id
                        )
                    except:
                        pass
                    # Then delete
                    await client.delete_api_service_integration_instance_secret(
                        instance_id, secret_id
                    )
                except:
                    pass

            if instance_id:
                try:
                    await client.delete_api_service_integration_instance(
                        instance_id
                    )
                except:
                    pass

