# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

from okta.constants import FINDING_OKTA_APP_CRED, FINDING_OKTA_DOMAIN, \
    GET_OKTA_API_TOKEN

ERROR_MESSAGE_ORG_URL_MISSING = (
    f"Your Okta URL is missing. You can copy your domain from the Okta Developer Console. Follow these instructions to find "
    f"it: {FINDING_OKTA_DOMAIN}"
)

ERROR_MESSAGE_ORG_URL_NOT_HTTPS = (
    "Your Okta URL must start with &#39;https&#39;."
)

ERROR_MESSAGE_AUTH_MODE_INVALID = (
    "The AuthorizationMode configuration option must be one of: [SSWS, Bearer, PrivateKey]. You provided the SDK with "
)

ERROR_MESSAGE_ORG_URL_YOUROKTADOMAIN = (
    f"Replace {{yourOktaDomain}} with your Okta domain. You can copy your domain from the Okta Developer Console. Follow "
    f"these instructions to find it: {FINDING_OKTA_DOMAIN}"
)

ERROR_MESSAGE_ORG_URL_ADMIN = (
    "Your Okta domain should not contain -admin. "
)

ERROR_MESSAGE_ORG_URL_TYPO = (
    "It looks like there&#39;s a typo in your Okta domain."
)

ERROR_MESSAGE_API_TOKEN_MISSING = (
    f"Your Okta API token is missing. You can generate one in the Okta Developer Console. Follow these instructions: "
    f"{GET_OKTA_API_TOKEN}"
)

ERROR_MESSAGE_API_TOKEN_DEFAULT = (
    f"Replace {{apiToken}} with your Okta API token. You can generate one in the Okta Developer Console. Follow these "
    f"instructions: {GET_OKTA_API_TOKEN}"
)

ERROR_MESSAGE_CLIENT_ID_MISSING = (
    f"Your client ID is missing. You can copy it from the Okta Developer Console in the details for the Application you "
    f"created. Follow these instructions to find it: {FINDING_OKTA_APP_CRED}"
)

ERROR_MESSAGE_CLIENT_ID_DEFAULT = (
    f"Replace {{clientId}} with the client ID of your Application. You can copy it from the Okta Developer Console in the "
    f"details for the Application you created. Follow these instructions to find it: {FINDING_OKTA_APP_CRED}"
)

ERROR_MESSAGE_SCOPES_PK_MISSING = (
    "When using authorization mode &#39;PrivateKey&#39;, you must supply &#39;okta.client.scopes&#39; and "
    "&#39;okta.client.privateKey&#39;"
)

ERROR_MESSAGE_429_MISSING_DATE_X_RESET = (
    "429 response must have the &#39;X-Rate-Limit-Reset&#39; and &#39;Date&#39; headers"
)

ERROR_MESSAGE_PROXY_MISSING_HOST = (
    "Please add a host URL to your proxy configuration."
)

ERROR_MESSAGE_PROXY_MISSING_AUTH = (
    "Proxy configuration must include BOTH your username and password if authentication is required"
)

ERROR_MESSAGE_PROXY_INVALID_PORT = (
    "Proxy port number must be a number, and between 1 and 65535 (inclusive)"
)
