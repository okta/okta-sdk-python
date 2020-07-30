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

from enum import Enum


class InlineHookType(
    str,
    Enum
):
    """
    An enumeration class for InlineHookType.
    """

    COM_OKTA_OAUTH_2_TOKENS_TRANSFORM = "com.okta.oauth2.tokens.transform"
    COM_OKTA_IMPORT_TRANSFORM = "com.okta.import.transform"
    COM_OKTA_SAML_TOKENS_TRANSFORM = "com.okta.saml.tokens.transform"
    COM_OKTA_USER_PRE_REGISTRATION = "com.okta.user.pre-registration"
    COM_OKTA_USER_CREDENTIAL_PASSWORD_IMPORT = "com.okta.user.credential.password.import"
