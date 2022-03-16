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
from okta.models import lifecycle_deactivate_setting_object\
    as lifecycle_deactivate_setting_object
from okta.models import password_setting_object\
    as password_setting_object
from okta.models import profile_setting_object\
    as profile_setting_object


class CapabilitiesUpdateObject(
    OktaObject
):
    """
    A class for CapabilitiesUpdateObject objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "lifecycleDeactivate" in config:
                if isinstance(config["lifecycleDeactivate"],
                              lifecycle_deactivate_setting_object.LifecycleDeactivateSettingObject):
                    self.lifecycle_deactivate = config["lifecycleDeactivate"]
                elif config["lifecycleDeactivate"] is not None:
                    self.lifecycle_deactivate = lifecycle_deactivate_setting_object.LifecycleDeactivateSettingObject(
                        config["lifecycleDeactivate"]
                    )
                else:
                    self.lifecycle_deactivate = None
            else:
                self.lifecycle_deactivate = None
            if "password" in config:
                if isinstance(config["password"],
                              password_setting_object.PasswordSettingObject):
                    self.password = config["password"]
                elif config["password"] is not None:
                    self.password = password_setting_object.PasswordSettingObject(
                        config["password"]
                    )
                else:
                    self.password = None
            else:
                self.password = None
            if "profile" in config:
                if isinstance(config["profile"],
                              profile_setting_object.ProfileSettingObject):
                    self.profile = config["profile"]
                elif config["profile"] is not None:
                    self.profile = profile_setting_object.ProfileSettingObject(
                        config["profile"]
                    )
                else:
                    self.profile = None
            else:
                self.profile = None
        else:
            self.lifecycle_deactivate = None
            self.password = None
            self.profile = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "lifecycleDeactivate": self.lifecycle_deactivate,
            "password": self.password,
            "profile": self.profile
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
