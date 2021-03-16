import aiohttp
import asyncio
import logging
from aiohttp.client_reqrep import ConnectionKey
from ssl import SSLCertVerificationError

from okta.client import Client as OktaClient
import pytest
from okta.constants import FINDING_OKTA_DOMAIN
import yaml
import os
from okta.error_messages import ERROR_MESSAGE_API_TOKEN_DEFAULT, \
    ERROR_MESSAGE_API_TOKEN_MISSING, ERROR_MESSAGE_AUTH_MODE_INVALID, \
    ERROR_MESSAGE_CLIENT_ID_DEFAULT, ERROR_MESSAGE_CLIENT_ID_MISSING,\
    ERROR_MESSAGE_ORG_URL_ADMIN, ERROR_MESSAGE_ORG_URL_MISSING, \
    ERROR_MESSAGE_ORG_URL_NOT_HTTPS, ERROR_MESSAGE_ORG_URL_TYPO, \
    ERROR_MESSAGE_ORG_URL_YOUROKTADOMAIN, ERROR_MESSAGE_SCOPES_PK_MISSING, \
    ERROR_MESSAGE_PROXY_MISSING_HOST, ERROR_MESSAGE_PROXY_MISSING_AUTH, \
    ERROR_MESSAGE_PROXY_INVALID_PORT
from okta.constants import _GLOBAL_YAML_PATH, _LOCAL_YAML_PATH
from okta.exceptions import HTTPException
from okta.http_client import HTTPClient


"""
Testing Okta Client Instantiation in different scenarios
"""


def test_constructor_user_config_empty(fs):
    config = {}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert ERROR_MESSAGE_ORG_URL_MISSING in str(exception_info.value)
    assert ERROR_MESSAGE_API_TOKEN_MISSING in str(exception_info.value)


def test_constructor_user_config_url_empty():
    config = {'orgUrl': '', 'token': 'TOKEN'}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert ERROR_MESSAGE_ORG_URL_MISSING in str(exception_info.value)


def test_constructor_user_config_url_not_https():
    config = {'orgUrl': 'http://test.okta.com', 'token': 'TOKEN'}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert ERROR_MESSAGE_ORG_URL_NOT_HTTPS in str(exception_info.value)
    assert FINDING_OKTA_DOMAIN in str(exception_info.value)


def test_constructor_user_config_url_has_yourOktaDomain():
    config = {
        'orgUrl': 'https://{yourOktaDomain}.okta.com', 'token': 'TOKEN'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert ERROR_MESSAGE_ORG_URL_YOUROKTADOMAIN in str(exception_info.value)


@ pytest.mark.parametrize("url", ["https://dev-admin.okta.com",
                                  "https://dev-admin.oktapreview.com",
                                  "https://dev-admin.okta-emea.com",
                                  "https://test-admin.okta.com"])
def test_constructor_user_config_url_has_admin(url):
    config = {
        'orgUrl': url, 'token': 'TOKEN'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_ORG_URL_ADMIN, f"Current value: {url}"])


def test_constructor_user_config_url_dot_com_twice():
    url = 'https://test.okta.com.com'
    config = {
        'orgUrl': url, 'token': 'TOKEN'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_ORG_URL_TYPO, f"Current value: {url}"])


def test_constructor_user_config_url_punctuation():
    # test for urls with '://' multiple times
    url = 'https://://test.okta.com'
    config = {
        'orgUrl': url, 'token': 'TOKEN'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_ORG_URL_TYPO, f"Current value: {url}"])


def test_constructor_user_config_token_empty(fs):
    config = {'orgUrl': 'https://test.okta.com', 'token': ''}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert ERROR_MESSAGE_API_TOKEN_MISSING in str(exception_info.value)


def test_constructor_user_config_url_has_apiToken(fs):
    config = {
        'orgUrl': 'https://test.okta.com', 'token': '{apiToken}'
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert ERROR_MESSAGE_API_TOKEN_DEFAULT in str(exception_info.value)


def test_constructor_user_config_auth_mode_invalid():
    authorizationMode = "blah"
    config = {'orgUrl': "https://test.okta.com",
              'token': "TOKEN",
              'authorizationMode': authorizationMode}
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_AUTH_MODE_INVALID, f"with {authorizationMode}"])


