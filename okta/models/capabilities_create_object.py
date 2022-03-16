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
from okta.models import lifecycle_create_setting_object\
    as lifecycle_create_setting_object


class CapabilitiesCreateObject(
    OktaObject
):
    """
    A class for CapabilitiesCreateObject objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "lifecycleCreate" in config:
                if isinstance(config["lifecycleCreate"],
                              lifecycle_create_setting_object.LifecycleCreateSettingObject):
                    self.lifecycle_create = config["lifecycleCreate"]
                elif config["lifecycleCreate"] is not None:
                    self.lifecycle_create = lifecycle_create_setting_object.LifecycleCreateSettingObject(
                        config["lifecycleCreate"]
                    )
                else:
                    self.lifecycle_create = None
            else:
                self.lifecycle_create = None
        else:
            self.lifecycle_create = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "lifecycleCreate": self.lifecycle_create
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
