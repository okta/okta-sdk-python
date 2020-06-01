from okta.http_client import HTTPClient
from okta.request_executor import RequestExecutor
from okta.cache.no_op_cache import NoOpCache
from okta.user_agent import UserAgent
import pytest
import aiohttp
import asyncio
import json

REQUEST_TIMEOUT = 5  # seconds
ORG_URL = "https://your.okta.com"
API_TOKEN = "yourApiToken"
GET_USERS_CALL = "/api/v1/users?limit=200"


class MockHTTPRequest:
    def __init__(self):
        self.headers = {
            "User-Agent": UserAgent().get_user_agent_string(),
            "Authorization": f"SSWS {API_TOKEN}",
            # etc
        }
        self.url = ORG_URL + GET_USERS_CALL


class MockClientResponse:
    def __init__(self, request, response_details, response_data):
        self.req = request
        self.response_details = response_details
        self.response_data = response_data

    def response(self):
        return (self.req, self.response_details, self.response_data, None)


async def mock_return(*args, **kwargs):
    response_details = {
        'Content-Type': "application/json"
    }
    response_data = json.loads(json.dumps([{'ID': 1}, {'ID': 2}]))

    response = MockClientResponse(MockHTTPRequest(),
                                  response_details, response_data)
    return response.response()


async def mock_return_error(*args, **kwargs):
    return (None, None, None, json.dumps({
        'errorCode': '',
        'errorSummary': '',
        'errorLink': '',
        'errorId': '',
        'errorCauses': []
    }))


async def mock_timeout_response(*args, **kwargs):
    return (None, None, None, asyncio.exceptions.TimeoutError())


async def mock_invalid_HTTP_response(*args, **kwargs):
    return (None, None, None, aiohttp.ContentTypeError(None, None))


@ pytest.mark.asyncio
async def test_client_successful_call_SSWS(monkeypatch):

    http_client = HTTPClient({
        'oauth': None,
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {
            "User-Agent": UserAgent().get_user_agent_string(),
            "Authorization": f"SSWS {API_TOKEN}"
        }
    })

    monkeypatch.setattr(HTTPClient, 'send_request', mock_return)

    req, res_details, res_json, error = await http_client.send_request({
        'method': 'GET',
        'url': ORG_URL + GET_USERS_CALL,  # Get all users in org
        'headers': {},
        'data': {}
    })

    assert error is None
    assert "User-Agent" in req.headers
    assert "Authorization" in req.headers
    assert req.headers["Authorization"].startswith("SSWS")
    assert res_details['Content-Type'] == "application/json"
    assert type(res_json) == list


@ pytest.mark.asyncio
async def test_client_error_call_SSWS(monkeypatch):

    http_client = HTTPClient({
        'oauth': None,
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {
            "User-Agent": UserAgent().get_user_agent_string(),
            "Authorization": "SSWS wrong_token"
        }
    })

    monkeypatch.setattr(HTTPClient, 'send_request', mock_return_error)

    req, res_details, res_json, error = await http_client.send_request({
        'method': 'GET',
        'url': ORG_URL + GET_USERS_CALL,  # Get all users in org
        'headers': {},
        'data': {}
    })

    assert error is not None
    assert req is None
    assert res_details is None
    assert res_json is None


@ pytest.mark.asyncio
async def test_client_invalid_url():
    http_client = HTTPClient({
        'oauth': None,
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {}
    })
    req, res_details, res_json, error = await http_client.send_request({
        'method': 'GET',
        'url': "",
        'headers': {},
        'data': {}
    })
    assert all(values in [None] for values in [req, res_details, res_json])
    assert issubclass(type(error), aiohttp.ClientError)
    assert type(error) == aiohttp.InvalidURL


@ pytest.mark.asyncio
async def test_client_invalid_HTTP_method(monkeypatch):
    http_client = HTTPClient({
        'oauth': None,
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {}
    })

    monkeypatch.setattr(HTTPClient, 'send_request', mock_invalid_HTTP_response)

    req, res_details, res_json, error = await http_client.send_request({
        'method': 'INVALID',
        'url': ORG_URL,
        'headers': {},
        'data': {}
    })
    assert all(values in [None] for values in [req, res_details, res_json])
    assert issubclass(type(error), aiohttp.ClientError)
    assert type(error) == aiohttp.ContentTypeError

    req, res_details, res_json, error = await http_client.send_request({
        'method': '',
        'url': ORG_URL,
        'headers': {},
        'data': {}
    })
    assert all(values in [None] for values in [req, res_details, res_json])
    assert issubclass(type(error), aiohttp.ClientError)
    assert type(error) == aiohttp.ContentTypeError


@ pytest.mark.asyncio
async def test_client_user_agent(monkeypatch):
    req_exec = RequestExecutor({
        "client": {
            "authorizationMode": 'SSWS',
            "token": 'token',
            "userAgent": ''
        }
    }, NoOpCache(), None)

    assert 'User-Agent' in req_exec._http_client._default_headers
    assert req_exec._http_client._default_headers["User-Agent"] == UserAgent(
    ).get_user_agent_string()

    # mock and shoot request
    monkeypatch.setattr(HTTPClient, 'send_request', mock_return)

    req, res_details, res_json, error = await req_exec._http_client.\
        send_request({
            'method': 'GET',
            'url': ORG_URL + GET_USERS_CALL,
            'headers': {'Authorization': f"SSWS {API_TOKEN}"},
            'data': {}
        })
    assert error is None
    assert 'User-Agent' in req.headers
    assert req_exec._http_client._default_headers["User-Agent"] == \
        req.headers["User-Agent"]

    # with extra user agent string
    extra = "testing"
    req_exec = RequestExecutor({
        "client": {
            "authorizationMode": 'SSWS',
            "token": 'token',
            "userAgent": extra
        }
    }, NoOpCache(), None)
    assert 'User-Agent' in req_exec._http_client._default_headers
    assert req_exec._http_client._default_headers["User-Agent"] == \
        UserAgent(extra).get_user_agent_string()


@ pytest.mark.asyncio
async def test_client_timeout(monkeypatch):
    http_client = HTTPClient({
        'oauth': None,
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {}
    })

    # mock and shoot request
    monkeypatch.setattr(HTTPClient, 'send_request', mock_timeout_response)

    req, res_details, res_json, error = await http_client.send_request({
        'method': 'INVALID',
        'url': ORG_URL,
        'headers': {},
        'data': {}
    })

    assert all(values in [None] for values in [req, res_details, res_json])
    assert type(error) == asyncio.exceptions.TimeoutError