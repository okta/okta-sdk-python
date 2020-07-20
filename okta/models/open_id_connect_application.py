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

from okta.models.application\
    import Application
from okta.models.o_auth_application_credentials\
    import OAuthApplicationCredentials
from okta.models.open_id_connect_application_settings\
    import OpenIdConnectApplicationSettings


class OpenIdConnectApplication(
    Application
):
    """
    A class for OpenIdConnectApplication objects.
    """

    def __init__(self, config=None):
        if config:
            if "credentials" in config:
                if isinstance(config["credentials"],
                              OAuthApplicationCredentials):
                    self.credentials = config["credentials"]
                else:
                    self.credentials = OAuthApplicationCredentials(
                        config["credentials"]
                    )
            else:
                self.credentials = None
            self.name = config["name"]\
                if "name" in config else None
            if "settings" in config:
                if isinstance(config["settings"],
                              OpenIdConnectApplicationSettings):
                    self.settings = config["settings"]
                else:
                    self.settings = OpenIdConnectApplicationSettings(
                        config["settings"]
                    )
            else:
                self.settings = None
        else:
            self.credentials = None
            self.name = "oidc_client"
            self.settings = None

    def request_format(self):
        return {
            "credentials": self.credentials,
            "name": self.name,
            "settings": self.settings
        }
