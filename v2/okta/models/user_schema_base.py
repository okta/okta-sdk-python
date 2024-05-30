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
from okta.models import user_schema_base_properties\
    as user_schema_base_properties


class UserSchemaBase(
    OktaObject
):
    """
    A class for UserSchemaBase objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.id = config["id"]\
                if "id" in config else None
            if "properties" in config:
                if isinstance(config["properties"],
                              user_schema_base_properties.UserSchemaBaseProperties):
                    self.properties = config["properties"]
                elif config["properties"] is not None:
                    self.properties = user_schema_base_properties.UserSchemaBaseProperties(
                        config["properties"]
                    )
                else:
                    self.properties = None
            else:
                self.properties = None
            self.required = OktaCollection.form_list(
                config["required"] if "required"\
                    in config else [],
                str
            )
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.id = None
            self.properties = None
            self.required = []
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "id": self.id,
            "properties": self.properties,
            "required": self.required,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