def test_constructor_user_config_SSWS():
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token}
    client = OktaClient(user_config=config)
    loaded_config = client.get_config()
    assert org_url == loaded_config['client']['orgUrl']
    assert token == loaded_config['client']['token']


@ pytest.mark.parametrize("private_key", ["private key hash",
                                          "pem_file.pem",
                                          "{'Jwks'}"])
def test_constructor_user_config_PK(private_key):
    org_url = "https://test.okta.com"
    authorizationMode = "PrivateKey"
    client_id = "clientID"
    scopes = ["scope1"]

    config = {
        'orgUrl': org_url,
        'authorizationMode': authorizationMode,
        'clientId': client_id,
        'scopes': scopes,
        'privateKey': private_key
    }
    client = OktaClient(user_config=config)
    loaded_config = client.get_config()
    assert org_url == loaded_config['client']['orgUrl']
    assert authorizationMode == loaded_config['client']['authorizationMode']
    assert client_id == loaded_config['client']['clientId']
    assert scopes == loaded_config['client']['scopes']
    assert private_key == loaded_config['client']['privateKey']


def test_constructor_user_config_PK_empty(fs):
    org_url = "https://test.okta.com"
    authorizationMode = "PrivateKey"

    config = {
        'orgUrl': org_url,
        'authorizationMode': authorizationMode,
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_CLIENT_ID_MISSING, ERROR_MESSAGE_SCOPES_PK_MISSING
               ])


def test_constructor_user_config_PK_client_id_empty():
    org_url = "https://test.okta.com"
    authorizationMode = "PrivateKey"
    scopes = ["scope1"]
    private_key_hash = "private key hash"

    config = {
        'orgUrl': org_url,
        'authorizationMode': authorizationMode,
        'clientId': "",
        'scopes': scopes,
        'privateKey': private_key_hash
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_CLIENT_ID_MISSING
               ])


def test_constructor_user_config_PK_client_id_default():
    org_url = "https://test.okta.com"
    authorizationMode = "PrivateKey"
    scopes = ["scope1"]
    private_key_hash = "private key hash"

    config = {
        'orgUrl': org_url,
        'authorizationMode': authorizationMode,
        'clientId': "{clientId}",
        'scopes': scopes,
        'privateKey': private_key_hash
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_CLIENT_ID_DEFAULT
               ])


@ pytest.mark.parametrize("scopes,private_key", [([], "private key hash"),
                                                 (["scope1"], ""),
                                                 ([], "")])
def test_constructor_user_config_PK_scopes_and_or_private_key_empty(
        scopes,
        private_key):
    org_url = "https://test.okta.com"
    authorizationMode = "PrivateKey"
    client_id = "clientID"

    config = {
        'orgUrl': org_url,
        'authorizationMode': authorizationMode,
        'clientId': client_id,
        'scopes': scopes,
        'privateKey': private_key
    }
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
    assert all(string in str(exception_info.value) for string in [
               ERROR_MESSAGE_SCOPES_PK_MISSING
               ])


"""
Testing constructor with YAML configurations
"""


def test_constructor_global_config_SSWS(fs):
    fs.pause()
    global_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-global.yaml")
    with open(global_sample) as file:
        global_config = yaml.load(file, Loader=yaml.SafeLoader)
        org_url = global_config["okta"]["client"]["orgUrl"]
        token = global_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_GLOBAL_YAML_PATH, contents=yaml.dump(global_config))

    client = OktaClient()
    loaded_config = client.get_config()

    assert org_url == loaded_config['client']['orgUrl']
    assert token == loaded_config['client']['token']


