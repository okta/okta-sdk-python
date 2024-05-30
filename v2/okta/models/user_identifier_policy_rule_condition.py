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
from okta.models import user_identifier_condition_evaluator_pattern\
    as user_identifier_condition_evaluator_pattern


class UserIdentifierPolicyRuleCondition(
    OktaObject
):
    """
    A class for UserIdentifierPolicyRuleCondition objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.attribute = config["attribute"]\
                if "attribute" in config else None
            self.patterns = OktaCollection.form_list(
                config["patterns"] if "patterns"\
                    in config else [],
                user_identifier_condition_evaluator_pattern.UserIdentifierConditionEvaluatorPattern
            )
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.attribute = None
            self.patterns = []
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "attribute": self.attribute,
            "patterns": self.patterns,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
