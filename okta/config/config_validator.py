class ConfigValidator():
    FINDING_OKTA_DOMAIN = "https://bit.ly/finding-okta-domain"
    GET_OKTA_API_TOKEN = "https://bit.ly/get-okta-api-token"
    FINDING_OKTA_APP_CRED = "https://bit.ly/finding-okta-app-credentials"
    REPO_URL = "https://github.com/okta/okta-sdk-python"

    def __init__(self, config):
        self._config = config
        self.validate_config()

    """
    Configuration Validators
    """

    def validate_config(self):
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
                'client').get(field, "") for field in client_fields]
            errors += self._validate_client_fields(*client_fields_values)
        else:  # Not a valid authorization mode
            errors += [("The AuthorizationMode configuration option must "
                        "be one of: [SSWS, PrivateKey]. You provided the SDK "
                        f"with {client.get('authorizationMode', None)}")]

        if errors:  # raise exception and stop program if errors
            newline = '\n'
            raise ValueError(f"{newline}Errors:"
                             f"{newline + newline.join(errors) + 2*newline}"
                             f"See {ConfigValidator.REPO_URL} for usage")

    def _validate_client_fields(self, client_id, client_scopes,
                                client_private_key):
        client_fields_errors = []

        # check client id
        client_id = client_id.strip().lower()
        # null or empty string
        if not client_id:
            client_fields_errors.append((
                "Your client ID is missing. You can copy it from the "
                "Okta Developer Console in the details for the Application "
                "you created. Follow these instructions to find it: "
                f"{ConfigValidator.FINDING_OKTA_APP_CRED}"))
        # contains {clientId}
        if "{clientId}" in client_id:
            client_fields_errors.append((
                "Replace {{clientId}} with the client ID of your Application. "
                "You can copy it from the Okta Developer Console in the "
                "details for the Application you created. Follow these "
                "instructions to find it: "
                f"{ConfigValidator.FINDING_OKTA_APP_CRED}"))

        # check that at least 1 scope is provided and private key is provided
        if not (client_scopes and client_private_key):
            client_fields_errors.append((
                "When using authorization mode 'PrivateKey', you must supply "
                "'okta.client.scopes' and 'okta.client.privateKey'"))

        return client_fields_errors

    def _validate_token(self, token: str):
        # remove whitespaces and lowercase token for comparisons
        token = token.strip().lower()

        token_errors = []

        # token is null or empty
        if not token:
            token_errors.append((
                "Your Okta API token is missing. "
                "You can generate one in the Okta Developer Console. "
                "Follow these instructions: "
                f"{ConfigValidator.GET_OKTA_API_TOKEN}"))
        # token contains {apiToken}
        if "{apiToken}".lower() in token:
            token_errors.append((
                "Replace {{apiToken}} with your Okta API token. "
                "You can generate one in the Okta Developer Console. "
                "Follow these instructions: "
                f"{ConfigValidator.GET_OKTA_API_TOKEN}"))

        return token_errors

    def _validate_org_url(self, url: str):
        # remove whitespaces and lowercase URL for comparisons
        url = url.strip().lower()

        url_errors = []

        # if empty or null string
        if not url:
            url_errors.append(
                ("Your Okta URL is missing. You can copy your domain from the"
                 " Okta Developer Console. Follow these instructions to find"
                 f" it: {ConfigValidator.FINDING_OKTA_DOMAIN}"))
        # if url is not https (in non-testing env)
        if url and not (self._config["testing"]["testingDisableHttpsCheck"]
                        or url.startswith('https')):
            url_errors.append(
                ("Your Okta URL must start with 'https'. Current value: "
                 f"{url or None}. "
                 "You can copy your domain from the Okta Developer Console. "
                 "Follow these instructions to find it: "
                 f"{ConfigValidator.FINDING_OKTA_DOMAIN}"))
        # url still contains default {yourOktaDomain}
        if "{yourOktaDomain}".lower() in url\
                or "{{yourOktaDomain}}".lower() in url:
            url_errors.append((
                "Replace {{yourOktaDomain}} with your Okta domain. "
                "You can copy your domain from the Okta Developer Console. "
                "Follow these instructions to find it: "
                f"{ConfigValidator.FINDING_OKTA_DOMAIN}"))
        # url contains -admin string
        admin_strings = ["-admin.okta.com",
                         "-admin.oktapreview.com", "-admin.okta-emea.com"]
        if any(string in url for string in admin_strings) or "-admin" in url:
            url_errors.append(
                ("Your Okta domain should not contain -admin. "
                 f"Current value: {url}. You can copy your domain "
                 "from the Okta Developer Console. Follow these instructions "
                 f"to find it: {ConfigValidator.FINDING_OKTA_DOMAIN}"))
        # url ends with .com.com
        if url.endswith(".com.com"):
            url_errors.append((
                "It looks like there's a typo in your Okta domain. Current "
                f"value: {url}. You can copy your domain from "
                "the Okta Developer Console. Follow these instructions to find"
                f" it: {ConfigValidator.FINDING_OKTA_DOMAIN}"))
        # url contains multiple '://' segments
        if url.count("://") > 1:
            url_errors.append((
                "It looks like there's a typo in your Okta domain. Current "
                f"value: {url}. You can copy your domain from "
                "the Okta Developer Console. Follow these instructions to find"
                f" it: {ConfigValidator.FINDING_OKTA_DOMAIN}"))

        return url_errors