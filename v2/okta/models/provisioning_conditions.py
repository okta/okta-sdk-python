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
from okta.models import provisioning_deprovisioned_condition\
    as provisioning_deprovisioned_condition
from okta.models import provisioning_suspended_condition\
    as provisioning_suspended_condition


class ProvisioningConditions(
    OktaObject
):
    """
    A class for ProvisioningConditions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "deprovisioned" in config:
                if isinstance(config["deprovisioned"],
                              provisioning_deprovisioned_condition.ProvisioningDeprovisionedCondition):
                    self.deprovisioned = config["deprovisioned"]
                elif config["deprovisioned"] is not None:
                    self.deprovisioned = provisioning_deprovisioned_condition.ProvisioningDeprovisionedCondition(
                        config["deprovisioned"]
                    )
                else:
                    self.deprovisioned = None
            else:
                self.deprovisioned = None
            if "suspended" in config:
                if isinstance(config["suspended"],
                              provisioning_suspended_condition.ProvisioningSuspendedCondition):
                    self.suspended = config["suspended"]
                elif config["suspended"] is not None:
                    self.suspended = provisioning_suspended_condition.ProvisioningSuspendedCondition(
                        config["suspended"]
                    )
                else:
                    self.suspended = None
            else:
                self.suspended = None
        else:
            self.deprovisioned = None
            self.suspended = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "deprovisioned": self.deprovisioned,
            "suspended": self.suspended
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
