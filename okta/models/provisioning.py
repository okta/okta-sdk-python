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
from okta.models import provisioning_conditions\
    as provisioning_conditions
from okta.models import provisioning_groups\
    as provisioning_groups


class Provisioning(
    OktaObject
):
    """
    A class for Provisioning objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.action = config["action"]\
                if "action" in config else None
            if "conditions" in config:
                if isinstance(config["conditions"],
                              provisioning_conditions.ProvisioningConditions):
                    self.conditions = config["conditions"]
                elif config["conditions"] is not None:
                    self.conditions = provisioning_conditions.ProvisioningConditions(
                        config["conditions"]
                    )
                else:
                    self.conditions = None
            else:
                self.conditions = None
            if "groups" in config:
                if isinstance(config["groups"],
                              provisioning_groups.ProvisioningGroups):
                    self.groups = config["groups"]
                elif config["groups"] is not None:
                    self.groups = provisioning_groups.ProvisioningGroups(
                        config["groups"]
                    )
                else:
                    self.groups = None
            else:
                self.groups = None
            self.profile_master = config["profileMaster"]\
                if "profileMaster" in config else None
        else:
            self.action = None
            self.conditions = None
            self.groups = None
            self.profile_master = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "action": self.action,
            "conditions": self.conditions,
            "groups": self.groups,
            "profileMaster": self.profile_master
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
