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


class ApplicationSettingsApplication(
    OktaObject
):
    """
    A class for ApplicationSettingsApplication objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.acs_url = config["acsUrl"]\
                if "acsUrl" in config else None
            self.button_field = config["buttonField"]\
                if "buttonField" in config else None
            self.login_url_regex = config["loginUrlRegex"]\
                if "loginUrlRegex" in config else None
            self.org_name = config["orgName"]\
                if "orgName" in config else None
            self.password_field = config["passwordField"]\
                if "passwordField" in config else None
            self.url = config["url"]\
                if "url" in config else None
            self.username_field = config["usernameField"]\
                if "usernameField" in config else None
        else:
            self.acs_url = None
            self.button_field = None
            self.login_url_regex = None
            self.org_name = None
            self.password_field = None
            self.url = None
            self.username_field = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "acsUrl": self.acs_url,
            "buttonField": self.button_field,
            "loginUrlRegex": self.login_url_regex,
            "orgName": self.org_name,
            "passwordField": self.password_field,
            "url": self.url,
            "usernameField": self.username_field
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
