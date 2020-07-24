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
from okta.models.password_dictionary\
    import PasswordDictionary


class PasswordPolicyPasswordSettingsComplexity(
    OktaObject
):
    """
    A class for PasswordPolicyPasswordSettingsComplexity objects.
    """

    def __init__(self, config=None):
        if config:
            if "dictionary" in config:
                if isinstance(config["dictionary"],
                              PasswordDictionary):
                    self.dictionary = config["dictionary"]
                else:
                    self.dictionary = PasswordDictionary(
                        config["dictionary"]
                    )
            else:
                self.dictionary = None
            self.exclude_attributes = config["excludeAttributes"]\
                if "excludeAttributes" in config else None
            self.exclude_username = config["excludeUsername"]\
                if "excludeUsername" in config else None
            self.min_length = config["minLength"]\
                if "minLength" in config else None
            self.min_lower_case = config["minLowerCase"]\
                if "minLowerCase" in config else None
            self.min_number = config["minNumber"]\
                if "minNumber" in config else None
            self.min_symbol = config["minSymbol"]\
                if "minSymbol" in config else None
            self.min_upper_case = config["minUpperCase"]\
                if "minUpperCase" in config else None
        else:
            self.dictionary = None
            self.exclude_attributes = "1"
            self.exclude_username = "true"
            self.min_length = "8"
            self.min_lower_case = "1"
            self.min_number = "1"
            self.min_symbol = "1"
            self.min_upper_case = "1"

    def request_format(self):
        return {
            "dictionary": self.dictionary,
            "excludeAttributes": self.exclude_attributes,
            "excludeUsername": self.exclude_username,
            "minLength": self.min_length,
            "minLowerCase": self.min_lower_case,
            "minNumber": self.min_number,
            "minSymbol": self.min_symbol,
            "minUpperCase": self.min_upper_case
        }
