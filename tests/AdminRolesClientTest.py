import json
import os
import unittest

from okta import AppInstanceClient
from okta import UserGroupsClient
from okta import UsersClient
from okta.AdminRolesClient import AdminRolesClient

config_path = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                            '../.sdk.config.json'))

with open(config_path) as sdk_config_data:
    sdk_config = json.load(sdk_config_data)


def build_admin_roles_client(test_description):
    url = '{}:{}'.format(sdk_config['mockOkta']['proxy'],
                         sdk_config['mockOkta']['port'])
    return AdminRolesClient(
        base_url=url,
        api_token=sdk_config['mockOkta']['apiKey'],
        headers={
            'x-test-description': test_description
        }
    )


def build_users_client(test_description):
    url = '{}:{}'.format(sdk_config['mockOkta']['proxy'],
                         sdk_config['mockOkta']['port'])
    return UsersClient(
        base_url=url,
        api_token=sdk_config['mockOkta']['apiKey'],
        headers={
            'x-test-description': test_description
        }
    )


def build_user_groups_client(test_description):
    url = '{}:{}'.format(sdk_config['mockOkta']['proxy'],
                         sdk_config['mockOkta']['port'])
    return UserGroupsClient(
        base_url=url,
        api_token=sdk_config['mockOkta']['apiKey'],
        headers={
            'x-test-description': test_description
        }
    )


def build_app_client(test_description):
    url = '{}:{}'.format(sdk_config['mockOkta']['proxy'],
                         sdk_config['mockOkta']['port'])
    return AppInstanceClient(
        base_url=url,
        api_token=sdk_config['mockOkta']['apiKey'],
        headers={
            'x-test-description': test_description
        }
    )


class AdminRolesClientTest(unittest.TestCase):
    @staticmethod
    def tests_client_initializer_args():
        AdminRolesClient('https://example.okta.com', 'api_key')

    @staticmethod
    def tests_client_initializer_kwargs():
        AdminRolesClient(base_url='https://example.okta.com',
                         api_token='api_key')

    @staticmethod
    def test_get_user_admin_roles():
        test_description = '/api/v1/users/:id/roles -' \
                           ' get all roles assigned to a user'
        users_client = build_users_client(test_description)

        user = users_client.get_user(
            'mocktestexample-frutis@mocktestexample.com'
        )

        admin_roles_client = build_admin_roles_client(test_description)

        admin_roles_client.get_user_admin_roles(user.id)

    @staticmethod
    def test_assign_role_to_user():
        test_description = '/api/v1/users/:id/roles - assign role to a user'
        users_client = build_users_client(test_description)
        user = users_client.get_user(
            'mocktestexample-frutis@mocktestexample.com'
        )

        admin_roles_client = build_admin_roles_client(test_description)

        admin_roles_client.assign_roles_to_user(user.id, 'USER_ADMIN')

    @staticmethod
    def test_unassign_role_from_user():
        test_description = '/api/v1/users/:id/roles/:rid -' \
                           ' unassign role from user'

        users_client = build_users_client(test_description)

        user = users_client.get_user(
            'mocktestexample-frutis@mocktestexample.com'
        )

        admin_roles_client = build_admin_roles_client(test_description)

        roles = admin_roles_client.get_user_admin_roles(user.id)
        admin_roles_client.unassign_role_from_user(user.id, roles[0].id)

    @staticmethod
    def test_get_admin_groups_target_for_user_admin_role():
        test_description = '/api/v1/users/:uid/roles/:rid/' \
                           'targets/groups/:gid - get all group targets for ' \
                           'a USER_ADMIN role assignment'
        users_client = build_users_client(test_description)

        user = users_client.get_user(
            'mocktestexample-frutis@mocktestexample.com'
        )

        admin_roles_client = build_admin_roles_client(test_description)

        roles = admin_roles_client.get_user_admin_roles(user.id)
        admin_roles_client.get_group_targets_for_user_role_assignment(
            user.id,
            roles[0].id
        )

    @staticmethod
    def test_add_group_target_for_user_admin_role():
        test_description = '/api/v1/users/:uid/roles' \
                           '/:rid/targets/groups/:gid - ' \
                           'adds a group target for a USER_ADMIN ' \
                           'role assignment'
        users_client = build_users_client(test_description)
        admin_roles_client = build_admin_roles_client(test_description)
        user_groups_client = build_user_groups_client(test_description)

        user = users_client.get_user(
            'mocktestexample-frutis@mocktestexample.com'
        )

        role = admin_roles_client.get_user_admin_roles(user.id)[0]
        group = user_groups_client.get_groups()[1]

        admin_roles_client.add_group_target_for_user_admin_role(
            user.id,
            role.id,
            group.id
        )

    @staticmethod
    def test_assign_app_admin_role_to_user():
        test_description = '/api/v1/users/:id/roles - assign APP_ADMIN role ' \
                           'to a user'
        users_client = build_users_client(test_description)

        user = users_client.get_user(
            'mocktestexample-applicationrolus@mocktestexample.com'
        )
        admin_roles_client = build_admin_roles_client(test_description)

        admin_roles_client.assign_roles_to_user(user.id, 'APP_ADMIN')

    @staticmethod
    def test_get_app_targets_for_app_admin_role():
        test_description = '/api/v1/users/:uid/roles/:rid/targets/' \
                           'catalog/apps - get all app targets for an ' \
                           'APP_ADMIN role assignment'
        users_client = build_users_client(test_description)
        admin_roles_client = build_admin_roles_client(test_description)

        user = users_client.get_user(
            'mocktestexample-applicationrolus@mocktestexample.com'
        )
        role = admin_roles_client.get_user_admin_roles(user.id)[0]
        admin_roles_client.get_app_targets_for_app_role(
            user.id,
            role.id
        )

    @staticmethod
    def test_add_app_target_to_app_admin_role():
        test_description = '/api/v1/users/:uid/roles/:rid/targets/' \
                           'catalog/apps - adds an app target for an ' \
                           'APP_ADMIN role assignment'
        users_client = build_users_client(test_description)
        admin_roles_client = build_admin_roles_client(test_description)
        app_client = build_app_client(test_description)

        user = users_client.get_user(
            'mocktestexample-applicationrolus@mocktestexample.com'
        )

        role = admin_roles_client.get_user_admin_roles(user.id)[0]
        app = app_client.get_app_instances()[0]

        admin_roles_client.add_app_target_to_app_admin_role(
            user.id,
            role.id,
            app.name
        )

    @staticmethod
    def test_removes_add_app_target_to_app_admin_role():
        test_description = '/api/v1/users/:uid/roles/:rid/targets/' \
                           'catalog/apps - removes an app target for an ' \
                           'APP_ADMIN role assignment'
        users_client = build_users_client(test_description)
        admin_roles_client = build_admin_roles_client(test_description)
        app_client = build_app_client(test_description)

        user = users_client.get_user(
            'mocktestexample-applicationrolus@mocktestexample.com'
        )

        role = admin_roles_client.get_user_admin_roles(user.id)[0]
        app = app_client.get_app_instances()[0]

        admin_roles_client.add_app_target_to_app_admin_role(
            user.id,
            role.id,
            app.name
        )

        admin_roles_client.remove_app_target_to_app_admin_role(
            user.id,
            role.id,
            app.name
        )
