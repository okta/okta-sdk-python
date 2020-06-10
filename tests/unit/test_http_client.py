from okta.http_client import HTTPClient
from okta.request_executor import RequestExecutor
from okta.cache.no_op_cache import NoOpCache
from okta.user_agent import UserAgent
from okta.client import Client
from okta.oauth import OAuth
from okta.errors.okta_api_error import OktaAPIError
from okta.jwt import JWT
import os
import pytest
import aiohttp
import asyncio
import json

REQUEST_TIMEOUT = 5  # seconds
ORG_URL = "https://your.okta.com"
API_TOKEN = "yourApiToken"
CLIENT_ID = "yourClientId"
SCOPES = ["okta.scope.1"]
PRIVATE_KEY = "yourPrivateKey"
GET_USERS_CALL = "/api/v1/users?limit=200"

SAMPLE_RSA = '''-----BEGIN RSA PRIVATE KEY-----
                MIIEogIBAAKCAQEAvlhONz/qR7dBung7VW
                MhA6V61sGF+VOAELUq7HOr53YxHyyH0Fuh
                ET78wTbRM51dbKVMiY2e3jTTQ8HZyEs6pn
                2apud3gRWa3mmW9sCU9Iu9AaQPVYc9SrfY
                RY6iCvxNVMyfvYrWsbsKxKjLviRL2o3iO2
                gdlZMJfJl+PIm0nJAZ6wdnjNi7uXlVMu48
                xj5Uw8ZBWHGPtDH9ZyYm9HhxYY4CxY2oTV
                6azqnDYUIpFio2sZBcyU+3bnlxcbHI0A4z
                wIiuJbH8KNFcHp13gs5MvsLDFTEx8pMry3
                2rHkCTRrRhad/OsvIVa3J6yvWlL5sz3iai
                SqEjnwBC4nhNv/JKhQIDAQABAoIBAApGZo
                x9dwZhilsIR/2rQPo7Kdcjcbm8i+569SL3
                +IjhXLP32aoB9D8j1Q2SCbd9UHB/uNK5Ei
                EhHWFsOrcg9nzLzXgiiRUvByHn9cYCrdfI
                nk6THl/J0eFxbKuOkElDBuKjvCDFeKL1+5
                YTnZH5UB3vaE24KFatbgbrm0Cl11nXJrXd
                3EUOtjpkPvUo0WzGvK0Ha509ucsUfBCQcy
                mDY6I3Z5bfSNNKsdQrvoHlOONA0nN0uSZR
                IdFgxtvdB8D8yseqg0BN4Bl+/EMA7lprXf
                a+C7vljMCMY9JNtSjuBCM43o3Yy/H6NtzB
                Qa7H/nuzEt5O6s20va12SDA/55PRbVkCgY
                EA28pOgvfOROPVamvz+/kbEEfi1YJx74mv
                20EMVRab1DPkzQnVHVRX53Wqjtd5afLj3W
                2drGQOgLhq2XTXuSh9Ikat1R80NG69klO3
                9X4Uk5+Qk+6c8B84K2w/vCucKT0D8VHO3C
                SdXO3yLIVCJWJjH3NeIK5A6BPs4P71El2Z
                6i0CgYEA3bQjKk8tJCvOxDuo90rbDaZy1U
                Y53/ewmQAgrYZ7ASzvQK0YPvNYIr289nDy
                f1DiVECWsNOoymuNlzMdD2sIP3J9KZ02hz
                5CVbS9W2yIDgf8L3sBZ66fDLIhhAXAUrhM
                k21pC66ccYFGBbnroh+ivKsOeP2lVDjkoB
                mYxbTyULkCgYAaNKbjyrQXVqrtg22Vz3/A
                kzGij2kSTHJhTAIyav2tcXqIT/HPC21ntY
                neeiaJ0WIF1roEAfIQuuxSfTHza7ZvzcmQ
                LaZF0iZcOgsnBB9j8pSEbuDbaH2D/+Yhg3
                mdGR9NOJnXea4hlGVZlZHrby2uZE0GzIAE
                q8uEkCGcTPi7CQKBgEB0N2j8fcYvSjx4j8
                XdKFQOmQHyGa9IRjok9FseZrJPyvrFl+/t
                NSlcegw3h/iFnlcaM/USg9bdb9uOS5uI5W
                v0r/iiMREeg5CBLC/hHKjfn2x6WU04UhsR
                ynakaWZjGDggLdLsn6TMDXxqsdt/UQOCw4
                FfVGpo4+a7qlOIKI5ZAoGAFkC1F269uXAi
                ACUTA1XmTgQ4AiXztKZe1ALUqa4WrgZ6/J
                6XR+VwM4QuWjnlczpF4kHsfHpFi4d4qS3J
                5kMvVUyIY3DwOsQenLo8C+orgmo4UstEjN
                Q1OQt04mV1fp1aE2b9JVjv72cPEE1SMqaE
                p7W0dBcm49L0mY7sNyEFS0U=
                -----END RSA PRIVATE KEY-----'''

