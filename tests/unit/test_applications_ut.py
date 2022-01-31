import aiohttp
import asyncio
import json
import okta.models as models

from okta.client import Client as OktaClient


def test_set_provisioning_connection(monkeypatch, mocker):
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
    asyncio.run(client.set_default_provisioning_connection_for_application('test_app_id', provisioning_conn_req, query_params={'activate': True}))
    data = mock_http_request.request_info['data']
    assert json.loads(data) == {"profile": {"authScheme": "TOKEN", "token": "TEST"}}
