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
from okta.models import linked_object_details\
    as linked_object_details


class LinkedObject(
    OktaObject
):
    """
    A class for LinkedObject objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.links = config["links"]\
                if "links" in config else None
            if "associated" in config:
                if isinstance(config["associated"],
                              linked_object_details.LinkedObjectDetails):
                    self.associated = config["associated"]
                elif config["associated"] is not None:
                    self.associated = linked_object_details.LinkedObjectDetails(
                        config["associated"]
                    )
                else:
                    self.associated = None
            else:
                self.associated = None
            if "primary" in config:
                if isinstance(config["primary"],
                              linked_object_details.LinkedObjectDetails):
                    self.primary = config["primary"]
                elif config["primary"] is not None:
                    self.primary = linked_object_details.LinkedObjectDetails(
                        config["primary"]
                    )
                else:
                    self.primary = None
            else:
                self.primary = None
        else:
            self.links = None
            self.associated = None
            self.primary = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "_links": self.links,
            "associated": self.associated,
            "primary": self.primary
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
