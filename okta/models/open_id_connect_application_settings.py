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

from okta.models.application_settings\
    import ApplicationSettings
from okta.models import open_id_connect_application_settings_client\
    as open_id_connect_application_settings_client


class OpenIdConnectApplicationSettings(
    ApplicationSettings
):
    """
    A class for OpenIdConnectApplicationSettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "oauthClient" in config:
                if isinstance(config["oauthClient"],
                              open_id_connect_application_settings_client.OpenIdConnectApplicationSettingsClient):
                    self.oauth_client = config["oauthClient"]
                elif config["oauthClient"] is not None:
                    self.oauth_client = open_id_connect_application_settings_client.OpenIdConnectApplicationSettingsClient(
                        config["oauthClient"]
                    )
                else:
                    self.oauth_client = None
            else:
                self.oauth_client = None
        else:
            self.oauth_client = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "oauthClient": self.oauth_client
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
