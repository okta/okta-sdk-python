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
from okta.okta_collection import OktaCollection
from okta.models import password_dictionary\
    as password_dictionary


class PasswordPolicyPasswordSettingsComplexity(
    OktaObject
):
    """
    A class for PasswordPolicyPasswordSettingsComplexity objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "dictionary" in config:
                if isinstance(config["dictionary"],
                              password_dictionary.PasswordDictionary):
                    self.dictionary = config["dictionary"]
                elif config["dictionary"] is not None:
                    self.dictionary = password_dictionary.PasswordDictionary(
                        config["dictionary"]
                    )
                else:
                    self.dictionary = None
            else:
                self.dictionary = None
            self.exclude_attributes = OktaCollection.form_list(
                config["excludeAttributes"] if "excludeAttributes"\
                    in config else [],
                str
            )
            self.exclude_username = config["excludeUsername"]\
                if "excludeUsername" in config else True
            self.min_length = config["minLength"]\
                if "minLength" in config else 8
            self.min_lower_case = config["minLowerCase"]\
                if "minLowerCase" in config else 1
            self.min_number = config["minNumber"]\
                if "minNumber" in config else 1
            self.min_symbol = config["minSymbol"]\
                if "minSymbol" in config else 1
            self.min_upper_case = config["minUpperCase"]\
                if "minUpperCase" in config else 1
        else:
            self.dictionary = None
            self.exclude_attributes = 1
            self.exclude_username = True
            self.min_length = 8
            self.min_lower_case = 1
            self.min_number = 1
            self.min_symbol = 1
            self.min_upper_case = 1

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "dictionary": self.dictionary,
            "excludeAttributes": self.exclude_attributes,
            "excludeUsername": self.exclude_username,
            "minLength": self.min_length,
            "minLowerCase": self.min_lower_case,
            "minNumber": self.min_number,
            "minSymbol": self.min_symbol,
            "minUpperCase": self.min_upper_case
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
