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
from okta.models.application_settings_application\
    import ApplicationSettingsApplication


class SwaApplicationSettingsApplication(
    OktaObject,
    ApplicationSettingsApplication
):
    def __init__(self, config=None):
        if config:
            self.button_field = config["buttonField"]\
                if "buttonField" in config else None
            self.login_url_regex = config["loginUrlRegex"]\
                if "loginUrlRegex" in config else None
            self.password_field = config["passwordField"]\
                if "passwordField" in config else None
            self.url = config["url"]\
                if "url" in config else None
            self.username_field = config["usernameField"]\
                if "usernameField" in config else None
        else:
            self.button_field = None
            self.login_url_regex = None
            self.password_field = None
            self.url = None
            self.username_field = None