SAMPLE_JWK = {'alg': 'RS256',
              'kty': 'RSA',
              'n': '''vlhONz_qR7dBung7VWMhA6V61sGF-
                 VOAELUq7HOr53YxHyyH0FuhET78wTbRM51dbK
                 VMiY2e3jTTQ8HZyEs6pn2apud3gRWa3mmW9sC
                 U9Iu9AaQPVYc9SrfYRY6iCvxNVMyfvYrWsbsK
                 xKjLviRL2o3iO2gdlZMJfJl-PIm0nJAZ6wdnj
                 Ni7uXlVMu48xj5Uw8ZBWHGPtDH9ZyYm9HhxYY
                 4CxY2oTV6azqnDYUIpFio2sZBcyU-3bnlxcbH
                 I0A4zwIiuJbH8KNFcHp13gs5MvsLDFTEx8pMr
                 y32rHkCTRrRhad_OsvIVa3J6yvWlL5sz3iaiS
                 qEjnwBC4nhNv_JKhQ''',
              'e': '''AQAB''',
              'd': '''CkZmjH13BmGKWwhH_atA-jsp1yNxu
                 byL7nr1Ivf4iOFcs_fZqgH0PyPVDZIJt31QcH
                 -40rkSISEdYWw6tyD2fMvNeCKJFS8HIef1xgK
                 t18ieTpMeX8nR4XFsq46QSUMG4qO8IMV4ovX7
                 lhOdkflQHe9oTbgoVq1uBuubQKXXWdcmtd3cR
                 Q62OmQ-9SjRbMa8rQdrnT25yxR8EJBzKYNjoj
                 dnlt9I00qx1Cu-geU440DSc3S5JlEh0WDG290
                 HwPzKx6qDQE3gGX78QwDuWmtd9r4Lu-WMwIxj
                 0k21KO4EIzjejdjL8fo23MFBrsf-e7MS3k7qz
                 bS9rXZIMD_nk9FtWQ''',
              'p': '''28pOgvfOROPVamvz-_kbEEfi1YJx7
                 4mv20EMVRab1DPkzQnVHVRX53Wqjtd5afLj3W
                 2drGQOgLhq2XTXuSh9Ikat1R80NG69klO39X4
                 Uk5-Qk-6c8B84K2w_vCucKT0D8VHO3CSdXO3y
                 LIVCJWJjH3NeIK5A6BPs4P71El2Z6i0''',
              'q': '''3bQjKk8tJCvOxDuo90rbDaZy1UY53
                 _ewmQAgrYZ7ASzvQK0YPvNYIr289nDyf1DiVE
                 CWsNOoymuNlzMdD2sIP3J9KZ02hz5CVbS9W2y
                 IDgf8L3sBZ66fDLIhhAXAUrhMk21pC66ccYFG
                 Bbnroh-ivKsOeP2lVDjkoBmYxbTyULk''',
              'dp': '''GjSm48q0F1aq7YNtlc9_wJMxoo9p
                 EkxyYUwCMmr9rXF6iE_xzwttZ7WJ3nomidFiB
                 da6BAHyELrsUn0x82u2b83JkC2mRdImXDoLJw
                 QfY_KUhG7g22h9g__mIYN5nRkfTTiZ13muIZR
                 lWZWR628trmRNBsyABKvLhJAhnEz4uwk''',
              'dq': '''QHQ3aPx9xi9KPHiPxd0oVA6ZAfIZ
                 r0hGOiT0Wx5msk_K-sWX7-01KVx6DDeH-IWeV
                 xoz9RKD1t1v245Lm4jla_Sv-KIxER6DkIEsL-
                 EcqN-fbHpZTThSGxHKdqRpZmMYOCAt0uyfpMw
                 NfGqx239RA4LDgV9Uamjj5ruqU4gojlk''',
              'qi': '''FkC1F269uXAiACUTA1XmTgQ4AiXz
                 tKZe1ALUqa4WrgZ6_J6XR-VwM4QuWjnlczpF4
                 kHsfHpFi4d4qS3J5kMvVUyIY3DwOsQenLo8C-
                 orgmo4UstEjNQ1OQt04mV1fp1aE2b9JVjv72c
                 PEE1SMqaEp7W0dBcm49L0mY7sNyEFS0U'''}


