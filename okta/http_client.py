import aiohttp
import asyncio
import json
import xmltodict
from okta.errors.http_error import HTTPError
from okta.errors.okta_api_error import OktaAPIError


class HTTPClient:
    """
    This class is the basic HTTPClient for the Okta Client.
    Custom HTTP clients should inherit from this class.
    """

    def __init__(self, http_config={}):
        # Get headers from Request Executor
        self._default_headers = http_config["headers"]
        # Create timeout for all HTTP requests
        self._timeout = aiohttp.ClientTimeout(
            total=http_config["requestTimeout"] if "requestTimeout" in
            http_config and http_config["requestTimeout"] > 0 else None
        )

    async def send_request(self, request):
        """
        This method fires HTTP requests

        Arguments:
            request {dict} -- This dictionary contains all information needed
            for the request.
            - HTTP method (as str)
            - Headers (as dict)
            - Request body (as dict)

        Returns:
            Tuple(aiohttp.RequestInfo, aiohttp.ClientResponse, JSON object)
            -- A tuple containing the request and response of the HTTP call
        """
        try:
            # Set headers
            self._default_headers.update(request["headers"])
            # Fire request
            async with aiohttp.request(
                method=request["method"],
                url=request["url"],
                headers=self._default_headers,
                json=request["data"] if "data" in request else {},
                timeout=self._timeout
            ) as response:
                return (response.request_info,
                        response,
                        await response.text(),
                        None)
        except (aiohttp.ClientError, asyncio.exceptions.TimeoutError) as error:
            # Return error if arises
            return (None, None, None, error)

    @staticmethod
    def check_response_for_error(url, response_details, response_body):
        """
        Checks HTTP response for errors in the response body

        Args:
            url (str): URL of response
            response_details (aiohttp.ClientResponse): Response object with
            details response_body (json): Response body in JSON format

        Returns:
            dict, (OktaAPIError or HTTPError): Tuple of: dict repr of the
            response (if no error), any error found
        """
        # Retrieve dictionary repr and response status code
        if response_details.content_type == "application/xml":
            formatted_response = xmltodict.parse(response_body)
        elif response_details.content_type == "application/json":
            formatted_response = json.loads(response_body)
        else:
            formatted_response = response_body

        status_code = response_details.status

        # check if call was succesful
        if 200 <= status_code <= 299:
            return (formatted_response, None)
        else:
            # create errors
            try:
                error = OktaAPIError(url, response_details, formatted_response)
            except Exception:
                error = HTTPError(url, response_details, formatted_response)
            return (None, error)

    @staticmethod
    def format_binary_data(data):
        with aiohttp.MultipartWriter("mixed") as mpwriter:
            mpwriter.append(data)
        return mpwriter