def test_constructor_local_config_SSWS(fs):
    fs.pause()
    local_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-local.yaml")
    with open(local_sample) as file:
        local_config = yaml.load(file, Loader=yaml.SafeLoader)
        org_url = local_config["okta"]["client"]["orgUrl"]
        token = local_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_LOCAL_YAML_PATH, contents=yaml.dump(local_config))

    client = OktaClient()
    loaded_config = client.get_config()

    assert org_url == loaded_config['client']['orgUrl']
    assert token == loaded_config['client']['token']


def test_constructor_global_config_PK(fs):
    fs.pause()
    global_sample = os.path.join(os.path.dirname(
        __file__), "files", "PK-sample-global.yaml")
    with open(global_sample) as file:
        global_config = yaml.load(file, Loader=yaml.SafeLoader)
        org_url = global_config["okta"]["client"]["orgUrl"]
        client_id = global_config["okta"]["client"]["clientId"]
        private_key = global_config["okta"]["client"]["privateKey"]
        fs.resume()
        fs.create_file(_GLOBAL_YAML_PATH, contents=yaml.dump(global_config))

    client = OktaClient()
    loaded_config = client.get_config()

    assert org_url == loaded_config['client']['orgUrl']
    assert client_id == loaded_config['client']['clientId']
    assert private_key == loaded_config['client']['privateKey']


def test_constructor_local_config_PK(fs):
    fs.pause()
    local_sample = os.path.join(os.path.dirname(
        __file__), "files", "PK-sample-local.yaml")
    with open(local_sample) as file:
        local_config = yaml.load(file, Loader=yaml.SafeLoader)
        org_url = local_config["okta"]["client"]["orgUrl"]
        client_id = local_config["okta"]["client"]["clientId"]
        private_key = local_config["okta"]["client"]["privateKey"]
        fs.resume()
        fs.create_file(_LOCAL_YAML_PATH, contents=yaml.dump(local_config))

    client = OktaClient()
    loaded_config = client.get_config()

    assert org_url == loaded_config['client']['orgUrl']
    assert client_id == loaded_config['client']['clientId']
    assert private_key == loaded_config['client']['privateKey']


def test_constructor_env_vars_SSWS():
    org_url = "https://test.okta.com"
    token = "TOKEN"
    os.environ["OKTA_CLIENT_ORGURL"] = org_url
    os.environ["OKTA_CLIENT_TOKEN"] = token

    client = OktaClient()
    loaded_config = client.get_config()

    os.environ.pop("OKTA_CLIENT_ORGURL")
    os.environ.pop("OKTA_CLIENT_TOKEN")

    assert org_url == loaded_config['client']['orgUrl']
    assert token == loaded_config['client']['token']


def test_constructor_env_vars_PK():
    authorizationMode = "PrivateKey"
    org_url = "https://test.okta.com"
    client_id = "clientID"
    scopes = "scope1,scope2,scope3"
    private_key = "private key"
    os.environ["OKTA_CLIENT_AUTHORIZATIONMODE"] = authorizationMode
    os.environ["OKTA_CLIENT_ORGURL"] = org_url
    os.environ["OKTA_CLIENT_CLIENTID"] = client_id
    os.environ["OKTA_CLIENT_SCOPES"] = scopes
    os.environ["OKTA_CLIENT_PRIVATEKEY"] = private_key

    client = OktaClient()
    loaded_config = client.get_config()

    os.environ.pop("OKTA_CLIENT_ORGURL")
    os.environ.pop("OKTA_CLIENT_AUTHORIZATIONMODE")
    os.environ.pop("OKTA_CLIENT_CLIENTID")
    os.environ.pop("OKTA_CLIENT_SCOPES")
    os.environ.pop("OKTA_CLIENT_PRIVATEKEY")

    assert authorizationMode == loaded_config['client']['authorizationMode']
    assert org_url == loaded_config['client']['orgUrl']
    assert client_id == loaded_config['client']['clientId']
    assert scopes.split(',') == loaded_config['client']['scopes']
    assert private_key == loaded_config['client']['privateKey']


