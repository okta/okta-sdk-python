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
from okta.models.group_rule_group_condition\
    import GroupRuleGroupCondition
from okta.models.group_rule_user_condition\
    import GroupRuleUserCondition


class GroupRulePeopleCondition(
    OktaObject
):
    """
    A class for GroupRulePeopleCondition objects.
    """

    def __init__(self, config=None):
        if config:
            if "groups" in config:
                if isinstance(config["groups"],
                              GroupRuleGroupCondition):
                    self.groups = config["groups"]
                else:
                    self.groups = GroupRuleGroupCondition(
                        config["groups"]
                    )
            else:
                self.groups = None
            if "users" in config:
                if isinstance(config["users"],
                              GroupRuleUserCondition):
                    self.users = config["users"]
                else:
                    self.users = GroupRuleUserCondition(
                        config["users"]
                    )
            else:
                self.users = None
        else:
            self.groups = None
            self.users = None
