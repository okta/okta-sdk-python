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
from okta.models import group_rule_action\
    as group_rule_action
from okta.models import group_rule_conditions\
    as group_rule_conditions
from okta.models import group_rule_status\
    as group_rule_status


class GroupRule(
    OktaObject
):
    """
    A class for GroupRule objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "actions" in config:
                if isinstance(config["actions"],
                              group_rule_action.GroupRuleAction):
                    self.actions = config["actions"]
                elif config["actions"] is not None:
                    self.actions = group_rule_action.GroupRuleAction(
                        config["actions"]
                    )
                else:
                    self.actions = None
            else:
                self.actions = None
            if "conditions" in config:
                if isinstance(config["conditions"],
                              group_rule_conditions.GroupRuleConditions):
                    self.conditions = config["conditions"]
                elif config["conditions"] is not None:
                    self.conditions = group_rule_conditions.GroupRuleConditions(
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
            if "status" in config:
                if isinstance(config["status"],
                              group_rule_status.GroupRuleStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = group_rule_status.GroupRuleStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.actions = None
            self.conditions = None
            self.created = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.status = None
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
            "status": self.status,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
