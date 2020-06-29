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


from urllib.parse import urlencode


class OpenIdConnectApplicationSettingsClient:
    def __init__(self, config=None):
        if config:
            self.application_type = config["application_type"]
            self.client_uri = config["client_uri"]
            self.consent_method = config["consent_method"]
            self.grant_types = config["grant_types"]
            self.initiate_login_uri = config["initiate_login_uri"]
            self.issuer_mode = config["issuer_mode"]
            self.logo_uri = config["logo_uri"]
            self.policy_uri = config["policy_uri"]
            self.post_logout_redirect_uris = config["post_logout_redirect_uris"]
            self.redirect_uris = config["redirect_uris"]
            self.response_types = config["response_types"]
            self.tos_uri = config["tos_uri"]
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


# End of File Generation
