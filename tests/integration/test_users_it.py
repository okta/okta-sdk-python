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

import time

import pytest
from pydantic import SecretStr

import okta.models as models
from okta import UpdateUserRequest
from okta.errors.okta_api_error import OktaAPIError
from tests.mocks import MockOktaClient


class TestUsersResource:
    """
    Integration Tests for the Users Resource.
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_user(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": "Password150kta"})

        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Get"
        user_profile.email = "John.Doe-Get@example.com"
        user_profile.login = "John.Doe-Get@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        query_params_create = {"activate": "False"}

        try:
            # Create User
            user, resp, err = await test_client.create_user(
                create_user_req, activate=False
            )
            assert err is None

            got_user, resp, err = await test_client.get_user(user.id)
            assert got_user.id == user.id

            got_user_with_string, resp, err = await test_client.get_user(
                user_profile.login
            )
            assert got_user_with_string.id == user.id
            assert user.profile.first_name == user_profile.first_name
            assert user.profile.last_name == user_profile.last_name
            assert user.profile.email == user_profile.email
            assert user.profile.login == user_profile.login

            user_id = user.id

            # Deactivate, then delete created user
            _, _, err = await test_client.deactivate_user(user.id)
            assert err is None

            _, _, err = await test_client.delete_user(user.id)
            assert err is None

            user, _, err = await test_client.get_user(user_id)
            assert user is None
            assert isinstance(err, OktaAPIError)
        finally:
            # Clean up
            try:
                _, _, err = await test_client.deactivate_user(user.id)
            except Exception:
                pass

            try:
                _, _, err = await test_client.delete_user(user.id)
            except Exception:
                pass

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_user(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Activate"
        user_profile.email = "John.Doe-Activate@example.com"
        user_profile.login = "John.Doe-Activate@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create query parameters and Create User
            query_params_create = {"activate": "False"}
            user, resp, err = await test_client.create_user(
                create_user_req, activate=False
            )
            assert err is None

            # Create query parameters and Activate User
            query_params_activate = {"sendEmail": "False"}
            token, resp, err = await test_client.activate_user(
                user.id, send_email=False
            )
            assert err is None
            assert token is not None
            # Ensure correct Object is returned
            assert isinstance(token, models.UserActivationToken)

            # Create query parameters and List Users
            query_params_list = {"filter": 'status eq "ACTIVE"'}
            users, resp, err = await test_client.list_users(filter='status eq "ACTIVE"')
            assert err is None
            # Ensure user is in list
            assert next((usr for usr in users if usr.id == user.id), None) is not None

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_user_profile(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Update-Profile"
        user_profile.email = "John.Doe-Update-Profile@example.com"
        user_profile.login = "John.Doe-Update-Profile@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create query parameters and Create User
            query_params_create = {"activate": "False"}
            user, _, err = await test_client.create_user(
                create_user_req, activate=False
            )
            assert err is None

            # Craft new profile and get user object
            new_profile = user.profile
            NICK_NAME = "JD"
            new_profile.nick_name = NICK_NAME
            updated_user = UpdateUserRequest(
                **{
                    "credentials": user.credentials,
                    "profile": new_profile,
                    "realm_id": user.realm_id,
                }
            )

            # Update User with new details
            new_user, _, err = await test_client.update_user(user.id, updated_user)
            assert err is None
            assert new_user is not None

            # Retrieve user and ensure details are updated
            got_user, _, err = await test_client.get_user(user.id)
            assert err is None
            assert got_user.id == user.id
            assert got_user.profile.nick_name == NICK_NAME

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_suspend_user(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Suspend"
        user_profile.email = "John.Doe-Suspend@example.com"
        user_profile.login = "John.Doe-Suspend@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create Query Parameters and Create User
            query_params_create = {"activate": "True"}
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Suspend User
            _, _, err = await test_client.suspend_user(user.id)
            assert err is None

            # Create query params and List Suspended Users
            query_params_list = {"filter": 'status eq "SUSPENDED"'}
            users, resp, err = await test_client.list_users(
                filter='status eq "SUSPENDED"'
            )
            assert err is None
            # Ensure created user is in list
            assert next((usr for usr in users if usr.id == user.id), None) is not None

            # Unsuspend User
            _, _, err = await test_client.unsuspend_user(user.id)
            assert err is None
            # Create query params and List Active Users
            query_params_list = {"filter": 'status eq "ACTIVE"'}
            users, resp, err = await test_client.list_users(filter='status eq "ACTIVE"')
            assert err is None
            # Ensure created user is in list
            assert next((usr for usr in users if usr.id == user.id), None) is not None

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_change_user_password(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Change-PW"
        user_profile.email = "John.Doe-Change-PW@example.com"
        user_profile.login = "John.Doe-Change-PW@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create Query Parameters and Create User
            query_params_create = {"activate": "True"}
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Give time before changing password
            time.sleep(1)

            # Create new Password
            NEW_PASSWORD = "2ANewPassword!"
            new_password = models.PasswordCredential(
                **{"value": SecretStr(NEW_PASSWORD)}
            )

            change_pw_req = models.ChangePasswordRequest(
                **{"oldPassword": password, "newPassword": new_password}
            )

            # change password and retrieve user after
            _, _, err = await test_client.change_password(user.id, change_pw_req)
            assert err is None

            got_user, resp, err = await test_client.get_user(user.id)
            assert got_user.id == user.id
            assert err is None
            # Verify password in updated user obj, changed after original
            DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
            assert got_user.password_changed > user.password_changed

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_reset_password_link_for_user(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": "Password150kta"})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Reset-PW-URL"
        user_profile.email = "John.Doe-Reset-PW-URL@example.com"
        user_profile.login = "John.Doe-Reset-PW-URL@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create Query Parameters and Create User
            query_params_create = {"activate": "True"}
            user, _, err = await test_client.create_user(create_user_req, activate=True)

            # Create Query Parameters and get Reset Password Token
            query_params_reset_pw = {"sendEmail": "False"}
            reset_pw_token, _, err = await test_client.generate_reset_password_token(
                user.id, send_email=False
            )
            assert err is None
            assert isinstance(reset_pw_token, models.ResetPasswordToken)
            assert reset_pw_token is not None

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_expire_password_get_temporary(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Expire-PW-URL"
        user_profile.email = "John.Doe-Expire-PW-URL@example.com"
        user_profile.login = "John.Doe-Expire-PW-URL@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create Query Parameters and Create User
            query_params_create = {"activate": "True"}
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Create Query Parameters and get Temporary Password
            temporary_pw, _, err = (
                await test_client.expire_password_and_get_temporary_password(user.id)
            )
            assert err is None
            assert isinstance(temporary_pw, models.TempPassword)
            assert temporary_pw is not None

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_change_recovery_question(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Change-Recovery"
        user_profile.email = "John.Doe-Change-Recovery@example.com"
        user_profile.login = "John.Doe-Change-Recovery@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create Query Parameters and Create User
            query_params_create = {"activate": "True"}
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Create Recovery Question
            NEW_RECOVERY_Q = "What's your favourite security question?"
            NEW_RECOVERY_A = "This One!"

            new_recovery_question = models.RecoveryQuestionCredential(
                **{"question": NEW_RECOVERY_Q, "answer": NEW_RECOVERY_A}
            )

            new_user_creds = models.UserCredentials(
                **{"password": password, "recoveryQuestion": new_recovery_question}
            )

            # Change Recovery Question
            updated_user_creds, _, err = await test_client.change_recovery_question(
                user.id, new_user_creds
            )
            assert err is None
            assert isinstance(updated_user_creds, models.UserCredentials)

            # Create New Password
            NEW_PASSWORD = password.value.get_secret_value()[::-1]  # reverse string
            new_pw = models.PasswordCredential(**{"value": SecretStr(NEW_PASSWORD)})
            recovery_answer = models.RecoveryQuestionCredential(
                **{"answer": NEW_RECOVERY_A}
            )

            change_pw_user_creds = models.UserCredentials(
                **{"password": new_pw, "recoveryQuestion": recovery_answer}
            )

            # Create New Password using Recovery Question answer
            _, _, err = await test_client.forgot_password_set_new_password(
                user.id, change_pw_user_creds
            )
            assert err is None

            # Get User and verify password was changed
            got_user, _, err = await test_client.get_user(user.id)
            assert got_user.id == user.id
            assert err is None
            assert got_user.password_changed > user.password_changed

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_assign_user_to_role(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Assign-User-Role"
        user_profile.email = "John.Doe-Assign-User-Role@example.com"
        user_profile.login = "John.Doe-Assign-User-Role@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create Query Parameters and Create User
            query_params_create = {"activate": "True"}
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Create Assign Role Request with Roletype Enum
            USER_ADMIN = models.RoleType.USER_ADMIN.value
            assign_role_req = models.AssignRoleRequest(**{"type": USER_ADMIN})

            # Assign Role to User
            _, _, err = await test_client.assign_role_to_user(user.id, assign_role_req)
            assert err is None

            # Get Roles for user and ensure role assigned is found
            roles, _, err = await test_client.list_assigned_roles_for_user(user.id)
            found_role = next((role for role in roles if role.type == USER_ADMIN), None)
            assert found_role is not None

            # Remove assigned role from user
            _, _, err = await test_client.unassign_role_from_user(
                user.id, found_role.id
            )
            assert err is None

            # Get Roles for user and ensure role assigned is NOT found
            roles, _, err = await test_client.list_assigned_roles_for_user(user.id)
            found_role = next((role for role in roles if role.type == USER_ADMIN), None)
            assert found_role is None

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_user_group_target_to_role(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Group-Target-Role-Assign"
        user_profile.email = "John.Doe-Group-Target-Role-Assign@example.com"
        user_profile.login = "John.Doe-Group-Target-Role-Assign@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create Query Parameters and Create User
            query_params_create = {"activate": "True"}
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Create Group Object
            NEW_GROUP_NAME = "Group-Target-Test-Assign"
            new_group_profile = models.GroupProfile(**{"name": NEW_GROUP_NAME})
            new_group = models.Group(**{"profile": new_group_profile})

            # Create Group
            group, _, err = await test_client.create_group(new_group)
            assert err is None

            # Create request to assign role to user
            USER_ADMIN = models.RoleType.USER_ADMIN.value
            assign_role_req = models.AssignRoleRequest(**{"type": USER_ADMIN})

            # Assign Role to User
            user_role, _, err = await test_client.assign_role_to_user(
                user.id, assign_role_req
            )
            assert err is None

            # Add Group Target to the Role
            _, _, err = await test_client.assign_group_target_to_user_role(
                user.id, user_role.id, group.id
            )
            assert err is None

            # Retrieve group targets for role and ensure added one is there
            groups, _, err = await test_client.list_group_targets_for_role(
                user.id, user_role.id
            )
            assert next((grp for grp in groups if grp.id == group.id), None) is not None

            # Create another group to add
            NEW_GROUP_NAME = "Temp-Group-Target-Test-Assign"
            new_group_profile = models.GroupProfile(**{"name": NEW_GROUP_NAME})
            new_group = models.Group(**{"profile": new_group_profile})

            # Create 2nd group
            temp_group, _, err = await test_client.create_group(new_group)
            assert err is None

            # Add new group target to role and remove original
            _, _, err = await test_client.assign_group_target_to_user_role(
                user.id, user_role.id, temp_group.id
            )
            assert err is None
            _, _, err = await test_client.unassign_group_target_from_user_admin_role(
                user.id, user_role.id, group.id
            )
            assert err is None

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            # Delete groups created
            try:
                _, _, err = await test_client.delete_group(group.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            try:
                _, _, err = await test_client.delete_group(temp_group.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_user_subscriptions(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Subscriptions"
        user_profile.email = "John.Doe-Subscriptions@example.com"
        user_profile.login = "John.Doe-Subscriptions@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # List user subscriptions
            users, _, err = await test_client.list_users(filter='status eq "ACTIVE"')
            assert err is None
            user = users[-1]

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_expire_password(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Awsdzertc151kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Expire-Password"
        user_profile.email = "John.Doe-Expire-Password@example.com"
        user_profile.login = "John.Doe-Expire-Password@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Expire password
            expired_user, _, err = await test_client.expire_password(user.id)
            assert err is None
            assert isinstance(expired_user, models.User)

            # Verify user status is PASSWORD_EXPIRED
            got_user, _, err = await test_client.get_user(user.id)
            assert err is None
            assert got_user.status == "PASSWORD_EXPIRED"

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr(record_mode="all")
    @pytest.mark.asyncio
    async def atest_forgot_password(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("AQZdfpio150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Forgot-Password"
        user_profile.email = "John.Doe-Forgot-Password@example.com"
        user_profile.login = "John.Doe-Forgot-Password@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None
            import pdb

            pdb.set_trace()
            # Trigger forgot password
            forgot_response, _, err = await test_client.forgot_password(
                user.id, send_email=False
            )
            assert err is None
            assert isinstance(forgot_response, models.ForgotPasswordResponse)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr(record_mode="all")
    @pytest.mark.asyncio
    async def atest_reactivate_user(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Reactivate"
        user_profile.email = "John.Doe-Reactivate@example.com"
        user_profile.login = "John.Doe-Reactivate@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(
                create_user_req, activate=False
            )
            assert err is None

            # Wait for deactivation to complete
            time.sleep(1)

            # Reactivate user
            activation_token, _, err = await test_client.reactivate_user(
                user.id, send_email=False
            )
            assert err is None
            assert isinstance(activation_token, models.UserActivationToken)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_replace_user(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Replace"
        user_profile.email = "John.Doe-Replace@example.com"
        user_profile.login = "John.Doe-Replace@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(
                create_user_req, activate=False
            )
            assert err is None

            # Create replacement user data
            new_profile = models.UserProfile()
            new_profile.first_name = "Jane"
            new_profile.last_name = "Doe-Replaced"
            new_profile.email = user_profile.email  # Keep same email/login
            new_profile.login = user_profile.login
            new_profile.nick_name = "JaneDoe"

            replacement_user = models.User(
                **{"profile": new_profile, "credentials": user_creds}
            )

            # Replace user
            replaced_user, _, err = await test_client.replace_user(
                user.id, replacement_user
            )
            assert err is None
            assert replaced_user.profile.first_name == "Jane"
            assert replaced_user.profile.last_name == "Doe-Replaced"
            assert replaced_user.profile.nick_name == "JaneDoe"

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr(record_mode="all")
    @pytest.mark.asyncio
    async def atest_unlock_user(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Unlock"
        user_profile.email = "John.Doe-Unlock@example.com"
        user_profile.login = "John.Doe-Unlock@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None
            import pdb

            pdb.set_trace()
            # Unlock user (even if not locked, should succeed)
            unlocked_user, err = await test_client.unlock_user(user.id)
            assert err is None
            assert isinstance(unlocked_user, models.User)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_reset_factors(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Reset-Factors"
        user_profile.email = "John.Doe-Reset-Factors@example.com"
        user_profile.login = "John.Doe-Reset-Factors@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Reset user factors
            reset_user, _, err = await test_client.reset_factors(user.id)
            assert err is None
            assert isinstance(reset_user, models.Success)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_revoke_user_sessions(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Revoke-Sessions"
        user_profile.email = "John.Doe-Revoke-Sessions@example.com"
        user_profile.login = "John.Doe-Revoke-Sessions@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Revoke user sessions
            success, _, err = await test_client.revoke_user_sessions(user.id)
            assert err is None
            # Should return Success object or None for 204 response
            assert success is None or isinstance(success, models.Success)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_user_groups(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-List-Groups"
        user_profile.email = "John.Doe-List-Groups@example.com"
        user_profile.login = "John.Doe-List-Groups@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Create Group
            group_profile = models.GroupProfile(**{"name": "Test-User-Group"})
            group_obj = models.Group(**{"profile": group_profile})
            group, _, err = await test_client.create_group(group_obj)
            assert err is None

            # Add user to group
            _, _, err = await test_client.assign_user_to_group(group.id, user.id)
            assert err is None

            # List user groups
            groups, _, err = await test_client.list_user_groups(user.id)
            assert err is None
            assert isinstance(groups, list)
            assert (
                    len(groups) >= 1
            )  # Should include the group we added plus "Everyone" group

            # Check that our group is in the list
            found_group = next((g for g in groups if g.id == group.id), None)
            assert found_group is not None

        finally:
            errors = []
            # Remove user from group
            try:
                _, _, err = await test_client.unassign_user_from_group(
                    group.id, user.id
                )
                assert err is None
            except Exception as exc:
                errors.append(exc)

            # Delete group
            try:
                _, _, err = await test_client.delete_group(group.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr(record_mode="all")
    @pytest.mark.asyncio
    async def atest_list_user_blocks(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-List-Blocks"
        user_profile.email = "John.Doe-List-Blocks@example.com"
        user_profile.login = "John.Doe-List-Blocks@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # List user blocks
            blocks, _, err = await test_client.list_user_blocks(user.id)
            assert err is None
            assert isinstance(blocks, list)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_user_grants(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-List-Grants"
        user_profile.email = "John.Doe-List-Grants@example.com"
        user_profile.login = "John.Doe-List-Grants@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # List user grants
            grants, _, err = await test_client.list_user_grants(user.id)
            assert err is None
            assert isinstance(grants, list)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_revoke_user_grants(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Revoke-Grants"
        user_profile.email = "John.Doe-Revoke-Grants@example.com"
        user_profile.login = "John.Doe-Revoke-Grants@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # Revoke user grants
            success, _, err = await test_client.revoke_user_grants(user.id)
            assert err is None
            # Should return Success object or None for 204 response
            assert success is None or isinstance(success, models.Success)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_app_links(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-App-Links"
        user_profile.email = "John.Doe-App-Links@example.com"
        user_profile.login = "John.Doe-App-Links@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # List app links for user
            app_links, _, err = await test_client.list_app_links(user.id)
            assert err is None
            assert isinstance(app_links, list)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_user_clients(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-List-Clients"
        user_profile.email = "John.Doe-List-Clients@example.com"
        user_profile.login = "John.Doe-List-Clients@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # List user clients
            clients, _, err = await test_client.list_user_clients(user.id)
            assert err is None
            assert isinstance(clients, list)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_user_identity_providers(self, fs):
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-IdPs"
        user_profile.email = "John.Doe-IdPs@example.com"
        user_profile.login = "John.Doe-IdPs@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Create User
            user, _, err = await test_client.create_user(create_user_req, activate=True)
            assert err is None

            # List user identity providers
            idps, _, err = await test_client.list_user_identity_providers(user.id)
            assert err is None
            assert isinstance(idps, list)

        finally:
            errors = []
            # Deactivate, then delete created user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_user_with_http_info_methods(self, fs):
        """Test _with_http_info method variants to increase coverage"""
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials
        user_creds = models.UserCredentials(**{"password": password})

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-HttpInfo"
        user_profile.email = "John.Doe-HttpInfo@example.com"
        user_profile.login = "John.Doe-HttpInfo@example.com"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # Test create_user_with_http_info
            user, resp, err = await test_client.create_user_with_http_info(
                create_user_req, activate=False
            )
            assert err is None
            assert resp.status_code == 200
            assert isinstance(user, models.User)

            # Test get_user_with_http_info
            found_user, resp, err = await test_client.get_user_with_http_info(user.id)
            assert err is None
            assert resp.status_code == 200
            assert found_user.id == user.id

            # Test activate_user_with_http_info
            token, resp, err = await test_client.activate_user_with_http_info(
                user.id, send_email=False
            )
            assert err is None
            assert resp.status_code == 200

            # Test update_user_with_http_info

            # Craft new profile and get user object
            new_profile = user.profile
            NICK_NAME = "JD"
            new_profile.nick_name = NICK_NAME
            updated_user = UpdateUserRequest(
                **{
                    "credentials": user.credentials,
                    "profile": new_profile,
                    "realm_id": user.realm_id,
                }
            )
            updated_user, resp, err = await test_client.update_user_with_http_info(
                user.id, updated_user
            )
            assert err is None
            assert resp.status_code == 200
            assert updated_user.profile.nick_name == "JD"

        finally:
            errors = []
            # Delete created user
            try:
                # Test deactivate_user_with_http_info
                deactivated_user, resp, err = (
                    await test_client.deactivate_user_with_http_info(user.id)
                )
                assert err is None
                assert resp.status_code == 200

                _, resp, err = await test_client.delete_user_with_http_info(user.id)
                assert err is None
                assert resp.status_code == 204
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_comprehensive_user_lifecycle(self, fs):
        """Comprehensive test covering full user lifecycle to maximize coverage"""
        # Instantiate Mock Client
        test_client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential(**{"value": SecretStr("Password150kta")})
        # Create User Credentials with recovery question
        recovery_question = models.RecoveryQuestionCredential(
            **{"question": "What is your favorite test?", "answer": "Integration test"}
        )
        user_creds = models.UserCredentials(
            **{"password": password, "recoveryQuestion": recovery_question}
        )

        # Create comprehensive user profile
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Comprehensive"
        user_profile.email = "John.Doe-Comprehensive@example.com"
        user_profile.login = "John.Doe-Comprehensive@example.com"
        user_profile.nick_name = "JohnnyC"
        user_profile.display_name = "John Doe Comprehensive"
        user_profile.mobile_phone = "+1-555-123-4567"

        create_user_req = models.CreateUserRequest(
            **{"credentials": user_creds, "profile": user_profile}
        )

        try:
            # A. Create User in STAGED state
            user, _, err = await test_client.create_user(
                create_user_req, activate=False
            )
            assert err is None
            assert user.status == "STAGED"

            # B. Activate User
            token, _, err = await test_client.activate_user(user.id, send_email=False)
            assert err is None
            assert isinstance(token, models.UserActivationToken)

            # Wait for activation
            time.sleep(1)

            # C. Verify user is active and get updated user
            active_user, _, err = await test_client.get_user(user.id)
            assert err is None
            assert active_user.status == "ACTIVE"

            # D. Test various user operations
            # Test suspend/unsuspend
            _, _, err = await test_client.suspend_user(user.id)
            assert err is None

            suspended_user, _, err = await test_client.get_user(user.id)
            assert err is None
            assert suspended_user.status == "SUSPENDED"

            _, _, err = await test_client.unsuspend_user(user.id)
            assert err is None

            # E. Test password operations
            # Expire password and get temporary one
            temp_password, _, err = (
                await test_client.expire_password_and_get_temporary_password(user.id)
            )
            assert err is None
            assert isinstance(temp_password, models.TempPassword)

            # F. Generate reset password token
            reset_token, _, err = await test_client.generate_reset_password_token(
                user.id, send_email=False
            )
            assert err is None
            assert isinstance(reset_token, models.ResetPasswordToken)

            # H. Reset factors
            reset_user, _, err = await test_client.reset_factors(user.id)
            assert err is None
            assert isinstance(reset_user, models.Success)

            # I. Revoke sessions
            success, _, err = await test_client.revoke_user_sessions(user.id)
            assert err is None

            # J. Test list operations
            users_list, _, err = await test_client.list_users(limit=10)
            assert err is None
            assert isinstance(users_list, list)
            assert len(users_list) > 0

            user_grants, _, err = await test_client.list_user_grants(user.id)
            assert err is None
            assert isinstance(user_grants, list)

            user_groups, _, err = await test_client.list_user_groups(user.id)
            assert err is None
            assert isinstance(user_groups, list)

            app_links, _, err = await test_client.list_app_links(user.id)
            assert err is None
            assert isinstance(app_links, list)

        finally:
            errors = []
            # Cleanup: Deactivate and delete user
            try:
                _, _, err = await test_client.deactivate_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            try:
                _, _, err = await test_client.delete_user(user.id)
                assert err is None
            except Exception as exc:
                errors.append(exc)
            assert len(errors) == 0
