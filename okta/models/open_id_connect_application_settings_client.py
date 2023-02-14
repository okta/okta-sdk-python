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

from okta.okta_object import OktaObject
from okta.okta_collection import OktaCollection
from okta.models import open_id_connect_application_type\
    as open_id_connect_application_type
from okta.models import open_id_connect_application_consent_method\
    as open_id_connect_application_consent_method
from okta.models import o_auth_grant_type\
    as o_auth_grant_type
from okta.models import open_id_connect_application_idp_initiated_login\
    as open_id_connect_application_idp_initiated_login
from okta.models import open_id_connect_application_issuer_mode\
    as open_id_connect_application_issuer_mode
from okta.models import open_id_connect_application_settings_client_keys\
    as open_id_connect_application_settings_client_keys
from okta.models import open_id_connect_application_settings_refresh_token\
    as open_id_connect_application_settings_refresh_token
from okta.models import o_auth_response_type\
    as o_auth_response_type


class OpenIdConnectApplicationSettingsClient(
    OktaObject
):
    """
    A class for OpenIdConnectApplicationSettingsClient objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "application_type" in config:
                if isinstance(config["application_type"],
                              open_id_connect_application_type.OpenIdConnectApplicationType):
                    self.application_type = config["application_type"]
                elif config["application_type"] is not None:
                    self.application_type = open_id_connect_application_type.OpenIdConnectApplicationType(
                        config["application_type"].upper()
                    )
                else:
                    self.application_type = None
            else:
                self.application_type = None
            self.client_uri = config["client_uri"]\
                if "client_uri" in config else None
            if "consent_method" in config:
                if isinstance(config["consent_method"],
                              open_id_connect_application_consent_method.OpenIdConnectApplicationConsentMethod):
                    self.consent_method = config["consent_method"]
                elif config["consent_method"] is not None:
                    self.consent_method = open_id_connect_application_consent_method.OpenIdConnectApplicationConsentMethod(
                        config["consent_method"].upper()
                    )
                else:
                    self.consent_method = None
            else:
                self.consent_method = None
            self.grant_types = OktaCollection.form_list(
                config["grant_types"] if "grant_types"\
                    in config else [],
                o_auth_grant_type.OAuthGrantType
            )
            if "idp_initiated_login" in config:
                if isinstance(config["idp_initiated_login"],
                              open_id_connect_application_idp_initiated_login.OpenIdConnectApplicationIdpInitiatedLogin):
                    self.idp_initiated_login = config["idp_initiated_login"]
                elif config["idp_initiated_login"] is not None:
                    self.idp_initiated_login = open_id_connect_application_idp_initiated_login.OpenIdConnectApplicationIdpInitiatedLogin(
                        config["idp_initiated_login"]
                    )
                else:
                    self.idp_initiated_login = None
            else:
                self.idp_initiated_login = None
            self.initiate_login_uri = config["initiate_login_uri"]\
                if "initiate_login_uri" in config else None
            if "issuer_mode" in config:
                if isinstance(config["issuer_mode"],
                              open_id_connect_application_issuer_mode.OpenIdConnectApplicationIssuerMode):
                    self.issuer_mode = config["issuer_mode"]
                elif config["issuer_mode"] is not None:
                    self.issuer_mode = open_id_connect_application_issuer_mode.OpenIdConnectApplicationIssuerMode(
                        config["issuer_mode"].upper()
                    )
                else:
                    self.issuer_mode = None
            else:
                self.issuer_mode = None
            if "jwks" in config:
                if isinstance(config["jwks"],
                              open_id_connect_application_settings_client_keys.OpenIdConnectApplicationSettingsClientKeys):
                    self.jwks = config["jwks"]
                elif config["jwks"] is not None:
                    self.jwks = open_id_connect_application_settings_client_keys.OpenIdConnectApplicationSettingsClientKeys(
                        config["jwks"]
                    )
                else:
                    self.jwks = None
            else:
                self.jwks = None
            self.logo_uri = config["logo_uri"]\
                if "logo_uri" in config else None
            self.policy_uri = config["policy_uri"]\
                if "policy_uri" in config else None
            self.post_logout_redirect_uris = OktaCollection.form_list(
                config["post_logout_redirect_uris"] if "post_logout_redirect_uris"\
                    in config else [],
                str
            )
            self.redirect_uris = OktaCollection.form_list(
                config["redirect_uris"] if "redirect_uris"\
                    in config else [],
                str
            )
            if "refresh_token" in config:
                if isinstance(config["refresh_token"],
                              open_id_connect_application_settings_refresh_token.OpenIdConnectApplicationSettingsRefreshToken):
                    self.refresh_token = config["refresh_token"]
                elif config["refresh_token"] is not None:
                    self.refresh_token = open_id_connect_application_settings_refresh_token.OpenIdConnectApplicationSettingsRefreshToken(
                        config["refresh_token"]
                    )
                else:
                    self.refresh_token = None
            else:
                self.refresh_token = None
            self.response_types = OktaCollection.form_list(
                config["response_types"] if "response_types"\
                    in config else [],
                o_auth_response_type.OAuthResponseType
            )
            self.tos_uri = config["tos_uri"]\
                if "tos_uri" in config else None
            self.wildcard_redirect = config["wildcard_redirect"]\
                if "wildcard_redirect" in config else None
        else:
            self.application_type = None
            self.client_uri = None
            self.consent_method = None
            self.grant_types = []
            self.idp_initiated_login = None
            self.initiate_login_uri = None
            self.issuer_mode = None
            self.jwks = None
            self.logo_uri = None
            self.policy_uri = None
            self.post_logout_redirect_uris = []
            self.redirect_uris = []
            self.refresh_token = None
            self.response_types = []
            self.tos_uri = None
            self.wildcard_redirect = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "application_type": self.application_type,
            "client_uri": self.client_uri,
            "consent_method": self.consent_method,
            "grant_types": self.grant_types,
            "idp_initiated_login": self.idp_initiated_login,
            "initiate_login_uri": self.initiate_login_uri,
            "issuer_mode": self.issuer_mode,
            "jwks": self.jwks,
            "logo_uri": self.logo_uri,
            "policy_uri": self.policy_uri,
            "post_logout_redirect_uris": self.post_logout_redirect_uris,
            "redirect_uris": self.redirect_uris,
            "refresh_token": self.refresh_token,
            "response_types": self.response_types,
            "tos_uri": self.tos_uri,
            "wildcard_redirect": self.wildcard_redirect
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
