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


class UserType(
    OktaObject
):
    """
    A class for UserType objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.created_by = config["createdBy"]\
                if "createdBy" in config else None
            self.default = config["default"]\
                if "default" in config else None
            self.description = config["description"]\
                if "description" in config else None
            self.display_name = config["displayName"]\
                if "displayName" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.last_updated_by = config["lastUpdatedBy"]\
                if "lastUpdatedBy" in config else None
            self.name = config["name"]\
                if "name" in config else None
        else:
            self.links = None
            self.created = None
            self.created_by = None
            self.default = None
            self.description = None
            self.display_name = None
            self.id = None
            self.last_updated = None
            self.last_updated_by = None
            self.name = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "created": self.created,
            "createdBy": self.created_by,
            "default": self.default,
            "description": self.description,
            "displayName": self.display_name,
            "id": self.id,
            "lastUpdated": self.last_updated,
            "lastUpdatedBy": self.last_updated_by,
            "name": self.name
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
