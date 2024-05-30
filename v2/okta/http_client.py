import aiohttp
import asyncio
import json
import logging
import os
import xmltodict
from okta.errors.http_error import HTTPError
from okta.errors.okta_api_error import OktaAPIError
from okta.exceptions import HTTPException, OktaAPIException


logger = logging.getLogger('okta-sdk-python')


class HTTPClient:
    """
    This class is the basic HTTPClient for the Okta Client.
    Custom HTTP clients should inherit from this class.
    """
    raise_exception = False

    def __init__(self, http_config={}):
        # Get headers from Request Executor
        self._default_headers = http_config["headers"]
        # Create timeout for all HTTP requests
        self._timeout = aiohttp.ClientTimeout(
            total=http_config["requestTimeout"] if "requestTimeout" in
            http_config and http_config["requestTimeout"] > 0 else None
        )
        if "proxy" in http_config:
            self._proxy = self._setup_proxy(http_config["proxy"])
        else:
            self._proxy = None
        if "sslContext" in http_config:
            self._ssl_context = http_config["sslContext"]
        else:
            self._ssl_context = None
        self._session = None

    def set_session(self, session):
        """Set Client Session to improve performance by reusing session.

        Session should be closed manually or within context manager.
        """
        self._session = session

    async def close_session(self):
        await self._session.close()

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
            logger.debug(f"Request: {request}")
            # Set headers
            self._default_headers.update(request["headers"])
            # Prepare request parameters
            params = {'method': request['method'],
                      'url': request['url'],
                      'headers': self._default_headers}
            if request['data']:
                params['data'] = json.dumps(request['data'])
            elif request['form']:
                params['data'] = request['form']
            json_data = request.get('json')
            # empty json param may cause issue, so include it if needed only
            # more details: https://github.com/okta/okta-sdk-python/issues/131
            if json_data:
                params['json'] = json_data
            if self._timeout:
                params['timeout'] = self._timeout
            if self._proxy:
                params['proxy'] = self._proxy
            if self._ssl_context:
                params['ssl_context'] = self._ssl_context
            # Fire request
            if self._session is not None:
                logger.debug('Request with re-usable session.')
                async with self._session.request(**params) as response:
                    return (response.request_info,
                            response,
                            await response.text(),
                            None)
            else:
                logger.debug('Request without re-usable session.')
                async with aiohttp.ClientSession() as session:
                    async with session.request(**params) as response:
                        return (response.request_info,
                                response,
                                await response.text(),
                                None)
        except (aiohttp.ClientError, asyncio.TimeoutError) as error:
            # Return error if arises
            logger.exception(error)
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
                if HTTPClient.raise_exception:
                    raise OktaAPIException(formatted_response)
            except OktaAPIException:
                raise
            except Exception:
                error = HTTPError(url, response_details, formatted_response)
                if HTTPClient.raise_exception:
                    logger.exception(formatted_response)
                    raise HTTPException(formatted_response)
            logger.error(error)
            return (None, error)

    @staticmethod
    def format_binary_data(data):
        with aiohttp.MultipartWriter("mixed") as mpwriter:
            mpwriter.append(data)
        return mpwriter

    def _setup_proxy(self, proxy):
        proxy_string = ""

        if proxy is None:
            # check if env vars contain proxies
            if "HTTP_PROXY" in os.environ:
                proxy_string = os.environ["HTTP_PROXY"]
            if "HTTPS_PROXY" in os.environ:
                proxy_string = os.environ["HTTPS_PROXY"]
            return proxy_string if proxy_string != "" else None

        host = proxy["host"]
        port = int(proxy["port"]) if "port" in proxy else ""

        # config has credentials
        if "username" in proxy and "password" in proxy:
            username = proxy["username"]
            password = proxy["password"]
            proxy_string = f"http://{username}:{password}@{host}"
        else:
            proxy_string = f"http://{host}"

        if port:
            proxy_string += f":{port}/"

        return proxy_string if proxy_string != "" else None
