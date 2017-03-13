import unittest
import os
import json

from okta import EventsClient

config_path = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                            '../.sdk.config.json'))

with open(config_path) as sdk_config_data:
    sdk_config = json.load(sdk_config_data)


class EventsClientTest(unittest.TestCase):

    def tests_client_initializer_args(self):
        client = EventsClient('https://example.okta.com', 'api_key')

    def tests_client_initializer_kwargs(self):
        client = EventsClient(base_url='https://example.okta.com', api_token='api_key')
