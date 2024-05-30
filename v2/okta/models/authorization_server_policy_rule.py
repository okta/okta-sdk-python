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
from okta.models import authorization_server_policy_rule_actions\
    as authorization_server_policy_rule_actions
from okta.models import authorization_server_policy_rule_conditions\
    as authorization_server_policy_rule_conditions


class AuthorizationServerPolicyRule(
    OktaObject
):
    """
    A class for AuthorizationServerPolicyRule objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "actions" in config:
                if isinstance(config["actions"],
                              authorization_server_policy_rule_actions.AuthorizationServerPolicyRuleActions):
                    self.actions = config["actions"]
                elif config["actions"] is not None:
                    self.actions = authorization_server_policy_rule_actions.AuthorizationServerPolicyRuleActions(
                        config["actions"]
                    )
                else:
                    self.actions = None
            else:
                self.actions = None
            if "conditions" in config:
                if isinstance(config["conditions"],
                              authorization_server_policy_rule_conditions.AuthorizationServerPolicyRuleConditions):
                    self.conditions = config["conditions"]
                elif config["conditions"] is not None:
                    self.conditions = authorization_server_policy_rule_conditions.AuthorizationServerPolicyRuleConditions(
                        config["conditions"]
                    )
                else:
                    self.conditions = None
            else:
                self.conditions = None
            self.created = config["created"]\
                if "created" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.priority = config["priority"]\
                if "priority" in config else None
            self.status = config["status"]\
                if "status" in config else "ACTIVE"
            self.system = config["system"]\
                if "system" in config else False
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.actions = None
            self.conditions = None
            self.created = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.priority = None
            self.status = "ACTIVE"
            self.system = False
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "actions": self.actions,
            "conditions": self.conditions,
            "created": self.created,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "name": self.name,
            "priority": self.priority,
            "status": self.status,
            "system": self.system,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
