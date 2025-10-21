# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import os

import okta.models as models
from okta.models.application_sign_on_mode import ApplicationSignOnMode as ASM
from okta.models.factor_type import FactorType as FT
from okta.models.policy_type import PolicyType as PT

DEV_OKTA = "https://developer.okta.com"

FINDING_OKTA_DOMAIN = f"{DEV_OKTA}" "/docs/guides/find-your-domain/overview"
GET_OKTA_API_TOKEN = f"{DEV_OKTA}" "/docs/guides/create-an-api-token/overview"
FINDING_OKTA_APP_CRED = f"{DEV_OKTA}" "/docs/guides/find-your-app-credentials/overview"
REPO_URL = "https://github.com/okta/okta-sdk-python"

EPOCH_YEAR = 1970
EPOCH_MONTH = 1
EPOCH_DAY = 1

DATETIME_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"

_GLOBAL_YAML_PATH = os.path.join(os.path.expanduser("~"), ".okta", "okta.yaml")
_LOCAL_YAML_PATH = os.path.join(os.getcwd(), "okta.yaml")

# This dictionary is now built by iterating through all models to find the 'Application' model
# and then accessing its discriminator mapping.


OKTA_APP_SIGN_ON_TO_MODEL = {
    ASM.AUTO_LOGIN: models.AutoLoginApplication,
    ASM.BASIC_AUTH: models.BasicAuthApplication,
    ASM.BOOKMARK: models.BookmarkApplication,
    ASM.BROWSER_PLUGIN: models.BrowserPluginApplication,
    ASM.OPENID_CONNECT: models.OpenIdConnectApplication,
    ASM.SAML_1_1: models.SamlApplication,
    ASM.SAML_2_0: models.SamlApplication,
    ASM.SECURE_PASSWORD_STORE: models.SecurePasswordStoreApplication,
    ASM.WS_FEDERATION: models.WsFederationApplication,
}

SWA_APP_NAME = "template_swa"
SWA3_APP_NAME = "template_swa3field"


def find_app_model(sign_on_mode, template_name):
    # If ASM found in model map, return model
    if sign_on_mode in OKTA_APP_SIGN_ON_TO_MODEL:
        return OKTA_APP_SIGN_ON_TO_MODEL[sign_on_mode]
    # O/W must be BROWSER PLUGIN APP
    # if template_name in OKTA_APP_NAME_TO_MODEL:
    #     return OKTA_APP_NAME_TO_MODEL[template_name]
    # If nothing matches, use default basic application:
    return models.Application


OKTA_FACTOR_TYPE_TO_FACTOR = {
    FT.CALL: models.CallUserFactor,
    FT.EMAIL: models.EmailUserFactor,
    FT.PUSH: models.PushUserFactor,
    FT.QUESTION: models.SecurityQuestionUserFactor,
    FT.SMS: models.SmsUserFactor,
    FT.TOKEN: models.TokenUserFactor,
    FT.TOKEN_COLON_HARDWARE: models.HardwareUserFactor,
    FT.TOKEN_COLON_HOTP: models.CustomHotpUserFactor,
    FT.TOKEN_COLON_SOFTWARE_COLON_TOTP: models.TotpUserFactor,
    FT.U2F: models.U2fUserFactor,
    FT.WEB: models.WebUserFactor,
    FT.WEBAUTHN: models.WebAuthnUserFactor,
    FT.HOTP: models.CustomHotpUserFactor,
}


def find_factor_model(factor_type):
    return OKTA_FACTOR_TYPE_TO_FACTOR[factor_type]


OKTA_POLICY_TYPE_TO_MODEL = {
    PT.ACCESS_POLICY: models.AccessPolicy,
    PT.IDP_DISCOVERY: models.IdpDiscoveryPolicy,
    PT.MFA_ENROLL: models.MultifactorEnrollmentPolicy,
    PT.OKTA_SIGN_ON: models.OktaSignOnPolicy,
    PT.PASSWORD: models.PasswordPolicy,
    PT.PROFILE_ENROLLMENT: models.ProfileEnrollmentPolicy,
}


def find_policy_model(policy_type):
    return OKTA_POLICY_TYPE_TO_MODEL[policy_type]


OKTA_POLICY_RULE_TYPE_TO_MODEL = {
    "ACCESS_POLICY": models.AccessPolicyRule,
    "PASSWORD": models.PasswordPolicyRule,
    "PROFILE_ENROLLMENT": models.ProfileEnrollmentPolicyRule,
    "RESOURCE_ACCESS": models.AuthorizationServerPolicyRule,
    "SIGN_ON": models.OktaSignOnPolicyRule,
    "IDP_DISCOVERY": models.IdpDiscoveryPolicyRule,
}


def find_policy_rule_model(policy_rule):
    if policy_rule in OKTA_POLICY_RULE_TYPE_TO_MODEL:
        return OKTA_POLICY_RULE_TYPE_TO_MODEL[policy_rule]
    return models.PolicyRule
