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

from okta.models.policy\
    import Policy
from okta.models.policy_type import PolicyType
from okta.models import password_policy_conditions\
    as password_policy_conditions
from okta.models import password_policy_settings\
    as password_policy_settings


class PasswordPolicy(
    Policy
):
    """
    A class for PasswordPolicy objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.type = PolicyType("PASSWORD")
            if "conditions" in config:
                if isinstance(config["conditions"],
                              password_policy_conditions.PasswordPolicyConditions):
                    self.conditions = config["conditions"]
                elif config["conditions"] is not None:
                    self.conditions = password_policy_conditions.PasswordPolicyConditions(
                        config["conditions"]
                    )
                else:
                    self.conditions = None
            else:
                self.conditions = None
            if "settings" in config:
                if isinstance(config["settings"],
                              password_policy_settings.PasswordPolicySettings):
                    self.settings = config["settings"]
                elif config["settings"] is not None:
                    self.settings = password_policy_settings.PasswordPolicySettings(
                        config["settings"]
                    )
                else:
                    self.settings = None
            else:
                self.settings = None
        else:
            self.conditions = None
            self.settings = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "conditions": self.conditions,
            "settings": self.settings
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