def test_constructor_precedence_highest_rank_local_yaml(fs):
    # Setup Global config
    fs.pause()
    global_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-global.yaml")
    with open(global_sample) as file:
        global_config = yaml.load(file, Loader=yaml.SafeLoader)
        global_org_url = global_config["okta"]["client"]["orgUrl"]
        global_token = global_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_GLOBAL_YAML_PATH, contents=yaml.dump(global_config))

    # Setup Local config
    fs.pause()
    local_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-local.yaml")
    with open(local_sample) as file:
        local_config = yaml.load(file, Loader=yaml.SafeLoader)
        local_org_url = local_config["okta"]["client"]["orgUrl"]
        local_token = local_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_LOCAL_YAML_PATH, contents=yaml.dump(local_config))

    # Create client and validate values
    client = OktaClient()
    loaded_config = client.get_config()

    assert local_org_url == loaded_config['client']['orgUrl']
    assert local_token == loaded_config['client']['token']
    assert local_org_url != global_org_url
    assert local_token != global_token
    assert global_org_url != loaded_config['client']['orgUrl']
    assert global_token != loaded_config['client']['token']


def test_constructor_precedence_highest_rank_env_vars(fs):
    # Setup Local config
    fs.pause()
    local_sample = os.path.join(os.path.dirname(
        __file__), "files", "SSWS-sample-local.yaml")
    with open(local_sample) as file:
        local_config = yaml.load(file, Loader=yaml.SafeLoader)
        local_org_url = local_config["okta"]["client"]["orgUrl"]
        local_token = local_config["okta"]["client"]["token"]
        fs.resume()
        fs.create_file(_LOCAL_YAML_PATH, contents=yaml.dump(local_config))
    # Setup env. vars
    env_org_url = "https://test.env.okta.com"
    env_token = "envTOKEN"
    os.environ["OKTA_CLIENT_ORGURL"] = env_org_url
    os.environ["OKTA_CLIENT_TOKEN"] = env_token

    client = OktaClient()
    loaded_config = client.get_config()

    os.environ.pop("OKTA_CLIENT_ORGURL")
    os.environ.pop("OKTA_CLIENT_TOKEN")

    assert local_org_url != loaded_config['client']['orgUrl']
    assert local_token != loaded_config['client']['token']
    assert local_org_url != env_org_url
    assert local_token != env_token
    assert env_org_url == loaded_config['client']['orgUrl']
    assert env_token == loaded_config['client']['token']


def test_constructor_precedence_highest_rank_user_config():
    # Setup env. vars
    env_org_url = "https://test.env.okta.com"
    env_token = "envTOKEN"
    os.environ["OKTA_CLIENT_ORGURL"] = env_org_url
    os.environ["OKTA_CLIENT_TOKEN"] = env_token

    # Setup user config
    user_org_url = "https://test.user.okta.com"
    user_token = "userTOKEN"
    config = {'orgUrl': user_org_url, 'token': user_token}

    client = OktaClient(config)
    loaded_config = client.get_config()

    os.environ.pop("OKTA_CLIENT_ORGURL")
    os.environ.pop("OKTA_CLIENT_TOKEN")

    assert user_org_url == loaded_config['client']['orgUrl']
    assert user_token == loaded_config['client']['token']
    assert user_org_url != env_org_url
    assert user_token != env_token
    assert env_org_url != loaded_config['client']['orgUrl']
    assert env_token != loaded_config['client']['token']


def test_constructor_valid_proxy():
    org_url = "https://test.okta.com"
    token = "TOKEN"

    port = 8080
    host = "test.okta.com"
    username = "username"
    password = "password"

    config = {
        'orgUrl': org_url,
        'token': token,
        'proxy': {
            'port': port,
            'host': host,
            'username': username,
            'password': password
        }
    }
    # Ensure no error is raised and correct proxy is determined
    client = OktaClient(user_config=config)
    assert client.get_request_executor(
    )._http_client._proxy == f"http://{username}:{password}@{host}:{port}/"


