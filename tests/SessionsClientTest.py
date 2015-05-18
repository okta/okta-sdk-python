from okta.SessionsClient import SessionsClient
from okta.framework.OktaError import OktaError
import unittest
import os


class SessionsClientTest(unittest.TestCase):

    def setUp(self):
        self.client = SessionsClient(os.environ.get('OKTA_TEST_URL'), os.environ.get('OKTA_TEST_KEY'))
        self.username = os.environ.get('OKTA_TEST_ADMIN_NAME')
        self.password = os.environ.get('OKTA_TEST_ADMIN_PASSWORD')

    def test_create_session(self):
        session = self.client.create_session(self.username, self.password)
        self.assertIsNotNone(session.id, "The session wasn't created with an id")

        session = self.client.create_session_with_cookie_token(self.username, self.password)
        self.assertIsNotNone(session.cookieToken, "The session wasn't created with a cookieToken")

        session = self.client.create_session_with_cookie_token_url(self.username, self.password)
        self.assertIsNotNone(session.cookieTokenUrl, "The session wasn't created with a cookieTokenUrl")

    def test_validate_session(self):
        session = self.client.create_session(self.username, self.password)

        # This shouldn't throw an error
        session = self.client.validate_session(session.id)

    def test_extend_session(self):
        session = self.client.create_session(self.username, self.password)

        # This shouldn't throw an error
        session = self.client.extend_session(session.id)

    def test_close_session(self):
        session = self.client.create_session(self.username, self.password)

        self.client.clear_session(session.id)
        self.assertRaises(OktaError, self.client.validate_session, session.id)