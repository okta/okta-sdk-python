from okta.user_agent import UserAgent
from okta.constants import DATETIME_FORMAT
from okta.client import Client
import aiohttp
import asyncio
import json
from yarl import URL
import datetime as dt
import multidict
from tests.conftest import PYTEST_MOCK_CLIENT
import os
import time

REQUEST_TIMEOUT = 5  # seconds
ORG_URL = "https://test.okta.com"
API_TOKEN = "myApiToken"
CLIENT_ID = "yourClientId"
SCOPES = ["okta.scope.1", "okta.scope.2"]
PRIVATE_KEY = "yourPrivateKey"
GET_USERS_CALL = "/api/v1/users"
CLIENT_CONFIG = {'orgUrl': ORG_URL, 'token': API_TOKEN}

# Cache Test Details
TTI = 5.0
TTL = 5.0
CACHE_KEY = ("https://example.com/sample/cache-key/test+test@test."
             "com?with=a&query=string")
CACHE_VALUE = "54321"
ALT_CACHE_KEY = ("https://sample.com/example/cache-key/test+2@test."
                 "com?with=a&query=string")
ALT_CACHE_VALUE = "dbca"


class MockOktaClient(Client):
    def __init__(self, fs):
        if PYTEST_MOCK_CLIENT in os.environ:
            fs.pause()
            super().__init__()
            fs.resume()
        else:
            super().__init__(CLIENT_CONFIG)


async def mock_GET_HTTP_request(*args, **kwargs):
    return {
        "headers": {
            "User-Agent": UserAgent().get_user_agent_string(),
            "Authorization": f"SSWS {API_TOKEN}",
            # etc
        },
        "url": ORG_URL + GET_USERS_CALL,
        "data": {},
        "method": "GET"
    }


class MockHTTPResponseDetails():
    def __init__(self):
        self.status = 200
        self.headers = {
            "Date": "Tue, 1 Jan 2009 00:00:00 GMT",
            "Content-Type": "application/json",
            # etc
        }
        self.url = ORG_URL + GET_USERS_CALL
        self.method = "GET"
        self.links = {}
        self.content_type = "application/json"


class MockHTTP429ResponseDetails():
    def __init__(self):
        now = dt.datetime.now(dt.timezone.utc)
        now = now.replace(microsecond=0)

        one_sec_after = now + dt.timedelta(seconds=1)
        self.status = 429
        self.headers = multidict.CIMultiDict({
            "Date": now.strftime(DATETIME_FORMAT),
            "Content-Type": "application/json",
            "X-Okta-Now": "",
            "X-Rate-Limit-Reset": one_sec_after.timestamp(),
            "X-Okta-Request-id": "okta-request-id",
        })
        self.url = ORG_URL + GET_USERS_CALL
        self.method = "GET"
        self.links = {}
        self.content_type = "application/json"


class MockHTTP429NoXResetResponseDetails():
    def __init__(self):
        now = dt.datetime.now(dt.timezone.utc)
        now = now.replace(microsecond=0)

        self.status = 429
        self.headers = multidict.CIMultiDict({
            "Date": now.strftime(DATETIME_FORMAT),
            "Content-Type": "application/json",
            "X-Okta-Now": "",
            "X-Okta-Request-id": "okta-request-id",
        })
        self.url = ORG_URL + GET_USERS_CALL
        self.method = "GET"
        self.links = {}
        self.content_type = "application/json"


class MockHTTP429NoDateResponseDetails():
    def __init__(self):
        now = dt.datetime.now(dt.timezone.utc)
        now = now.replace(microsecond=0)

        one_sec_after = now + dt.timedelta(seconds=1)
        self.status = 429
        self.headers = multidict.CIMultiDict({
            "Content-Type": "application/json",
            "X-Okta-Now": "",
            "X-Rate-Limit-Reset": one_sec_after.timestamp(),
            "X-Okta-Request-id": "okta-request-id",
        })
        self.url = ORG_URL + GET_USERS_CALL
        self.method = "GET"
        self.links = {}
        self.content_type = "application/json"


class MockHTTP429MultiXResetResponseDetails():
    def __init__(self):
        now = dt.datetime.now(dt.timezone.utc)
        now = now.replace(microsecond=0)

        one_sec_after = now + dt.timedelta(seconds=1)
        two_sec_after = one_sec_after + dt.timedelta(seconds=1)

        base_headers = {
            "Date": now.strftime(DATETIME_FORMAT),
            "Content-Type": "application/json",
            "X-Okta-Now": "",
            "X-Rate-Limit-Reset": one_sec_after.timestamp(),
            "X-Okta-Request-id": "okta-request-id",
        }

        base_headers = list(zip(base_headers.keys(), base_headers.values()))
        base_headers.append(("X-Rate-Limit-Reset", two_sec_after.timestamp()))

        self.status = 429
        self.headers = multidict.CIMultiDict(base_headers)
        self.url = ORG_URL + GET_USERS_CALL
        self.method = "GET"
        self.links = {}
        self.content_type = "application/json"


async def mock_GET_HTTP_Client_response_valid(*args, **kwargs):
    request = await mock_GET_HTTP_request()
    response_details = MockHTTPResponseDetails()
    response_body = '[{"ID": "user.id.1"}]'
    error = None
    return (request, response_details, response_body, error)


async def mock_GET_HTTP_Client_response_valid_with_next(*args, **kwargs):
    request = await mock_GET_HTTP_request()
    response_details = MockHTTPResponseDetails()
    response_details.links = {
        "next": {"url": URL("https://www.next.okta.com")}
    }
    response_body = '[{"ID": "user.id.1"}, {"ID": "user.id.2"}]'
    error = None
    return (request, response_details, response_body, error)


async def mock_GET_HTTP_Client_response_429(*args, **kwargs):
    request = await mock_GET_HTTP_request()
    response_details = MockHTTP429ResponseDetails()
    response_body = '{}'
    error = None
    return (request, response_details, response_body, error)


async def mock_GET_HTTP_Client_response_429_no_x_reset(*args, **kwargs):
    request = await mock_GET_HTTP_request()
    response_details = MockHTTP429NoXResetResponseDetails()
    response_body = '{}'
    error = None
    return (request, response_details, response_body, error)


async def mock_GET_HTTP_Client_response_429_no_date(*args, **kwargs):
    request = await mock_GET_HTTP_request()
    response_details = MockHTTP429NoDateResponseDetails()
    response_body = '{}'
    error = None
    return (request, response_details, response_body, error)


async def mock_GET_HTTP_Client_response_429_multi_x_reset(*args, **kwargs):
    request = await mock_GET_HTTP_request()
    response_details = MockHTTP429MultiXResetResponseDetails()
    response_body = '{}'
    error = None
    return (request, response_details, response_body, error)


async def mock_GET_HTTP_Client_response_error(*args, **kwargs):
    return (None, None, None, json.dumps({
        "errorCode": "",
        "errorSummary": "",
        "errorLink": "",
        "errorId": "",
        "errorCauses": []
    }))


async def mock_timeout_response(*args, **kwargs):
    return (None, None, None, asyncio.TimeoutError())


async def mock_invalid_HTTP_response(*args, **kwargs):
    return (None, None, None, aiohttp.ContentTypeError(None, None))


async def mock_access_token(*args, **kwargs):
    return ("myOAuthToken", None)


def mock_pause_function(*args, **kwargs):
    if PYTEST_MOCK_CLIENT in os.environ:
        time.sleep(args[0])


def mock_cache_return_none(*args, **kwargs):
    return None


def mock_cache_return_value(*args, **kwargs):
    return CACHE_VALUE


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
