import unittest
import os
import json

from okta import AuthClient

config_path = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                            '../.sdk.config.json'))

with open(config_path) as sdk_config_data:
    sdk_config = json.load(sdk_config_data)


def build_client(test_description):
    url = '{}:{}'.format(sdk_config['mockOkta']['proxy'],
                         sdk_config['mockOkta']['port'])
    return AuthClient(
        base_url=url,
        api_token=sdk_config['mockOkta']['apiKey'],
        headers={
            'x-test-description': test_description
        }
    )


class AuthClientTest(unittest.TestCase):

    def tests_client_initializer(self):
        client = build_client('/api/v1/events - initialize auth client')
