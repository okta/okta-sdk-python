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


class ApplicationSignOnMode(
    str,
    MultiValueEnum
):
    """
    An enumeration class for ApplicationSignOnMode.
    """

    BOOKMARK = "BOOKMARK", "bookmark"
    BASIC_AUTH = "BASIC_AUTH", "basic_auth"
    BROWSER_PLUGIN = "BROWSER_PLUGIN", "browser_plugin"
    SECURE_PASSWORD_STORE = "SECURE_PASSWORD_STORE", "secure_password_store"
    AUTO_LOGIN = "AUTO_LOGIN", "auto_login"
    WS_FEDERATION = "WS_FEDERATION", "ws_federation"
    SAML_2_0 = "SAML_2_0", "saml_2_0"
    OPENID_CONNECT = "OPENID_CONNECT", "openid_connect"
    SAML_1_1 = "SAML_1_1", "saml_1_1"
