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


class TestRoleAPIResource:
    """
    Integration Tests for the Role API Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_delete_role(self, fs):
        """Test basic CRUD operations for IAM Role"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Role Object
        ROLE_LABEL = "Test-Custom-Role"
        ROLE_DESCRIPTION = "Test custom role for VCR testing"

        create_role_request = models.CreateIamRoleRequest(
            **{
                "label": ROLE_LABEL,
                "description": ROLE_DESCRIPTION,
                "permissions": [
                    models.RolePermissionType.OKTA_DOT_USERS_DOT_READ,
                    models.RolePermissionType.OKTA_DOT_GROUPS_DOT_READ,
                ],
            }
        )

        try:
            # Create Role
            role, _, err = await client.create_role(create_role_request)
            assert err is None
            assert isinstance(role, models.IamRole)
            assert role.label == ROLE_LABEL
            assert role.description == ROLE_DESCRIPTION
            assert role.id is not None

            # Get role using ID
            found_role, _, err = await client.get_role(role.id)
            assert err is None
            assert found_role.id == role.id
            assert found_role.label == ROLE_LABEL
            assert found_role.description == ROLE_DESCRIPTION

            # Get role using label
            found_role_by_label, _, err = await client.get_role(role.label)
            assert err is None
            assert found_role_by_label.id == role.id
            assert found_role_by_label.label == ROLE_LABEL

        finally:
            if "role" in locals() and role.id:
                _, _, err = await client.delete_role(role.id)
                assert err is None

                # Ensure role cannot be found again
                found_role, resp, err = await client.get_role(role.id)
                assert err is not None
                assert resp.status == HTTPStatus.NOT_FOUND
                assert found_role is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_roles(self, fs):
        """Test listing roles with pagination"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # List all roles
        roles, resp, err = await client.list_roles()
        assert err is None
        assert isinstance(roles, models.IamRoles)
        assert hasattr(roles, "roles")

        # Verify that we get some roles (there should be default system roles)
        if roles.roles:
            for role in roles.roles:
                assert isinstance(role, models.IamRole)
                assert role.id is not None
                assert role.label is not None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_role(self, fs):
        """Test updating a role"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Role Object
        ROLE_LABEL = "Test-Update-Role"
        ORIGINAL_DESCRIPTION = "Original description for update test"
        UPDATED_DESCRIPTION = "Updated description for update test"
        UPDATED_LABEL = "Test-Update-Role-Modified"

        create_role_request = models.CreateIamRoleRequest(
            **{
                "label": ROLE_LABEL,
                "description": ORIGINAL_DESCRIPTION,
                "permissions": [models.RolePermissionType.OKTA_DOT_USERS_DOT_READ],
            }
        )

        try:
            # Create Role
            role, _, err = await client.create_role(create_role_request)
            assert err is None
            assert role.description == ORIGINAL_DESCRIPTION

            # Update Role (both label and description are required)
            update_role_request = models.UpdateIamRoleRequest(
                **{"label": UPDATED_LABEL, "description": UPDATED_DESCRIPTION}
            )

            updated_role, _, err = await client.replace_role(
                role.id, update_role_request
            )
            assert err is None
            assert updated_role.id == role.id
            assert updated_role.label == UPDATED_LABEL
            assert updated_role.description == UPDATED_DESCRIPTION

            # Verify the update by getting the role again
            found_role, _, err = await client.get_role(role.id)
            assert err is None
            assert found_role.description == UPDATED_DESCRIPTION
            assert found_role.label == UPDATED_LABEL

        finally:
            # Cleanup: Delete created role
            if "role" in locals() and role.id:
                _, _, err = await client.delete_role(role.id)
                assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_role_permissions_operations(self, fs):
        """Test role permission CRUD operations"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Role Object
        ROLE_LABEL = "Test-Permission-Role"
        ROLE_DESCRIPTION = "Test role for permission operations"

        create_role_request = models.CreateIamRoleRequest(
            **{
                "label": ROLE_LABEL,
                "description": ROLE_DESCRIPTION,
                "permissions": [models.RolePermissionType.OKTA_DOT_USERS_DOT_READ],
            }
        )

        try:
            # Create Role
            role, _, err = await client.create_role(create_role_request)
            assert err is None

            # List role permissions
            permissions, _, err = await client.list_role_permissions(role.id)
            assert err is None
            assert isinstance(permissions, models.Permissions)
            initial_permission_count = (
                len(permissions.permissions) if permissions.permissions else 0
            )

            # Add a new permission without conditions (create_role_permission returns 3 values)
            new_permission_type = (
                models.RolePermissionType.OKTA_DOT_GROUPS_DOT_READ.value
            )
            create_permission_request = models.CreateUpdateIamRolePermissionRequest(
                **{"conditions": {}}
            )

            _, _, err = await client.create_role_permission(
                role.id, new_permission_type, create_permission_request
            )
            assert err is None

            # Verify permission was added
            permissions, _, err = await client.list_role_permissions(role.id)
            assert err is None
            new_permission_count = (
                len(permissions.permissions) if permissions.permissions else 0
            )
            assert new_permission_count == initial_permission_count + 1

            # Get specific permission
            permission, _, err = await client.get_role_permission(
                role.id, new_permission_type
            )
            assert err is None
            assert isinstance(permission, models.Permission)
            assert permission.label == new_permission_type

            # Delete the permission (delete_role_permission returns 3 values)
            _, _, err = await client.delete_role_permission(
                role.id, new_permission_type
            )
            assert err is None

            # Verify permission was deleted
            permissions, _, err = await client.list_role_permissions(role.id)
            assert err is None
            final_permission_count = (
                len(permissions.permissions) if permissions.permissions else 0
            )
            assert final_permission_count == initial_permission_count

        finally:
            # Cleanup: Delete created role
            if "role" in locals() and role.id:
                _, _, err = await client.delete_role(role.id)
                assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_role_with_multiple_permissions(self, fs):
        """Test creating a role with multiple permissions"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Role Object with multiple permissions
        ROLE_LABEL = "Test-Multi-Permission-Role"
        ROLE_DESCRIPTION = "Test role with multiple permissions"

        create_role_request = models.CreateIamRoleRequest(
            **{
                "label": ROLE_LABEL,
                "description": ROLE_DESCRIPTION,
                "permissions": [
                    models.RolePermissionType.OKTA_DOT_USERS_DOT_READ,
                    models.RolePermissionType.OKTA_DOT_GROUPS_DOT_READ,
                    models.RolePermissionType.OKTA_DOT_APPS_DOT_READ,
                ],
            }
        )

        try:
            # Create Role
            role, _, err = await client.create_role(create_role_request)
            assert err is None
            assert isinstance(role, models.IamRole)

            # List role permissions to verify all permissions were created
            permissions, _, err = await client.list_role_permissions(role.id)
            assert err is None
            assert isinstance(permissions, models.Permissions)

            if permissions.permissions:
                assert len(permissions.permissions) >= 3

                # Verify specific permissions exist
                permission_labels = [perm.label for perm in permissions.permissions]
                assert (
                        models.RolePermissionType.OKTA_DOT_USERS_DOT_READ.value
                        in permission_labels
                )
                assert (
                        models.RolePermissionType.OKTA_DOT_GROUPS_DOT_READ.value
                        in permission_labels
                )
                assert (
                        models.RolePermissionType.OKTA_DOT_APPS_DOT_READ.value
                        in permission_labels
                )

        finally:
            # Cleanup: Delete created role
            if "role" in locals() and role.id:
                _, _, err = await client.delete_role(role.id)
                assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_role_error_handling(self, fs):
        """Test error handling for role operations"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Test getting non-existent role
        non_existent_role_id = "non-existent-role-id"

        # Test deleting non-existent role (delete methods return only 2 values: response, error)
        resp, err = await client.delete_role(non_existent_role_id)

        assert err is not None
        assert resp.status == HTTPStatus.NOT_FOUND

        # Test creating role with duplicate label
        ROLE_LABEL = "Test-Duplicate-Role"
        ROLE_DESCRIPTION = "Test role for duplicate testing"

        create_role_request = models.CreateIamRoleRequest(
            **{
                "label": ROLE_LABEL,
                "description": ROLE_DESCRIPTION,
                "permissions": [models.RolePermissionType.OKTA_DOT_USERS_DOT_READ],
            }
        )

        try:
            # Create first role
            role1, _, err = await client.create_role(create_role_request)
            assert err is None

            # Try to create second role with same label (should fail)
            role2, resp, err = await client.create_role(create_role_request)
            assert err is not None
            assert resp.status == HTTPStatus.BAD_REQUEST
            assert role2 is None

        finally:
            # Cleanup: Delete created role (delete methods return only 2 values: response, error)
            if "role1" in locals() and role1.id:
                _, _, err = await client.delete_role(role1.id)
                assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_role_permission_with_conditions(self, fs):
        """Test creating role permissions with specific conditions"""
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Role Object
        ROLE_LABEL = "Test-Conditional-Permission-Role"
        ROLE_DESCRIPTION = "Test role for conditional permission operations"

        create_role_request = models.CreateIamRoleRequest(
            **{
                "label": ROLE_LABEL,
                "description": ROLE_DESCRIPTION,
                "permissions": [models.RolePermissionType.OKTA_DOT_USERS_DOT_READ],
            }
        )

        try:
            # Create Role
            role, _, err = await client.create_role(create_role_request)
            assert err is None

            # Add a permission with empty conditions (create_role_permission returns 3 values)
            permission_type = models.RolePermissionType.OKTA_DOT_APPS_DOT_READ.value
            create_permission_request = models.CreateUpdateIamRolePermissionRequest(
                **{"conditions": {}}
            )

            _, _, err = await client.create_role_permission(
                role.id, permission_type, create_permission_request
            )
            assert err is None

            # Get the permission and verify it was created
            permission, _, err = await client.get_role_permission(
                role.id, permission_type
            )
            assert err is None
            assert isinstance(permission, models.Permission)
            assert permission.label == permission_type
            # Verify conditions field exists (even if empty)
            assert hasattr(permission, "conditions")

        finally:
            # Cleanup: Delete created role
            if "role" in locals() and role.id:
                _, _, err = await client.delete_role(role.id)
                assert err is None
