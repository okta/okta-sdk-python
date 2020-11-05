import os
import okta.models as models
from okta.models.application_sign_on_mode import ApplicationSignOnMode as ASM
from okta.models.factor_type import FactorType as FT
from okta.models.policy_type import PolicyType as PT

DEV_OKTA = "https://developer.okta.com"

FINDING_OKTA_DOMAIN = (f"{DEV_OKTA}"
                       "/docs/guides/find-your-domain/overview")
GET_OKTA_API_TOKEN = (f"{DEV_OKTA}"
                      "/docs/guides/create-an-api-token/overview")
FINDING_OKTA_APP_CRED = (f"{DEV_OKTA}"
                         "/docs/guides/find-your-app-credentials/overview")
REPO_URL = "https://github.com/okta/okta-sdk-python"

EPOCH_YEAR = 1970
EPOCH_MONTH = 1
EPOCH_DAY = 1

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

_GLOBAL_YAML_PATH = os.path.join(os.path.expanduser('~'), ".okta",
                                 "okta.yaml")
_LOCAL_YAML_PATH = os.path.join(os.getcwd(), "okta.yaml")

OKTA_APP_SIGN_ON_TO_MODEL = {
    ASM.AUTO_LOGIN: models.AutoLoginApplication,
    ASM.BASIC_AUTH: models.BasicAuthApplication,
    ASM.BOOKMARK: models.BookmarkApplication,
    ASM.OPENID_CONNECT: models.OpenIdConnectApplication,
    ASM.SAML_1_1: models.SamlApplication,
    ASM.SAML_2_0: models.SamlApplication,
    ASM.SECURE_PASSWORD_STORE: models.SecurePasswordStoreApplication,
    ASM.WS_FEDERATION: models.WsFederationApplication
}

OKTA_APP_NAME_TO_MODEL = {
    "template_swa": models.SwaApplication,
    "template_swa3field": models.SwaThreeFieldApplication
}

SWA_APP_NAME = "template_swa"
SWA3_APP_NAME = "template_swa3field"


def find_app_model(sign_on_mode, template_name):
    # If ASM found in model map, return model
    if sign_on_mode in OKTA_APP_SIGN_ON_TO_MODEL:
        return OKTA_APP_SIGN_ON_TO_MODEL[sign_on_mode]
    # O/W must be BROWSER PLUGIN APP
    return OKTA_APP_NAME_TO_MODEL[template_name]


OKTA_FACTOR_TYPE_TO_FACTOR = {
    FT.CALL: models.CallUserFactor,
    FT.EMAIL: models.EmailUserFactor,
    FT.PUSH: models.PushUserFactor,
    FT.QUESTION: models.SecurityQuestionUserFactor,
    FT.SMS: models.SmsUserFactor,
    FT.TOKEN: models.TokenUserFactor,
    FT.TOKEN_HARDWARE: models.HardwareUserFactor,
    FT.TOKEN_HOTP: models.CustomHotpUserFactor,
    FT.TOKEN_SOFTWARE_TOTP: models.TotpUserFactor,
    FT.U_2_F: models.U2FUserFactor,
    FT.WEB: models.WebUserFactor,
    FT.WEBAUTHN: models.WebAuthnUserFactor
}


def find_factor_model(factor_type):
    return OKTA_FACTOR_TYPE_TO_FACTOR[factor_type]


OKTA_POLICY_TYPE_TO_MODEL = {
    PT.IDP_DISCOVERY: models.IdentityProviderPolicy,
    PT.OAUTH_AUTHORIZATION_POLICY: models.OAuthAuthorizationPolicy,
    PT.OKTA_SIGN_ON: models.OktaSignOnPolicy,
    PT.PASSWORD: models.PasswordPolicy
}


def find_policy_model(policy_type):
    return OKTA_POLICY_TYPE_TO_MODEL[policy_type]


OKTA_POLICY_RULE_TYPE_TO_MODEL = {
    "PASSWORD": models.PasswordPolicyRule,
    "SIGN_ON": models.OktaSignOnPolicyRule
}


def find_policy_rule_model(policy_rule):
    if policy_rule in OKTA_POLICY_RULE_TYPE_TO_MODEL:
        return OKTA_POLICY_RULE_TYPE_TO_MODEL[policy_rule]
    return models.PolicyRule
