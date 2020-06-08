from urllib.parse import urlencode, quote
from okta.jwt import JWT
from okta.http_client import HTTPClient


class OAuth:
    """
    This class contains the OAuth actions for the Okta Client.
    """
    OAUTH_ENDPOINT = "/oauth2/v1/token"

    def __init__(self, request_executor, config):
        self._request_executor = request_executor
        self._config = config
        self._access_token = None

    def get_JWT(self):
        org_url = self._config["client"]["orgUrl"]
        client_id = self._config["client"]["clientId"]
        private_key = self._config["client"]["privateKey"]

        return JWT.create_token(org_url, client_id, private_key)

    async def get_access_token(self):
        if self._access_token:
            return self._access_token

        jwt = self.get_JWT()
        parameters = {
            'grant_type': 'client_credentials',
            'scope': ' '.join(self._config["client"]["scopes"]),
            'client_assertion_type':
                'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            'client_assertion': jwt
        }

        encoded_parameters = urlencode(parameters, quote_via=quote)
        org_url = self._config["client"]["orgUrl"]
        url = f"{org_url}{OAuth.OAUTH_ENDPOINT}?" + \
            encoded_parameters
        request = {
            'url': url,
            'method': "POST",
            'headers': {
                'Accept': "application/json",
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }
        # Work on handling response
        # Make max 1 retry
        _, res_details, res_json, err = \
            await self._request_executor.fire_request(request)

        if err:
            return (None, err)

        parsed_response, err = HTTPClient.check_response_for_error(
            url, res_details, res_json)

        if err:
            return (None, err)

        self._access_token = parsed_response["access_token"]
        return (self._access_token, None)

    def clear_access_token(self):
        self._access_token = None
