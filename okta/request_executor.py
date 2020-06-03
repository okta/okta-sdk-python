from okta.http_client import HTTPClient
from okta.jwt import JWT
from okta.user_agent import UserAgent
# import time
# import json


class RequestExecutor:
    """
    This class handles all of the requests sent by the Okta Client.
    """

    RETRY_COUNT_HEADER = 'X-Okta-Retry-Count'
    RETRY_FOR_HEADER = 'X-Okta-Retry-For'

    def __init__(self, config, cache, http_client=None):
        """
        Constructor for Request Executor object for Okta Client

        Arguments:
            config {dict} -- This dictionary contains the configuration
                             of the Request Executor
        """
        # Raise Value Error if numerical inputs are invalid (< 0)
        self._request_timeout = config.get('requestTimeout', 0)
        if self._request_timeout < 0:
            raise ValueError(
                ("okta.client.rateLimit.requestTimeout provided as "
                 f"{self._request_timeout} but must be 0 (disabled) or "
                 "greater than zero"))
        self._max_retries = config.get('maxRetries', 2)
        if self._max_retries < 0:
            raise ValueError(
                ("okta.client.rateLimit.maxRetries provided as "
                 f"{self._max_retries} but must be 0 (disabled) or "
                 "greater than zero"))
        # Setup other fields
        self._authorization_mode = config["client"]["authorizationMode"]
        self._base_url = config["client"]["orgUrl"]
        self._config = config
        self._cache = cache
        self._default_headers = {
            'User-Agent': UserAgent(config["client"].get("userAgent", None))
            .get_user_agent_string()
        }

        if config["client"]["authorizationMode"] == "SSWS":
            self._default_headers['Authorization'] = (
                "SSWS "
                f"{self._config['client']['token']}"
            )

        self._http_client = HTTPClient({
            'requestTimeout': self._request_timeout,
            'headers': self._default_headers
        })

    def create_request(self, method: str, url: str, body: dict = None,
                       headers: dict = None):
        request = {
            "method": method
        }

        # Build request
        headers = self._default_headers
        url = self._config["client"]["orgUrl"] + url

        if self._authorization_mode == "PrivateKey":
            # check if access token exists
            # if not, make one
            # finally, add to header
            if self._cache.contains("OKTA_ACCESS_TOKEN"):
                access_token = self._cache.get("OKTA_ACCESS_TOKEN")
                headers.update({"Authorization": f"Bearer {access_token}"})
            else:
                # Generate using private key provided
                private_key = self._config["client"]["privateKey"]
                client_id = self._config["client"]["clientId"]
                org_url = self._base_url

                my_jwk, my_pem = JWT.get_PEM_JWK(private_key)

                jwt = JWT.create_token(org_url, client_id, my_jwk, my_pem)
                type(jwt)

        return request

    def fire_request(self, request):
        # Get start request time
        # request_start_time = time.time()

        url = request["url"]
        method = request["method"]

        if method.upper() == "GET":
            self._cache.delete(url)

        # check if in cache
        if not self._cache.contains(url):
            # shoot request
            req, res_details, res_json, error = self._http_client.send_request(
                request)
        pass

    def retry_request(self, request):
        pass

    def parse_response(self, request, response):
        pass
