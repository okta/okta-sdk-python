from okta.http_client import HTTPClient
from okta.request_executor import RequestExecutor
from okta.cache.no_op_cache import NoOpCache
from okta.user_agent import UserAgent
from okta.client import Client
from okta.oauth import OAuth
from okta.errors.http_error import HTTPError
import tests.mocks as mocks
import pytest
import aiohttp
import asyncio

REQUEST_TIMEOUT = mocks.REQUEST_TIMEOUT
ORG_URL = mocks.ORG_URL
API_TOKEN = mocks.API_TOKEN
CLIENT_ID = mocks.CLIENT_ID
SCOPES = mocks.SCOPES
PRIVATE_KEY = mocks.PRIVATE_KEY
GET_USERS_CALL = mocks.GET_USERS_CALL


@pytest.mark.vcr()
@ pytest.mark.asyncio
async def test_client_success_call_SSWS(fs):
    ssws_client = mocks.MockOktaClient(fs)

    req, error = await ssws_client.get_request_executor()\
        .create_request("GET",
                        GET_USERS_CALL,
                        {},
                        {})

    req, res_details, resp_body, error = await ssws_client\
        .get_request_executor().fire_request(req)

    assert error is None
    assert "User-Agent" in req["headers"]
    assert "Authorization" in req["headers"]
    assert req["headers"]["Authorization"].startswith("SSWS")
    assert res_details.status == 200
    assert "application/json" in res_details.headers["Content-Type"]
    assert resp_body is not None


@ pytest.mark.vcr()
@ pytest.mark.asyncio
async def test_client_error_call_SSWS(fs):
    ssws_client = Client({
        "orgUrl": ORG_URL,
        "token": API_TOKEN + "wrong token"
    })

    req, error = await ssws_client.get_request_executor()\
        .create_request("GET",
                        GET_USERS_CALL,
                        {},
                        {})

    req, res_details, resp_body, error = await ssws_client\
        .get_request_executor().fire_request(req)

    parsed, error = HTTPClient.check_response_for_error(
        req["url"], res_details, resp_body)

    assert parsed is None
    assert res_details.status == 404
    assert isinstance(error, HTTPError)
    assert error.message.startswith("HTTP 404")


@pytest.mark.vcr()
@pytest.mark.asyncio
async def test_client_success_call_oauth(fs, monkeypatch):
    oauth_client = Client({
        "orgUrl": ORG_URL,
        "authorizationMode": "PrivateKey",
        "clientId": CLIENT_ID,
        "scopes": SCOPES,
        "privateKey": PRIVATE_KEY
    })

    request_executor = oauth_client.get_request_executor()

    monkeypatch.setattr(OAuth, 'get_access_token', mocks.mock_access_token)
    req, err = await request_executor.create_request(
        "GET",
        GET_USERS_CALL,
        {},
        {})

    req, res_details, resp_body, error = await oauth_client\
        .get_request_executor().fire_request(req)

    assert error is None
    assert "User-Agent" in req["headers"]
    assert "Authorization" in req["headers"]
    assert req["headers"]["Authorization"].startswith("Bearer")
    assert res_details.status == 200
    assert "application/json" in res_details.headers["Content-Type"]
    assert resp_body is not None


@pytest.mark.vcr()
@ pytest.mark.asyncio
async def test_client_error_call_oauth(fs, monkeypatch):
    oauth_client = Client({
        "orgUrl": ORG_URL,
        "authorizationMode": "PrivateKey",
        "clientId": CLIENT_ID,
        "scopes": SCOPES,
        "privateKey": PRIVATE_KEY + "Wrong one"
    })

    monkeypatch.setattr(OAuth, 'get_access_token', mocks.mock_access_token)

    req, err = await oauth_client.get_request_executor()\
        .create_request("GET",
                        GET_USERS_CALL,
                        {},
                        {})

    req, res_details, resp_body, error = await oauth_client\
        .get_request_executor().fire_request(req)

    parsed, error = HTTPClient.check_response_for_error(
        req["url"], res_details, resp_body)

    assert parsed is None
    assert res_details.status == 404
    assert isinstance(error, HTTPError)
    assert error.message.startswith("HTTP 404")


