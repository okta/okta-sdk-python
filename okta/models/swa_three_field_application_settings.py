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
from okta.models.swa_three_field_application_settings_application\
    import SwaThreeFieldApplicationSettingsApplication


class SwaThreeFieldApplicationSettings(
    ApplicationSettings
):
    """
    A class for SwaThreeFieldApplicationSettings objects.
    """

    def __init__(self, config=None):
        if config:
            if "app" in config:
                if isinstance(config["app"],
                              SwaThreeFieldApplicationSettingsApplication):
                    self.app = config["app"]
                else:
                    self.app = SwaThreeFieldApplicationSettingsApplication(
                        config["app"]
                    )
            else:
                self.app = None
        else:
            self.app = None

    def request_format(self):
        return {
            "app": self.app
        }
