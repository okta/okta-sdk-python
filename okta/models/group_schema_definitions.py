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
from okta.models import group_schema_base\
    as group_schema_base
from okta.models import group_schema_custom\
    as group_schema_custom


class GroupSchemaDefinitions(
    OktaObject
):
    """
    A class for GroupSchemaDefinitions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "base" in config:
                if isinstance(config["base"],
                              group_schema_base.GroupSchemaBase):
                    self.base = config["base"]
                elif config["base"] is not None:
                    self.base = group_schema_base.GroupSchemaBase(
                        config["base"]
                    )
                else:
                    self.base = None
            else:
                self.base = None
            if "custom" in config:
                if isinstance(config["custom"],
                              group_schema_custom.GroupSchemaCustom):
                    self.custom = config["custom"]
                elif config["custom"] is not None:
                    self.custom = group_schema_custom.GroupSchemaCustom(
                        config["custom"]
                    )
                else:
                    self.custom = None
            else:
                self.custom = None
        else:
            self.base = None
            self.custom = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "base": self.base,
            "custom": self.custom
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
