import unittest
import os
import json

from okta import EventsClient

class EventsClientTest(unittest.TestCase):

    def tests_client_initializer_args(self):
        client = EventsClient('https://example.okta.com', 'api_key')

    def tests_client_initializer_kwargs(self):
        client = EventsClient(base_url='https://example.okta.com', api_token='api_key')
