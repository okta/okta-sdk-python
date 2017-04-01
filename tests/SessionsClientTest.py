import unittest
import os
import json

from okta import SessionsClient

class SessionsClientTest(unittest.TestCase):

    def tests_client_initializer_args(self):
        client = SessionsClient('https://example.okta.com', 'api_key')

    def tests_client_initializer_kwargs(self):
        client = SessionsClient(base_url='https://example.okta.com', api_token='api_key')
