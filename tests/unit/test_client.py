from okta import client
import pytest
import constants as const


class TestOktaClient():
    ERROR_MESSAGE_ORG_URL_MISSING = ("Your Okta URL is missing. You can copy "
                                     "your domain from the Okta Developer "
                                     "Console. Follow these instructions to"
                                     f" find it: {const.FINDING_OKTA_DOMAIN}")
    ERROR_MESSAGE_ORG_URL_NOT_HTTPS = (
        "Your Okta URL must start with 'https'.")
    ERROR_MESSAGE_AUTH_MODE_INVALID = ("The AuthorizationMode configuration "
                                       "option must be one of: "
                                       "[SSWS, PrivateKey]. "
                                       "You provided the SDK with ")

    def test_constructor_no_config_at_all(self):
        config = {}
        with pytest.raises(ValueError) as exception_info:
            client.Client(input_config=config)
            assert TestOktaClient.ERROR_MESSAGE_ORG_URL_MISSING in\
                exception_info.value
            assert TestOktaClient.ERROR_MESSAGE_ORG_URL_NOT_HTTPS in\
                exception_info.value
            assert TestOktaClient.ERROR_MESSAGE_AUTH_MODE_INVALID in\
                exception_info.value

    def test_constructor_user_config_SSWS(self):
        pass

    def test_constructor_user_config_PK(self):
        pass

    def test_constructor_global_config_SSWS(self):
        pass

    def test_constructor_global_config_PK(self):
        pass

    def test_constructor_local_config_SSWS(self):
        pass

    def test_constructor_local_config_PK(self):
        pass
