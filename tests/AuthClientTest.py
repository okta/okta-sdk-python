from okta.AuthClient import AuthClient
import unittest
import os


class SessionsClientTest(unittest.TestCase):

    def setUp(self):
        self.client = AuthClient(os.environ.get('OKTA_TEST_URL'), os.environ.get('OKTA_TEST_KEY'))
        self.username = os.environ.get('OKTA_TEST_ADMIN_NAME')
        self.password = os.environ.get('OKTA_TEST_ADMIN_PASSWORD')

    def test_simple_auth(self):
        response = self.client.authenticate(self.username, self.password)
        self.assertTrue(response.sessionToken or response.status == 'MFA_REQUIRED', "The simple auth failed")