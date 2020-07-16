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
from okta.models.password_policy_delegation_settings\
    import PasswordPolicyDelegationSettings
from okta.models.password_policy_password_settings\
    import PasswordPolicyPasswordSettings
from okta.models.password_policy_recovery_settings\
    import PasswordPolicyRecoverySettings


class PasswordPolicySettings(
    OktaObject
):
    """
    A class for PasswordPolicySettings objects.
    """

    def __init__(self, config=None):
        if config:
            if "delegation" in config:
                if isinstance(config["delegation"],
                              PasswordPolicyDelegationSettings):
                    self.delegation = config["delegation"]
                else:
                    self.delegation = PasswordPolicyDelegationSettings(
                        config["delegation"]
                    )
            else:
                self.delegation = None
            if "password" in config:
                if isinstance(config["password"],
                              PasswordPolicyPasswordSettings):
                    self.password = config["password"]
                else:
                    self.password = PasswordPolicyPasswordSettings(
                        config["password"]
                    )
            else:
                self.password = None
            if "recovery" in config:
                if isinstance(config["recovery"],
                              PasswordPolicyRecoverySettings):
                    self.recovery = config["recovery"]
                else:
                    self.recovery = PasswordPolicyRecoverySettings(
                        config["recovery"]
                    )
            else:
                self.recovery = None
        else:
            self.delegation = None
            self.password = None
            self.recovery = None
