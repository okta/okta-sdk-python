import pytest
from okta.config.config_validator import ConfigValidator

"""
Testing Config Validator
"""

def test_validate_config_valid():
    config = {
        "client": {
            "orgUrl": "https://example.okta.com",
            "authorizationMode": "PrivateKey",
            "clientId": "valid-client-id",
            "scopes": ["scope1", "scope2"],
            "privateKey": "valid-private-key",
            "oauthTokenRenewalOffset": 5
        },
        "testing": {
            "testingDisableHttpsCheck": False
        }
    }
    validator = ConfigValidator(config)
    assert validator.validate_config() is None

def test_validate_config_invalid_org_url():
    config = {
        "client": {
            "orgUrl": "http://example.okta.com",
            "authorizationMode": "PrivateKey",
            "clientId": "valid-client-id",
            "scopes": ["scope1", "scope2"],
            "privateKey": "valid-private-key",
            "oauthTokenRenewalOffset": 5
        },
        "testing": {
            "testingDisableHttpsCheck": False
        }
    }
    with pytest.raises(ValueError) as excinfo:
        ConfigValidator(config)
    assert "must start with 'https'." in str(excinfo.value)