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
from okta.models.app_and_instance_policy_rule_condition\
    import AppAndInstancePolicyRuleCondition
from okta.models.app_instance_policy_rule_condition\
    import AppInstancePolicyRuleCondition
from okta.models.policy_rule_auth_context_condition\
    import PolicyRuleAuthContextCondition
from okta.models.password_policy_authentication_provider_condition\
    import PasswordPolicyAuthenticationProviderCondition
from okta.models.before_scheduled_action_policy_rule_condition\
    import BeforeScheduledActionPolicyRuleCondition
from okta.models.client_policy_condition\
    import ClientPolicyCondition
from okta.models.context_policy_rule_condition\
    import ContextPolicyRuleCondition
from okta.models.device_policy_rule_condition\
    import DevicePolicyRuleCondition
from okta.models.grant_type_policy_rule_condition\
    import GrantTypePolicyRuleCondition
from okta.models.group_policy_rule_condition\
    import GroupPolicyRuleCondition
from okta.models.identity_provider_policy_rule_condition\
    import IdentityProviderPolicyRuleCondition
from okta.models.mdm_enrollment_policy_rule_condition\
    import MdmEnrollmentPolicyRuleCondition
from okta.models.policy_network_condition\
    import PolicyNetworkCondition
from okta.models.policy_people_condition\
    import PolicyPeopleCondition
from okta.models.platform_policy_rule_condition\
    import PlatformPolicyRuleCondition
from okta.models.risk_policy_rule_condition\
    import RiskPolicyRuleCondition
from okta.models.risk_score_policy_rule_condition\
    import RiskScorePolicyRuleCondition
from okta.models.o_auth_2_scopes_mediation_policy_rule_condition\
    import OAuth2ScopesMediationPolicyRuleCondition
from okta.models.user_identifier_policy_rule_condition\
    import UserIdentifierPolicyRuleCondition
from okta.models.user_status_policy_rule_condition\
    import UserStatusPolicyRuleCondition
from okta.models.user_policy_rule_condition\
    import UserPolicyRuleCondition