def test_constructor_valid_no_proxy():
    org_url = "https://test.okta.com"
    token = "TOKEN"

    config = {
        'orgUrl': org_url,
        'token': token
    }

    # Ensure no error is raised and proxy is None
    client = OktaClient(user_config=config)
    assert client.get_request_executor(
    )._http_client._proxy is None


def test_constructor_valid_env_vars():
    org_url = "https://test.okta.com"
    token = "TOKEN"

    config = {
        'orgUrl': org_url,
        'token': token
    }

    # Setting up env vars
    os.environ["HTTP_PROXY"] = "http://user:pass@test.okta.com:8080"
    os.environ["HTTPS_PROXY"] = "https://user:pass@test.okta.com:8080"

    expected = os.environ["HTTPS_PROXY"]
    client = OktaClient(user_config=config)

    # Deleting env vars
    del os.environ['HTTP_PROXY']
    del os.environ['HTTPS_PROXY']

    # Ensure no error is raised and proxy is None
    assert client.get_request_executor(
    )._http_client._proxy == expected


def test_constructor_invalid_missing_host():
    org_url = "https://test.okta.com"
    token = "TOKEN"

    port = 8080
    username = "username"
    password = "password"

    config = {
        'orgUrl': org_url,
        'token': token,
        'proxy': {
            'port': port,

            'username': username,
            'password': password
        }
    }

    # Expect error with config
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
        assert ERROR_MESSAGE_PROXY_MISSING_HOST in exception_info.value


@pytest.mark.parametrize("username,password", [("", "password"),
                                               ("username", "")])
def test_constructor_invalid_missing_username_or_password(username, password):
    org_url = "https://test.okta.com"
    token = "TOKEN"

    port = 8080
    host = "test.okta.com"

    config = {
        'orgUrl': org_url,
        'token': token,
        'proxy': {
            'port': port,
            'host': host,
            'username': username,
            'password': password
        }
    }

    # Expect error with config
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
        assert ERROR_MESSAGE_PROXY_MISSING_AUTH in exception_info.value


@pytest.mark.parametrize("port", [-1, 0, 65536, "port"])
def test_constructor_invalid_port_number(port):
    org_url = "https://test.okta.com"
    token = "TOKEN"

    host = "test.okta.com"
    username = "username"
    password = "password"

    config = {
        'orgUrl': org_url,
        'token': token,
        'proxy': {
            'port': port,
            'host': host,
            'username': username,
            'password': password
        }
    }

    # Expect error with config
    with pytest.raises(ValueError) as exception_info:
        OktaClient(user_config=config)
        assert ERROR_MESSAGE_PROXY_INVALID_PORT in exception_info.value


def test_constructor_custom_http_client_impl():
    class CustomHTTPClient(HTTPClient):
        pass
    config = {'httpClient': CustomHTTPClient}
    client = OktaClient(config)
    assert isinstance(client._request_executor._http_client, CustomHTTPClient)


def test_constructor_client_logging():
    logger = logging.getLogger('okta-sdk-python')
    assert logger.disabled
    config = {'logging': {"enabled": True, "logLevel": logging.DEBUG}}
    client = OktaClient(config)
    assert not logger.disabled
    assert logger.level == logging.DEBUG


def test_client_raise_exception():
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token, 'raiseException': True}
    client = OktaClient(config)
    with pytest.raises(HTTPException):
        asyncio.run(client.list_users())


def test_client_custom_headers(monkeypatch, mocker):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token}
    custom_headers = {'Header-Test-1': 'test value 1',
                      'Header-Test-2': 'test value 2'}
    client = OktaClient(config)

    # verify custom headers are set
    client.set_custom_headers(custom_headers)
    assert client.get_custom_headers() == custom_headers

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
    monkeypatch.setattr(aiohttp, 'request', mock_http_request)
    asyncio.run(client.list_users())
    assert 'Header-Test-1' in mock_http_request.headers
    assert 'Header-Test-2' in mock_http_request.headers

    # verify custom headers are cleared
    client.clear_custom_headers()
    assert client.get_custom_headers() == {}


