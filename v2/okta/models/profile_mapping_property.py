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
from okta.models import profile_mapping_property_push_status\
    as profile_mapping_property_push_status


class ProfileMappingProperty(
    OktaObject
):
    """
    A class for ProfileMappingProperty objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.expression = config["expression"]\
                if "expression" in config else None
            if "pushStatus" in config:
                if isinstance(config["pushStatus"],
                              profile_mapping_property_push_status.ProfileMappingPropertyPushStatus):
                    self.push_status = config["pushStatus"]
                elif config["pushStatus"] is not None:
                    self.push_status = profile_mapping_property_push_status.ProfileMappingPropertyPushStatus(
                        config["pushStatus"].upper()
                    )
                else:
                    self.push_status = None
            else:
                self.push_status = None
        else:
            self.expression = None
            self.push_status = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "expression": self.expression,
            "pushStatus": self.push_status
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
