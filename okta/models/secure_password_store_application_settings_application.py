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


class SecurePasswordStoreApplicationSettingsApplication:
    def __init__(self, config=None):
        if config:
            self.optional_field_1 = config["optionalField1"]
            self.optional_field_1_value = config["optionalField1Value"]
            self.optional_field_2 = config["optionalField2"]
            self.optional_field_2_value = config["optionalField2Value"]
            self.optional_field_3 = config["optionalField3"]
            self.optional_field_3_value = config["optionalField3Value"]
            self.password_field = config["passwordField"]
            self.url = config["url"]
            self.username_field = config["usernameField"]
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

# End of File Generation
