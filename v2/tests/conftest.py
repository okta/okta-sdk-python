import pytest
import re
import os

from pytest_recording._vcr import use_cassette

TEST_OKTA_URL = "test"
B_TEST_OKTA_URL = b"test"
URL_REGEX = r"dev-\d+"
B_URL_REGEX = rb"dev-\d+"
PYTEST_MOCK_CLIENT = "pytest_mock_client"
PYTEST_RE_RECORD = "record_mode"
MOCK_TESTS = 'MOCK_TESTS'


def is_mock_tests_flag_true():
    """Return True by default, i.e. variable is not set.
    Return False if env variable `MOCK_TESTS` is set to `false`, `FALSE`, etc.
    Return True in all other cases.
    """
    return os.environ.get('MOCK_TESTS', 'true').strip().lower() != 'false'


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
            pytestconfig
        ) as cassette:
            yield cassette
    else:
        yield None


def pytest_generate_tests(metafunc):
    ''' just to attach the cmd-line args to a test-class that needs them '''
    record_mode = metafunc.config.getoption(PYTEST_RE_RECORD)
    # check if this function is in a test-class that needs the cmd-line args
    if record_mode == "rewrite":
        os.environ[PYTEST_MOCK_CLIENT] = "1"


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
            response["headers"]["content-security-policy-report-only"][0])
    if "link" in response["headers"]:
        current = response["headers"]["link"]
        response["headers"]["link"] = re.sub(
            URL_REGEX, TEST_OKTA_URL, current)

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
