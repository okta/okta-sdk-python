from okta.jwt import JWT
import tests.mocks as mocks
import os
import pytest

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
