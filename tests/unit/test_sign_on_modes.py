import asyncio
import copy

from okta.client import Client
from okta.models import Application, SamlApplication, ApplicationSignOnMode
from okta.request_executor import RequestExecutor


SAML_APP_RESP_DICT = {
    "id": "test_id",
    "name": "test_org_custom_saml_app",
    "label": "Custom Saml 2.0 App",
    "status": "ACTIVE",
    "lastUpdated": "2021-02-10T14:21:41.000Z",
    "created": "2021-02-10T14:21:41.000Z",
    "accessibility": {
        "selfService": False,
        "errorRedirectUrl": None,
        "loginRedirectUrl": None,
    },
    "visibility": {
        "autoSubmitToolbar": False,
        "hide": {"iOS": False, "web": False},
        "appLinks": {"test_org_custom_saml_app_link": True},
    },
    "features": [],
    "signOnMode": "SAML_2_0",
    "credentials": {
        "userNameTemplate": {
            "template": '${fn:substringBefore(source.login, "@")}',
            "type": "BUILT_IN",
        },
        "signing": {"kid": "test_kid"},
    },
    "settings": {
        "app": {},
        "notifications": {
            "vpn": {
                "network": {"connection": "DISABLED"},
                "message": None,
                "helpUrl": None,
            }
        },
        "signOn": {
            "defaultRelayState": "",
            "ssoAcsUrl": "http://example.okta.com",
            "idpIssuer": "http://www.okta.com/${org.externalKey}",
            "audience": "https://example.com/tenant/123",
            "recipient": "http://recipient.okta.com",
            "destination": "http://destination.okta.com",
            "subjectNameIdTemplate": "${user.userName}",
            "subjectNameIdFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
            "responseSigned": True,
            "assertionSigned": True,
            "signatureAlgorithm": "RSA_SHA256",
            "digestAlgorithm": "SHA256",
            "honorForceAuthn": True,
            "authnContextClassRef": "urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport",
            "spIssuer": None,
            "requestCompressed": False,
            "attributeStatements": [],
            "allowMultipleAcsEndpoints": False,
            "acsEndpoints": [],
            "slo": {"enabled": False},
        },
    },
    "_links": {
        "help": {"href": "https://test_help_link", "type": "text/html"},
        "metadata": {
            "href": "https://test_metadata_link",
            "type": "application/xml",
        },
        "appLinks": [
            {
                "name": "test_app_link",
                "href": "https://test_app_link",
                "type": "text/html",
            }
        ],
        "groups": {"href": "https://test_groups_link"},
        "logo": [
            {
                "name": "medium",
                "href": "https://test_logo_link",
                "type": "image/png",
            }
        ],
        "users": {"href": "https://test_users_link"},
        "deactivate": {"href": "https://test_deactivate_link"},
    },
}


EXPECTED_SAML_APP_AS_DICT = {
    "_links": {
        "help": {"href": "https://test_help_link", "type": "text/html"},
        "metadata": {
            "href": "https://test_metadata_link",
            "type": "application/xml",
        },
        "appLinks": [
            {
                "name": "test_app_link",
                "href": "https://test_app_link",
                "type": "text/html",
            }
        ],
        "groups": {"href": "https://test_groups_link"},
        "logo": [
            {
                "name": "medium",
                "href": "https://test_logo_link",
                "type": "image/png",
            }
        ],
        "users": {"href": "https://test_users_link"},
        "deactivate": {"href": "https://test_deactivate_link"},
    },
    "accessibility": {"selfService": False},
    "created": "2021-02-10T14:21:41.000Z",
    "credentials": {
        "signing": {"kid": "test_kid"},
        "userNameTemplate": {
            "template": '${fn:substringBefore(source.login, "@")}',
            "type": "BUILT_IN",
        },
    },
    "features": [],
    "id": "test_id",
    "label": "Custom Saml 2.0 App",
    "lastUpdated": "2021-02-10T14:21:41.000Z",
    "name": "test_org_custom_saml_app",
    "settings": {
        "app": {},
        "notifications": {
            "vpn": {"network": {"connection": "DISABLED", "exclude": [], "include": []}}
        },
        "signOn": {
            "acsEndpoints": [],
            "allowMultipleAcsEndpoints": False,
            "assertionSigned": True,
            "attributeStatements": [],
            "audience": "https://example.com/tenant/123",
            "authnContextClassRef": "urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport",
            "defaultRelayState": "",
            "destination": "http://destination.okta.com",
            "digestAlgorithm": "SHA256",
            "honorForceAuthn": True,
            "idpIssuer": "http://www.okta.com/${org.externalKey}",
            "inlineHooks": [],
            "recipient": "http://recipient.okta.com",
            "requestCompressed": False,
            "responseSigned": True,
            "signatureAlgorithm": "RSA_SHA256",
            "slo": {"enabled": False},
            "ssoAcsUrl": "http://example.okta.com",
            "subjectNameIdFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
            "subjectNameIdTemplate": "${user.userName}",
        },
    },
    "signOnMode": ApplicationSignOnMode('SAML_2_0'),
    "status": "ACTIVE",
    "visibility": {
        "appLinks": {"testOrgCustomSamlAppLink": True},
        "autoSubmitToolbar": False,
        "hide": {"iOS": False, "web": False},
    },
}


