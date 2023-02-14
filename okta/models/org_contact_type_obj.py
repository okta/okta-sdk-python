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
from okta.models import org_contact_type\
    as org_contact_type


class OrgContactTypeObj(
    OktaObject
):
    """
    A class for OrgContactTypeObj objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "contactType" in config:
                if isinstance(config["contactType"],
                              org_contact_type.OrgContactType):
                    self.contact_type = config["contactType"]
                elif config["contactType"] is not None:
                    self.contact_type = org_contact_type.OrgContactType(
                        config["contactType"].upper()
                    )
                else:
                    self.contact_type = None
            else:
                self.contact_type = None
        else:
            self.links = None
            self.contact_type = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "contactType": self.contact_type
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