class PolicyRuleConditions(
    OktaObject
):
    """
    A class for PolicyRuleConditions objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "app" in config:
                if isinstance(config["app"],
                              AppAndInstancePolicyRuleCondition):
                    self.app = config["app"]
                else:
                    self.app = AppAndInstancePolicyRuleCondition(
                        config["app"]
                    )
            else:
                self.app = None
            if "apps" in config:
                if isinstance(config["apps"],
                              AppInstancePolicyRuleCondition):
                    self.apps = config["apps"]
                else:
                    self.apps = AppInstancePolicyRuleCondition(
                        config["apps"]
                    )
            else:
                self.apps = None
            if "authContext" in config:
                if isinstance(config["authContext"],
                              PolicyRuleAuthContextCondition):
                    self.auth_context = config["authContext"]
                else:
                    self.auth_context = PolicyRuleAuthContextCondition(
                        config["authContext"]
                    )
            else:
                self.auth_context = None
            if "authProvider" in config:
                if isinstance(config["authProvider"],
                              PasswordPolicyAuthenticationProviderCondition):
                    self.auth_provider = config["authProvider"]
                else:
                    self.auth_provider = PasswordPolicyAuthenticationProviderCondition(
                        config["authProvider"]
                    )
            else:
                self.auth_provider = None
            if "beforeScheduledAction" in config:
                if isinstance(config["beforeScheduledAction"],
                              BeforeScheduledActionPolicyRuleCondition):
                    self.before_scheduled_action = config["beforeScheduledAction"]
                else:
                    self.before_scheduled_action = BeforeScheduledActionPolicyRuleCondition(
                        config["beforeScheduledAction"]
                    )
            else:
                self.before_scheduled_action = None
            if "clients" in config:
                if isinstance(config["clients"],
                              ClientPolicyCondition):
                    self.clients = config["clients"]
                else:
                    self.clients = ClientPolicyCondition(
                        config["clients"]
                    )
            else:
                self.clients = None
            if "context" in config:
                if isinstance(config["context"],
                              ContextPolicyRuleCondition):
                    self.context = config["context"]
                else:
                    self.context = ContextPolicyRuleCondition(
                        config["context"]
                    )
            else:
                self.context = None
            if "device" in config:
                if isinstance(config["device"],
                              DevicePolicyRuleCondition):
                    self.device = config["device"]
                else:
                    self.device = DevicePolicyRuleCondition(
                        config["device"]
                    )
            else:
                self.device = None
            if "grantTypes" in config:
                if isinstance(config["grantTypes"],
                              GrantTypePolicyRuleCondition):
                    self.grant_types = config["grantTypes"]
                else:
                    self.grant_types = GrantTypePolicyRuleCondition(
                        config["grantTypes"]
                    )
            else:
                self.grant_types = None
            if "groups" in config:
                if isinstance(config["groups"],
                              GroupPolicyRuleCondition):
                    self.groups = config["groups"]
                else:
                    self.groups = GroupPolicyRuleCondition(
                        config["groups"]
                    )
            else:
                self.groups = None
            if "identityProvider" in config:
                if isinstance(config["identityProvider"],
                              IdentityProviderPolicyRuleCondition):
                    self.identity_provider = config["identityProvider"]
                else:
                    self.identity_provider = IdentityProviderPolicyRuleCondition(
                        config["identityProvider"]
                    )
            else:
                self.identity_provider = None
            if "mdmEnrollment" in config:
                if isinstance(config["mdmEnrollment"],
                              MdmEnrollmentPolicyRuleCondition):
                    self.mdm_enrollment = config["mdmEnrollment"]
                else:
                    self.mdm_enrollment = MdmEnrollmentPolicyRuleCondition(
                        config["mdmEnrollment"]
                    )
            else:
                self.mdm_enrollment = None
            if "network" in config:
                if isinstance(config["network"],
                              PolicyNetworkCondition):
                    self.network = config["network"]
                else:
                    self.network = PolicyNetworkCondition(
                        config["network"]
                    )
            else:
                self.network = None
            if "people" in config:
                if isinstance(config["people"],
                              PolicyPeopleCondition):
                    self.people = config["people"]
                else:
                    self.people = PolicyPeopleCondition(
                        config["people"]
                    )
            else:
                self.people = None
            if "platform" in config:
                if isinstance(config["platform"],
                              PlatformPolicyRuleCondition):
                    self.platform = config["platform"]
                else:
                    self.platform = PlatformPolicyRuleCondition(
                        config["platform"]
                    )
            else:
                self.platform = None
            if "risk" in config:
                if isinstance(config["risk"],
                              RiskPolicyRuleCondition):
                    self.risk = config["risk"]
                else:
                    self.risk = RiskPolicyRuleCondition(
                        config["risk"]
                    )
            else:
                self.risk = None
            if "riskScore" in config:
                if isinstance(config["riskScore"],
                              RiskScorePolicyRuleCondition):
                    self.risk_score = config["riskScore"]
                else:
                    self.risk_score = RiskScorePolicyRuleCondition(
                        config["riskScore"]
                    )
            else:
                self.risk_score = None
            if "scopes" in config:
                if isinstance(config["scopes"],
                              OAuth2ScopesMediationPolicyRuleCondition):
                    self.scopes = config["scopes"]
                else:
                    self.scopes = OAuth2ScopesMediationPolicyRuleCondition(
                        config["scopes"]
                    )
            else:
                self.scopes = None
            if "userIdentifier" in config:
                if isinstance(config["userIdentifier"],
                              UserIdentifierPolicyRuleCondition):
                    self.user_identifier = config["userIdentifier"]
                else:
                    self.user_identifier = UserIdentifierPolicyRuleCondition(
                        config["userIdentifier"]
                    )
            else:
                self.user_identifier = None
            if "userStatus" in config:
                if isinstance(config["userStatus"],
                              UserStatusPolicyRuleCondition):
                    self.user_status = config["userStatus"]
                else:
                    self.user_status = UserStatusPolicyRuleCondition(
                        config["userStatus"]
                    )
            else:
                self.user_status = None
            if "users" in config:
                if isinstance(config["users"],
                              UserPolicyRuleCondition):
                    self.users = config["users"]
                else:
                    self.users = UserPolicyRuleCondition(
                        config["users"]
                    )
            else:
                self.users = None
        else:
            self.app = None
            self.apps = None
            self.auth_context = None
            self.auth_provider = None
            self.before_scheduled_action = None
            self.clients = None
            self.context = None
            self.device = None
            self.grant_types = None
            self.groups = None
            self.identity_provider = None
            self.mdm_enrollment = None
            self.network = None
            self.people = None
            self.platform = None
            self.risk = None
            self.risk_score = None
            self.scopes = None
            self.user_identifier = None
            self.user_status = None
            self.users = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "app": self.app,
            "apps": self.apps,
            "authContext": self.auth_context,
            "authProvider": self.auth_provider,
            "beforeScheduledAction": self.before_scheduled_action,
            "clients": self.clients,
            "context": self.context,
            "device": self.device,
            "grantTypes": self.grant_types,
            "groups": self.groups,
            "identityProvider": self.identity_provider,
            "mdmEnrollment": self.mdm_enrollment,
            "network": self.network,
            "people": self.people,
            "platform": self.platform,
            "risk": self.risk,
            "riskScore": self.risk_score,
            "scopes": self.scopes,
            "userIdentifier": self.user_identifier,
            "userStatus": self.user_status,
            "users": self.users
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
