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


class FactorType(
    str,
    MultiValueEnum
):
    """
    An enumeration class for FactorType.
    """

    CALL = "CALL", "call"
    EMAIL = "EMAIL", "email"
    PUSH = "PUSH", "push"
    QUESTION = "QUESTION", "question"
    SMS = "SMS", "sms"
    TOKEN_HARDWARE = "TOKEN:HARDWARE", "token:hardware"
    TOKEN_HOTP = "TOKEN:HOTP", "token:hotp"
    TOKEN_SOFTWARE_TOTP = "TOKEN:SOFTWARE:TOTP", "token:software:totp"
    TOKEN = "TOKEN", "token"
    U_2_F = "U2F", "u2f"
    WEB = "WEB", "web"
    WEBAUTHN = "WEBAUTHN", "webauthn"
