from urllib.parse import urlencode, quote


class OAuth:
    """
    This class contains the OAuth actions for the Okta Client.
    """

    def __init__(self, okta_client):
        self._client = okta_client
        self._jwt = None

    def getJwt(self):
        return self._jwt or self.create_jwt(self._client)

    def create_jwt(self, okta_client):
        pass

    def get_access_token(self):
        jwt = self.getJwt()
        parameters = {
            'grant_type': 'client_credentials',
            'scope': ' '.join(self._client.get_scopes()),
            'client_assertion_type':
                'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            'client_assertion': jwt
        }
        encoded_parameters = urlencode(parameters, quote_via=quote)
        http_options = {
            'url': f"{self._client.get_base_url()}/oauth2/v1/token",
            'method': "POST",
            'body': encoded_parameters,
            'headers': {
                'Accept': "application/json",
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }
        return self._client.request_executor.send_request(http_options)
