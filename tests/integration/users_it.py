import pytest
import okta.models as models
import time
from datetime import datetime
from tests.mocks import MockOktaClient as Client
from okta.errors.okta_api_error import OktaAPIError


class TestUsersResource:
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_user(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Get"
        user_profile.email = "John.Doe-Get@example.com"
        user_profile.login = "John.Doe-Get@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params = {"activate": "False"}

        user, resp, err = await test_client.create_user(
            create_user_req, query_params)
        assert err is None

        got_user, resp, err = await test_client.get_user(user.id)
        assert got_user.id == user.id

        got_user_with_string, resp, err = await test_client.get_user(
            user_profile.login)
        assert got_user_with_string.id == user.id

        assert user.profile.first_name == user_profile.first_name
        assert user.profile.last_name == user_profile.last_name
        assert user.profile.email == user_profile.email
        assert user.profile.login == user_profile.login

        user_id = user.id

        _, err = await test_client.deactivate_or_delete_user(user_id)
        assert err is None

        _, err = await test_client.deactivate_or_delete_user(user_id)
        assert err is None

        user, _, err = await test_client.get_user(user_id)
        assert user is None
        assert isinstance(err, OktaAPIError)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_user(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Activate"
        user_profile.email = "John.Doe-Activate@example.com"
        user_profile.login = "John.Doe-Activate@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "False"}
        user, resp, err = await test_client.create_user(
            create_user_req, query_params_create)
        assert err is None

        query_params_activate = {"sendEmail": "False"}
        token, resp, err = await test_client.activate_user(
            user.id, query_params_activate)

        assert err is None
        assert token is not None
        assert isinstance(token, models.UserActivationToken)

        query_params_list = {"filter": "status eq \"ACTIVE\""}
        users, resp, err = await test_client.list_users(query_params_list)
        assert err is None
        assert next((usr for usr in users if usr.id ==
                     user.id), None) is not None

        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_user_profile(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Update-Profile"
        user_profile.email = "John.Doe-Update-Profile@example.com"
        user_profile.login = "John.Doe-Update-Profile@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "False"}
        user, _, err = await test_client.create_user(
            create_user_req, query_params_create)
        assert err is None

        new_profile = user.profile
        NICK_NAME = "JD"
        new_profile.nick_name = NICK_NAME
        updated_user = models.User({"profile": new_profile})

        new_user, _, err = await test_client.update_user(user.id, updated_user)
        assert err is None
        assert new_user is not None

        got_user, _, err = await test_client.get_user(user.id)
        assert err is None
        assert got_user.id == user.id
        assert got_user.profile.nick_name == NICK_NAME

        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_suspend_user(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Suspend"
        user_profile.email = "John.Doe-Suspend@example.com"
        user_profile.login = "John.Doe-Suspend@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "True"}
        user, _, err = await test_client.create_user(
            create_user_req, query_params_create)
        assert err is None

        _, err = await test_client.suspend_user(user.id)
        assert err is None

        query_params_list = {"filter": "status eq \"SUSPENDED\""}
        users, resp, err = await test_client.list_users(query_params_list)
        assert err is None
        assert next((usr for usr in users if usr.id ==
                     user.id), None) is not None

        _, err = await test_client.unsuspend_user(user.id)
        assert err is None

        query_params_list = {"filter": "status eq \"ACTIVE\""}
        users, resp, err = await test_client.list_users(query_params_list)
        assert err is None
        assert next((usr for usr in users if usr.id ==
                     user.id), None) is not None

        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_change_user_password(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Change-PW"
        user_profile.email = "John.Doe-Change-PW@example.com"
        user_profile.login = "John.Doe-Change-PW@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "True"}
        user, _, err = await test_client.create_user(
            create_user_req, query_params_create)
        assert err is None

        time.sleep(1)

        NEW_PASSWORD = "2ANewPassword!"
        new_password = models.PasswordCredential({
            "value": NEW_PASSWORD
        })

        change_pw_req = models.ChangePasswordRequest({
            "oldPassword": password,
            "newPassword": new_password
        })

        _, _, err = await test_client.change_password(user.id, change_pw_req)
        assert err is None

        got_user, resp, err = await test_client.get_user(user.id)
        assert got_user.id == user.id
        assert err is None
        DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
        assert datetime.strptime(got_user.password_changed, DATETIME_FORMAT)\
            > datetime.strptime(user.password_changed, DATETIME_FORMAT)

        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_reset_password_link_for_user(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Reset-PW-URL"
        user_profile.email = "John.Doe-Reset-PW-URL@example.com"
        user_profile.login = "John.Doe-Reset-PW-URL@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "True"}
        user, _, err = await test_client.create_user(
            create_user_req, query_params_create)

        query_params_reset_pw = {"sendEmail": "False"}
        reset_pw_token, _, err = await test_client.reset_password(
            user.id, query_params_reset_pw)
        assert err is None
        assert isinstance(reset_pw_token, models.ResetPasswordToken)
        assert reset_pw_token is not None

        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_expire_password_get_temporary(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Expire-PW-URL"
        user_profile.email = "John.Doe-Expire-PW-URL@example.com"
        user_profile.login = "John.Doe-Expire-PW-URL@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "True"}
        user, _, err = await test_client.create_user(
            create_user_req, query_params_create)
        assert err is None

        temporary_pw, _, err = await\
            test_client.expire_password_and_get_temporary_password(user.id)
        assert err is None
        assert isinstance(temporary_pw, models.TempPassword)
        assert temporary_pw is not None

        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_change_recovery_question(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Change-Recovery"
        user_profile.email = "John.Doe-Change-Recovery@example.com"
        user_profile.login = "John.Doe-Change-Recovery@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "True"}
        user, _, err = await test_client.create_user(
            create_user_req, query_params_create)
        assert err is None

        NEW_RECOVERY_Q = "What's your favourite security question?"
        NEW_RECOVERY_A = "This One!"

        new_recovery_question = models.RecoveryQuestionCredential({
            "question": NEW_RECOVERY_Q,
            "answer": NEW_RECOVERY_A
        })

        new_user_creds = models.UserCredentials({
            "password": password,
            "recoveryQuestion": new_recovery_question
        })

        updated_user_creds, _, err = await\
            test_client.change_recovery_question(user.id, new_user_creds)
        assert err is None
        assert isinstance(updated_user_creds, models.UserCredentials)

        NEW_PASSWORD = password.value[::-1]  # reverse string
        new_pw = models.PasswordCredential({
            "value": NEW_PASSWORD
        })
        recovery_answer = models.RecoveryQuestionCredential({
            "answer": NEW_RECOVERY_A
        })

        change_pw_user_creds = models.UserCredentials({
            "password": new_pw,
            "recoveryQuestion": recovery_answer
        })

        _, _, err = await test_client.forgot_password_set_new_password(
            user.id, change_pw_user_creds)
        assert err is None

        got_user, _, err = await test_client.get_user(user.id)
        assert got_user.id == user.id
        assert err is None
        DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
        assert datetime.strptime(got_user.password_changed, DATETIME_FORMAT)\
            > datetime.strptime(user.password_changed, DATETIME_FORMAT)

        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_assign_user_to_role(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Assign-User-Role"
        user_profile.email = "John.Doe-Assign-User-Role@example.com"
        user_profile.login = "John.Doe-Assign-User-Role@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "True"}
        user, _, err = await test_client.create_user(
            create_user_req, query_params_create)
        assert err is None

        USER_ADMIN = models.RoleType.USER_ADMIN
        assign_role_req = models.AssignRoleRequest({
            "type": USER_ADMIN
        })

        _, _, err = await test_client.assign_role_to_user(user.id,
                                                          assign_role_req)
        assert err is None

        roles, _, err = await test_client.list_assigned_roles_for_user(user.id)
        found_role = next((role for role in roles if role.type ==
                           USER_ADMIN), None)
        assert found_role is not None

        _, err = await test_client.remove_role_from_user(user.id,
                                                         found_role.id)
        assert err is None

        roles, _, err = await test_client.list_assigned_roles_for_user(
            user.id)
        found_role = next((role for role in roles if role.type ==
                           USER_ADMIN), None)
        assert found_role is None

        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_user_group_target_to_role(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Group-Target-Role"
        user_profile.email = "John.Doe-Group-Target-Role@example.com"
        user_profile.login = "John.Doe-Group-Target-Role@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        query_params_create = {"activate": "True"}
        user, _, err = await test_client.create_user(
            create_user_req, query_params_create)
        assert err is None

        NEW_GROUP_NAME = "Group-Target-Test"
        new_group_profile = models.GroupProfile({
            "name": NEW_GROUP_NAME
        })
        new_group = models.Group({
            "profile": new_group_profile
        })

        group, _, err = await test_client.create_group(new_group)
        assert err is None

        USER_ADMIN = models.RoleType.USER_ADMIN
        assign_role_req = models.AssignRoleRequest({
            "type": USER_ADMIN
        })

        user_role, _, err = await test_client.assign_role_to_user(
            user.id, assign_role_req)
        assert err is None

        _, err = await test_client.add_group_target_to_role(
            user.id, user_role.id, group.id)
        assert err is None

        groups, _, err = await test_client.list_group_targets_for_role(
            user.id, user_role.id)
        assert next((grp for grp in groups if grp.id ==
                     group.id), None) is not None

        NEW_GROUP_NAME = "Temp-Group-Target-Test"
        new_group_profile = models.GroupProfile({
            "name": NEW_GROUP_NAME
        })
        new_group = models.Group({
            "profile": new_group_profile
        })

        temp_group, _, err = await test_client.create_group(new_group)
        assert err is None

        _, err = await test_client.add_group_target_to_role(
            user.id, user_role.id, temp_group.id)
        assert err is None
        _, err = await test_client.remove_group_target_from_role(
            user.id, user_role.id, group.id)
        assert err is None

        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user.id)
        assert err is None

        await test_client.delete_group(group.id)
        await test_client.delete_group(temp_group.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_user_pagination(self, fs):
        test_client = Client()

        password = models.PasswordCredential({
            "value": "Password150kta"
        })

        user_creds = models.UserCredentials({
            "password": password
        })

        first_user_profile = models.UserProfile()
        first_user_profile.first_name = "John"
        first_user_profile.last_name = "Doe-Paginate-1"
        first_user_profile.email = "John.Doe-Paginate-1@example.com"
        first_user_profile.login = "John.Doe-Paginate-1@example.com"

        second_user_profile = models.UserProfile()
        second_user_profile.first_name = "John"
        second_user_profile.last_name = "Doe-Paginate-2"
        second_user_profile.email = "John.Doe-Paginate-2@example.com"
        second_user_profile.login = "John.Doe-Paginate-2@example.com"

        first_create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": first_user_profile
        })
        second_create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": second_user_profile
        })

        query_params = {"activate": "False"}

        user1, _, err = await test_client.create_user(
            first_create_user_req, query_params)
        assert err is None
        user2, _, err = await test_client.create_user(
            second_create_user_req, query_params)
        assert err is None

        query_params_limit = {"limit": "1"}
        usr_list, resp, err = await test_client.list_users(query_params_limit)
        assert err is None
        assert len(usr_list) == 1
        assert isinstance(usr_list[0], models.User)
        assert resp.has_next()

        second_usr_list, err = await resp.next()
        assert err is None
        assert len(second_usr_list) == 1
        assert isinstance(second_usr_list[0], models.User)

        _, err = await test_client.deactivate_or_delete_user(user1.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user1.id)
        assert err is None

        _, err = await test_client.deactivate_or_delete_user(user2.id)
        assert err is None
        _, err = await test_client.deactivate_or_delete_user(user2.id)
        assert err is None

        found_user, _, err = await test_client.get_user(user1.id)
        assert found_user is None
        assert isinstance(err, OktaAPIError)
