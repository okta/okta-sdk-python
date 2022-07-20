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
from okta.models import knowledge_constraint\
    as knowledge_constraint
from okta.models import possession_constraint\
    as possession_constraint


class AccessPolicyConstraints(
    OktaObject
):
    """
    A class for AccessPolicyConstraints objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "knowledge" in config:
                if isinstance(config["knowledge"],
                              knowledge_constraint.KnowledgeConstraint):
                    self.knowledge = config["knowledge"]
                elif config["knowledge"] is not None:
                    self.knowledge = knowledge_constraint.KnowledgeConstraint(
                        config["knowledge"]
                    )
                else:
                    self.knowledge = None
            else:
                self.knowledge = None
            if "possession" in config:
                if isinstance(config["possession"],
                              possession_constraint.PossessionConstraint):
                    self.possession = config["possession"]
                elif config["possession"] is not None:
                    self.possession = possession_constraint.PossessionConstraint(
                        config["possession"]
                    )
                else:
                    self.possession = None
            else:
                self.possession = None
        else:
            self.knowledge = None
            self.possession = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "knowledge": self.knowledge,
            "possession": self.possession
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
