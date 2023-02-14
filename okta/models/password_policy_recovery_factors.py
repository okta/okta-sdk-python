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
from okta.models import password_policy_recovery_factor_settings\
    as password_policy_recovery_factor_settings
from okta.models import password_policy_recovery_email\
    as password_policy_recovery_email
from okta.models import password_policy_recovery_question\
    as password_policy_recovery_question


class PasswordPolicyRecoveryFactors(
    OktaObject
):
    """
    A class for PasswordPolicyRecoveryFactors objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "okta_call" in config:
                if isinstance(config["okta_call"],
                              password_policy_recovery_factor_settings.PasswordPolicyRecoveryFactorSettings):
                    self.okta_call = config["okta_call"]
                elif config["okta_call"] is not None:
                    self.okta_call = password_policy_recovery_factor_settings.PasswordPolicyRecoveryFactorSettings(
                        config["okta_call"]
                    )
                else:
                    self.okta_call = None
            else:
                self.okta_call = None
            if "okta_email" in config:
                if isinstance(config["okta_email"],
                              password_policy_recovery_email.PasswordPolicyRecoveryEmail):
                    self.okta_email = config["okta_email"]
                elif config["okta_email"] is not None:
                    self.okta_email = password_policy_recovery_email.PasswordPolicyRecoveryEmail(
                        config["okta_email"]
                    )
                else:
                    self.okta_email = None
            else:
                self.okta_email = None
            if "okta_sms" in config:
                if isinstance(config["okta_sms"],
                              password_policy_recovery_factor_settings.PasswordPolicyRecoveryFactorSettings):
                    self.okta_sms = config["okta_sms"]
                elif config["okta_sms"] is not None:
                    self.okta_sms = password_policy_recovery_factor_settings.PasswordPolicyRecoveryFactorSettings(
                        config["okta_sms"]
                    )
                else:
                    self.okta_sms = None
            else:
                self.okta_sms = None
            if "recovery_question" in config:
                if isinstance(config["recovery_question"],
                              password_policy_recovery_question.PasswordPolicyRecoveryQuestion):
                    self.recovery_question = config["recovery_question"]
                elif config["recovery_question"] is not None:
                    self.recovery_question = password_policy_recovery_question.PasswordPolicyRecoveryQuestion(
                        config["recovery_question"]
                    )
                else:
                    self.recovery_question = None
            else:
                self.recovery_question = None
        else:
            self.okta_call = None
            self.okta_email = None
            self.okta_sms = None
            self.recovery_question = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "okta_call": self.okta_call,
            "okta_email": self.okta_email,
            "okta_sms": self.okta_sms,
            "recovery_question": self.recovery_question
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