class MockHTTPRequest:
    def __init__(self):
        self.headers = {
            "User-Agent": UserAgent().get_user_agent_string(),
            "Authorization": f"SSWS {API_TOKEN}",
            # etc
        }
        self.url = ORG_URL + GET_USERS_CALL


class MockClientResponse:
    def __init__(self, request, response_details, response_data):
        self.req = request
        self.response_details = response_details
        self.response_data = response_data

    def response(self):
        return (self.req, self.response_details, self.response_data, None)


async def mock_return(*args, **kwargs):
    response_details = {
        'Content-Type': "application/json"
    }
    response_data = json.loads(json.dumps([{'ID': 1}, {'ID': 2}]))

    response = MockClientResponse(MockHTTPRequest(),
                                  response_details, response_data)
    return response.response()


async def mock_return_api_error(*args, **kwargs):
    return (None, None, None, json.dumps({
        'errorCode': '',
        'errorSummary': '',
        'errorLink': '',
        'errorId': '',
        'errorCauses': []
    }))


async def mock_timeout_response(*args, **kwargs):
    return (None, None, None, asyncio.exceptions.TimeoutError())


async def mock_invalid_HTTP_response(*args, **kwargs):
    return (None, None, None, aiohttp.ContentTypeError(None, None))


async def mock_access_token(*args, **kwargs):
    return ("This is an OAuth access token", None)


@ pytest.mark.asyncio
async def test_client_success_call_SSWS(monkeypatch):
    ssws_client = Client({
        "orgUrl": ORG_URL,
        "token": API_TOKEN
    })

    req, error = await ssws_client.get_request_executor()\
        .create_request("GET",
                        GET_USERS_CALL,
                        {},
                        {})

    monkeypatch.setattr(RequestExecutor, 'fire_request',
                        mock_return)

    req, res_details, res_json, error = await ssws_client\
        .get_request_executor().fire_request(req)

    assert error is None
    assert "User-Agent" in req.headers
    assert "Authorization" in req.headers
    assert req.headers["Authorization"].startswith("SSWS")
    assert res_details['Content-Type'] == "application/json"
    assert type(res_json) == list


@ pytest.mark.vcr()
@ pytest.mark.asyncio
async def test_client_error_call_SSWS():
    ssws_client = Client({
        "orgUrl": ORG_URL,
        "token": API_TOKEN + "wrong token"
    })

    req, error = await ssws_client.get_request_executor()\
        .create_request("GET",
                        GET_USERS_CALL,
                        {},
                        {})

    req, res_details, res_json, error = await ssws_client\
        .get_request_executor().fire_request(req)

    parsed, error = HTTPClient.check_response_for_error(
        req.url, res_details, res_json)

    assert isinstance(error, OktaAPIError)
    assert error.message.startswith("Okta HTTP")


@ pytest.mark.asyncio
async def test_client_successful_call_oauth(monkeypatch):
    oauth_client = Client({
        "orgUrl": ORG_URL,
        "authorizationMode": "PrivateKey",
        "clientId": CLIENT_ID,
        "scopes": SCOPES,
        "privateKey": PRIVATE_KEY
    })

    request_executor = oauth_client.get_request_executor()

    monkeypatch.setattr(OAuth, 'get_access_token', mock_access_token)
    req, err = await request_executor.create_request(
        "GET",
        GET_USERS_CALL,
        {},
        {})

    monkeypatch.setattr(RequestExecutor, 'fire_request',
                        mock_return)
    req, res_details, res_json, error = await oauth_client\
        .get_request_executor().fire_request(req)

    assert error is None
    assert "User-Agent" in req.headers
    assert "Authorization" in req.headers
    assert req.headers["Authorization"].startswith("SSWS")
    assert res_details['Content-Type'] == "application/json"
    assert type(res_json) == list


@pytest.mark.vcr()
@ pytest.mark.asyncio
async def test_client_error_call_oauth(monkeypatch):
    oauth_client = Client({
        "orgUrl": ORG_URL,
        "authorizationMode": "PrivateKey",
        "clientId": CLIENT_ID,
        "scopes": SCOPES,
        "privateKey": PRIVATE_KEY + "Wrong one"
    })

    monkeypatch.setattr(OAuth, 'get_access_token', mock_access_token)

    req, err = await oauth_client.get_request_executor()\
        .create_request("GET",
                        GET_USERS_CALL,
                        {},
                        {})

    req, res_details, res_json, error = await oauth_client\
        .get_request_executor().fire_request(req)

    parsed, error = HTTPClient.check_response_for_error(
        req.url, res_details, res_json)

    assert isinstance(error, OktaAPIError)
    assert error.message.startswith("Okta HTTP")


