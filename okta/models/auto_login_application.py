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
from okta.models.scheme_application_credentials\
    import SchemeApplicationCredentials
from okta.models.auto_login_application_settings\
    import AutoLoginApplicationSettings


class AutoLoginApplication(
    Application
):
    """
    A class for AutoLoginApplication objects.
    """

    def __init__(self, config=None):
        if config:
            if "credentials" in config:
                if isinstance(config["credentials"],
                              SchemeApplicationCredentials):
                    self.credentials = config["credentials"]
                else:
                    self.credentials = SchemeApplicationCredentials(
                        config["credentials"]
                    )
            else:
                self.credentials = None
            if "settings" in config:
                if isinstance(config["settings"],
                              AutoLoginApplicationSettings):
                    self.settings = config["settings"]
                else:
                    self.settings = AutoLoginApplicationSettings(
                        config["settings"]
                    )
            else:
                self.settings = None
        else:
            self.credentials = None
            self.settings = None
