from okta.UserGroupsClient import UserGroupsClient
from okta.models.usergroup.UserGroup import UserGroup
import random
import unittest
import os


class UserGroupsClientTest(unittest.TestCase):

    def setUp(self):
        self.client = UserGroupsClient(os.environ.get('OKTA_TEST_URL'), os.environ.get('OKTA_TEST_KEY'))

    def test_single_group(self):
        name = 'random_group_' + str(random.random())
        group = UserGroup(name=name, description='something interesting here')
        group = self.client.create_group(group)
        self.assertEqual(group.profile.name, name, "The name for the group wasn't set properly")