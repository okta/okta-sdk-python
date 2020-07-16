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
from okta.models.auto_login_application_settings_sign_on\
    import AutoLoginApplicationSettingsSignOn


class AutoLoginApplicationSettings(
    ApplicationSettings
):
    """
    A class for AutoLoginApplicationSettings objects.
    """

    def __init__(self, config=None):
        if config:
            if "signOn" in config:
                if isinstance(config["signOn"],
                              AutoLoginApplicationSettingsSignOn):
                    self.sign_on = config["signOn"]
                else:
                    self.sign_on = AutoLoginApplicationSettingsSignOn(
                        config["signOn"]
                    )
            else:
                self.sign_on = None
        else:
            self.sign_on = None