def test_client_handle_aiohttp_error(monkeypatch, mocker):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token}
    client = OktaClient(config)

    class MockHTTPRequest():
        def __call__(self, **params):
            raise aiohttp.ClientConnectorCertificateError(
                ConnectionKey(host=org_url,
                              port=443,
                              is_ssl=True,
                              ssl=None,
                              proxy=None,
                              proxy_auth=None,
                              proxy_headers_hash=None),
                SSLCertVerificationError(1,
                                         '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: '
                                         'unable to get local issuer certificate (_ssl.c:1123)'))

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        @staticmethod
        async def mock_response_text():
            return '[{"text": "mock response text"}]'

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp, 'request', mock_http_request)
    res, resp_body, error = asyncio.run(client.list_users())
    assert res is None
    assert resp_body is None
    assert isinstance(error, aiohttp.ClientError)


def test_client_log_debug(monkeypatch, caplog):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token,
              'logging': {'enabled': True, 'logLevel': logging.DEBUG}}
    client = OktaClient(config)

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
            return '[{"embedded": null,' \
                   '"links": {"self": {"href": "https://test.okta.com/v1/users/test_id"}},' \
                   '"activated": "2021-01-01T00:00:00.000Z",' \
                   '"created": "2021-01-01T00:00:00.000Z",' \
                   '"credentials": null,' \
                   '"id": "test_id",' \
                   '"last_login": null,' \
                   '"profile": {"name": "test_name"},' \
                   '"status": null,' \
                   '"status_changed": null,' \
                   '"transitioning_to_status": null,' \
                   '"type": null}]'

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp, 'request', mock_http_request)
    with caplog.at_level(logging.DEBUG):
        res, resp_body, error = asyncio.run(client.list_users())
        assert 'okta-sdk-python' in caplog.text
        assert 'DEBUG' in caplog.text
        assert "'method': 'GET'" in caplog.text
        assert "'url': 'https://test.okta.com/api/v1/users'" in caplog.text


def test_client_log_info(monkeypatch, caplog):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token,
              'logging': {'enabled': True, 'logLevel': logging.INFO}}
    client = OktaClient(config)

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
            return '[{"embedded": null,' \
                   '"links": {"self": {"href": "https://test.okta.com/v1/users/test_id"}},' \
                   '"activated": "2021-01-01T00:00:00.000Z",' \
                   '"created": "2021-01-01T00:00:00.000Z",' \
                   '"credentials": null,' \
                   '"id": "test_id",' \
                   '"last_login": null,' \
                   '"profile": {"name": "test_name"},' \
                   '"status": null,' \
                   '"status_changed": null,' \
                   '"transitioning_to_status": null,' \
                   '"type": null}]'

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp, 'request', mock_http_request)
    with caplog.at_level(logging.INFO):
        res, resp_body, error = asyncio.run(client.list_users())
        assert caplog.text == ''


def test_client_log_exception(monkeypatch, caplog):
    org_url = "https://test.okta.com"
    token = "TOKEN"
    config = {'orgUrl': org_url, 'token': token,
              'logging': {'enabled': True, 'logLevel': logging.DEBUG}}
    client = OktaClient(config)

    class MockHTTPRequest():
        def __call__(self, **params):
            raise aiohttp.ClientConnectorCertificateError(
                ConnectionKey(host=org_url,
                              port=443,
                              is_ssl=True,
                              ssl=None,
                              proxy=None,
                              proxy_auth=None,
                              proxy_headers_hash=None),
                SSLCertVerificationError(1,
                                         '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: '
                                         'unable to get local issuer certificate (_ssl.c:1123)'))

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            pass

        @staticmethod
        async def mock_response_text():
            return '[{"text": "mock response text"}]'

    mock_http_request = MockHTTPRequest()
    monkeypatch.setattr(aiohttp, 'request', mock_http_request)
    with caplog.at_level(logging.DEBUG):
        res, resp_body, error = asyncio.run(client.list_users())
        assert 'Cannot connect to host https://test.okta.com' in caplog.text
