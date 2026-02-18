import aiohttp
import datetime
import pytest
import time

from http import HTTPStatus
from multidict import MultiDict
from okta.client import Client as OktaClient
from okta.request_executor import RequestExecutor


@pytest.mark.asyncio
async def test_retry_count_header(monkeypatch):
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
            self.headers = MultiDict(
                {'Date': datetime.datetime.now(tz=datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S %Z'),
                 'Content-Type': 'application/json',
                 'X-Rate-Limit-Limit': 600,
                 'X-Rate-Limit-Remaining': 599,
                 'X-Rate-Limit-Reset': str(time.time())}
            )
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
    monkeypatch.setattr(aiohttp.ClientSession, 'request', mock_http_request)
    res, resp_body, error = await client.list_users()
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
            'list_value': [1, 2, 3],
            'empty_list_value': [],
            'dict_value': {'int_value': 0},
            'empty_dict_value': {},
            'nested_empty_dict_value': {'list_value': [1, 2, 3], 'empty_list_value': []},
            'nested_empty_list_value': {'empty_list_value': []}}

    cleared_body = {'int_value': 0,
                    'str_value': '0',
                    'list_value': [1, 2, 3],
                    'dict_value': {'int_value': 0},
                    'nested_empty_dict_value': {'list_value': [1, 2, 3]}}

    assert req_exec.clear_empty_params(body) == cleared_body


class TestRequestExecutorStringConfig:
    """Tests that string config values (as from env vars) are handled correctly."""

    def _build_config(self, request_timeout=0, max_retries=2):
        return {'client': {'orgUrl': 'https://test.okta.com',
                           'token': 'TOKEN',
                           'rateLimit': {'maxRetries': max_retries},
                           'requestTimeout': request_timeout,
                           'authorizationMode': None}}

    def test_request_timeout_string_value(self):
        """String requestTimeout (e.g. from env var) must be converted to int."""
        config = self._build_config(request_timeout='30')
        req_exec = RequestExecutor(config=config, cache=None)
        assert req_exec._request_timeout == 30
        assert isinstance(req_exec._request_timeout, int)

    def test_max_retries_string_value(self):
        """String maxRetries (e.g. from env var) must be converted to int."""
        config = self._build_config(max_retries='4')
        req_exec = RequestExecutor(config=config, cache=None)
        assert req_exec._max_retries == 4
        assert isinstance(req_exec._max_retries, int)

    def test_request_timeout_int_value(self):
        """Int requestTimeout should still work as before."""
        config = self._build_config(request_timeout=30)
        req_exec = RequestExecutor(config=config, cache=None)
        assert req_exec._request_timeout == 30

    def test_max_retries_int_value(self):
        """Int maxRetries should still work as before."""
        config = self._build_config(max_retries=4)
        req_exec = RequestExecutor(config=config, cache=None)
        assert req_exec._max_retries == 4

    def test_request_timeout_zero_string(self):
        """String '0' for requestTimeout (disabled) must work."""
        config = self._build_config(request_timeout='0')
        req_exec = RequestExecutor(config=config, cache=None)
        assert req_exec._request_timeout == 0

    def test_max_retries_zero_string(self):
        """String '0' for maxRetries (disabled) must work."""
        config = self._build_config(max_retries='0')
        req_exec = RequestExecutor(config=config, cache=None)
        assert req_exec._max_retries == 0

    def test_request_timeout_negative_string_raises(self):
        """Negative string requestTimeout must still raise ValueError."""
        config = self._build_config(request_timeout='-1')
        with pytest.raises(ValueError):
            RequestExecutor(config=config, cache=None)

    def test_max_retries_negative_string_raises(self):
        """Negative string maxRetries must still raise ValueError."""
        config = self._build_config(max_retries='-1')
        with pytest.raises(ValueError):
            RequestExecutor(config=config, cache=None)


@pytest.mark.parametrize(
    "accept_header",
    ["", "application/xml", "application/json",
        "text/html", "application/xhtml+xml", "image/jpeg"]
)
@pytest.mark.asyncio
async def test_overwrite_default_request_executor_headers(accept_header):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'client': {'orgUrl': org_url,
                         'token': token,
                         'rateLimit': {},
                         'authorizationMode': None}}
    req_exec = RequestExecutor(config=config, cache=None)

    # overwrite headers if parameter present
    header_overwrite = {'Accept': accept_header} if accept_header else {}
    request, error = await req_exec.create_request(
        'GET',
        f'{org_url}/api/v1/users',
        {},
        header_overwrite,
        {}
    )
    assert request is not None
    assert request["headers"]["Accept"] ==\
        accept_header if accept_header else "application/json"
