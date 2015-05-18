from okta.EventsClient import EventsClient
import unittest
import os


class SessionsClientTest(unittest.TestCase):

    def setUp(self):
        self.client = EventsClient(os.environ.get('OKTA_TEST_URL'), os.environ.get('OKTA_TEST_KEY'))
        self.username = os.environ.get('OKTA_TEST_ADMIN_NAME')
        self.password = os.environ.get('OKTA_TEST_ADMIN_PASSWORD')

    def test_get_events(self):
        events = self.client.get_events(limit=1)
        self.assertEqual(len(events), 1, "Limits aren't enforced on events")

        events = self.client.get_events()
        self.assertGreaterEqual(len(events), 1, "There were no events returned, when there should be")