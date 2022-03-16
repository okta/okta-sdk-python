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

from okta.models.policy_rule_actions\
    import PolicyRuleActions
from okta.models import profile_enrollment_policy_rule_action\
    as profile_enrollment_policy_rule_action


class ProfileEnrollmentPolicyRuleActions(
    PolicyRuleActions
):
    """
    A class for ProfileEnrollmentPolicyRuleActions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "profileEnrollment" in config:
                if isinstance(config["profileEnrollment"],
                              profile_enrollment_policy_rule_action.ProfileEnrollmentPolicyRuleAction):
                    self.profile_enrollment = config["profileEnrollment"]
                elif config["profileEnrollment"] is not None:
                    self.profile_enrollment = profile_enrollment_policy_rule_action.ProfileEnrollmentPolicyRuleAction(
                        config["profileEnrollment"]
                    )
                else:
                    self.profile_enrollment = None
            else:
                self.profile_enrollment = None
        else:
            self.profile_enrollment = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "profileEnrollment": self.profile_enrollment
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
