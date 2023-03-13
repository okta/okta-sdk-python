# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from aenum import MultiValueEnum


class OAuthGrantType(
    str,
    MultiValueEnum
):
    """
    An enumeration class for OAuthGrantType.
    """

    AUTHORIZATION_CODE = "authorization_code", "AUTHORIZATION_CODE"
    IMPLICIT = "implicit", "IMPLICIT"
    PASSWORD = "password", "PASSWORD"
    REFRESH_TOKEN = "refresh_token", "REFRESH_TOKEN"
    CLIENT_CREDENTIALS = "client_credentials", "CLIENT_CREDENTIALS"
    SAML_2_BEARER = "urn:ietf:params:oauth:grant-type:saml2-bearer", "URN:IETF:PARAMS:OAUTH:GRANT-TYPE:SAML2-BEARER"
    DEVICE_CODE = "urn:ietf:params:oauth:grant-type:device_code", "URN:IETF:PARAMS:OAUTH:GRANT-TYPE:DEVICE_CODE"
    TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange", "URN:IETF:PARAMS:OAUTH:GRANT-TYPE:TOKEN-EXCHANGE"
    INTERACTION_CODE = "interaction_code", "INTERACTION_CODE"
