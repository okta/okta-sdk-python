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
from okta.models import role_assignment_type\
    as role_assignment_type
from okta.models import role_status\
    as role_status
from okta.models import role_type\
    as role_type


class Role(
    OktaObject
):
    """
    A class for Role objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.embedded = config["embedded"]\
                if "embedded" in config else None
            self.links = config["links"]\
                if "links" in config else None
            if "assignmentType" in config:
                if isinstance(config["assignmentType"],
                              role_assignment_type.RoleAssignmentType):
                    self.assignment_type = config["assignmentType"]
                elif config["assignmentType"] is not None:
                    self.assignment_type = role_assignment_type.RoleAssignmentType(
                        config["assignmentType"].upper()
                    )
                else:
                    self.assignment_type = None
            else:
                self.assignment_type = None
            self.created = config["created"]\
                if "created" in config else None
            self.description = config["description"]\
                if "description" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.label = config["label"]\
                if "label" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            if "status" in config:
                if isinstance(config["status"],
                              role_status.RoleStatus):
                    self.status = config["status"]
                elif config["status"] is not None:
                    self.status = role_status.RoleStatus(
                        config["status"].upper()
                    )
                else:
                    self.status = None
            else:
                self.status = None
            if "type" in config:
                if isinstance(config["type"],
                              role_type.RoleType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = role_type.RoleType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
        else:
            self.embedded = None
            self.links = None
            self.assignment_type = None
            self.created = None
            self.description = None
            self.id = None
            self.label = None
            self.last_updated = None
            self.status = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_embedded": self.embedded,
            "_links": self.links,
            "assignmentType": self.assignment_type,
            "created": self.created,
            "description": self.description,
            "id": self.id,
            "label": self.label,
            "lastUpdated": self.last_updated,
            "status": self.status,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
