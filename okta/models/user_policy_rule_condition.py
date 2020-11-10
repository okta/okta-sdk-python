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
from okta.okta_collection import OktaCollection
from okta.models import inactivity_policy_rule_condition\
    as inactivity_policy_rule_condition
from okta.models import lifecycle_expiration_policy_rule_condition\
    as lifecycle_expiration_policy_rule_condition
from okta.models import password_expiration_policy_rule_condition\
    as password_expiration_policy_rule_condition
from okta.models import user_lifecycle_attribute_policy_rule_condition\
    as user_lifecycle_attribute_policy_rule_condition


class UserPolicyRuleCondition(
    OktaObject
):
    """
    A class for UserPolicyRuleCondition objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.exclude = OktaCollection.form_list(
                config["exclude"] if "exclude"\
                    in config else [],
                str
            )
            if "inactivity" in config:
                if isinstance(config["inactivity"],
                              inactivity_policy_rule_condition.InactivityPolicyRuleCondition):
                    self.inactivity = config["inactivity"]
                elif config["inactivity"] is not None:
                    self.inactivity = inactivity_policy_rule_condition.InactivityPolicyRuleCondition(
                        config["inactivity"]
                    )
                else:
                    self.inactivity = None
            else:
                self.inactivity = None
            self.include = OktaCollection.form_list(
                config["include"] if "include"\
                    in config else [],
                str
            )
            if "lifecycleExpiration" in config:
                if isinstance(config["lifecycleExpiration"],
                              lifecycle_expiration_policy_rule_condition.LifecycleExpirationPolicyRuleCondition):
                    self.lifecycle_expiration = config["lifecycleExpiration"]
                elif config["lifecycleExpiration"] is not None:
                    self.lifecycle_expiration = lifecycle_expiration_policy_rule_condition.LifecycleExpirationPolicyRuleCondition(
                        config["lifecycleExpiration"]
                    )
                else:
                    self.lifecycle_expiration = None
            else:
                self.lifecycle_expiration = None
            if "passwordExpiration" in config:
                if isinstance(config["passwordExpiration"],
                              password_expiration_policy_rule_condition.PasswordExpirationPolicyRuleCondition):
                    self.password_expiration = config["passwordExpiration"]
                elif config["passwordExpiration"] is not None:
                    self.password_expiration = password_expiration_policy_rule_condition.PasswordExpirationPolicyRuleCondition(
                        config["passwordExpiration"]
                    )
                else:
                    self.password_expiration = None
            else:
                self.password_expiration = None
            if "userLifecycleAttribute" in config:
                if isinstance(config["userLifecycleAttribute"],
                              user_lifecycle_attribute_policy_rule_condition.UserLifecycleAttributePolicyRuleCondition):
                    self.user_lifecycle_attribute = config["userLifecycleAttribute"]
                elif config["userLifecycleAttribute"] is not None:
                    self.user_lifecycle_attribute = user_lifecycle_attribute_policy_rule_condition.UserLifecycleAttributePolicyRuleCondition(
                        config["userLifecycleAttribute"]
                    )
                else:
                    self.user_lifecycle_attribute = None
            else:
                self.user_lifecycle_attribute = None
        else:
            self.exclude = []
            self.inactivity = None
            self.include = []
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
