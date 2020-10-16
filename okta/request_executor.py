from okta.http_client import HTTPClient
from okta.user_agent import UserAgent
from okta.oauth import OAuth
from okta.api_response import OktaAPIResponse
from okta.error_messages import ERROR_MESSAGE_429_MISSING_DATE_X_RESET
from okta.utils import convert_date_time_to_seconds
import time
from http import HTTPStatus
import json


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
        self._request_timeout = config["client"].get('requestTimeout', 0)
        if self._request_timeout < 0:
            raise ValueError(
                ("okta.client.requestTimeout provided as "
                 f"{self._request_timeout} but must be 0 (disabled) or "
                 "greater than zero"))
        self._max_retries = config["client"]["rateLimit"].get('maxRetries', 2)
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
            'headers': self._default_headers,
            'proxy': self._config["client"]["proxy"] if "proxy"
            in self._config["client"] else None
        })

    async def create_request(self, method: str, url: str, body: dict = None,
                             headers: dict = {}, oauth=False):
        """
        Creates request for request executor's HTTP client.

        Args:
            method (str): HTTP Method to be used
            url (str): URL to send request to
            body (dict, optional): Request body. Defaults to None.
            headers (dict, optional): Request headers. Defaults to {}.

        Returns:
            dict, Exception: Tuple of Dictionary repr of HTTP request and
            exception raised during execution
        """
        # Base HTTP Request
        request = {
            "method": method
        }

        # Build request
        # Get predetermined headers and build URL
        headers.update(self._default_headers)
        if self._config["client"]["orgUrl"] not in url:
            url = self._config["client"]["orgUrl"] + url

        # OAuth
        if self._authorization_mode == "PrivateKey" and not oauth:
            # check if access token exists
            if self._cache.contains("OKTA_ACCESS_TOKEN"):
                access_token = self._cache.get("OKTA_ACCESS_TOKEN")
            else:
                # if not, make one
                # Generate using private key provided
                access_token, error = await self._oauth.get_access_token()
                # return error if problem retrieving token
                if error:
                    return (None, error)

            # finally, add to header and cache
            headers.update({"Authorization": f"Bearer {access_token}"})
            self._cache.add("OKTA_ACCESS_TOKEN", access_token)

        # Add content type header if request body exists
        if body is not None:
            headers.update({"Content-Type": "application/json"})

        # finish building request and return
        request["headers"] = headers
        request["url"] = url
        request["data"] = body

        return (request, None)

    async def execute(self, request, response_type=None):
        """
        This function is the high level request execution method. Performs the
        API call and returns a formatted response object

        Args:
            request (dict): dictionary object containing request details

        Returns:
            (OktaAPIResponse, Exception): Response obj for the Okta API, Error
        """
        _, response, response_body, error = await self.fire_request(request)

        if error is not None:
            return (None, error)

        _, error = self._http_client.check_response_for_error(
            request["url"], response, response_body)

        return (
            OktaAPIResponse(self, request, response,
                            response_body, response_type),
            error
        )

    async def fire_request(self, request):
        """
        Send Request using HTTP Client

        Args:
            request (dict): HTTP request in dictionary format

        Returns:
            aiohttp.RequestInfo, aiohttp.ClientResponse, json, Exception: Tuple
            of request, response object, response json, and error if raised
        """
        # Retrieve URL from request and generate cache key
        url = request["url"]
        url_cache_key = self._cache.create_key(url)

        # Remove cache entry if not GET call
        method = request["method"]
        if method.upper() != "GET":
            self._cache.delete(url_cache_key)

        # check if in cache
        if not self._cache.contains(url_cache_key):
            # shoot request and return
            _, res_details, resp_body, error = await\
                self.fire_request_helper(request, 0, time.time())
            if error is not None:
                return (None, res_details, resp_body, error)

            # add to cache if not a list and valid response
            if method.upper() == "GET" and 200 <= res_details.status <= 299:
                try:
                    json_object = json.loads(resp_body)
                    if not isinstance(json_object, list):
                        self._cache.add(
                            url_cache_key, (res_details, resp_body))
                except Exception:
                    pass

            return (request, res_details, resp_body, error)

        # otherwise return cache response
        res_details, resp_body = self._cache.get(url_cache_key)
        return (request, res_details, resp_body, None)

    async def fire_request_helper(self, request, attempts, request_start_time):
        """
        Helper method to perform HTTP call with retries if needed

        Args:
            request (dict): HTTP request representation
            attempts (int): number of attempted HTTP calls so far
            request_start_time (float): original start time of request

        Returns:
            aiohttp.RequestInfo, aiohttp.ClientResponse, json, Exception: Tuple
            of request, response object, response json, and error if raised
        """
        # Get start request time
        current_req_start_time = time.time()
        max_retries = self._max_retries
        req_timeout = self._request_timeout

        if req_timeout > 0 and \
                (current_req_start_time - request_start_time) > req_timeout:
            # Timeout is hit for request
            return (None, None, None, Exception("Request Timeout exceeded."))

        # Execute request
        _, res_details, resp_body, error = \
            await self._http_client.send_request(request)

        check_429 = self.is_too_many_requests(res_details.status, resp_body)
        headers = res_details.headers

        if attempts < max_retries and (error or check_429):
            date_time = headers.get("Date", "")
            if date_time:
                date_time = convert_date_time_to_seconds(date_time)
            retry_limit_reset_headers = list(map(float, headers.getall(
                "X-Rate-Limit-Reset", [])))
            retry_limit_reset = min(retry_limit_reset_headers) if len(
                retry_limit_reset_headers) > 0 else None
            if not date_time or not retry_limit_reset:
                return (None, res_details, resp_body,
                        Exception(
                            ERROR_MESSAGE_429_MISSING_DATE_X_RESET
                        ))

            if check_429:
                # backoff
                backoff_seconds = self.calculate_backoff(
                    retry_limit_reset, date_time)
                self.pause_for_backoff(backoff_seconds)
                if (current_req_start_time + backoff_seconds)\
                        - request_start_time > req_timeout and req_timeout > 0:
                    return (None, res_details, resp_body, resp_body)

            # Setup retry request
            attempts += 1
            request['headers'].update(
                {
                    RequestExecutor.RETRY_FOR_HEADER: headers.get(
                        "X-Okta-Request-Id", ""),
                    RequestExecutor.RETRY_COUNT_HEADER: attempts
                }
            )

            _, res_details, resp_body, error = await self.fire_request_helper(
                request, attempts, request_start_time
            )
            if error:
                return (None, res_details, resp_body, error)

        return (request, res_details, resp_body, error)

    def is_too_many_requests(self, status, response):
        """
        Determines if HTTP request has been made too many times

        Args:
            status (int): HTTP response status code
            response (json): Response Body

        Returns:
            bool: Returns True if this request has been called too many times
        """
        return response is not None and status is not None\
            and status == HTTPStatus.TOO_MANY_REQUESTS

    def parse_response(self, request, response):
        pass

    def calculate_backoff(self, retry_limit_reset, date_time):
        return retry_limit_reset - date_time + 1

    def pause_for_backoff(self, backoff_time):
        time.sleep(backoff_time)
