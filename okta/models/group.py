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
from okta.models import group_profile\
    as group_profile
from okta.models import group_type\
    as group_type


class Group(
    OktaObject
):
    """
    A class for Group objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.embedded = config["embedded"]\
                if "embedded" in config else None
            self.links = config["links"]\
                if "links" in config else None
            self.created = config["created"]\
                if "created" in config else None
            self.id = config["id"]\
                if "id" in config else None
            self.last_membership_updated = config["lastMembershipUpdated"]\
                if "lastMembershipUpdated" in config else None
            self.last_updated = config["lastUpdated"]\
                if "lastUpdated" in config else None
            self.object_class = OktaCollection.form_list(
                config["objectClass"] if "objectClass"\
                    in config else [],
                str
            )
            if "profile" in config:
                if isinstance(config["profile"],
                              group_profile.GroupProfile):
                    self.profile = config["profile"]
                elif config["profile"] is not None:
                    self.profile = group_profile.GroupProfile(
                        config["profile"]
                    )
                else:
                    self.profile = None
            else:
                self.profile = None
            if "type" in config:
                if isinstance(config["type"],
                              group_type.GroupType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = group_type.GroupType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
        else:
            self.embedded = None
            self.links = None
            self.created = None
            self.id = None
            self.last_membership_updated = None
            self.last_updated = None
            self.object_class = []
            self.profile = None
            self.type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_embedded": self.embedded,
            "_links": self.links,
            "created": self.created,
            "id": self.id,
            "lastMembershipUpdated": self.last_membership_updated,
            "lastUpdated": self.last_updated,
            "objectClass": self.object_class,
            "profile": self.profile,
            "type": self.type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
