from okta import UserGroupsClient
from okta.models.usergroup import UserGroup
from okta import UsersClient
from okta.models.user import User
import random
import unittest
import os


class UserGroupsClientTest(unittest.TestCase):

    def setUp(self):
        self.client = UserGroupsClient(os.environ.get('OKTA_TEST_URL'), os.environ.get('OKTA_TEST_KEY'))
        self.user_client = UsersClient(os.environ.get('OKTA_TEST_URL'), os.environ.get('OKTA_TEST_KEY'))

    def test_single_group(self):
        name = 'random_group_' + str(random.random())
        group = UserGroup(name=name, description='something interesting here')
        group = self.client.create_group(group)
        self.assertEqual(group.profile.name, name, "The name for the group wasn't set properly")

    def test_add_user_to_group(self):
        # Create group
        name = 'random_group_' + str(random.random())
        group = UserGroup(name=name, description='something interesting here')
        group = self.client.create_group(group)

        # Create user
        user = User(login='fake' + str(random.random()) + '@asdf.com',
                    email='fake@asdf.com',
                    firstName='Joe',
                    lastName='Schmoe')
        user = self.user_client.create_user(user, activate=False)

        self.client.add_user_to_group(group, user)