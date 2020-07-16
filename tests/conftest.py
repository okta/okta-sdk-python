import pytest
import re

TEST_OKTA_URL = "test"
B_TEST_OKTA_URL = b"test"
URL_REGEX = r"dev-\d+"
B_URL_REGEX = rb"dev-\d+"


@pytest.fixture(scope='module')
def vcr_config():
    return {
        # Remove personal details from Integration Tests
        "before_record_request": before_record_request,
        "before_record_response": before_record_response
    }


def before_record_request(request):
    request.uri = re.sub(URL_REGEX, TEST_OKTA_URL, request.uri)
    if "authorization" in request.headers:
        if request.headers["authorization"].startswith("SSWS"):
            request.headers["authorization"] = "SSWS myAPIToken"
        else:
            request.headers["authorization"] = "Bearer myOAuthToken"

    return request


def before_record_response(response):
    response["url"] = re.sub(URL_REGEX, TEST_OKTA_URL, response["url"])
    if "body" in response:
        if "string" in response["body"]:
            # body = response["body"]["string"]
            response["body"]["string"] = re.sub(
                B_URL_REGEX, B_TEST_OKTA_URL, response["body"]["string"])

    # if "Public-Key-Pins-Report-Only" in response["headers"]:
    #     del response["headers"]["Public-Key-Pins-Report-Only"]
    if "content-security-policy-report-only" in response["headers"]:
        response["headers"]["content-security-policy-report-only"] = re.sub(
            URL_REGEX, TEST_OKTA_URL,
            response["headers"]["content-security-policy-report-only"])
    if "link" in response["headers"]:
        current = response["headers"]["link"]
        response["headers"]["link"] = re.sub(
            URL_REGEX, TEST_OKTA_URL, current)

    return response
