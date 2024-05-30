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
from okta.models import client_policy_condition\
    as client_policy_condition
from okta.models import grant_type_policy_rule_condition\
    as grant_type_policy_rule_condition
from okta.models import policy_people_condition\
    as policy_people_condition
from okta.models import o_auth_2_scopes_mediation_policy_rule_condition\
    as o_auth_2_scopes_mediation_policy_rule_condition


class AuthorizationServerPolicyRuleConditions(
    OktaObject
):
    """
    A class for AuthorizationServerPolicyRuleConditions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "clients" in config:
                if isinstance(config["clients"],
                              client_policy_condition.ClientPolicyCondition):
                    self.clients = config["clients"]
                elif config["clients"] is not None:
                    self.clients = client_policy_condition.ClientPolicyCondition(
                        config["clients"]
                    )
                else:
                    self.clients = None
            else:
                self.clients = None
            if "grantTypes" in config:
                if isinstance(config["grantTypes"],
                              grant_type_policy_rule_condition.GrantTypePolicyRuleCondition):
                    self.grant_types = config["grantTypes"]
                elif config["grantTypes"] is not None:
                    self.grant_types = grant_type_policy_rule_condition.GrantTypePolicyRuleCondition(
                        config["grantTypes"]
                    )
                else:
                    self.grant_types = None
            else:
                self.grant_types = None
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
            if "scopes" in config:
                if isinstance(config["scopes"],
                              o_auth_2_scopes_mediation_policy_rule_condition.OAuth2ScopesMediationPolicyRuleCondition):
                    self.scopes = config["scopes"]
                elif config["scopes"] is not None:
                    self.scopes = o_auth_2_scopes_mediation_policy_rule_condition.OAuth2ScopesMediationPolicyRuleCondition(
                        config["scopes"]
                    )
                else:
                    self.scopes = None
            else:
                self.scopes = None
        else:
            self.clients = None
            self.grant_types = None
            self.people = None
            self.scopes = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "clients": self.clients,
            "grantTypes": self.grant_types,
            "people": self.people,
            "scopes": self.scopes
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
