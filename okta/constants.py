import os
import okta.models as models
from okta.models.application_sign_on_mode import ApplicationSignOnMode as ASM

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

DATETIME_STRING_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"

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
    ASM.WS_FEDERATION: models.WsFederationApplication,
}

SWA_APP_NAME = "template_swa"

SWA3_APP_NAME = "template_swa3field"


def find_app_model(sign_on_mode, template_name):
    # If ASM found in model map, return model
    if sign_on_mode in OKTA_APP_SIGN_ON_TO_MODEL:
        return OKTA_APP_SIGN_ON_TO_MODEL[sign_on_mode]
    # O/W must be BROWSER PLUGIN APP
    if template_name == SWA_APP_NAME:
        return models.SwaApplication
    # O/W SWA 3
    return models.SwaThreeFieldApplication
