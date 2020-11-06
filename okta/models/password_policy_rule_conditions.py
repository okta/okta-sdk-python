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
from okta.models import policy_network_condition\
    as policy_network_condition
from okta.models import policy_people_condition\
    as policy_people_condition


class PasswordPolicyRuleConditions(
    OktaObject
):
    """
    A class for PasswordPolicyRuleConditions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "network" in config:
                if isinstance(config["network"],
                              policy_network_condition.PolicyNetworkCondition):
                    self.network = config["network"]
                elif config["network"] is not None:
                    self.network = policy_network_condition.PolicyNetworkCondition(
                        config["network"]
                    )
                else:
                    self.network = None
            else:
                self.network = None
            if "people" in config:
                if isinstance(config["people"],
                              policy_people_condition.PolicyPeopleCondition):
                    self.people = config["people"]
                elif config["people"] is not None:
                    self.people = policy_people_condition.PolicyPeopleCondition(
                        config["people"]
                    )
                else:
                    self.people = None
            else:
                self.people = None
        else:
            self.network = None
            self.people = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "network": self.network,
            "people": self.people
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
