from okta.jwt import JWT
import tests.mocks as mocks

"""
Testing JWT functions with different inputs
"""


def test_private_key_with_kid_in_private_key(mocker):
    mocked_encode = mocker.patch('jose.jwt.encode')
    JWT.create_token("test.com", "test-client-id", mocks.SAMPLE_JWK_WITH_KID)
    expected_kid = mocks.SAMPLE_JWK_WITH_KID["kid"]
    _, kwargs = mocked_encode.call_args
    mocked_encode.assert_called_once()
    assert "kid" in kwargs["headers"]
    assert kwargs["headers"]["kid"] == expected_kid


def test_private_key_with_kid_in_config(mocker):
    mocked_encode = mocker.patch('jose.jwt.encode')
    expected_kid = "test-kid"
    JWT.create_token("test.com", "test-client-id", mocks.SAMPLE_JWK, kid=expected_kid)
    _, kwargs = mocked_encode.call_args
    mocked_encode.assert_called_once()
    assert "kid" in kwargs["headers"]
    assert kwargs["headers"]["kid"] == expected_kid
