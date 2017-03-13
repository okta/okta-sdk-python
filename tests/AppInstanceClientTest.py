import unittest
import os
import json

from okta import AppInstanceClient

class AppInstanceClientTest(unittest.TestCase):

    def tests_client_initializer_args(self):
        client = AppInstanceClient('https://example.okta.com', 'api_key')

    def tests_client_initializer_kwargs(self):
        client = AppInstanceClient(base_url='https://example.okta.com', api_token='api_key')

