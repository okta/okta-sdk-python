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

from okta.models.policy_rule\
    import PolicyRule
from okta.models import access_policy_rule_actions\
    as access_policy_rule_actions
from okta.models import access_policy_rule_conditions\
    as access_policy_rule_conditions


class AccessPolicyRule(
    PolicyRule
):
    """
    A class for AccessPolicyRule objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.type = "ACCESS_POLICY"
            if "actions" in config:
                if isinstance(config["actions"],
                              access_policy_rule_actions.AccessPolicyRuleActions):
                    self.actions = config["actions"]
                elif config["actions"] is not None:
                    self.actions = access_policy_rule_actions.AccessPolicyRuleActions(
                        config["actions"]
                    )
                else:
                    self.actions = None
            else:
                self.actions = None
            if "conditions" in config:
                if isinstance(config["conditions"],
                              access_policy_rule_conditions.AccessPolicyRuleConditions):
                    self.conditions = config["conditions"]
                elif config["conditions"] is not None:
                    self.conditions = access_policy_rule_conditions.AccessPolicyRuleConditions(
                        config["conditions"]
                    )
                else:
                    self.conditions = None
            else:
                self.conditions = None
            self.name = config["name"]\
                if "name" in config else None
        else:
            self.actions = None
            self.conditions = None
            self.name = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "actions": self.actions,
            "conditions": self.conditions,
            "name": self.name
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
