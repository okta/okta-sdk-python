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
from okta.models import policy_rule_actions_enroll\
    as policy_rule_actions_enroll
from okta.models import password_policy_rule_action\
    as password_policy_rule_action
from okta.models import okta_sign_on_policy_rule_signon_actions\
    as okta_sign_on_policy_rule_signon_actions


class PolicyRuleActions(
    OktaObject
):
    """
    A class for PolicyRuleActions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "enroll" in config:
                if isinstance(config["enroll"],
                              policy_rule_actions_enroll.PolicyRuleActionsEnroll):
                    self.enroll = config["enroll"]
                elif config["enroll"] is not None:
                    self.enroll = policy_rule_actions_enroll.PolicyRuleActionsEnroll(
                        config["enroll"]
                    )
                else:
                    self.enroll = None
            else:
                self.enroll = None
            if "passwordChange" in config:
                if isinstance(config["passwordChange"],
                              password_policy_rule_action.PasswordPolicyRuleAction):
                    self.password_change = config["passwordChange"]
                elif config["passwordChange"] is not None:
                    self.password_change = password_policy_rule_action.PasswordPolicyRuleAction(
                        config["passwordChange"]
                    )
                else:
                    self.password_change = None
            else:
                self.password_change = None
            if "selfServicePasswordReset" in config:
                if isinstance(config["selfServicePasswordReset"],
                              password_policy_rule_action.PasswordPolicyRuleAction):
                    self.self_service_password_reset = config["selfServicePasswordReset"]
                elif config["selfServicePasswordReset"] is not None:
                    self.self_service_password_reset = password_policy_rule_action.PasswordPolicyRuleAction(
                        config["selfServicePasswordReset"]
                    )
                else:
                    self.self_service_password_reset = None
            else:
                self.self_service_password_reset = None
            if "selfServiceUnlock" in config:
                if isinstance(config["selfServiceUnlock"],
                              password_policy_rule_action.PasswordPolicyRuleAction):
                    self.self_service_unlock = config["selfServiceUnlock"]
                elif config["selfServiceUnlock"] is not None:
                    self.self_service_unlock = password_policy_rule_action.PasswordPolicyRuleAction(
                        config["selfServiceUnlock"]
                    )
                else:
                    self.self_service_unlock = None
            else:
                self.self_service_unlock = None
            if "signon" in config:
                if isinstance(config["signon"],
                              okta_sign_on_policy_rule_signon_actions.OktaSignOnPolicyRuleSignonActions):
                    self.signon = config["signon"]
                elif config["signon"] is not None:
                    self.signon = okta_sign_on_policy_rule_signon_actions.OktaSignOnPolicyRuleSignonActions(
                        config["signon"]
                    )
                else:
                    self.signon = None
            else:
                self.signon = None
        else:
            self.enroll = None
            self.password_change = None
            self.self_service_password_reset = None
            self.self_service_unlock = None
            self.signon = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "enroll": self.enroll,
            "passwordChange": self.password_change,
            "selfServicePasswordReset": self.self_service_password_reset,
            "selfServiceUnlock": self.self_service_unlock,
            "signon": self.signon
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
