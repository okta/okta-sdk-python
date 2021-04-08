import aiohttp
import asyncio
import datetime
import time

from http import HTTPStatus
from multidict import MultiDict
from okta.client import Client as OktaClient
from okta.request_executor import RequestExecutor


def test_retry_count_header(monkeypatch):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token, 'rateLimit': {'maxRetries': 2}}
    client = OktaClient(config)

    class MockHTTPRequest():
        """
        async with aiohttp.request(**params) as response:
            return (response.request_info,
                    response,
                    await response.text(),
                    None)

        _, res_details, resp_body, error = \
        headers = res_details.headers
        """

        def __call__(self, **params):
            self.request_info = params
            self.headers = MultiDict({'Date': datetime.datetime.now(tz=datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S %Z'),
                                      'Content-Type': 'application/json',
                                      'X-Rate-Limit-Limit': 600,
                                      'X-Rate-Limit-Remaining': 599,
                                      'X-Rate-Limit-Reset': str(time.time())})
            self.url = params['url']
            self.content_type = 'application/json'
            self.links = ''
            self.text = MockHTTPRequest.mock_response_text
            self.status = HTTPStatus.TOO_MANY_REQUESTS
            return self

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        @staticmethod
        async def mock_response_text():
            return '[{"embedded": null,' \
                   '"links": {"self": {"href": "https://test.okta.com/v1/users/test_id"}},' \
                   '"activated": "2021-01-01T00:00:00.000Z",' \
                   '"created": "2021-01-01T00:00:00.000Z",' \
                   '"credentials": null,' \
                   '"id": "test_id",' \
                   '"last_login": null,' \
                   '"profile": {"name": "test_name"},' \
                   '"status": null,' \
                   '"status_changed": null,' \
                   '"transitioning_to_status": null,' \
                   '"type": null}]'

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp, 'request', mock_http_request)
    res, resp_body, error = asyncio.run(client.list_users())
    # Check request was retried max times and header 'X-Okta-Retry-Count' was set properly
    assert mock_http_request.request_info['headers'].get('X-Okta-Retry-Count') == '2'


def test_is_retryable_status():
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'client': {'orgUrl': org_url,
                         'token': token,
                         'rateLimit': {},
                         'authorizationMode': None}}
    req_exec = RequestExecutor(config=config, cache=None)
    assert req_exec.is_retryable_status(HTTPStatus.TOO_MANY_REQUESTS)
    assert req_exec.is_retryable_status(HTTPStatus.SERVICE_UNAVAILABLE)
    assert req_exec.is_retryable_status(HTTPStatus.GATEWAY_TIMEOUT)
    assert not req_exec.is_retryable_status(HTTPStatus.FORBIDDEN)


def test_clear_empty_params():
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'client': {'orgUrl': org_url,
                         'token': token,
                         'rateLimit': {},
                         'authorizationMode': None}}
    req_exec = RequestExecutor(config=config, cache=None)

    body = {'int_value': 0,
            'str_value': '0',
            'empty_str_value': '',
            'list_value': [1,2,3],
            'empty_list_value': [],
            'dict_value': {'int_value': 0},
            'empty_dict_value': {},
            'nested_empty_dict_value': {'list_value': [1,2,3], 'empty_list_value': []},
            'nested_empty_list_value': {'empty_list_value': []}}

    cleared_body = {'int_value': 0,
                    'str_value': '0',
                    'list_value': [1,2,3],
                    'dict_value': {'int_value': 0},
                    'nested_empty_dict_value': {'list_value': [1,2,3]}}

    assert req_exec.clear_empty_params(body) == cleared_body
