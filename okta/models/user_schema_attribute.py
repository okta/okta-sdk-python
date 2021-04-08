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
from okta.models import user_schema_attribute_master\
    as user_schema_attribute_master
from okta.models import user_schema_attribute_permission\
    as user_schema_attribute_permission


class UserSchemaAttribute(
    OktaObject
):
    """
    A class for UserSchemaAttribute objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.description = config["description"]\
                if "description" in config else None
            if "master" in config:
                if isinstance(config["master"],
                              user_schema_attribute_master.UserSchemaAttributeMaster):
                    self.master = config["master"]
                elif config["master"] is not None:
                    self.master = user_schema_attribute_master.UserSchemaAttributeMaster(
                        config["master"]
                    )
                else:
                    self.master = None
            else:
                self.master = None
            self.max_length = config["maxLength"]\
                if "maxLength" in config else None
            self.min_length = config["minLength"]\
                if "minLength" in config else None
            self.mutability = config["mutability"]\
                if "mutability" in config else None
            self.permissions = OktaCollection.form_list(
                config["permissions"] if "permissions"\
                    in config else [],
                user_schema_attribute_permission.UserSchemaAttributePermission
            )
            self.required = config["required"]\
                if "required" in config else None
            self.scope = config["scope"]\
                if "scope" in config else None
            self.title = config["title"]\
                if "title" in config else None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.description = None
            self.master = None
            self.max_length = None
            self.min_length = None
            self.mutability = None
            self.permissions = []
            self.required = None
            self.scope = None
            self.title = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "description": self.description,
            "master": self.master,
            "maxLength": self.max_length,
            "minLength": self.min_length,
            "mutability": self.mutability,
            "permissions": self.permissions,
            "required": self.required,
            "scope": self.scope,
            "title": self.title,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