@ pytest.mark.asyncio
async def test_client_invalid_url():
    http_client = HTTPClient({
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {}
    })
    req, res_details, res_json, error = await http_client.send_request({
        'method': 'GET',
        'url': "",
        'headers': {},
        'data': {}
    })
    assert all(values in [None] for values in [req, res_details, res_json])
    assert issubclass(type(error), aiohttp.ClientError)
    assert type(error) == aiohttp.InvalidURL


@ pytest.mark.asyncio
async def test_client_invalid_HTTP_method(monkeypatch):
    http_client = HTTPClient({
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {}
    })

    monkeypatch.setattr(HTTPClient, 'send_request', mock_invalid_HTTP_response)

    req, res_details, res_json, error = await http_client.send_request({
        'method': 'INVALID',
        'url': ORG_URL,
        'headers': {},
        'data': {}
    })
    assert all(values in [None] for values in [req, res_details, res_json])
    assert issubclass(type(error), aiohttp.ClientError)
    assert type(error) == aiohttp.ContentTypeError

    req, res_details, res_json, error = await http_client.send_request({
        'method': '',
        'url': ORG_URL,
        'headers': {},
        'data': {}
    })
    assert all(values in [None] for values in [req, res_details, res_json])
    assert issubclass(type(error), aiohttp.ClientError)
    assert type(error) == aiohttp.ContentTypeError


@ pytest.mark.asyncio
async def test_client_user_agent(monkeypatch):
    req_exec = RequestExecutor({
        "client": {
            "orgUrl": "https://test.okta.com",
            "authorizationMode": 'SSWS',
            "token": 'token',
            "userAgent": ''
        }
    }, NoOpCache(), None)

    assert 'User-Agent' in req_exec._http_client._default_headers
    assert req_exec._http_client._default_headers["User-Agent"] == UserAgent(
    ).get_user_agent_string()

    # mock and shoot request
    monkeypatch.setattr(HTTPClient, 'send_request', mock_return)

    req, res_details, res_json, error = await req_exec._http_client.\
        send_request({
            'method': 'GET',
            'url': ORG_URL + GET_USERS_CALL,
            'headers': {'Authorization': f"SSWS {API_TOKEN}"},
            'data': {}
        })
    assert error is None
    assert 'User-Agent' in req.headers
    assert req_exec._http_client._default_headers["User-Agent"] == \
        req.headers["User-Agent"]

    # with extra user agent string
    extra = "testing"
    req_exec = RequestExecutor({
        "client": {
            "orgUrl": "https://test.okta.com",
            "authorizationMode": 'SSWS',
            "token": 'token',
            "userAgent": extra
        }
    }, NoOpCache(), None)
    assert 'User-Agent' in req_exec._http_client._default_headers
    assert req_exec._http_client._default_headers["User-Agent"] == \
        UserAgent(extra).get_user_agent_string()


@ pytest.mark.asyncio
async def test_client_timeout(monkeypatch):
    http_client = HTTPClient({
        'requestTimeout': REQUEST_TIMEOUT,
        'headers': {}
    })

    # mock and shoot request
    monkeypatch.setattr(HTTPClient, 'send_request', mock_timeout_response)

    req, res_details, res_json, error = await http_client.send_request({
        'method': 'INVALID',
        'url': ORG_URL,
        'headers': {},
        'data': {}
    })

    assert all(values in [None] for values in [req, res_details, res_json])
    assert type(error) == asyncio.exceptions.TimeoutError


@ pytest.mark.parametrize("jwk_input", [SAMPLE_JWK, str(SAMPLE_JWK)])
def test_private_key_PEM_JWK_dict(jwk_input):
    generated_pem, generated_jwk = JWT.get_PEM_JWK(SAMPLE_JWK)
    assert generated_pem is not None and generated_jwk is not None
    assert not generated_jwk.is_public()


def test_private_key_PEM_JWK_file(fs):

    file_path = os.path.join(os.path.dirname(
        __file__), "test.pem")

    fs.create_file(file_path, contents=SAMPLE_RSA)

    generated_pem, generated_jwk = JWT.get_PEM_JWK(file_path)

    assert generated_pem is not None and generated_jwk is not None
    assert not generated_jwk.is_public()


def test_private_key_PEM_JWK_explicit_string():
    generated_pem, generated_jwk = JWT.get_PEM_JWK(SAMPLE_RSA)
    assert generated_pem is not None and generated_jwk is not None
    assert not generated_jwk.is_public()
