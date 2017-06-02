import unittest
import os
import json

from okta.api_client import Client
from okta.models.user import User


class ClientTest(unittest.TestCase):

    def tests_client_initializer_with_config_file(self):
        """ Tests creating a client from .yaml config.
        """
        client = Client()
        self.assertIsNotNone(client)

    def test_requests_a_user(self):
        """ Tests retrieving a user.
        """
        client = Client()
        users = client.list_users()
        for user in users:
            user = client.get_user(user.id)
            self.assertIsNotNone(user)
            self.assertIsInstance(user, User)
            break

    def test_creates_a_user_model(self):
        """
        Tests creating a User model.
        TODO: Create a user via mock-server
        """
        client = Client()
        user = User()
        user.profile.login = 'foo@example.com'
        user.profile.email = 'foo@example.com'
        user.profile.first_name = 'Foo'
        user.profile.last_name = 'Bar'
        self.assertIsNotNone(user)
        self.assertIsInstance(user, User)
