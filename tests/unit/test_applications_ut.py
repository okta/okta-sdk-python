import aiohttp
import asyncio
import json
import pytest
import okta.models as models

from okta.client import Client as OktaClient


@pytest.mark.asyncio
async def test_set_provisioning_connection(monkeypatch, mocker):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token}
    client = OktaClient(config)

    # mock http requests, verify if custom header is present in request
    class MockHTTPRequest():
        def __call__(self, **params):
            self.request_info = params
            self.headers = params['headers']
            self.url = params['url']
            self.content_type = 'application/json'
            self.links = ''
            self.text = MockHTTPRequest.mock_response_text
            self.status = 200
            return self

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        @staticmethod
        async def mock_response_text():
            return '[{"text": "mock response text"}]'

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp.ClientSession, 'request', mock_http_request)

    profile = models.ProvisioningConnectionProfile(
        {
            'authScheme': models.ProvisioningConnectionAuthScheme('TOKEN'),
            'token': 'TEST'
        }
    )
    provisioning_conn_req = models.ProvisioningConnectionRequest({'profile': profile})
    _ = await client.set_default_provisioning_connection_for_application('test_app_id', provisioning_conn_req, query_params={'activate': True})
    assert mock_http_request.request_info['url'].endswith('/apps/test_app_id/connections/default/?activate=True')
    data = mock_http_request.request_info['data']
    assert json.loads(data) == {"profile": {"authScheme": "TOKEN", "token": "TEST"}}


@pytest.mark.asyncio
async def test_list_features_for_application(monkeypatch, mocker):
    mocked_response = """[
        {
            "name": "USER_PROVISIONING",
            "status": "ENABLED",
            "description": "User provisioning settings from Okta to a downstream application",
            "capabilities": {
                "create": {
                    "lifecycleCreate": {
                        "status": "DISABLED"
                    }
                },
                "update": {
                    "profile": {
                        "status": "DISABLED"
                    },
                    "lifecycleDeactivate": {
                        "status": "DISABLED"
                    },
                    "password": {
                        "status": "DISABLED",
                        "seed": "RANDOM",
                        "change": "KEEP_EXISTING"
                    }
                }
            },
            "_links": {
                "self": {
                    "href": "https://${yourOktaDomain}/api/v1/apps/${applicationId}/features/USER_PROVISIONING",
                    "hints": {
                        "allow": [
                            "GET",
                            "PUT"
                        ]
                    }
                }
            }
        }
    ]"""

    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token}
    client = OktaClient(config)

    # mock http requests, verify if custom header is present in request
    class MockHTTPRequest():
        def __call__(self, **params):
            self.request_info = params
            self.headers = params['headers']
            self.url = params['url']
            self.content_type = 'application/json'
            self.links = ''
            self.text = MockHTTPRequest.mock_response_text
            self.status = 200
            return self

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        @staticmethod
        async def mock_response_text():
            return mocked_response

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp.ClientSession, 'request', mock_http_request)

    features, _, err = await client.list_features_for_application('test_app_id')
    assert isinstance(features[0], models.ApplicationFeature)
    assert features[0].name == 'USER_PROVISIONING'
    assert isinstance(features[0].capabilities, models.CapabilitiesObject)
    assert isinstance(features[0].capabilities.create, models.CapabilitiesCreateObject)
    assert isinstance(features[0].capabilities.update, models.CapabilitiesUpdateObject)
    assert isinstance(features[0].capabilities.update, models.CapabilitiesUpdateObject)
    assert isinstance(features[0].capabilities.update.password, models.PasswordSettingObject)
    assert isinstance(features[0].capabilities.update.password.change, models.ChangeEnum)
    assert isinstance(features[0].status, models.EnabledStatus)

