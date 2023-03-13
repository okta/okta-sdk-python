import asyncio
import logging
import tests.mocks as mocks
import pytest
import datetime as dt
from http import HTTPStatus
from okta.client import Client
from okta.errors.http_error import HTTPError
from okta.utils import convert_date_time_to_seconds
from okta.http_client import HTTPClient
from okta.request_executor import RequestExecutor
from okta.error_messages import ERROR_MESSAGE_429_MISSING_DATE_X_RESET

REQUEST_TIMEOUT = mocks.REQUEST_TIMEOUT
ORG_URL = mocks.ORG_URL
API_TOKEN = mocks.API_TOKEN
CLIENT_ID = mocks.CLIENT_ID
SCOPES = mocks.SCOPES
PRIVATE_KEY = mocks.PRIVATE_KEY
GET_USERS_CALL = mocks.GET_USERS_CALL

CLIENT_CONFIG = {'orgUrl': ORG_URL, 'token': API_TOKEN}


@pytest.mark.asyncio
async def test_max_retries_no_timeout(monkeypatch, mocker):
    client = Client(user_config=CLIENT_CONFIG)
    query_params = {"limit": "1"}

    monkeypatch.setattr(HTTPClient, 'send_request',
                        mocks.mock_GET_HTTP_Client_response_429)

    http_spy = mocker.spy(HTTPClient, 'send_request')
    sleep_spy = mocker.spy(asyncio, 'sleep')

    users, resp, error = await client.list_users(query_params)

    http_spy.assert_called()
    assert http_spy.call_count ==\
        client.get_request_executor()._max_retries + 1
    sleep_spy.assert_called()
    assert client.get_request_executor()._request_timeout == 0
    assert isinstance(error, HTTPError)
    assert error is not None
    assert error.status == HTTPStatus.TOO_MANY_REQUESTS
    assert resp.get_status() == HTTPStatus.TOO_MANY_REQUESTS


@pytest.mark.asyncio
async def test_backoff_calculation():
    client = Client(user_config=CLIENT_CONFIG)

    response_429 = (await mocks.mock_GET_HTTP_Client_response_429())[1]
    # ^ has a 1 second difference in retry and datetime
    # backoff should be 2 by Okta standards

    retry_limit_reset = float(response_429.headers["X-Rate-Limit-Reset"])
    date_time = convert_date_time_to_seconds(response_429.headers["Date"])

    backoff_time = client.get_request_executor(
    ).calculate_backoff(retry_limit_reset, date_time)

    assert (backoff_time == 2)


@pytest.mark.asyncio
async def test_no_x_date_header(monkeypatch):
    client = Client(user_config=CLIENT_CONFIG)

    monkeypatch.setattr(HTTPClient, 'send_request',
                        mocks.mock_GET_HTTP_Client_response_429_no_x_reset)

    users, resp, error = await client.list_users()

    assert error is not None
    assert isinstance(error, Exception)
    assert error.args[0] == ERROR_MESSAGE_429_MISSING_DATE_X_RESET
    assert users is None
    assert resp is None


@pytest.mark.asyncio
async def test_no_x_reset_header(monkeypatch):
    client = Client(user_config=CLIENT_CONFIG)

    monkeypatch.setattr(HTTPClient, 'send_request',
                        mocks.mock_GET_HTTP_Client_response_429_no_x_reset)

    users, resp, error = await client.list_users()

    assert error is not None
    assert isinstance(error, Exception)
    assert error.args[0] == ERROR_MESSAGE_429_MISSING_DATE_X_RESET
    assert users is None
    assert resp is None


@pytest.mark.asyncio
async def test_multiple_x_reset_headers(monkeypatch, mocker):
    client = Client(user_config=CLIENT_CONFIG)

    backoff_spy = mocker.spy(RequestExecutor, 'calculate_backoff')

    monkeypatch.setattr(HTTPClient, 'send_request',
                        mocks.mock_GET_HTTP_Client_response_429_multi_x_reset)
    # the X Rate Limit Resets used are 1 sec and 2 sec after the Date header,
    # -> the min. one should be used (1 sec. after) and the backoff calculated
    #    should be equal to 2 (by Okta standards)

    users, resp, error = await client.list_users()

    assert error is not None
    assert users is None
    assert backoff_spy.spy_return == 2


@pytest.mark.asyncio
async def test_req_timeout(monkeypatch):
    this_config = CLIENT_CONFIG.copy()
    this_config.update({"requestTimeout": 1})
    client = Client(user_config=this_config)

    request = await mocks.mock_GET_HTTP_request()

    monkeypatch.setattr(HTTPClient, 'send_request',
                        mocks.mock_GET_HTTP_Client_response_429)

    now = dt.datetime.now(dt.timezone.utc)
    now = now.replace(microsecond=0)
    two_sec_before = (now - dt.timedelta(seconds=2)).timestamp()

    a, b, c, error = await client.get_request_executor(
    ).fire_request_helper(request, 0, two_sec_before)

    assert isinstance(error, Exception)
    assert "Request Timeout exceeded." == error.args[0]


@pytest.mark.asyncio
async def test_concurrent_rate_limit_headers(monkeypatch, mocker):
    client = Client(user_config=CLIENT_CONFIG)
    logger = logging.getLogger('okta-sdk-python')
    logger_spy = mocker.spy(logger, 'warning')

    # response should have following headers set to 0 to indicate concurrent rate limit error
    # X-Rate-Limit-Limit, X-Rate-Limit-Remaining
    response_429 = (await mocks.mock_GET_HTTP_Client_response_429_concurrent_limit_error())[1]

    retry_limit_limit = float(response_429.headers["X-Rate-Limit-Limit"])
    retry_limit_remaining = float(response_429.headers["X-Rate-Limit-Remaining"])

    assert retry_limit_limit == 0
    assert retry_limit_remaining == 0

    request = await mocks.mock_GET_HTTP_request()

    monkeypatch.setattr(HTTPClient, 'send_request',
                        mocks.mock_GET_HTTP_Client_response_429_concurrent_limit_error)

    now = dt.datetime.now(dt.timezone.utc)
    now = now.replace(microsecond=0)
    two_sec_before = (now - dt.timedelta(seconds=1)).timestamp()

    _ = await client.get_request_executor(
    ).fire_request_helper(request, 0, two_sec_before)

    logger_spy.assert_called()
    logger_spy.assert_called_with('Concurrent limit rate exceeded')
