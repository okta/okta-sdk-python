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
from okta.models.inactivity_policy_rule_condition\
    import InactivityPolicyRuleCondition
from okta.models.lifecycle_expiration_policy_rule_condition\
    import LifecycleExpirationPolicyRuleCondition
from okta.models.password_expiration_policy_rule_condition\
    import PasswordExpirationPolicyRuleCondition
from okta.models.user_lifecycle_attribute_policy_rule_condition\
    import UserLifecycleAttributePolicyRuleCondition


class UserPolicyRuleCondition(
    OktaObject
):
    """
    A class for UserPolicyRuleCondition objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.exclude = config["exclude"]\
                if "exclude" in config else None
            if "inactivity" in config:
                if isinstance(config["inactivity"],
                              InactivityPolicyRuleCondition):
                    self.inactivity = config["inactivity"]
                else:
                    self.inactivity = InactivityPolicyRuleCondition(
                        config["inactivity"]
                    )
            else:
                self.inactivity = None
            self.include = config["include"]\
                if "include" in config else None
            if "lifecycleExpiration" in config:
                if isinstance(config["lifecycleExpiration"],
                              LifecycleExpirationPolicyRuleCondition):
                    self.lifecycle_expiration = config["lifecycleExpiration"]
                else:
                    self.lifecycle_expiration = LifecycleExpirationPolicyRuleCondition(
                        config["lifecycleExpiration"]
                    )
            else:
                self.lifecycle_expiration = None
            if "passwordExpiration" in config:
                if isinstance(config["passwordExpiration"],
                              PasswordExpirationPolicyRuleCondition):
                    self.password_expiration = config["passwordExpiration"]
                else:
                    self.password_expiration = PasswordExpirationPolicyRuleCondition(
                        config["passwordExpiration"]
                    )
            else:
                self.password_expiration = None
            if "userLifecycleAttribute" in config:
                if isinstance(config["userLifecycleAttribute"],
                              UserLifecycleAttributePolicyRuleCondition):
                    self.user_lifecycle_attribute = config["userLifecycleAttribute"]
                else:
                    self.user_lifecycle_attribute = UserLifecycleAttributePolicyRuleCondition(
                        config["userLifecycleAttribute"]
                    )
            else:
                self.user_lifecycle_attribute = None
        else:
            self.exclude = None
            self.inactivity = None
            self.include = None
            self.lifecycle_expiration = None
            self.password_expiration = None
            self.user_lifecycle_attribute = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "exclude": self.exclude,
            "inactivity": self.inactivity,
            "include": self.include,
            "lifecycleExpiration": self.lifecycle_expiration,
            "passwordExpiration": self.password_expiration,
            "userLifecycleAttribute": self.user_lifecycle_attribute
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
