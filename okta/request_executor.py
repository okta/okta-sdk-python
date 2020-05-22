import requests
import json


class RequestExecutor:
    """
    This class handles all of the requests sent by the Okta Client.
    """

    def __init__(self, config: dict = {}):
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
                f"okta.client.rateLimit.requestTimeout provided as \
                {self._request_timeout} but must be 0 (disabled) or \
                greater than zero")
        self._max_retries = config.get('maxRetries', 2)
        if self._max_retries < 0:
            raise ValueError(
                f"okta.client.rateLimit.maxRetries provided as \
                {self._max_retries} but must be 0 (disabled) or \
                greater than zero")

        self._retryCountHeader = 'X-Okta-Retry-Count'
        self._retryForHeader = 'X-Okta-Retry-For'

    def create_request(self, method: str, url: str, body: dict = None,
                       headers: dict = None):

        pass

    def send_request(self, request):
        # look into making this async
        pass

    def retry_request(self, request):
        pass

    def parse_response(self, request, response):
        pass
