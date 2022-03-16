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

from okta.models.policy_rule_conditions\
    import PolicyRuleConditions
from okta.models import device_access_policy_rule_condition\
    as device_access_policy_rule_condition
from okta.models import access_policy_rule_custom_condition\
    as access_policy_rule_custom_condition
from okta.models import user_type_condition\
    as user_type_condition


class AccessPolicyRuleConditions(
    PolicyRuleConditions
):
    """
    A class for AccessPolicyRuleConditions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "device" in config:
                if isinstance(config["device"],
                              device_access_policy_rule_condition.DeviceAccessPolicyRuleCondition):
                    self.device = config["device"]
                elif config["device"] is not None:
                    self.device = device_access_policy_rule_condition.DeviceAccessPolicyRuleCondition(
                        config["device"]
                    )
                else:
                    self.device = None
            else:
                self.device = None
            if "elCondition" in config:
                if isinstance(config["elCondition"],
                              access_policy_rule_custom_condition.AccessPolicyRuleCustomCondition):
                    self.el_condition = config["elCondition"]
                elif config["elCondition"] is not None:
                    self.el_condition = access_policy_rule_custom_condition.AccessPolicyRuleCustomCondition(
                        config["elCondition"]
                    )
                else:
                    self.el_condition = None
            else:
                self.el_condition = None
            if "userType" in config:
                if isinstance(config["userType"],
                              user_type_condition.UserTypeCondition):
                    self.user_type = config["userType"]
                elif config["userType"] is not None:
                    self.user_type = user_type_condition.UserTypeCondition(
                        config["userType"]
                    )
                else:
                    self.user_type = None
            else:
                self.user_type = None
        else:
            self.device = None
            self.el_condition = None
            self.user_type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "device": self.device,
            "elCondition": self.el_condition,
            "userType": self.user_type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
