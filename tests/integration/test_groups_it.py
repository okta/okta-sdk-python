import pytest
from tests.mocks import MockOktaClient
from tests.mocks import mock_pause_function
from http import HTTPStatus
import okta.models as models


class TestGroupsResource:
    """
    Integration Tests for the Groups Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_group(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        # Get group using ID
        found_group, _, err = await client.get_group(group.id)
        assert err is None
        assert found_group.id == group.id

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None

        # Ensure group cannot be found again
        found_group, resp, err = await client.get_group(group.id)
        assert err is not None
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert found_group is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_groups(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        groups_list, resp, err = await client.list_groups()
        assert err is None
        assert not resp.has_next()
        assert next((grp for grp in groups_list if grp.id == group.id))

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_search_group(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        query_params_query = {"q": GROUP_NAME}
        groups_list, _, err = await client.list_groups(query_params_query)
        assert err is None
        assert groups_list
        assert len(groups_list) == 1
        assert next((grp for grp in groups_list if grp.id == group.id))

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_group(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        # Create Updated Group Object
        # Create Group Object
        NEW_GROUP_NAME = "Group-Target-Test NEW"
        new_group_profile = models.GroupProfile({
            "name": NEW_GROUP_NAME
        })
        new_group_obj = models.Group({
            "profile": new_group_profile
        })

        _, _, err = await client.update_group(group.id, new_group_obj)
        assert err is None

        # Verify update worked
        found_group, _, err = await client.get_group(group.id)
        assert err is None
        assert found_group.id == group.id
        assert found_group.profile.name == NEW_GROUP_NAME

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_remove_group(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential({
            "value": "Password150kta"
        })
        # Create User Credentials
        user_creds = models.UserCredentials({
            "password": password
        })

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Remove-Group"
        user_profile.email = "John.Doe-Remove-Group@example.com"
        user_profile.login = "John.Doe-Remove-Group@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        # Create query parameters and Create User
        query_params_create = {"activate": "False"}
        user, _, err = await client.create_user(
            create_user_req, query_params_create)
        assert err is None
        assert isinstance(user, models.User)

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        # Add user to group
        _, err = await client.add_user_to_group(group.id, user.id)
        assert err is None

        users_in_group, _, err = await client.list_group_users(group.id)
        assert err is None
        assert next((usr for usr in users_in_group if usr.id == user.id))

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None

        # Retrieve group list again to ensure deleted
        groups_list, _, err = await client.list_groups()
        assert err is None
        assert next((grp for grp in groups_list if grp.id ==
                     group.id), None) is None

        # Deactivate, then delete created user
        _, err = await client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(user.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_group_roles_operations(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        # Create roles
        assign_role_req_ua = models.AssignRoleRequest({
            "type": models.RoleType.USER_ADMIN
        })
        assign_role_req_aa = models.AssignRoleRequest({
            "type": models.RoleType.APP_ADMIN
        })

        ua_role, _, err = await client.assign_role_to_group(
            group.id, assign_role_req_ua)
        assert err is None
        aa_role, _, err = await client.assign_role_to_group(
            group.id, assign_role_req_aa)
        assert err is None

        group_roles, _, err = await client.list_group_assigned_roles(group.id)
        assert err is None
        assert len(group_roles) == 2
        assert next((rle for rle in group_roles if rle.id == ua_role.id))
        assert next((rle for rle in group_roles if rle.id == aa_role.id))

        _, err = await client.remove_role_from_group(group.id, ua_role.id)
        assert err is None

        group_roles, _, err = await client.list_group_assigned_roles(group.id)
        assert err is None
        assert len(group_roles) == 1
        assert next((rle for rle in group_roles if rle.id ==
                     ua_role.id), None) is None
        assert next((rle for rle in group_roles if rle.id == aa_role.id))

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_group_users_operations(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential({
            "value": "Password150kta"
        })
        # Create User Credentials
        user_creds = models.UserCredentials({
            "password": password
        })

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Activate"
        user_profile.email = "John.Doe-Activate@example.com"
        user_profile.login = "John.Doe-Activate@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        # Create query parameters and Create User
        query_params_create = {"activate": "False"}
        user, _, err = await client.create_user(
            create_user_req, query_params_create)
        assert err is None
        assert isinstance(user, models.User)

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        # Add user to group
        _, err = await client.add_user_to_group(group.id, user.id)
        assert err is None

        users_in_group, _, err = await client.list_group_users(group.id)
        assert err is None
        assert next((usr for usr in users_in_group if usr.id == user.id))

        # Remove user from group
        _, err = await client.remove_user_from_group(group.id, user.id)
        assert err is None

        users_in_group, _, err = await client.list_group_users(group.id)
        assert err is None
        assert len(users_in_group) == 0
        assert next(
            (usr for usr in users_in_group if usr.id == user.id), None) is None

        # Deactivate, then delete created user
        _, err = await client.deactivate_or_delete_user(user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(user.id)
        assert err is None

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_group_rule_operations(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Password
        password = models.PasswordCredential({
            "value": "Password150kta"
        })
        # Create User Credentials
        user_creds = models.UserCredentials({
            "password": password
        })

        # Create User Profile and CreateUser Request
        user_profile = models.UserProfile()
        user_profile.first_name = "John"
        user_profile.last_name = "Doe-Group-Rule-Ops"
        user_profile.email = "John.Doe-Group-Rule-Ops@example.com"
        user_profile.login = "John.Doe-Group-Rule-Ops@example.com"

        create_user_req = models.CreateUserRequest({
            "credentials": user_creds,
            "profile": user_profile
        })

        # Create query parameters and Create User
        query_params_create = {"activate": "False"}
        user, _, err = await client.create_user(
            create_user_req, query_params_create)
        assert err is None
        assert isinstance(user, models.User)

        # Create Group Object
        GROUP_NAME = "Group-Target-Test-Group-Rule-Ops"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        # Create Group Rule
        last_name = user.profile.last_name
        GROUP_RULE_NAME = "Test-Group-Rule-Group-Rule-Ops"
        GROUP_RULE_TYPE = "group_rule"
        GROUP_RULE_EXP_TYPE = "urn:okta:expression:1.0"
        GROUP_RULE_EXP_VALUE = f"user.lastName==\"{last_name}\""
        group_rule_exp = models.GroupRuleExpression({
            "type": GROUP_RULE_EXP_TYPE,
            "value": GROUP_RULE_EXP_VALUE
        })

        group_rule_cond = models.GroupRuleConditions({
            "expression": group_rule_exp
        })

        group_rule_group_assignment = models.GroupRuleGroupAssignment({
            "groupIds": [group.id]
        })

        group_rule_action = models.GroupRuleAction({
            "assignUserToGroups": group_rule_group_assignment
        })

        group_rule_object = models.GroupRule({
            "actions": group_rule_action,
            "conditions": group_rule_cond,
            "name": GROUP_RULE_NAME,
            "type": GROUP_RULE_TYPE
        })

        group_rule, _, err = await client.create_group_rule(group_rule_object)
        assert err is None
        assert isinstance(group_rule, models.GroupRule)

        # Activate Group Rule
        _, err = await client.activate_group_rule(group_rule.id)
        assert err is None

        # 15 second sleep for backend to update
        mock_pause_function(15)

        users_in_group, _, err = await client.list_group_users(group.id)
        assert err is None
        assert next((usr for usr in users_in_group if usr.id ==
                     user.id), None) is not None

        # Ensure activated rule is in group rules
        group_rules, _, err = await client.list_group_rules()
        assert err is None
        assert next((rule for rule in group_rules if rule.id ==
                     group_rule.id), None) is not None

        # Deactivate rule (to update)
        _, err = await client.deactivate_group_rule(group_rule.id)
        assert err is None

        # Update rule
        # Create new rule
        NEW_GROUP_RULE_NAME = "Test-Group-Rule Updated"
        NEW_GROUP_RULE_EXP_VALUE = "user.lastName==\"BLAHBLAHBLAH\""
        new_group_rule_exp = models.GroupRuleExpression({
            "type": GROUP_RULE_EXP_TYPE,
            "value": NEW_GROUP_RULE_EXP_VALUE
        })

        new_group_rule_cond = models.GroupRuleConditions({
            "expression": new_group_rule_exp
        })

        new_group_rule_group_assignment = models.GroupRuleGroupAssignment({
            "groupIds": [group.id]
        })

        new_group_rule_action = models.GroupRuleAction({
            "assignUserToGroups": new_group_rule_group_assignment
        })

        new_group_rule_object = models.GroupRule({
            "actions": new_group_rule_action,
            "conditions": new_group_rule_cond,
            "name": NEW_GROUP_RULE_NAME,
            "type": GROUP_RULE_TYPE
        })

        new_group_rule, _, err = await client.update_group_rule(
            group_rule.id,
            new_group_rule_object)
        assert err is None

        # Activate updated rule and verify user isn't in group
        _, err = await client.activate_group_rule(new_group_rule.id)
        assert err is None

        # 15 second sleep for backend to update
        mock_pause_function(15)

        users_in_group, _, err = await client.list_group_users(group.id)
        assert err is None
        assert next(
            (usr for usr in users_in_group if usr.id == user.id), None) is None

        # Deactivate rule
        _, err = await client.deactivate_group_rule(new_group_rule.id)
        assert err is None

        # Deactivate, then delete created user
        _, err = await client.deactivate_user(user.id)
        assert err is None
        _, err = await client.deactivate_or_delete_user(user.id)
        assert err is None

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None

        # Delete group rules
        _, err = await client.delete_group_rule(group_rule.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_group_target_add(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Group Objects
        GROUP_1_NAME = "Group-Target-Test 1"
        group_1_profile = models.GroupProfile({
            "name": GROUP_1_NAME
        })
        group_1_obj = models.Group({
            "profile": group_1_profile
        })

        GROUP_2_NAME = "Group-Target-Test 2"
        group_2_profile = models.GroupProfile({
            "name": GROUP_2_NAME
        })
        group_2_obj = models.Group({
            "profile": group_2_profile
        })

        # Create Groups
        group_1, _, err = await client.create_group(group_1_obj)
        assert err is None
        assert isinstance(group_1, models.Group)

        group_2, _, err = await client.create_group(group_2_obj)
        assert err is None
        assert isinstance(group_2, models.Group)

        # Create role and add group targets
        assign_role_req_ua = models.AssignRoleRequest({
            "type": models.RoleType.USER_ADMIN
        })

        ua_role, _, err = await client.assign_role_to_group(
            group_1.id, assign_role_req_ua)
        assert err is None

        _, err = await\
            client.add_group_target_to_group_administrator_role_for_group(
                group_1.id, ua_role.id, group_2.id)

        # Make sure targets are listed
        groups_list, _, err = await client.list_group_targets_for_group_role(
            group_1.id, ua_role.id)
        assert err is None
        assert next((grp for grp in groups_list if grp.id == group_2.id))

        # Delete created groups
        _, err = await client.delete_group(group_1.id)
        assert err is None
        _, err = await client.delete_group(group_2.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_group_target_remove(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Group Objects
        GROUP_1_NAME = "Group-Target-Test 1"
        group_1_profile = models.GroupProfile({
            "name": GROUP_1_NAME
        })
        group_1_obj = models.Group({
            "profile": group_1_profile
        })

        GROUP_2_NAME = "Group-Target-Test 2"
        group_2_profile = models.GroupProfile({
            "name": GROUP_2_NAME
        })
        group_2_obj = models.Group({
            "profile": group_2_profile
        })

        GROUP_3_NAME = "Group-Target-Test 3"
        group_3_profile = models.GroupProfile({
            "name": GROUP_3_NAME
        })
        group_3_obj = models.Group({
            "profile": group_3_profile
        })

        # Create Groups
        group_1, _, err = await client.create_group(group_1_obj)
        assert err is None
        assert isinstance(group_1, models.Group)

        group_2, _, err = await client.create_group(group_2_obj)
        assert err is None
        assert isinstance(group_2, models.Group)

        group_3, _, err = await client.create_group(group_3_obj)
        assert err is None
        assert isinstance(group_3, models.Group)

        # Create role and add group targets
        assign_role_req_ua = models.AssignRoleRequest({
            "type": models.RoleType.USER_ADMIN
        })

        ua_role, _, err = await client.assign_role_to_group(
            group_1.id, assign_role_req_ua)
        assert err is None

        _, err = await\
            client.add_group_target_to_group_administrator_role_for_group(
                group_1.id, ua_role.id, group_2.id)
        _, err = await\
            client.add_group_target_to_group_administrator_role_for_group(
                group_1.id, ua_role.id, group_3.id)

        groups_list, _, err = await client.list_group_targets_for_group_role(
            group_1.id, ua_role.id)
        assert err is None
        assert next((grp for grp in groups_list if grp.id == group_2.id))
        assert next((grp for grp in groups_list if grp.id == group_3.id))

        # Remove from 2 and ensure 2 isn't listed
        _, err = await \
            client.remove_group_target_from_group_admin_role_given_to_group(
                group_1.id, ua_role.id, group_2.id)

        groups_list, _, err = await client.list_group_targets_for_group_role(
            group_1.id, ua_role.id)
        assert err is None
        assert next((grp for grp in groups_list if grp.id ==
                     group_2.id), None) is None
        assert next((grp for grp in groups_list if grp.id == group_3.id))

        # Delete created groups
        _, err = await client.delete_group(group_1.id)
        assert err is None
        _, err = await client.delete_group(group_2.id)
        assert err is None
        _, err = await client.delete_group(group_3.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_group_assigned_applications(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Group Objects
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        # Create Application object and Application in Org
        APP_LABEL = "Test Assigned-Applications"
        BUTTON_FIELD = "btn-login"
        PASSWORD_FIELD = "txt-box-password"
        USERNAME_FIELD = "txt-box-username"
        URL = "https://example.com/login.html"
        LOGIN_URL_REGEX = f"^{URL}$"

        swa_app_settings_app = models.SwaApplicationSettingsApplication({
            "buttonField": BUTTON_FIELD,
            "passwordField": PASSWORD_FIELD,
            "usernameField": USERNAME_FIELD,
            "url": URL,
            "loginUrlRegex": LOGIN_URL_REGEX
        })

        swa_app_settings = models.SwaApplicationSettings({
            "app": swa_app_settings_app
        })

        swa_app_obj = models.SwaApplication({
            "label": APP_LABEL,
            "settings": swa_app_settings,
            "signOnMode": models.ApplicationSignOnMode.BROWSER_PLUGIN
        })

        swa_app, _, err = await client.create_application(swa_app_obj)
        assert err is None
        assert isinstance(swa_app, models.SwaApplication)

        # Assign app and group
        assign_ag_req = models.ApplicationGroupAssignment({
            "priority": 0,
            "applicationId": swa_app.id,
            "groupId": group.id
        })

        assign_app_group, _, err = await \
            client.create_application_group_assignment(
                swa_app.id, group.id, assign_ag_req)
        assert err is None

        # 3 second sleep for backend to update
        mock_pause_function(3)

        # Check assigned apps and ensure created app is found
        assigned_apps, _, err = await \
            client.list_assigned_applications_for_group(group.id)
        assert err is None
        assert assigned_apps is not None
        assert len(assigned_apps) > 0
        assert next((app for app in assigned_apps if app.id == swa_app.id))

        # Cleanup app and group created
        _, err = await client.deactivate_application(swa_app.id)
        assert err is None
        _, err = await client.delete_application(swa_app.id)
        assert err is None
        _, err = await client.delete_group(group.id)
        assert err is None
