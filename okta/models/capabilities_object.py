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
from okta.models import capabilities_create_object\
    as capabilities_create_object
from okta.models import capabilities_update_object\
    as capabilities_update_object


class CapabilitiesObject(
    OktaObject
):
    """
    A class for CapabilitiesObject objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "create" in config:
                if isinstance(config["create"],
                              capabilities_create_object.CapabilitiesCreateObject):
                    self.create = config["create"]
                elif config["create"] is not None:
                    self.create = capabilities_create_object.CapabilitiesCreateObject(
                        config["create"]
                    )
                else:
                    self.create = None
            else:
                self.create = None
            if "update" in config:
                if isinstance(config["update"],
                              capabilities_update_object.CapabilitiesUpdateObject):
                    self.update = config["update"]
                elif config["update"] is not None:
                    self.update = capabilities_update_object.CapabilitiesUpdateObject(
                        config["update"]
                    )
                else:
                    self.update = None
            else:
                self.update = None
        else:
            self.create = None
            self.update = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "create": self.create,
            "update": self.update
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
