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
from okta.models import device_policy_rule_condition_platform\
    as device_policy_rule_condition_platform


class DevicePolicyRuleCondition(
    OktaObject
):
    """
    A class for DevicePolicyRuleCondition objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.migrated = config["migrated"]\
                if "migrated" in config else None
            if "platform" in config:
                if isinstance(config["platform"],
                              device_policy_rule_condition_platform.DevicePolicyRuleConditionPlatform):
                    self.platform = config["platform"]
                elif config["platform"] is not None:
                    self.platform = device_policy_rule_condition_platform.DevicePolicyRuleConditionPlatform(
                        config["platform"]
                    )
                else:
                    self.platform = None
            else:
                self.platform = None
            self.rooted = config["rooted"]\
                if "rooted" in config else None
            self.trust_level = config["trustLevel"]\
                if "trustLevel" in config else None
        else:
            self.migrated = None
            self.platform = None
            self.rooted = None
            self.trust_level = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "migrated": self.migrated,
            "platform": self.platform,
            "rooted": self.rooted,
            "trustLevel": self.trust_level
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
