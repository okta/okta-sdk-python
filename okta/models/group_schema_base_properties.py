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
from okta.models import group_schema_attribute\
    as group_schema_attribute


class GroupSchemaBaseProperties(
    OktaObject
):
    """
    A class for GroupSchemaBaseProperties objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "description" in config:
                if isinstance(config["description"],
                              group_schema_attribute.GroupSchemaAttribute):
                    self.description = config["description"]
                elif config["description"] is not None:
                    self.description = group_schema_attribute.GroupSchemaAttribute(
                        config["description"]
                    )
                else:
                    self.description = None
            else:
                self.description = None
            if "name" in config:
                if isinstance(config["name"],
                              group_schema_attribute.GroupSchemaAttribute):
                    self.name = config["name"]
                elif config["name"] is not None:
                    self.name = group_schema_attribute.GroupSchemaAttribute(
                        config["name"]
                    )
                else:
                    self.name = None
            else:
                self.name = None
        else:
            self.description = None
            self.name = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "description": self.description,
            "name": self.name
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
