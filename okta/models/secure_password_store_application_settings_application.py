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


class SecurePasswordStoreApplicationSettingsApplication(
    ApplicationSettingsApplication
):
    """
    A class for SecurePasswordStoreApplicationSettingsApplication objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.optional_field_1 = config["optionalField1"]\
                if "optionalField1" in config else None
            self.optional_field_1_value = config["optionalField1Value"]\
                if "optionalField1Value" in config else None
            self.optional_field_2 = config["optionalField2"]\
                if "optionalField2" in config else None
            self.optional_field_2_value = config["optionalField2Value"]\
                if "optionalField2Value" in config else None
            self.optional_field_3 = config["optionalField3"]\
                if "optionalField3" in config else None
            self.optional_field_3_value = config["optionalField3Value"]\
                if "optionalField3Value" in config else None
            self.password_field = config["passwordField"]\
                if "passwordField" in config else None
            self.url = config["url"]\
                if "url" in config else None
            self.username_field = config["usernameField"]\
                if "usernameField" in config else None
        else:
            self.optional_field_1 = None
            self.optional_field_1_value = None
            self.optional_field_2 = None
            self.optional_field_2_value = None
            self.optional_field_3 = None
            self.optional_field_3_value = None
            self.password_field = None
            self.url = None
            self.username_field = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "optionalField1": self.optional_field_1,
            "optionalField1Value": self.optional_field_1_value,
            "optionalField2": self.optional_field_2,
            "optionalField2Value": self.optional_field_2_value,
            "optionalField3": self.optional_field_3,
            "optionalField3Value": self.optional_field_3_value,
            "passwordField": self.password_field,
            "url": self.url,
            "usernameField": self.username_field
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
