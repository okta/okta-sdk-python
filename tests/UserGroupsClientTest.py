import unittest
import os
import json

from okta import UserGroupsClient
from okta import UsersClient
from okta.models.usergroup import UserGroup
from okta.models.user import User

config_path = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                            '../.sdk.config.json'))

with open(config_path) as sdk_config_data:
    sdk_config = json.load(sdk_config_data)


def build_client(test_description):
    url = '{}:{}'.format(sdk_config['mockOkta']['proxy'],
                         sdk_config['mockOkta']['port'])
    return UserGroupsClient(
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


class UserGroupsClientTest(unittest.TestCase):

    def test_requests_a_group(self):
        client = build_client('/api/v1/groups/:id - requests a group')
        groups = client.get_groups()
        client.get_group(groups[0].id)

    def test_create_a_group(self):
        client = build_client('/api/v1/groups/:id - creates a group')
        group = {
            'profile': {
                'name': 'West Coast Users',
                'description': 'Straight Outta Compton'
            }
        }
        client.create_group(group)

    def test_updates_a_group(self):
        client = build_client('/api/v1/groups/:id - updates a group')
        groups = client.get_groups()
        group_ids = [group.id for group in groups
                     if group.profile.name == 'TestGroup']
        updated_group = {
            'profile': {
                'name': 'TestGroup',
                'description': 'Amended description'
            }
        }
        client.update_group_by_id(group_ids[0], updated_group)

    def test_request_group_members(self):
        client = build_client('/api/v1/groups/:id - request group members')
        groups = client.get_groups()
        client.get_group_users(groups[0].id)

    def test_delete_group(self):
        client = build_client('/api/v1/groups/:id - deletes a group')
        groups = client.get_groups()
        group_ids = [group.id for group in groups
                     if group.profile.name == 'DeleteGroup']
        client.delete_group(group_ids[0])

    def test_add_user_to_group(self):
        header_description = '/api/v1/groups/:id - add user to group'
        client = build_client(header_description)
        user_client = build_users_client(header_description)
        group = [group for group in client.get_groups()
                 if group.profile.name == 'TestGroup']
        user = user_client.get_user('mocktestexample-frutis@mocktestexample.com')
        client.add_user_to_group(group[0], user)
