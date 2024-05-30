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
from okta.models import user_schema_attribute_items\
    as user_schema_attribute_items
from okta.models import user_schema_attribute_master\
    as user_schema_attribute_master
from okta.models import user_schema_attribute_enum\
    as user_schema_attribute_enum
from okta.models import user_schema_attribute_permission\
    as user_schema_attribute_permission
from okta.models import user_schema_attribute_scope\
    as user_schema_attribute_scope
from okta.models import user_schema_attribute_type\
    as user_schema_attribute_type
from okta.models import user_schema_attribute_union\
    as user_schema_attribute_union


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
            self.enum = OktaCollection.form_list(
                config["enum"] if "enum"\
                    in config else [],
                str
            )
            self.external_name = config["externalName"]\
                if "externalName" in config else None
            self.external_namespace = config["externalNamespace"]\
                if "externalNamespace" in config else None
            if "items" in config:
                if isinstance(config["items"],
                              user_schema_attribute_items.UserSchemaAttributeItems):
                    self.items = config["items"]
                elif config["items"] is not None:
                    self.items = user_schema_attribute_items.UserSchemaAttributeItems(
                        config["items"]
                    )
                else:
                    self.items = None
            else:
                self.items = None
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
            self.one_of = OktaCollection.form_list(
                config["oneOf"] if "oneOf"\
                    in config else [],
                user_schema_attribute_enum.UserSchemaAttributeEnum
            )
            self.pattern = config["pattern"]\
                if "pattern" in config else None
            self.permissions = OktaCollection.form_list(
                config["permissions"] if "permissions"\
                    in config else [],
                user_schema_attribute_permission.UserSchemaAttributePermission
            )
            self.required = config["required"]\
                if "required" in config else None
            if "scope" in config:
                if isinstance(config["scope"],
                              user_schema_attribute_scope.UserSchemaAttributeScope):
                    self.scope = config["scope"]
                elif config["scope"] is not None:
                    self.scope = user_schema_attribute_scope.UserSchemaAttributeScope(
                        config["scope"].upper()
                    )
                else:
                    self.scope = None
            else:
                self.scope = None
            self.title = config["title"]\
                if "title" in config else None
            if "type" in config:
                if isinstance(config["type"],
                              user_schema_attribute_type.UserSchemaAttributeType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = user_schema_attribute_type.UserSchemaAttributeType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
            if "union" in config:
                if isinstance(config["union"],
                              user_schema_attribute_union.UserSchemaAttributeUnion):
                    self.union = config["union"]
                elif config["union"] is not None:
                    self.union = user_schema_attribute_union.UserSchemaAttributeUnion(
                        config["union"].upper()
                    )
                else:
                    self.union = None
            else:
                self.union = None
            self.unique = config["unique"]\
                if "unique" in config else None
        else:
            self.description = None
            self.enum = []
            self.external_name = None
            self.external_namespace = None
            self.items = None
            self.master = None
            self.max_length = None
            self.min_length = None
            self.mutability = None
            self.one_of = []
            self.pattern = None
            self.permissions = []
            self.required = None
            self.scope = None
            self.title = None
            self.type = None
            self.union = None
            self.unique = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "description": self.description,
            "enum": self.enum,
            "externalName": self.external_name,
            "externalNamespace": self.external_namespace,
            "items": self.items,
            "master": self.master,
            "maxLength": self.max_length,
            "minLength": self.min_length,
            "mutability": self.mutability,
            "oneOf": self.one_of,
            "pattern": self.pattern,
            "permissions": self.permissions,
            "required": self.required,
            "scope": self.scope,
            "title": self.title,
            "type": self.type,
            "union": self.union,
            "unique": self.unique
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