class MockResponseObj:
    def __init__(self, response):
        self.response = response

    def get_body(self):
        return self.response


class MockRequestExecutor(RequestExecutor):
    async def execute(self, *args, **kwargs):
        return self.response, None

    def set_response(self, response):
        self.response = MockResponseObj(response)


def test_known_sign_on_mode():
    response = copy.deepcopy(SAML_APP_RESP_DICT)

    config = {
        "orgUrl": "https://test_org.okta.com",
        "token": "test_token",
        "requestExecutor": MockRequestExecutor,
    }
    client = Client(config)

    # check list applications
    client._request_executor.set_response([response])
    event_loop = asyncio.get_event_loop()
    result, resp, err = event_loop.run_until_complete(client.list_applications())
    assert type(result[0]) == SamlApplication
    assert result[0].as_dict() == EXPECTED_SAML_APP_AS_DICT

    # check get application
    client._request_executor.set_response(response)
    event_loop = asyncio.get_event_loop()
    result, resp, err = event_loop.run_until_complete(client.get_application("test_id"))
    assert type(result) == SamlApplication
    assert result.as_dict() == EXPECTED_SAML_APP_AS_DICT


def test_unknown_sign_on_mode():
    response = copy.deepcopy(SAML_APP_RESP_DICT)
    response["signOnMode"] = "UNKNOWN_SIGN_ON_MODE"
    expected = copy.deepcopy(EXPECTED_SAML_APP_AS_DICT)
    expected["signOnMode"] = ApplicationSignOnMode("UNKNOWN_SIGN_ON_MODE")
    expected["settings"] = {
        "app": {},
        "notifications": {
            "vpn": {"network": {"connection": "DISABLED", "exclude": [], "include": []}}
        },
    }

    config = {
        "orgUrl": "https://test_org.okta.com",
        "token": "test_token",
        "requestExecutor": MockRequestExecutor,
    }
    client = Client(config)

    # check list applications
    client._request_executor.set_response([response])
    event_loop = asyncio.get_event_loop()
    result, resp, err = event_loop.run_until_complete(client.list_applications())
    # verify if result fallbacks to generic Application
    assert type(result[0]) != SamlApplication
    assert type(result[0]) == Application
    assert result[0].as_dict() == expected

    # check get application
    client._request_executor.set_response(response)
    event_loop = asyncio.get_event_loop()
    result, resp, err = event_loop.run_until_complete(client.get_application("test_id"))
    # verify if result fallbacks to generic Application
    assert type(result) != SamlApplication
    assert type(result) == Application
    assert result.as_dict() == expected


def test_no_sign_on_mode():
    response = copy.deepcopy(SAML_APP_RESP_DICT)
    response["signOnMode"] = None
    expected = copy.deepcopy(EXPECTED_SAML_APP_AS_DICT)
    expected.pop("signOnMode")
    expected["settings"] = {
        "app": {},
        "notifications": {
            "vpn": {"network": {"connection": "DISABLED", "exclude": [], "include": []}}
        },
    }

    config = {
        "orgUrl": "https://test_org.okta.com",
        "token": "test_token",
        "requestExecutor": MockRequestExecutor,
    }
    client = Client(config)

    # check list applications
    client._request_executor.set_response([response])
    event_loop = asyncio.get_event_loop()
    result, resp, err = event_loop.run_until_complete(client.list_applications())
    assert type(result[0]) != SamlApplication
    assert type(result[0]) == Application
    assert result[0].as_dict() == expected

    # check get application
    client._request_executor.set_response(response)
    event_loop = asyncio.get_event_loop()
    result, resp, err = event_loop.run_until_complete(client.get_application("test_id"))
    assert type(result) != SamlApplication
    assert type(result) == Application
    assert result.as_dict() == expected
