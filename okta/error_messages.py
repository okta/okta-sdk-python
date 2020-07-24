from okta.constants import FINDING_OKTA_APP_CRED, FINDING_OKTA_DOMAIN, \
    GET_OKTA_API_TOKEN

ERROR_MESSAGE_ORG_URL_MISSING = (
    "Your Okta URL is missing. You can copy "
    "your domain from the Okta Developer "
    "Console. Follow these instructions to"
    f" find it: {FINDING_OKTA_DOMAIN}"
)
ERROR_MESSAGE_ORG_URL_NOT_HTTPS = (
    "Your Okta URL must start with 'https'."
)
ERROR_MESSAGE_AUTH_MODE_INVALID = (
    "The AuthorizationMode configuration "
    "option must be one of: "
    "[SSWS, PrivateKey]. "
    "You provided the SDK with "
)
ERROR_MESSAGE_ORG_URL_YOUROKTADOMAIN = (
    "Replace {{yourOktaDomain}} with your Okta domain. "
    "You can copy your domain from the Okta Developer Console. "
    "Follow these instructions to find it: "
    f"{FINDING_OKTA_DOMAIN}"
)

ERROR_MESSAGE_ORG_URL_ADMIN = (
    "Your Okta domain should not contain -admin. "
)

ERROR_MESSAGE_ORG_URL_TYPO = (
    "It looks like there's a typo in your Okta domain."
)

ERROR_MESSAGE_API_TOKEN_MISSING = (
    "Your Okta API token is missing. "
    "You can generate one in the Okta Developer"
    " Console. Follow these instructions:"
    f" {GET_OKTA_API_TOKEN}"
)

ERROR_MESSAGE_API_TOKEN_DEFAULT = (
    "Replace {{apiToken}} with your Okta API token. "
    "You can generate one in the Okta Developer Console. "
    f"Follow these instructions: {GET_OKTA_API_TOKEN}"
)

ERROR_MESSAGE_CLIENT_ID_MISSING = (
    "Your client ID is missing. You can copy it from the "
    "Okta Developer Console in the details for the Application "
    "you created. Follow these instructions to find it: "
    f"{FINDING_OKTA_APP_CRED}"
)

ERROR_MESSAGE_CLIENT_ID_DEFAULT = (
    "Replace {{clientId}} with the client ID of your Application. "
    "You can copy it from the Okta Developer Console in the "
    "details for the Application you created. Follow these "
    f"instructions to find it: {FINDING_OKTA_APP_CRED}"
)

ERROR_MESSAGE_SCOPES_PK_MISSING = (
    "When using authorization mode 'PrivateKey', you must supply "
    "'okta.client.scopes' and 'okta.client.privateKey'"
)

ERROR_MESSAGE_429_MISSING_DATE_X_RESET = (
    "429 response must have the 'X-Rate-Limit-Reset' and 'Date' headers"
)

ERROR_MESSAGE_PROXY_MISSING_HOST = (
    "Please add a host URL to your proxy configuration."
)

ERROR_MESSAGE_PROXY_MISSING_AUTH = (
    "Proxy configuration must include BOTH your username and password "
    "if authentication is required"
)

ERROR_MESSAGE_PROXY_INVALID_PORT = (
    "Proxy port number must be a number, and between 1 and 65535 (inclusive)"
)