@ pytest.mark.asyncio
async def test_client_invalid_url():
    http_client = HTTPClient({
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {}
    })
    req, res_details, resp_body, error = await http_client.send_request({
        'method': 'GET',
        'url': "",
        'headers': {},
        'data': {}
    })
    assert all(values in [None] for values in [req, res_details, resp_body])
    assert issubclass(type(error), aiohttp.ClientError)
    assert type(error) == aiohttp.InvalidURL


@ pytest.mark.asyncio
async def test_client_invalid_HTTP_method(monkeypatch):
    http_client = HTTPClient({
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {}
    })

    monkeypatch.setattr(HTTPClient, 'send_request',
                        mocks.mock_invalid_HTTP_response)

    req, res_details, resp_body, error = await http_client.send_request({
        'method': 'INVALID',
        'url': ORG_URL,
        'headers': {},
        'data': {}
    })
    assert all(values in [None] for values in [req, res_details, resp_body])
    assert issubclass(type(error), aiohttp.ClientError)
    assert type(error) == aiohttp.ContentTypeError

    req, res_details, resp_body, error = await http_client.send_request({
        'method': '',
        'url': ORG_URL,
        'headers': {},
        'data': {}
    })
    assert all(values in [None] for values in [req, res_details, resp_body])
    assert issubclass(type(error), aiohttp.ClientError)
    assert type(error) == aiohttp.ContentTypeError


@ pytest.mark.asyncio
async def test_client_user_agent(monkeypatch):
    req_exec = RequestExecutor({
        "client": {
            "orgUrl": "https://test.okta.com",
            "authorizationMode": 'SSWS',
            "token": 'token',
            "userAgent": '',
            "rateLimit": {
                "maxRetries": 2
            }
        }
    }, NoOpCache(), None)

    assert 'User-Agent' in req_exec._http_client._default_headers
    assert req_exec._http_client._default_headers["User-Agent"] == UserAgent(
    ).get_user_agent_string()

    # mock and shoot request
    monkeypatch.setattr(HTTPClient, 'send_request',
                        mocks.mock_GET_HTTP_Client_response_valid)

    req, res_details, resp_body, error = await req_exec._http_client.\
        send_request({
            'method': 'GET',
            'url': ORG_URL + GET_USERS_CALL,
            'headers': {'Authorization': f"SSWS {API_TOKEN}"},
            'data': {}
        })
    assert error is None
    assert 'User-Agent' in req["headers"]
    assert req_exec._http_client._default_headers["User-Agent"] == \
        req["headers"]["User-Agent"]

    # with extra user agent string
    extra = "testing"
    req_exec = RequestExecutor({
        "client": {
            "orgUrl": "https://test.okta.com",
            "authorizationMode": 'SSWS',
            "token": 'token',
            "userAgent": extra,
            "rateLimit": {
                "maxRetries": 2
            }
        }
    }, NoOpCache(), None)
    assert 'User-Agent' in req_exec._http_client._default_headers
    assert req_exec._http_client._default_headers["User-Agent"] == \
        UserAgent(extra).get_user_agent_string()


@ pytest.mark.asyncio
async def test_client_timeout(monkeypatch):
    http_client = HTTPClient({
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {}
    })

    # mock and shoot request
    monkeypatch.setattr(HTTPClient, 'send_request',
                        mocks.mock_timeout_response)

    req, res_details, resp_body, error = await http_client.send_request({
        'method': 'INVALID',
        'url': ORG_URL,
        'headers': {},
        'data': {}
    })

    assert all(values in [None] for values in [req, res_details, resp_body])
    assert type(error) == asyncio.TimeoutError
