from okta.config_setter import ConfigSetter
from okta.request_executor import RequestExecutor
from okta.oauth import OAuth
from okta.http_client import HTTPClient
# from request_executor import RequestExecutor
# from oauth import OAuth
# from http_client import HTTPClient


class Client:
    """An Okta client object"""
    FINDING_OKTA_DOMAIN = "https://bit.ly/finding-okta-domain"
    GET_OKTA_API_TOKEN = "https://bit.ly/get-okta-api-token"
    FINDING_OKTA_APP_CRED = "https://bit.ly/finding-okta-app-credentials"
    REPO_URL = "https://github.com/okta/okta-sdk-python"
    DEFAULT_USER_AGENT = ""  # TODO: Figure out how to create this

    def __init__(self, input_config: dict = {}):
        # Load configuration
        client_config_setter = ConfigSetter()
        client_config_setter._apply_config({'client': input_config})
        self._config = client_config_setter.get_config()
        # Validate configuration
        self._validate_config()
        # set client variables since validation passes
        self._authorization_mode = self._config["client"]["authorizationMode"]
        self._base_url = self._config["client"]["orgUrl"]
        self._api_token = self._config["client"].get("token", None)
        self._oauth = None

        # set private key variables
        if self._authorization_mode == 'PrivateKey':
            self._client_id = self._config["client"]["clientId"]
            self._scopes = self._config["client"]["scopes"]
            self._private_key = self._config["client"]["privateKey"]
            self._oauth = OAuth(self)

        # Determine request executor to use
        self._request_executor = input_config.get("request_executor",
                                                  RequestExecutor())

        # Setup HTTP client
        self._http_client = HTTPClient({
            'request_executor': self._request_executor,
            'in_memory_cache': input_config.get('in_memory_cache', None),
            'cache_middleware': input_config.get('cache_middleware'),
            'oauth': self._oauth
        })

        if self._authorization_mode == 'SSWS':
            self._http_client.add_header({
                'Authorization': f"SSWS {self._api_token}"
            })

        self._http_client.add_header({
            'User-Agent': ' '.join([self._config["client"]["userAgent"],
                                    Client.DEFAULT_USER_AGENT])
            if self._config["client"].get("userAgent", None)
            else Client.DEFAULT_USER_AGENT
        })

    """
    Getters
    """

    def get_config(self):
        return self._config

    def get_scopes(self):
        return self._scopes

    def get_base_url(self):
        return self._base_url

    """
    Configuration Validators
    """

    def _validate_config(self):
        """
        This method validates the client configuration and validates
        the values provided. Throws a ValueError if anything is invalid.

        Raises:
            ValueError: A configuration provided needs to be corrected.
        """
        errors = []
        client = self._config.get('client')
        # check org url
        errors += \
            self._validate_org_url(
                client.get('orgUrl', ""))
        # check API details based on authorization mode
        if client.get('authorizationMode') == "SSWS":
            errors += \
                self._validate_token(
                    client.get('token', ""))
        elif client.get('authorizationMode') == "PrivateKey":
            client_fields = ['clientId', 'scopes', 'privateKey']
            client_fields_values = [self._config.get(
                'client').get(field) for field in client_fields]
            errors += self._validate_client_fields(*client_fields_values)
        else:  # Not a valid authorization mode
            errors += f"The AuthorizaitonMode configuration option must \
            be one of: [SSWS, PrivateKey].\nYou provided the SDK with \
            {client.get('authorizationMode')}"

        if errors:  # raise exception and stop program if errors
            newline = '\n'
            raise ValueError(f"Errors:\
                    {newline + newline.join(newline.join(errors) + newline)}\
                    See {Client.REPO_URL} for usage")

    def _validate_client_fields(self, client_id, client_scopes,
                                client_private_key):
        client_fields_errors = []

        # check client id
        client_id = client_id.strip().lower()
        # null or empty string
        if not client_id:
            client_fields_errors.append(
                f"Your client ID is missing. You can copy it from the \
                Okta Developer Console in the details for the Application \
                you created. Follow these instructions to find it: \
                {Client.FINDING_OKTA_APP_CRED}")
        # contains {clientId}
        if "{clientId}" in client_id:
            client_fields_errors.append(
                f"Replace {{clientId}} with the client ID of your Application. \
                You can copy it from the Okta Developer Console in the \
                details for the Application you created. Follow these \
                instructions to find it: {Client.FINDING_OKTA_APP_CRED}")

        # check that at least 1 scope is provided
        if not (client_scopes and client_private_key):
            client_fields_errors.append(
                "When using authorization mode 'PrivateKey', you must supply "
                "'okta.client.scopes' and 'okta.client.privateKey'")

        return client_fields_errors

    def _validate_token(self, token: str):
        # remove whitespaces and lowercase token for comparisons
        token = token.strip().lower()

        token_errors = []

        # token is null or empty
        if not token:
            token_errors.append(
                f"Your Okta API token is missing. \
                You can generate one in the Okta Developer Console. \
                Follow these instructions: {Client.GET_OKTA_API_TOKEN}")
        # token contains {apiToken}
        if "{apiToken}" in token:
            token_errors.append(
                f"Replace {{apiToken}} with your Okta API token. \
                You can generate one in the Okta Developer Console. \
                Follow these instructions: {Client.GET_OKTA_API_TOKEN}")

        return token_errors

    def _validate_org_url(self, url: str):
        # remove whitespaces and lowercase URL for comparisons
        url = url.strip().lower()

        url_errors = []

        # if empty or null string
        if not url:
            url_errors.append(
                f"Your Okta URL is missing. You can copy your domain from \
                the Okta Developer Console. Follow these instructions to find \
                it: {Client.FINDING_OKTA_DOMAIN}")
        # if url is not https (in non-testing env)
        if not (self._config["testing"]["testingDisableHttpsCheck"]
                or url.startswith('https')):
            url_errors.append(
                f"Your Okta URL must start with https. Current value: {url}. \
                You can copy your domain from the Okta Developer Console. \
                Follow these instructions to find it: \
                {Client.FINDING_OKTA_DOMAIN}")
        # url still contains default {yourOktaDomain}
        if "{yourOktaDomain}" in url:
            url_errors.append(
                f"Replace {{yourOktaDomain}} with your Okta domain. \
                You can copy your domain from the Okta Developer Console. \
                Follow these instructions to find it: \
                {Client.FINDING_OKTA_DOMAIN}")
        # url contains -admin string
        admin_strings = ["-admin.okta.com",
                         "-admin.oktapreview.com", "-admin.okta-emea.com"]
        if any(string in url for string in admin_strings):
            url_errors.append(
                f"Your Okta domain should not contain -admin. \
                Current value: {{existingValue}}. You can copy your domain \
                from the Okta Developer Console. Follow these instructions \
                to find it: {Client.FINDING_OKTA_DOMAIN}")
        # url ends with .com.com
        if url.endswith(".com.com"):
            url_errors.append(
                f"It looks like there's a typo in your Okta domain. Current \
                value: {{existingValue}}. You can copy your domain from \
                the Okta Developer Console. Follow these instructions to find \
                it: {Client.FINDING_OKTA_DOMAIN}")
        # url contains multiple '://' segments
        if url.count("://") > 1:
            url_errors.append(
                f"It looks like there's a typo in your Okta domain. Current \
                value: {{existingValue}}. You can copy your domain from \
                the Okta Developer Console. Follow these instructions to find \
                it: {Client.FINDING_OKTA_DOMAIN}")

        return url_errors


config = {
    "orgUrl": 'https://dev-195921.okta.com/',
    "token": '00UZXQa0IgHvIfKY6H1vkDtCPdotTQLIevu36LkMx5'
}
oauth_config = {
    "orgUrl": 'https://dev-195921.okta.com/',
    "authorizationMode": "PrivateKey",
    "clientId": '00UZXQa0IgHvIfKY6H1vkDtCPdotTQLIevu36LkMx5',
    "scopes": ['okta.users.manage'],
    "privateKey": "BLAHBLAHBLAH"
}
a = Client(input_config=oauth_config)
print(a.get_config())
