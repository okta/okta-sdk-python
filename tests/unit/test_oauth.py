from okta.jwt import JWT
import tests.mocks as mocks
import os
import pytest
from unittest.mock import AsyncMock, MagicMock
from okta.oauth import OAuth

"""
Testing Private Key Inputs
"""


@pytest.mark.parametrize("jwk_input",
                          [mocks.SAMPLE_JWK, str(mocks.SAMPLE_JWK), mocks.SAMPLE_JWK_WITH_KID])
def test_private_key_PEM_JWK_dict(jwk_input):
    generated_pem, generated_jwk = JWT.get_PEM_JWK(jwk_input)

    assert generated_pem is not None and generated_jwk is not None
    assert generated_jwk.has_private


def test_private_key_PEM_JWK_file(fs):
    file_path = os.path.join(os.path.dirname(
        __file__), "test.pem")
    fs.create_file(file_path, contents=mocks.SAMPLE_RSA)
    generated_pem, generated_jwk = JWT.get_PEM_JWK(file_path)

    assert generated_pem is not None and generated_jwk is not None
    assert generated_jwk.has_private


def test_private_key_PEM_JWK_explicit_string():
    generated_pem, generated_jwk = JWT.get_PEM_JWK(mocks.SAMPLE_RSA)

    assert generated_pem is not None and generated_jwk is not None
    assert generated_jwk.has_private


@pytest.mark.parametrize("private_key",
                          [mocks.SAMPLE_INVALID_JWK, str(mocks.SAMPLE_INVALID_JWK), mocks.SAMPLE_INVALID_RSA])
def test_invalid_private_key_PEM_JWK(private_key):
    with pytest.raises(ValueError):
        generated_pem, generated_jwk = JWT.get_PEM_JWK(private_key)


@pytest.mark.asyncio
async def test_get_access_token():
    mock_request_executor = MagicMock()
    mock_request_executor.create_request = AsyncMock(return_value=({"mock_request": "data"}, None))
    mock_response_details = MagicMock()
    mock_response_details.content_type = "application/json"
    mock_response_details.status = 200
    mock_request_executor.fire_request = AsyncMock(
        return_value=(None, mock_response_details, '{"access_token": "mock_token", "expires_in": 3600}', None))

    config = {
        "client": {
            "orgUrl": "https://example.okta.com",
            "clientId": "valid-client-id",
            "privateKey": mocks.SAMPLE_RSA,
            "scopes": ["scope1", "scope2"],
            "oauthTokenRenewalOffset": 5
        }
    }
    oauth = OAuth(mock_request_executor, config)
    token, error = await oauth.get_access_token()

    assert token == "mock_token"
    assert error is None


@pytest.mark.asyncio
async def test_clear_access_token():
    mock_request_executor = MagicMock()
    mock_request_executor._cache = MagicMock()
    mock_request_executor._default_headers = {}

    config = {
        "client": {
            "orgUrl": "https://example.okta.com",
            "clientId": "valid-client-id",
            "privateKey": "valid-private-key",
            "scopes": ["scope1", "scope2"],
            "oauthTokenRenewalOffset": 5
        }
    }
    oauth = OAuth(mock_request_executor, config)
    oauth._access_token = "mock_token"
    oauth._access_token_expiry_time = 1234567890

    oauth.clear_access_token()

    assert oauth._access_token is None
    assert oauth._access_token_expiry_time is None