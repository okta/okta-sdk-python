from okta import UsersClient
from okta.models.user import User
import random
import unittest
import os


class UsersClientTest(unittest.TestCase):

    def setUp(self):
        self.client = UsersClient(os.environ.get('OKTA_TEST_URL'), os.environ.get('OKTA_TEST_KEY'))

    def test_paging(self):
        users = self.client.get_paged_users(limit=1)

        first_page_hit = subsequent_page_hit = False

        for user in users.result:
            first_page_hit = True

        while not users.is_last_page():
            users = self.client.get_paged_users(url=users.next_url)
            for user in users.result:
                subsequent_page_hit = True

        self.assertTrue(first_page_hit and subsequent_page_hit, "The first and subsequent pages weren't hit")

    def test_single_user(self):
        user = User(login='fake' + str(random.random()) + '@asdf.com',
                    email='fake@asdf.com',
                    firstName='Joe',
                    lastName='Schmoe')
        user = self.client.create_user(user, activate=False)
        self.assertEqual(user.status, "STAGED", "User should be staged")

        user = User(login='fake' + str(random.random()) + '@asdf.com',
                    email='fake@asdf.com',
                    firstName='Joe',
                    lastName='Schmoe')
        user = self.client.create_user(user, activate=True)
        self.assertEqual(user.status, "PROVISIONED", "User should be provisioned")