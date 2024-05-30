from okta.client import Client as OktaClient
import logging
import pytest


@pytest.mark.parametrize('log_level', [logging.INFO, logging.ERROR, logging.WARNING, logging.DEBUG])
def test_client_log_level_set_correctly(log_level: int):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {
        'orgUrl': org_url,
        'token': token,
        'logging': {
            'enabled': True,
            'logLevel': log_level
        }
    }

    # Ensure no error is raised and logger is set to correct level
    _ = OktaClient(user_config=config)
    assert logging.getLogger('okta-sdk-python').getEffectiveLevel() == log_level


def test_client_log_level_set_correctly_default():
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {
        'orgUrl': org_url,
        'token': token,
        'logging': {
            'enabled': True
        }
    }

    # Ensure no error is raised and logger is set to correct level (INFO)
    _ = OktaClient(user_config=config)
    assert logging.getLogger('okta-sdk-python').getEffectiveLevel() == logging.INFO
