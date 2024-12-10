
import unittest
from okta.okta_configuration import OktaConfiguration
from okta.api_client import ApiClient


class TestApiClientEvents(unittest.TestCase):
    modify_method_asserted = False
    modify_url_asserted = False
    
    changed_url = "https://changed.com"
    
    def setUp(self) -> None:
        configuration = OktaConfiguration().get_configuration()
        self.api_client = ApiClient(configuration)
        
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_modify_method(self) -> None:
        def call_started_handler(call_info):
            call_info.method = "TEST"
            
        def test_request(method, url, headers, body, post_params, _request_timeout):
            self.assertTrue(method == "TEST")
            self.modify_method_asserted = True
            
        self.assertFalse(self.modify_method_asserted)
        self.api_client.rest_client.request = test_request
        self.api_client.call_api_started.connect(call_started_handler)
        self.api_client.call_api("POST", "https://example.com")
        self.assertTrue(self.modify_method_asserted)
        
    def test_modify_url(self) -> None:
        def call_started_handler(call_info):
            call_info.url = self.changed_url
            
        def test_request(method, url, headers, body, post_params, _request_timeout):
            self.assertTrue(url == self.changed_url)
            self.modify_url_asserted = True
        
        self.assertFalse(self.modify_url_asserted)
        self.api_client.rest_client.request = test_request
        self.api_client.call_api_started.connect(call_started_handler)
        self.api_client.call_api("POST", "https://notthis.com")
        self.assertTrue(self.modify_url_asserted)