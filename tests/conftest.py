# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import os
import re

import pytest
from pytest_recording._vcr import use_cassette

TEST_OKTA_URL = "https://test.okta.com"
B_TEST_OKTA_URL = b"https://test.okta.com"
URL_REGEX = r"https://(?:[\w-]+\.oktapreview\.com|dev-\d+\.okta\.com)"
B_URL_REGEX = rb"https://(?:[\w-]+\.oktapreview\.com|dev-\d+\.okta\.com)"

# Bare hostnames for content-security-policy headers (no https:// prefix)
BARE_HOST_ADMIN_REGEX = r"dev-\d+-admin\.okta\.com"
BARE_HOST_KERBEROS_REGEX = r"dev-\d+\.kerberos\.okta\.com"
BARE_HOST_REGEX = r"dev-\d+\.okta\.com"

# Sanitized JWT values for request/response bodies
SANITIZED_CLIENT_ASSERTION = (
    "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJzdWIiOiIwb2Ffc2FuaXRpemVkX2NsaWVudF9pZCJ9."
    "SANITIZED_SIGNATURE"
)
SANITIZED_ACCESS_TOKEN = (
    "eyJraWQiOiJzYW5pdGl6ZWRfa2V5X2lkIiwiYWxnIjoiUlMyNTYifQ."
    "eyJqdGkiOiJBVC5zYW5pdGl6ZWRfdG9rZW5faWQifQ."
    "SANITIZED_TOKEN_SIGNATURE"
)
PYTEST_MOCK_CLIENT = "pytest_mock_client"
PYTEST_RE_RECORD = "record_mode"
MOCK_TESTS = "MOCK_TESTS"


def is_mock_tests_flag_true():
    """Return True by default, i.e. variable is not set.
    Return False if env variable `MOCK_TESTS` is set to `false`, `FALSE`, etc.
    Return True in all other cases.
    """
    return os.environ.get("MOCK_TESTS", "true").strip().lower() != "false"


# Override vcr fixture from pytest_recording library
@pytest.fixture(autouse=True)
def vcr(request, vcr_markers, vcr_cassette_dir, record_mode, pytestconfig):
    """Install a cassette if a test is marked with `pytest.mark.vcr`."""
    if vcr_markers and is_mock_tests_flag_true():
        config = request.getfixturevalue("vcr_config")
        default_cassette = request.getfixturevalue("default_cassette_name")
        with use_cassette(
                default_cassette,
                vcr_cassette_dir,
                record_mode,
                vcr_markers,
                config,
                pytestconfig,
        ) as cassette:
            yield cassette
    else:
        yield None


def pytest_generate_tests(metafunc):
    """just to attach the cmd-line args to a test-class that needs them"""
    record_mode = metafunc.config.getoption(PYTEST_RE_RECORD)
    # check if this function is in a test-class that needs the cmd-line args
    if record_mode == "rewrite":
        os.environ[PYTEST_MOCK_CLIENT] = "1"


@pytest.fixture(scope="module")
def vcr_config():
    return {
        # Remove personal details from Integration Tests
        "before_record_request": before_record_request,
        "before_record_response": before_record_response,
    }


def before_record_request(request):
    request.uri = re.sub(URL_REGEX, TEST_OKTA_URL, request.uri)
    if "authorization" in request.headers:
        if request.headers["authorization"].startswith("SSWS"):
            request.headers["authorization"] = "SSWS myAPIToken"
        elif request.headers["authorization"].startswith("Bearer"):
            request.headers["authorization"] = "Bearer myOAuthToken"
        elif request.headers["authorization"].startswith("DPoP"):
            request.headers["authorization"] = "DPoP myDPoPToken"

    # Sanitize DPoP proof header (contains ephemeral keys and signatures)
    if "dpop" in request.headers:
        request.headers["dpop"] = "sanitized_dpop_proof_jwt"

    # Sanitize client_assertion JWT in request body (contains client ID and org URL)
    if request.body:
        body = request.body
        if isinstance(body, bytes):
            body = body.decode("utf-8", errors="replace")
        if isinstance(body, str) and "client_assertion=" in body:
            body = re.sub(
                r'(client_assertion=)eyJ[A-Za-z0-9_\-\.]+',
                r'\1' + SANITIZED_CLIENT_ASSERTION,
                body
            )
            request.body = body

    return request


def before_record_response(response):
    # response["url"] = re.sub(URL_REGEX, TEST_OKTA_URL, response["url"])
    if "body" in response:
        if "string" in response["body"]:
            body_bytes = response["body"]["string"]
            # Sanitize URLs in response body
            response["body"]["string"] = re.sub(
                B_URL_REGEX, B_TEST_OKTA_URL, body_bytes
            )
            # Sanitize access_token JWTs in response body
            body_str = response["body"]["string"]
            if isinstance(body_str, bytes):
                body_str = body_str.decode("utf-8", errors="replace")
            if "access_token" in body_str:
                body_str = re.sub(
                    r'("access_token":")eyJ[A-Za-z0-9_\-]+\.eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+(")',
                    r'\1' + SANITIZED_ACCESS_TOKEN + r'\2',
                    body_str
                )
                response["body"]["string"] = body_str.encode("utf-8")

    # Sanitize content-security-policy header (contains bare org hostnames)
    if "content-security-policy" in response["headers"]:
        csp = response["headers"]["content-security-policy"]
        if isinstance(csp, list):
            csp = csp[0]
        csp = re.sub(BARE_HOST_ADMIN_REGEX, "test-admin.okta.com", csp)
        csp = re.sub(BARE_HOST_KERBEROS_REGEX, "test.kerberos.okta.com", csp)
        csp = re.sub(BARE_HOST_REGEX, "test.okta.com", csp)
        response["headers"]["content-security-policy"] = csp

    if "content-security-policy-report-only" in response["headers"]:
        response["headers"]["content-security-policy-report-only"] = re.sub(
            URL_REGEX,
            TEST_OKTA_URL,
            response["headers"]["content-security-policy-report-only"][0],
        )
    if "link" in response["headers"]:
        current = response["headers"]["link"]
        response["headers"]["link"] = re.sub(URL_REGEX, TEST_OKTA_URL, current)

    # Sanitize DPoP nonce (server-provided nonce that changes each time)
    if "dpop-nonce" in response["headers"]:
        response["headers"]["dpop-nonce"] = "sanitized_dpop_nonce"

    # Sanitize JSESSIONID cookies
    if "set-cookie" in response["headers"]:
        cookies = response["headers"]["set-cookie"]
        if isinstance(cookies, list):
            response["headers"]["set-cookie"] = [
                re.sub(r'JSESSIONID=[A-F0-9]{32}', 'JSESSIONID=SANITIZED_SESSION_ID', c)
                for c in cookies
            ]
        elif isinstance(cookies, str):
            response["headers"]["set-cookie"] = re.sub(
                r'JSESSIONID=[A-F0-9]{32}', 'JSESSIONID=SANITIZED_SESSION_ID', cookies
            )

    return response


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """
    To run at the end of a test run
    """

    def clean_up_env_vars():
        if PYTEST_MOCK_CLIENT in os.environ:
            del os.environ[PYTEST_MOCK_CLIENT]

    request.addfinalizer(clean_up_env_vars)
