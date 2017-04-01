import unittest
import os
import json

from okta import AuthClient

class AuthClientTest(unittest.TestCase):

    def tests_client_initializer_args(self):
        client = AuthClient('https://example.okta.com', 'api_key')

    def tests_client_initializer_kwargs(self):
        client = AuthClient(base_url='https://example.okta.com', api_token='api_key')
