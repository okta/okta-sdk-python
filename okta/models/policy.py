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
from okta.models import policy_rule_conditions\
    as policy_rule_conditions
from okta.models import policy_type\
    as policy_type


class Policy(
    OktaObject
):
    """
    A class for Policy objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.embedded = config["embedded"]\
                if "embedded" in config else None
            self.links = config["links"]\
                if "links" in config else None
            if "conditions" in config:
                if isinstance(config["conditions"],
                              policy_rule_conditions.PolicyRuleConditions):
                    self.conditions = config["conditions"]
                elif config["conditions"] is not None:
                    self.conditions = policy_rule_conditions.PolicyRuleConditions(
                        config["conditions"]
                    )
                else:
                    self.conditions = None
            else:
                self.conditions = None
            self.created = config["created"]\
                if "created" in config else None
            self.description = config["description"]\
                if "description" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            self.priority = config["priority"]\
                if "priority" in config else None
            self.status = config["status"]\
                if "status" in config else None
            self.system = config["system"]\
                if "system" in config else None
            if "type" in config:
                if isinstance(config["type"],
                              policy_type.PolicyType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = policy_type.PolicyType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
        else:
            self.embedded = None
            self.links = None
            self.conditions = None
            self.created = None
            self.description = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.priority = None
            self.status = None
            self.system = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_embedded": self.embedded,
            "_links": self.links,
            "conditions": self.conditions,
            "created": self.created,
            "description": self.description,
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
