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
from okta.models.password_policy_recovery_factor_settings\
    import PasswordPolicyRecoveryFactorSettings
from okta.models.password_policy_recovery_email\
    import PasswordPolicyRecoveryEmail
from okta.models.password_policy_recovery_question\
    import PasswordPolicyRecoveryQuestion


class PasswordPolicyRecoveryFactors(
    OktaObject
):
    """
    A class for PasswordPolicyRecoveryFactors objects.
    """

    def __init__(self, config=None):
        if config:
            if "okta_call" in config:
                if isinstance(config["okta_call"],
                              PasswordPolicyRecoveryFactorSettings):
                    self.okta_call = config["okta_call"]
                else:
                    self.okta_call = PasswordPolicyRecoveryFactorSettings(
                        config["okta_call"]
                    )
            else:
                self.okta_call = None
            if "okta_email" in config:
                if isinstance(config["okta_email"],
                              PasswordPolicyRecoveryEmail):
                    self.okta_email = config["okta_email"]
                else:
                    self.okta_email = PasswordPolicyRecoveryEmail(
                        config["okta_email"]
                    )
            else:
                self.okta_email = None
            if "okta_sms" in config:
                if isinstance(config["okta_sms"],
                              PasswordPolicyRecoveryFactorSettings):
                    self.okta_sms = config["okta_sms"]
                else:
                    self.okta_sms = PasswordPolicyRecoveryFactorSettings(
                        config["okta_sms"]
                    )
            else:
                self.okta_sms = None
            if "recovery_question" in config:
                if isinstance(config["recovery_question"],
                              PasswordPolicyRecoveryQuestion):
                    self.recovery_question = config["recovery_question"]
                else:
                    self.recovery_question = PasswordPolicyRecoveryQuestion(
                        config["recovery_question"]
                    )
            else:
                self.recovery_question = None
        else:
            self.okta_call = None
            self.okta_email = None
            self.okta_sms = None
            self.recovery_question = None
