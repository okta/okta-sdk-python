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
from okta.models import group_rule_expression\
    as group_rule_expression
from okta.models import group_rule_people_condition\
    as group_rule_people_condition


class GroupRuleConditions(
    OktaObject
):
    """
    A class for GroupRuleConditions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "expression" in config:
                if isinstance(config["expression"],
                              group_rule_expression.GroupRuleExpression):
                    self.expression = config["expression"]
                elif config["expression"] is not None:
                    self.expression = group_rule_expression.GroupRuleExpression(
                        config["expression"]
                    )
                else:
                    self.expression = None
            else:
                self.expression = None
            if "people" in config:
                if isinstance(config["people"],
                              group_rule_people_condition.GroupRulePeopleCondition):
                    self.people = config["people"]
                elif config["people"] is not None:
                    self.people = group_rule_people_condition.GroupRulePeopleCondition(
                        config["people"]
                    )
                else:
                    self.people = None
            else:
                self.people = None
        else:
            self.expression = None
            self.people = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "expression": self.expression,
            "people": self.people
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
