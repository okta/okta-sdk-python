from okta.http_client import HTTPClient
from okta.user_agent import UserAgent
from okta.oauth import OAuth
import time
from http import HTTPStatus
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
            .get_user_agent_string(),
            'Accept': "application/json"
        }

        # SSWS header
        if config["client"]["authorizationMode"] == "SSWS":
            self._default_headers['Authorization'] = (
                "SSWS "
                f"{self._config['client']['token']}"
            )
        else:
            # OAuth
            self._oauth = OAuth(self, self._config)

        self._http_client = HTTPClient({
            'requestTimeout': self._request_timeout,
            'headers': self._default_headers
        })

    async def create_request(self, method: str, url: str, body: dict = None,
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
            else:
                # Generate using private key provided
                access_token, error = await self._oauth.get_access_token()
                if error:
                    return None, error

            headers.update({"Authorization": f"Bearer {access_token}"})
            self._cache.add("OKTA_ACCESS_TOKEN", access_token)

        if body is not None:
            headers.update({"Content-Type": "application/json"})

        request["headers"] = headers
        request["url"] = url
        request["body"] = body

        return request, None

    async def fire_request(self, request):
        url = request["url"]
        url_cache_key = self._cache.create_key(url)
        method = request["method"]

        if method.upper() == "GET":
            self._cache.delete(url_cache_key)

        # check if in cache
        if not self._cache.contains(url_cache_key):
            # shoot request
            return\
                await self._http_client.send_request(request)
            # return (req, res_details, res_json, error)

        return (request, None, self._cache.get(url_cache_key), None)

    async def fire_request_helper(self, request, attempts, request_start_time):
        # Get start request time
        current_req_start_time = int(time.time())
        max_retries = self._max_retries
        req_timeout = self._request_timeout

        if req_timeout > 0 and \
                (current_req_start_time-request_start_time) > req_timeout:
            # Timeout is hit for request
            return None, Exception("Request Timeout exceeded.")

        # Do request
        req, res_details, res_json, error = \
            await self._http_client.send_request(request)

        check_429 = self.is_too_many_requests(res_details.status, res_json)
        headers = res_details.headers

        if attempts < max_retries and (error or check_429):
            date_time = headers.get("Date", "")
            retry_limit_reset = headers.get("X-Rate-Limit-Reset", "")
            if not date_time or not retry_limit_reset:
                return None, \
                    Exception(("429 response must have the "
                               "'X-Rate-Limit-Reset' and 'Date' headers"))

            if check_429:
                # backoff
                pass

            attempts += 1

            request['headers'].update({
                RequestExecutor.RETRY_FOR_HEADER: headers.get(
                    "X-Okta-Request-Id", ""),
                RequestExecutor.RETRY_COUNT_HEADER: attempts
            })

            req, res_details, res_json, error = \
                await self._http_client.send_request(request)

        return req, res_details, res_json, error

    def is_too_many_requests(self, status, response):
        return response is not None\
            and status == HTTPStatus.TOO_MANY_REQUESTS

    def parse_response(self, request, response):
        pass
