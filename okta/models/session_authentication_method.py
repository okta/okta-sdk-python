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


class SessionAuthenticationMethod(
    str,
    MultiValueEnum
):
    """
    An enumeration class for SessionAuthenticationMethod.
    """

    PWD = "pwd", "PWD"
    SWK = "swk", "SWK"
    HWK = "hwk", "HWK"
    OTP = "otp", "OTP"
    SMS = "sms", "SMS"
    TEL = "tel", "TEL"
    GEO = "geo", "GEO"
    FPT = "fpt", "FPT"
    KBA = "kba", "KBA"
    MFA = "mfa", "MFA"
