from okta.constants import FINDING_OKTA_DOMAIN, REPO_URL
from okta.error_messages import ERROR_MESSAGE_ORG_URL_MISSING, \
    ERROR_MESSAGE_API_TOKEN_DEFAULT, ERROR_MESSAGE_API_TOKEN_MISSING, \
    ERROR_MESSAGE_AUTH_MODE_INVALID, ERROR_MESSAGE_CLIENT_ID_MISSING, \
    ERROR_MESSAGE_CLIENT_ID_DEFAULT, ERROR_MESSAGE_SCOPES_PK_MISSING, \
    ERROR_MESSAGE_ORG_URL_NOT_HTTPS, ERROR_MESSAGE_ORG_URL_YOUROKTADOMAIN, \
    ERROR_MESSAGE_ORG_URL_TYPO, ERROR_MESSAGE_ORG_URL_ADMIN, \
    ERROR_MESSAGE_PROXY_MISSING_HOST, ERROR_MESSAGE_PROXY_MISSING_AUTH, \
    ERROR_MESSAGE_PROXY_INVALID_PORT


class ConfigValidator():
    """
    This class performs validation checks on the Okta Client configuration.
    """

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
        # check proxy settings if provided
        if "proxy" in client:
            errors += self._validate_proxy_settings(client["proxy"])
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
            errors += [
                (f"{ERROR_MESSAGE_AUTH_MODE_INVALID}"
                 f"{client.get('authorizationMode', None)}")]

        if errors:  # raise exception and stop program if errors
            newline = '\n'
            raise ValueError(f"{newline}Errors:"
                             f"{newline + newline.join(errors) + 2*newline}"
                             f"See {REPO_URL} for usage")

    def _validate_client_fields(self, client_id, client_scopes,
                                client_private_key):
        client_fields_errors = []

        # check client id
        client_id = client_id.strip().lower()
        # null or empty string
        if not client_id:
            client_fields_errors.append(ERROR_MESSAGE_CLIENT_ID_MISSING)
        # contains {clientId}
        if "{clientId}".lower() in client_id:
            client_fields_errors.append(ERROR_MESSAGE_CLIENT_ID_DEFAULT)

        # check that at least 1 scope is provided and private key is provided
        if not (client_scopes and client_private_key):
            client_fields_errors.append(ERROR_MESSAGE_SCOPES_PK_MISSING)

        return client_fields_errors

    def _validate_token(self, token: str):
        # remove whitespaces and lowercase token for comparisons
        token = token.strip().lower()

        token_errors = []

        # token is null or empty
        if not token:
            token_errors.append(ERROR_MESSAGE_API_TOKEN_MISSING)
        # token contains {apiToken}
        if "{apiToken}".lower() in token:
            token_errors.append(ERROR_MESSAGE_API_TOKEN_DEFAULT)

        return token_errors

    def _validate_org_url(self, url: str):
        # remove whitespaces and lowercase URL for comparisons
        url = url.strip().lower()

        url_errors = []

        # if empty or null string
        if not url:
            url_errors.append(ERROR_MESSAGE_ORG_URL_MISSING)
        # if url is not https (in non-testing env)
        if url and not (self._config["testing"]["testingDisableHttpsCheck"]
                        or url.startswith('https')):
            url_errors.append(
                (f"{ERROR_MESSAGE_ORG_URL_NOT_HTTPS} Current value: "
                 f"{url or None}. "
                 "You can copy your domain from the Okta Developer Console. "
                 "Follow these instructions to find it: "
                 f"{FINDING_OKTA_DOMAIN}"))
        # url still contains default {yourOktaDomain}
        if "{yourOktaDomain}".lower() in url\
                or "{{yourOktaDomain}}".lower() in url:
            url_errors.append(ERROR_MESSAGE_ORG_URL_YOUROKTADOMAIN)
        # url contains -admin string
        admin_strings = ["-admin.okta.com",
                         "-admin.oktapreview.com", "-admin.okta-emea.com"]
        if any(string in url for string in admin_strings) or "-admin" in url:
            url_errors.append(
                (f"{ERROR_MESSAGE_ORG_URL_ADMIN} "
                 f"Current value: {url}. You can copy your domain "
                 "from the Okta Developer Console. Follow these instructions "
                 f"to find it: {FINDING_OKTA_DOMAIN}"))
        # url ends with .com.com
        if url.endswith(".com.com"):
            url_errors.append((
                f"{ERROR_MESSAGE_ORG_URL_TYPO} Current "
                f"value: {url}. You can copy your domain from "
                "the Okta Developer Console. Follow these instructions to find"
                f" it: {FINDING_OKTA_DOMAIN}"))
        # url contains multiple '://' segments
        if url.count("://") > 1:
            url_errors.append((
                f"{ERROR_MESSAGE_ORG_URL_TYPO} Current "
                f"value: {url}. You can copy your domain from "
                "the Okta Developer Console. Follow these instructions to find"
                f" it: {FINDING_OKTA_DOMAIN}"))

        return url_errors

    def _validate_proxy_settings(self, proxy):
        proxy_errors = []
        if "host" not in proxy:
            proxy_errors.append(ERROR_MESSAGE_PROXY_MISSING_HOST)
        if "username" in proxy and "password" not in proxy or\
                "username" not in proxy and "password" in proxy:
            proxy_errors.append(ERROR_MESSAGE_PROXY_MISSING_AUTH)
        if "port" in proxy:
            try:
                port_number = int(proxy["port"])
                if not 1 <= port_number <= 65535:
                    raise ValueError
            except (TypeError, ValueError):
                proxy_errors.append(ERROR_MESSAGE_PROXY_INVALID_PORT)

        return proxy_errors
