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

from enum import Enum


class ApplicationSignOnMode(
    str,
    Enum
):
    BOOKMARK = "BOOKMARK"
    BASIC_AUTH = "BASIC_AUTH"
    BROWSER_PLUGIN = "BROWSER_PLUGIN"
    SECURE_PASSWORD_STORE = "SECURE_PASSWORD_STORE"
    AUTO_LOGIN = "AUTO_LOGIN"
    WS_FEDERATION = "WS_FEDERATION"
    SAML_2_0 = "SAML_2_0"
    OPENID_CONNECT = "OPENID_CONNECT"
    SAML_1_1 = "SAML_1_1"