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

from okta.models.policy\
    import Policy
from okta.models.password_policy_conditions\
    import PasswordPolicyConditions
from okta.models.password_policy_settings\
    import PasswordPolicySettings


class PasswordPolicy(
    Policy
):
    """
    A class for PasswordPolicy objects.
    """

    def __init__(self, config=None):
        if config:
            if "conditions" in config:
                if isinstance(config["conditions"],
                              PasswordPolicyConditions):
                    self.conditions = config["conditions"]
                else:
                    self.conditions = PasswordPolicyConditions(
                        config["conditions"]
                    )
            else:
                self.conditions = None
            if "settings" in config:
                if isinstance(config["settings"],
                              PasswordPolicySettings):
                    self.settings = config["settings"]
                else:
                    self.settings = PasswordPolicySettings(
                        config["settings"]
                    )
            else:
                self.settings = None
        else:
            self.conditions = None
            self.settings = None

    def request_format(self):
        return {
            "conditions": self.conditions,
            "settings": self.settings
        }
