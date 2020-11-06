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

from okta.models.application\
    import Application
from okta.models import scheme_application_credentials\
    as scheme_application_credentials
from okta.models import auto_login_application_settings\
    as auto_login_application_settings


class AutoLoginApplication(
    Application
):
    """
    A class for AutoLoginApplication objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.sign_on_mode = "AUTO_LOGIN"
            if "credentials" in config:
                if isinstance(config["credentials"],
                              scheme_application_credentials.SchemeApplicationCredentials):
                    self.credentials = config["credentials"]
                elif config["credentials"] is not None:
                    self.credentials = scheme_application_credentials.SchemeApplicationCredentials(
                        config["credentials"]
                    )
                else:
                    self.credentials = None
            else:
                self.credentials = None
            if "settings" in config:
                if isinstance(config["settings"],
                              auto_login_application_settings.AutoLoginApplicationSettings):
                    self.settings = config["settings"]
                elif config["settings"] is not None:
                    self.settings = auto_login_application_settings.AutoLoginApplicationSettings(
                        config["settings"]
                    )
                else:
                    self.settings = None
            else:
                self.settings = None
        else:
            self.credentials = None
            self.settings = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "credentials": self.credentials,
            "settings": self.settings
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
