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
from okta.models import group_rule_group_condition\
    as group_rule_group_condition
from okta.models import group_rule_user_condition\
    as group_rule_user_condition


class GroupRulePeopleCondition(
    OktaObject
):
    """
    A class for GroupRulePeopleCondition objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "groups" in config:
                if isinstance(config["groups"],
                              group_rule_group_condition.GroupRuleGroupCondition):
                    self.groups = config["groups"]
                elif config["groups"] is not None:
                    self.groups = group_rule_group_condition.GroupRuleGroupCondition(
                        config["groups"]
                    )
                else:
                    self.groups = None
            else:
                self.groups = None
            if "users" in config:
                if isinstance(config["users"],
                              group_rule_user_condition.GroupRuleUserCondition):
                    self.users = config["users"]
                elif config["users"] is not None:
                    self.users = group_rule_user_condition.GroupRuleUserCondition(
                        config["users"]
                    )
                else:
                    self.users = None
            else:
                self.users = None
        else:
            self.groups = None
            self.users = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "groups": self.groups,
            "users": self.users
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
