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

from okta.models.application_settings_application\
    import ApplicationSettingsApplication


class SwaThreeFieldApplicationSettingsApplication(
    ApplicationSettingsApplication
):
    """
    A class for SwaThreeFieldApplicationSettingsApplication objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.button_selector = config["buttonSelector"]\
                if "buttonSelector" in config else None
            self.extra_field_selector = config["extraFieldSelector"]\
                if "extraFieldSelector" in config else None
            self.extra_field_value = config["extraFieldValue"]\
                if "extraFieldValue" in config else None
            self.login_url_regex = config["loginUrlRegex"]\
                if "loginUrlRegex" in config else None
            self.password_selector = config["passwordSelector"]\
                if "passwordSelector" in config else None
            self.target_url = config["targetUrl"]\
                if "targetUrl" in config else None
            self.user_name_selector = config["userNameSelector"]\
                if "userNameSelector" in config else None
        else:
            self.button_selector = None
            self.extra_field_selector = None
            self.extra_field_value = None
            self.login_url_regex = None
            self.password_selector = None
            self.target_url = None
            self.user_name_selector = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "buttonSelector": self.button_selector,
            "extraFieldSelector": self.extra_field_selector,
            "extraFieldValue": self.extra_field_value,
            "loginUrlRegex": self.login_url_regex,
            "passwordSelector": self.password_selector,
            "targetURL": self.target_url,
            "userNameSelector": self.user_name_selector
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
