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
from okta.models import user_schema_definitions\
    as user_schema_definitions
from okta.models import user_schema_properties\
    as user_schema_properties


class UserSchema(
    OktaObject
):
    """
    A class for UserSchema objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.schema = config["schema"]\
                if "schema" in config else None
            self.links = config["links"]\
                if "links" in config else None
            self.created = config["created"]\
                if "created" in config else None
            if "definitions" in config:
                if isinstance(config["definitions"],
                              user_schema_definitions.UserSchemaDefinitions):
                    self.definitions = config["definitions"]
                elif config["definitions"] is not None:
                    self.definitions = user_schema_definitions.UserSchemaDefinitions(
                        config["definitions"]
                    )
                else:
                    self.definitions = None
            else:
                self.definitions = None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.name = config["name"]\
                if "name" in config else None
            if "properties" in config:
                if isinstance(config["properties"],
                              user_schema_properties.UserSchemaProperties):
                    self.properties = config["properties"]
                elif config["properties"] is not None:
                    self.properties = user_schema_properties.UserSchemaProperties(
                        config["properties"]
                    )
                else:
                    self.properties = None
            else:
                self.properties = None
            self.title = config["title"]\
                if "title" in config else None
            self.type = config["type"]\
                if "type" in config else None
        else:
            self.schema = None
            self.links = None
            self.created = None
            self.definitions = None
            self.id = None
            self.last_updated = None
            self.name = None
            self.properties = None
            self.title = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "$schema": self.schema,
            "_links": self.links,
            "created": self.created,
            "definitions": self.definitions,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "name": self.name,
            "properties": self.properties,
            "title": self.title,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
