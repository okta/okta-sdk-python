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


class MultifactorEnrollmentPolicyAuthenticatorType(
    str,
    MultiValueEnum
):
    """
    An enumeration class for MultifactorEnrollmentPolicyAuthenticatorType.
    """

    CUSTOM_APP = "custom_app", "CUSTOM_APP"
    CUSTOM_OTP = "custom_otp", "CUSTOM_OTP"
    DUO = "duo", "DUO"
    EXTERNAL_IDP = "external_idp", "EXTERNAL_IDP"
    GOOGLE_OTP = "google_otp", "GOOGLE_OTP"
    OKTA_EMAIL = "okta_email", "OKTA_EMAIL"
    OKTA_PASSWORD = "okta_password", "OKTA_PASSWORD"
    OKTA_VERIFY = "okta_verify", "OKTA_VERIFY"
    ONPREM_MFA = "onprem_mfa", "ONPREM_MFA"
    PHONE_NUMBER = "phone_number", "PHONE_NUMBER"
    RSA_TOKEN = "rsa_token", "RSA_TOKEN"
    SECURITY_QUESTION = "security_question", "SECURITY_QUESTION"
    SYMANTEC_VIP = "symantec_vip", "SYMANTEC_VIP"
    WEBAUTHN = "webauthn", "WEBAUTHN"
    YUBIKEY_TOKEN = "yubikey_token", "YUBIKEY_TOKEN"
