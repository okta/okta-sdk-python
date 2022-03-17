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
from okta.models import access_policy_rule_application_sign_on\
    as access_policy_rule_application_sign_on


class AccessPolicyRuleActions(
    PolicyRuleActions
):
    """
    A class for AccessPolicyRuleActions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "appSignOn" in config:
                if isinstance(config["appSignOn"],
                              access_policy_rule_application_sign_on.AccessPolicyRuleApplicationSignOn):
                    self.app_sign_on = config["appSignOn"]
                elif config["appSignOn"] is not None:
                    self.app_sign_on = access_policy_rule_application_sign_on.AccessPolicyRuleApplicationSignOn(
                        config["appSignOn"]
                    )
                else:
                    self.app_sign_on = None
            else:
                self.app_sign_on = None
        else:
            self.app_sign_on = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "appSignOn": self.app_sign_on
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
