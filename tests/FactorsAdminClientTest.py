import unittest
import os
import json

from okta import FactorsAdminClient

class FactorsAdminClientTest(unittest.TestCase):

    def tests_client_initializer_args(self):
        client = FactorsAdminClient('https://example.okta.com', 'api_key')

    def tests_client_initializer_kwargs(self):
        client = FactorsAdminClient(base_url='https://example.okta.com', api_token='api_key')
