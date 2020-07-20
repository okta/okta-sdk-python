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

from okta.okta_object import OktaObject
from okta.models.open_id_connect_application_type\
    import OpenIdConnectApplicationType
from okta.models.open_id_connect_application_consent_method\
    import OpenIdConnectApplicationConsentMethod
from okta.models.open_id_connect_application_issuer_mode\
    import OpenIdConnectApplicationIssuerMode


class OpenIdConnectApplicationSettingsClient(
    OktaObject
):
    """
    A class for OpenIdConnectApplicationSettingsClient objects.
    """

    def __init__(self, config=None):
        if config:
            if "applicationType" in config:
                if isinstance(config["applicationType"],
                              OpenIdConnectApplicationType):
                    self.application_type = config["applicationType"]
                else:
                    self.application_type = OpenIdConnectApplicationType(
                        config["applicationType"]
                    )
            else:
                self.application_type = None
            self.client_uri = config["clientUri"]\
                if "clientUri" in config else None
            if "consentMethod" in config:
                if isinstance(config["consentMethod"],
                              OpenIdConnectApplicationConsentMethod):
                    self.consent_method = config["consentMethod"]
                else:
                    self.consent_method = OpenIdConnectApplicationConsentMethod(
                        config["consentMethod"]
                    )
            else:
                self.consent_method = None
            self.grant_types = config["grantTypes"]\
                if "grantTypes" in config else None
            self.initiate_login_uri = config["initiateLoginUri"]\
                if "initiateLoginUri" in config else None
            if "issuerMode" in config:
                if isinstance(config["issuerMode"],
                              OpenIdConnectApplicationIssuerMode):
                    self.issuer_mode = config["issuerMode"]
                else:
                    self.issuer_mode = OpenIdConnectApplicationIssuerMode(
                        config["issuerMode"]
                    )
            else:
                self.issuer_mode = None
            self.logo_uri = config["logoUri"]\
                if "logoUri" in config else None
            self.policy_uri = config["policyUri"]\
                if "policyUri" in config else None
            self.post_logout_redirect_uris = config["postLogoutRedirectUris"]\
                if "postLogoutRedirectUris" in config else None
            self.redirect_uris = config["redirectUris"]\
                if "redirectUris" in config else None
            self.response_types = config["responseTypes"]\
                if "responseTypes" in config else None
            self.tos_uri = config["tosUri"]\
                if "tosUri" in config else None
        else:
            self.application_type = None
            self.client_uri = None
            self.consent_method = None
            self.grant_types = None
            self.initiate_login_uri = None
            self.issuer_mode = None
            self.logo_uri = None
            self.policy_uri = None
            self.post_logout_redirect_uris = None
            self.redirect_uris = None
            self.response_types = None
            self.tos_uri = None

    def request_format(self):
        return {
            "application_type": self.application_type,
            "client_uri": self.client_uri,
            "consent_method": self.consent_method,
            "grant_types": self.grant_types,
            "initiate_login_uri": self.initiate_login_uri,
            "issuer_mode": self.issuer_mode,
            "logo_uri": self.logo_uri,
            "policy_uri": self.policy_uri,
            "post_logout_redirect_uris": self.post_logout_redirect_uris,
            "redirect_uris": self.redirect_uris,
            "response_types": self.response_types,
            "tos_uri": self.tos_uri
        }
