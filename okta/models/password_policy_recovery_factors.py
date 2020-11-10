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
            if "oktaCall" in config:
                if isinstance(config["oktaCall"],
                              password_policy_recovery_factor_settings.PasswordPolicyRecoveryFactorSettings):
                    self.okta_call = config["oktaCall"]
                elif config["oktaCall"] is not None:
                    self.okta_call = password_policy_recovery_factor_settings.PasswordPolicyRecoveryFactorSettings(
                        config["oktaCall"]
                    )
                else:
                    self.okta_call = None
            else:
                self.okta_call = None
            if "oktaEmail" in config:
                if isinstance(config["oktaEmail"],
                              password_policy_recovery_email.PasswordPolicyRecoveryEmail):
                    self.okta_email = config["oktaEmail"]
                elif config["oktaEmail"] is not None:
                    self.okta_email = password_policy_recovery_email.PasswordPolicyRecoveryEmail(
                        config["oktaEmail"]
                    )
                else:
                    self.okta_email = None
            else:
                self.okta_email = None
            if "oktaSms" in config:
                if isinstance(config["oktaSms"],
                              password_policy_recovery_factor_settings.PasswordPolicyRecoveryFactorSettings):
                    self.okta_sms = config["oktaSms"]
                elif config["oktaSms"] is not None:
                    self.okta_sms = password_policy_recovery_factor_settings.PasswordPolicyRecoveryFactorSettings(
                        config["oktaSms"]
                    )
                else:
                    self.okta_sms = None
            else:
                self.okta_sms = None
            if "recoveryQuestion" in config:
                if isinstance(config["recoveryQuestion"],
                              password_policy_recovery_question.PasswordPolicyRecoveryQuestion):
                    self.recovery_question = config["recoveryQuestion"]
                elif config["recoveryQuestion"] is not None:
                    self.recovery_question = password_policy_recovery_question.PasswordPolicyRecoveryQuestion(
                        config["recoveryQuestion"]
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
