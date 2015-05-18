from okta.AppInstanceClient import AppInstanceClient
from okta.framework.OktaError import OktaError
import unittest
import os
from okta.models.app.AppInstance import AppInstance


class SessionsClientTest(unittest.TestCase):

    def setUp(self):
        self.client = AppInstanceClient(os.environ.get('OKTA_TEST_URL'), os.environ.get('OKTA_TEST_KEY'))
        self.username = os.environ.get('OKTA_TEST_ADMIN_NAME')
        self.password = os.environ.get('OKTA_TEST_ADMIN_PASSWORD')

    def test_create_app(self):
        app = AppInstance.build_bookmark("https://www.google.com")
        app = self.client.create_app_instance(app)
        self.assertIsNotNone(app.id)

    def test_delete_app(self):
        app = AppInstance.build_bookmark("https://www.google.com")
        app = self.client.create_app_instance(app)
        self.client.deactivate_app_instance(app.id)
        self.client.delete_app_instance(app.id)
        self.assertRaises(OktaError, self.client.get_app_instance, app.id)