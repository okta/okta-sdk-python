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
        """
        Generates JWT using client configuration

        Returns:
            str: Generated JSON Web Token
        """
        org_url = self._config["client"]["orgUrl"]
        client_id = self._config["client"]["clientId"]
        private_key = self._config["client"]["privateKey"]

        return JWT.create_token(org_url, client_id, private_key)

    async def get_access_token(self):
        """
        Retrieves or generates the OAuth access token for the Okta Client

        Returns:
            str, Exception: Tuple of the access token, error that was raised
            (if any)
        """
        # Return token if already generated
        if self._access_token:
            return self._access_token

        # Otherwise create new one
        # Get JWT and create parameters for new Oauth token
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

        # Craft request
        oauth_req, err = await self._request_executor.create_request(
            "POST", url, None, {
                'Accept': "application/json",
                'Content-Type': 'application/x-www-form-urlencoded'
            }, oauth=True)

        # TODO Make max 1 retry
        # Shoot request
        if err:
            return (None, err)
        _, res_details, res_json, err = \
            await self._request_executor.fire_request(oauth_req)
        # Return HTTP Client error if raised
        if err:
            return (None, err)

        # Check response body for error message
        parsed_response, err = HTTPClient.check_response_for_error(
            url, res_details, res_json)
        # Return specific error if found in response
        if err:
            return (None, err)

        # Otherwise set token and return it
        self._access_token = parsed_response["access_token"]
        return (self._access_token, None)

    def clear_access_token(self):
        """
        Clear currently used OAuth access token, probably expired
        """
        self._access_token = None
