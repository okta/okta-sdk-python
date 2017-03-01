import unittest
import os
import json

from okta import UsersClient
from okta.models.user import User

config_path = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                                "../.sdk.config.json"))

with open(config_path) as sdk_config_data:
    sdk_config = json.load(sdk_config_data)


def build_client(test_description):
    url = "{}:{}".format(sdk_config['mockOkta']['proxy'],
                         sdk_config['mockOkta']['port'])
    return UsersClient(
        base_url=url,
        api_token=sdk_config['mockOkta']['apiKey'],
        headers={
            "x-test-description": test_description,
            "User-Agent": "mock-okta-client",
            }
    )


class UsersClientTest(unittest.TestCase):

    def test_requests_users(self):
        client = build_client("/api/v1/users - requests users")
        client.get_users()

    def test_requests_a_user(self):
        client = build_client("/api/v1/users/:id - requests a user")
        users = client.get_users()
        client.get_user(users[0].id)

    def test_creates_a_user_without_credentials(self):
        client = build_client("/api/v1/users/:id - creates a user without credentials")
        user = User(login='brutis.mcjanky@example.com',
                    email='brutis.mcjanky@example.com',
                    firstName='First',
                    lastName='McJanky')
        client.create_user(user)

    def test_update_a_user(self):
        client = build_client("/api/v1/users/:id - updates a user")
        user = client.get_user('frutis.mcjanky@example.com')
        user.profile.firstName = 'NewFirst'
        client.update_user_by_id(user.id, {'profile': user.profile})

    def test_delete_a_user(self):
        client = build_client("/api/v1/users/:id - deletes a user")
        user = client.get_user("deleteme.mcjanky@example.com")
        client.delete_user(user.id)

    def test_activate_user(self):
        client = build_client("/api/v1/users/:id/lifecycle - activates a user")
        user = client.get_user('deactive.mcjanky@example.com')
        client.activate_user(user.id)

    def test_deactivate_user(self):
        client = build_client("/api/v1/users/:id/lifecycle - deactivates a user")
        user = client.get_user('deactive.mcjanky@example.com')
        client.deactivate_user(user.id)

    def test_change_password(self):
        client = build_client("/api/v1/users/:id/credentials - change a user password")
        user = client.get_user('frutis.mcjanky@example.com')
        client.change_password(user.id, "Asdf1234", "Asdf1234!")

    def test_reset_password(self):
        client = build_client("/api/v1/users/:id/lifecycle - reset a user password")
        user = client.get_user('frutis.mcjanky@example.com')
        client.reset_password(user.id, False)

    def test_expire_password(self):
        client = build_client("/api/v1/users/:id/credentials - expires a user password")
        user = client.get_user('frutis.mcjanky@example.com')
        client.expire_password(user.id)
