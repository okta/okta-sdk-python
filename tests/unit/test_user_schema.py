import aiohttp
import json
import pytest
from okta.client import Client as OktaClient
from okta.models import UserSchema


MOCK_RESPONSE = """{
    "id": "https://${yourOktaDomain}/meta/schemas/apps/0oa25gejWwdXNnFH90g4/default",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "name": "Example App",
    "title": "Example App User",
    "lastUpdated": "2017-07-18T23:18:43.000Z",
    "created": "2017-07-18T22:35:30.000Z",
    "definitions": {
    "base": {
      "id": "#base",
      "type": "object",
      "properties": {
        "login": {
          "title": "Username",
          "type": "string",
          "required": true,
          "scope": "NONE",
          "minLength": 5,
          "maxLength": 100
        }
      },
      "required": [
        "login"
      ]
    },
    "custom": {
      "id": "#custom",
      "type": "object",
      "properties": {
      },
      "required": []
    }
    },
    "type": "object",
    "properties": {
    "profile": {
      "allOf": [
        {
          "$ref": "#/definitions/base"
        },
        {
          "$ref": "#/definitions/custom"
        }
      ]
    }
    }
    }"""


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
        return MOCK_RESPONSE


class TestUserSchemaResource:
    """
    Unit Tests for the User Schema Resource
    """

    @pytest.mark.asyncio
    async def test_get_application_user_schema(self, monkeypatch):
        mock_http_request = MockHTTPRequest()
        monkeypatch.setattr(aiohttp, 'request', mock_http_request)

        org_url = "https://test.okta.com"
        token = "TOKEN"
        config = {'orgUrl': org_url, 'token': token}
        client = OktaClient(config)

        resp, _, err = await client.get_application_user_schema('0oa25gejWwdXNnFH90g4')
        assert err is None
        assert isinstance(resp, UserSchema)
        assert resp.schema == 'http://json-schema.org/draft-04/schema#'
        assert resp.name == 'Example App'
        assert resp.title == 'Example App User'
        assert resp.type == 'object'
        assert resp.definitions.base.id == '#base'
        assert resp.definitions.base.type == 'object'
        assert resp.definitions.base.properties.login.title == 'Username'
        assert resp.definitions.base.properties.login.type == 'string'
        assert resp.definitions.base.properties.login.required
        assert resp.definitions.base.properties.login.scope == 'NONE'
        assert resp.definitions.base.properties.login.min_length == 5
        assert resp.definitions.base.properties.login.max_length == 100
        assert 'login' in resp.definitions.base.required

    @pytest.mark.asyncio
    async def test_update_application_user_profile(self, monkeypatch):
        mock_http_request = MockHTTPRequest()
        monkeypatch.setattr(aiohttp, 'request', mock_http_request)

        org_url = "https://test.okta.com"
        token = "TOKEN"
        config = {'orgUrl': org_url, 'token': token}
        client = OktaClient(config)

        schema = UserSchema(json.loads(MOCK_RESPONSE))
        resp, _, err = await client.update_application_user_profile('0oa25gejWwdXNnFH90g4', schema)
        assert err is None
        assert isinstance(resp, UserSchema)
        assert resp.schema == 'http://json-schema.org/draft-04/schema#'
        assert resp.name == 'Example App'
        assert resp.title == 'Example App User'
        assert resp.type == 'object'
        assert resp.definitions.base.id == '#base'
        assert resp.definitions.base.type == 'object'
        assert resp.definitions.base.properties.login.title == 'Username'
        assert resp.definitions.base.properties.login.type == 'string'
        assert resp.definitions.base.properties.login.required
        assert resp.definitions.base.properties.login.scope == 'NONE'
        assert resp.definitions.base.properties.login.min_length == 5
        assert resp.definitions.base.properties.login.max_length == 100
        assert 'login' in resp.definitions.base.required
