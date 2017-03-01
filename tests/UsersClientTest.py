from okta import UsersClient
from okta.models.user import User
import unittest
import os
import json

config_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "../.sdk.config.json"))
with open(config_path) as sdk_config_data:
    sdk_config = json.load(sdk_config_data)

def build_client(test_description):
    return UsersClient(
        base_url=sdk_config["TEST_URL"],
        api_token=sdk_config["API_KEY"],
        headers={
            "x-test-description": test_description
        }
    )

class UsersClientTest(unittest.TestCase):

    def test_requests_users(self):
        client = build_client("/api/v1/users - requests users")
        users = client.get_users()
    
    def test_requests_a_user(self):
        client = build_client("/api/v1/users/:id - requests a user")
        users = client.get_users()
        user = client.get_user(users[0].id)

    def test_creates_a_user_without_credentials(self):
        client = build_client("/api/v1/users/:id - creates a user without credentials")
        user = User(login='brutis.mcjanky@example.com',
                    email='brutis.mcjanky@example.com',
                    firstName='First',
                    lastName='McJanky')
        client.create_user(user)
