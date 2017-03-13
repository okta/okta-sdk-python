import unittest
import os
import json

from okta import AuthClient

config_path = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                            '../.sdk.config.json'))

with open(config_path) as sdk_config_data:
    sdk_config = json.load(sdk_config_data)


class AuthClientTest(unittest.TestCase):

    def tests_client_initializer_args(self):
        client = AuthClient('https://example.okta.com', 'api_key')

    def tests_client_initializer_kwargs(self):
        client = AuthClient(base_url='https://example.okta.com', api_token='api_key')
