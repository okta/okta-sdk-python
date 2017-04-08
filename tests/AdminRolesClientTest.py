import json
import os
import unittest

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
        users_client = build_users_client(
            '/api/v1/users/:id/roles - get all roles assigned to a user')

        user = users_client.get_user(
            'mocktestexample-frutis@mocktestexample.com'
        )

        admin_roles_client = build_admin_roles_client(
            '/api/v1/users/:id/roles - get all roles assigned to a user'
        )

        admin_roles_client.get_user_admin_roles(user.id)

    @staticmethod
    def test_assign_role_to_user():
        users_client = build_users_client(
            '/api/v1/users/:id/roles - assign role to a user')

        user = users_client.get_user(
            'mocktestexample-frutis@mocktestexample.com'
        )

        admin_roles_client = build_admin_roles_client(
            '/api/v1/users/:id/roles - assign role to a user'
        )

        admin_roles_client.assign_roles_to_user(user.id, 'ORG_ADMIN')

    @staticmethod
    def test_unassign_role_from_user():
        users_client = build_users_client(
            '/api/v1/users/:id/roles/:rid - unassign role from user')
        user = users_client.get_user(
            'mocktestexample-frutis@mocktestexample.com'
        )

        admin_roles_client = build_admin_roles_client(
            '/api/v1/users/:id/roles/:rid - unassign role from user'
        )

        roles = admin_roles_client.get_user_admin_roles(user.id)
        admin_roles_client.unassign_role_from_user(user.id, roles[0].id)
