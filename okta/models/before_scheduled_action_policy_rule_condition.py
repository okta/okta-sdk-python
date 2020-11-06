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
from okta.models import duration\
    as duration
from okta.models import scheduled_user_lifecycle_action\
    as scheduled_user_lifecycle_action


class BeforeScheduledActionPolicyRuleCondition(
    OktaObject
):
    """
    A class for BeforeScheduledActionPolicyRuleCondition objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "duration" in config:
                if isinstance(config["duration"],
                              duration.Duration):
                    self.duration = config["duration"]
                elif config["duration"] is not None:
                    self.duration = duration.Duration(
                        config["duration"]
                    )
                else:
                    self.duration = None
            else:
                self.duration = None
            if "lifecycleAction" in config:
                if isinstance(config["lifecycleAction"],
                              scheduled_user_lifecycle_action.ScheduledUserLifecycleAction):
                    self.lifecycle_action = config["lifecycleAction"]
                elif config["lifecycleAction"] is not None:
                    self.lifecycle_action = scheduled_user_lifecycle_action.ScheduledUserLifecycleAction(
                        config["lifecycleAction"]
                    )
                else:
                    self.lifecycle_action = None
            else:
                self.lifecycle_action = None
        else:
            self.duration = None
            self.lifecycle_action = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "duration": self.duration,
            "lifecycleAction": self.lifecycle_action
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