@pytest.mark.asyncio
async def test_get_feature_for_application(monkeypatch, mocker):
    mocked_response = """{
        "name": "USER_PROVISIONING",
        "status": "ENABLED",
        "description": "User provisioning settings from Okta to a downstream application",
        "capabilities": {
            "create": {
                "lifecycleCreate": {
                    "status": "DISABLED"
                }
            },
            "update": {
                "profile": {
                    "status": "DISABLED"
                },
                "lifecycleDeactivate": {
                    "status": "DISABLED"
                },
                "password": {
                    "status": "DISABLED",
                    "seed": "RANDOM",
                    "change": "KEEP_EXISTING"
                }
            }
        },
        "_links": {
            "self": {
                "href": "https://${yourOktaDomain}/api/v1/apps/${applicationId}/features/USER_PROVISIONING",
                "hints": {
                    "allow": [
                        "GET",
                        "PUT"
                    ]
                }
            }
        }
    }"""

    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token}
    client = OktaClient(config)

    # mock http requests, verify if custom header is present in request
    class MockHTTPRequest():
        def __call__(self, **params):
            self.request_info = params
            self.headers = params['headers']
            self.url = params['url']
            self.content_type = 'application/json'
            self.links = ''
            self.text = MockHTTPRequest.mock_response_text
            self.status = 200
            return self

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        @staticmethod
        async def mock_response_text():
            return mocked_response

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp.ClientSession, 'request', mock_http_request)

    feature, _, err = await client.get_feature_for_application('test_app_id', 'USER_PROVISIONING')
    assert isinstance(feature, models.ApplicationFeature)
    assert feature.name == 'USER_PROVISIONING'
    assert isinstance(feature.capabilities, models.CapabilitiesObject)
    assert isinstance(feature.capabilities.create, models.CapabilitiesCreateObject)
    assert isinstance(feature.capabilities.update, models.CapabilitiesUpdateObject)
    assert isinstance(feature.capabilities.update, models.CapabilitiesUpdateObject)
    assert isinstance(feature.capabilities.update.password, models.PasswordSettingObject)
    assert isinstance(feature.capabilities.update.password.change, models.ChangeEnum)
    assert isinstance(feature.status, models.EnabledStatus)


@pytest.mark.asyncio
async def test_update_feature_for_application(monkeypatch, mocker):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token}
    client = OktaClient(config)

    # mock http requests, verify if custom header is present in request
    class MockHTTPRequest():
        def __call__(self, **params):
            self.request_info = params
            self.headers = params['headers']
            self.url = params['url']
            self.content_type = 'application/json'
            self.links = ''
            self.text = MockHTTPRequest.mock_response_text
            self.status = 200
            return self

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        @staticmethod
        async def mock_response_text():
            return '[{"text": "mock response text"}]'

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp.ClientSession, 'request', mock_http_request)

    capabilities_object_dict = {
        "create": {
            "lifecycleCreate": {
                "status": "ENABLED"
            }
        },
        "update": {
            "lifecycleDeactivate": {
                "status": "ENABLED"
            },
            "profile":{
                "status": "ENABLED"
            },
            "password":{
                "status": "ENABLED",
                "seed": "RANDOM",
                "change": "CHANGE"
            }
        }
    }
    capabilities_object = models.CapabilitiesObject(capabilities_object_dict)

    feature, _, err = await client.update_feature_for_application('test_app_id', 'test_name', capabilities_object)
    assert mock_http_request.request_info['url'].endswith('/apps/test_app_id/features/test_name')
    data = mock_http_request.request_info['data']
    assert json.loads(data) == capabilities_object_dict


@pytest.mark.asyncio
async def test_upload_application_logo(monkeypatch, mocker):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token}
    client = OktaClient(config)

    # mock http requests, verify if custom header is present in request
    class MockHTTPRequest():
        def __call__(self, **params):
            self.request_info = params
            self.headers = params['headers']
            self.url = params['url']
            self.content_type = 'application/json'
            self.links = ''
            self.text = MockHTTPRequest.mock_response_text
            self.status = 200
            return self

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        @staticmethod
        async def mock_response_text():
            return '[{"text": "mock response text"}]'

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp.ClientSession, 'request', mock_http_request)

    logo = mocker.Mock()

    _, err = await client.upload_application_logo('test_app_id', logo)

    assert mock_http_request.request_info['url'].endswith('/apps/test_app_id/logo')
    data = mock_http_request.request_info['data']
    assert data == {'file': logo}
