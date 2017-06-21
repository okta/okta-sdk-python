import unittest
import os
import json

from datetime import datetime

from okta.api_client import Client
from okta.models.user import User
from okta.models.user_group import UserGroup


class ClientTests(unittest.TestCase):

    def test_client_initializer_with_params(self):
        """
        Tests creating a client from constructor args.
        """
        client = Client(
            orgUrl = "https://jordandemo.oktapreview.com",
            token="00uZWgNnWiLFsSpLSu7MI4xyOurF2m6xLBFAU6YCQW"
        )
        self.assertIsNotNone(client)

    def tests_client_initializer_with_config_file(self):
        """
        Tests creating a client from .yaml config.
        """
        client = Client()
        self.assertIsNotNone(client)

    def test_requests_a_user(self):
        """
        Tests retrieving a user.
        """
        client = Client()
        user = client.users['jordan.melberg@gmail.com']
        print "Test: User by email"
        print user.profile.email

        print ""
        print "Test: Users in bulk"
        for user in client.users:
            print user.profile.email


        print ""
        print "Test: Users by limit"
        for user in client.users.limit(5):
            print 'User:', user.profile.email

        print ""
        print "Test: Users by slice"
        for user in client.users[1:10:2]:
            print user.profile.email

        # users = client.list_users()
        # for user in users:
        #     user = client.get_user(user.id)
        #     self.assertIsNotNone(user)
        #     self.assertIsInstance(user, User)
        #     break

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

    # def test_request_a_group(self):
    #     """
    #     Tests retrieving a group.
    #     """
    #     client = Client()
    #     groups = client.list_groups()
    #     for group in groups:
    #         self.assertIsNotNone(group)
    #         self.assertIsInstance(group, UserGroup)
    #         break

    # def test_assign_user_to_group(self):
    #     """
    #     Tests adding a user to a group.
    #     """
    #     client = Client()

    #     # Get user
    #     users = client.list_users()
    #     group_user = None
    #     for user in users:
    #         group_user = client.get_user(user.id)
    #         self.assertIsNotNone(group_user)
    #         self.assertIsInstance(group_user, User)
    #         break
    #     groups = client.list_groups()
    #     for group in groups:
    #         client.add_user_to_group(group.id, group_user.id)

    #         # Verify user was added to group
    #         for g_user in client.list_group_users(group.id):
    #             if g_user.id == group_user.id:
    #                 self.assertEqual(g_user.id, group_user.id)
    #         break
