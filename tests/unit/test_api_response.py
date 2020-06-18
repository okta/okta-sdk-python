import tests.mocks as mocks
import pytest
from okta.client import Client
from okta.request_executor import RequestExecutor

REQUEST_TIMEOUT = mocks.REQUEST_TIMEOUT
ORG_URL = mocks.ORG_URL
API_TOKEN = mocks.API_TOKEN
CLIENT_ID = mocks.CLIENT_ID
SCOPES = mocks.SCOPES
PRIVATE_KEY = mocks.PRIVATE_KEY
GET_USERS_CALL = mocks.GET_USERS_CALL
API_LIMIT = "?limit=1"


@ pytest.mark.asyncio
async def test_response_pagination_with_next(monkeypatch):
    ssws_client = Client({
        "orgUrl": ORG_URL,
        "token": API_TOKEN
    })

    req, error = await ssws_client.get_request_executor()\
        .create_request("GET",
                        GET_USERS_CALL + API_LIMIT,
                        {},
                        {})

    monkeypatch.setattr(RequestExecutor, 'fire_request',
                        mocks.mock_GET_HTTP_Client_response_valid_with_next)

    result, error = await ssws_client.get_request_executor().execute(req)

    assert result.get_body() is not None
    assert result.has_next()
    monkeypatch.setattr(RequestExecutor, 'fire_request',
                        mocks.mock_GET_HTTP_Client_response_valid)
    assert await result.next() is not None
    assert not result.has_next()
    with pytest.raises(StopAsyncIteration):
        await result.next()


@ pytest.mark.asyncio
async def test_response_pagination_with_no_next(monkeypatch):
    ssws_client = Client({
        "orgUrl": ORG_URL,
        "token": API_TOKEN
    })

    req, error = await ssws_client.get_request_executor()\
        .create_request("GET",
                        GET_USERS_CALL + API_LIMIT,
                        {},
                        {})

    monkeypatch.setattr(RequestExecutor, 'fire_request',
                        mocks.mock_GET_HTTP_Client_response_valid)

    result, error = await ssws_client.get_request_executor().execute(req)

    assert result.get_body() is not None
    assert not result.has_next()
    with pytest.raises(StopAsyncIteration):
        await result.next()
