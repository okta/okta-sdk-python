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
from okta.models import password_policy_recovery_email_recovery_token\
    as password_policy_recovery_email_recovery_token


class PasswordPolicyRecoveryEmailProperties(
    OktaObject
):
    """
    A class for PasswordPolicyRecoveryEmailProperties objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "recoveryToken" in config:
                if isinstance(config["recoveryToken"],
                              password_policy_recovery_email_recovery_token.PasswordPolicyRecoveryEmailRecoveryToken):
                    self.recovery_token = config["recoveryToken"]
                elif config["recoveryToken"] is not None:
                    self.recovery_token = password_policy_recovery_email_recovery_token.PasswordPolicyRecoveryEmailRecoveryToken(
                        config["recoveryToken"]
                    )
                else:
                    self.recovery_token = None
            else:
                self.recovery_token = None
        else:
            self.recovery_token = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "recoveryToken": self.recovery_token
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
