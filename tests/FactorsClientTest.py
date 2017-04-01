import unittest
import os
import json

from okta import FactorsClient

class FactorsClientTest(unittest.TestCase):

    def tests_client_initializer_args(self):
        client = FactorsClient('https://example.okta.com', 'api_key')

    def tests_client_initializer_kwargs(self):
        client = FactorsClient(base_url='https://example.okta.com', api_token='api_key')
