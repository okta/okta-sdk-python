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
from okta.models import password_policy_password_settings_age\
    as password_policy_password_settings_age
from okta.models import password_policy_password_settings_complexity\
    as password_policy_password_settings_complexity
from okta.models import password_policy_password_settings_lockout\
    as password_policy_password_settings_lockout


class PasswordPolicyPasswordSettings(
    OktaObject
):
    """
    A class for PasswordPolicyPasswordSettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "age" in config:
                if isinstance(config["age"],
                              password_policy_password_settings_age.PasswordPolicyPasswordSettingsAge):
                    self.age = config["age"]
                elif config["age"] is not None:
                    self.age = password_policy_password_settings_age.PasswordPolicyPasswordSettingsAge(
                        config["age"]
                    )
                else:
                    self.age = None
            else:
                self.age = None
            if "complexity" in config:
                if isinstance(config["complexity"],
                              password_policy_password_settings_complexity.PasswordPolicyPasswordSettingsComplexity):
                    self.complexity = config["complexity"]
                elif config["complexity"] is not None:
                    self.complexity = password_policy_password_settings_complexity.PasswordPolicyPasswordSettingsComplexity(
                        config["complexity"]
                    )
                else:
                    self.complexity = None
            else:
                self.complexity = None
            if "lockout" in config:
                if isinstance(config["lockout"],
                              password_policy_password_settings_lockout.PasswordPolicyPasswordSettingsLockout):
                    self.lockout = config["lockout"]
                elif config["lockout"] is not None:
                    self.lockout = password_policy_password_settings_lockout.PasswordPolicyPasswordSettingsLockout(
                        config["lockout"]
                    )
                else:
                    self.lockout = None
            else:
                self.lockout = None
        else:
            self.age = None
            self.complexity = None
            self.lockout = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "age": self.age,
            "complexity": self.complexity,
            "lockout": self.lockout
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
