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
from okta.models.duration\
    import Duration
from okta.models.scheduled_user_lifecycle_action\
    import ScheduledUserLifecycleAction


class BeforeScheduledActionPolicyRuleCondition(
    OktaObject
):
    """
    A class for BeforeScheduledActionPolicyRuleCondition objects.
    """

    def __init__(self, config=None):
        if config:
            if "duration" in config:
                if isinstance(config["duration"],
                              Duration):
                    self.duration = config["duration"]
                else:
                    self.duration = Duration(
                        config["duration"]
                    )
            else:
                self.duration = None
            if "lifecycleAction" in config:
                if isinstance(config["lifecycleAction"],
                              ScheduledUserLifecycleAction):
                    self.lifecycle_action = config["lifecycleAction"]
                else:
                    self.lifecycle_action = ScheduledUserLifecycleAction(
                        config["lifecycleAction"]
                    )
            else:
                self.lifecycle_action = None
        else:
            self.duration = None
            self.lifecycle_action = None

    def request_format(self):
        return {
            "duration": self.duration,
            "lifecycleAction": self.lifecycle_action
        }
