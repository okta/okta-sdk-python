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
from okta.models import password_policy_delegation_settings\
    as password_policy_delegation_settings
from okta.models import password_policy_password_settings\
    as password_policy_password_settings
from okta.models import password_policy_recovery_settings\
    as password_policy_recovery_settings


class PasswordPolicySettings(
    OktaObject
):
    """
    A class for PasswordPolicySettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "delegation" in config:
                if isinstance(config["delegation"],
                              password_policy_delegation_settings.PasswordPolicyDelegationSettings):
                    self.delegation = config["delegation"]
                elif config["delegation"] is not None:
                    self.delegation = password_policy_delegation_settings.PasswordPolicyDelegationSettings(
                        config["delegation"]
                    )
                else:
                    self.delegation = None
            else:
                self.delegation = None
            if "password" in config:
                if isinstance(config["password"],
                              password_policy_password_settings.PasswordPolicyPasswordSettings):
                    self.password = config["password"]
                elif config["password"] is not None:
                    self.password = password_policy_password_settings.PasswordPolicyPasswordSettings(
                        config["password"]
                    )
                else:
                    self.password = None
            else:
                self.password = None
            if "recovery" in config:
                if isinstance(config["recovery"],
                              password_policy_recovery_settings.PasswordPolicyRecoverySettings):
                    self.recovery = config["recovery"]
                elif config["recovery"] is not None:
                    self.recovery = password_policy_recovery_settings.PasswordPolicyRecoverySettings(
                        config["recovery"]
                    )
                else:
                    self.recovery = None
            else:
                self.recovery = None
        else:
            self.delegation = None
            self.password = None
            self.recovery = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "delegation": self.delegation,
            "password": self.password,
            "recovery": self.recovery
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
