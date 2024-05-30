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
from okta.models import app_and_instance_policy_rule_condition\
    as app_and_instance_policy_rule_condition
from okta.models import app_instance_policy_rule_condition\
    as app_instance_policy_rule_condition
from okta.models import policy_rule_auth_context_condition\
    as policy_rule_auth_context_condition
from okta.models import password_policy_authentication_provider_condition\
    as password_policy_authentication_provider_condition
from okta.models import before_scheduled_action_policy_rule_condition\
    as before_scheduled_action_policy_rule_condition
from okta.models import client_policy_condition\
    as client_policy_condition
from okta.models import context_policy_rule_condition\
    as context_policy_rule_condition
from okta.models import device_policy_rule_condition\
    as device_policy_rule_condition
from okta.models import grant_type_policy_rule_condition\
    as grant_type_policy_rule_condition
from okta.models import group_policy_rule_condition\
    as group_policy_rule_condition
from okta.models import identity_provider_policy_rule_condition\
    as identity_provider_policy_rule_condition
from okta.models import mdm_enrollment_policy_rule_condition\
    as mdm_enrollment_policy_rule_condition
from okta.models import policy_network_condition\
    as policy_network_condition
from okta.models import policy_people_condition\
    as policy_people_condition
from okta.models import platform_policy_rule_condition\
    as platform_policy_rule_condition
from okta.models import risk_policy_rule_condition\
    as risk_policy_rule_condition
from okta.models import risk_score_policy_rule_condition\
    as risk_score_policy_rule_condition
from okta.models import o_auth_2_scopes_mediation_policy_rule_condition\
    as o_auth_2_scopes_mediation_policy_rule_condition
from okta.models import user_identifier_policy_rule_condition\
    as user_identifier_policy_rule_condition
from okta.models import user_status_policy_rule_condition\
    as user_status_policy_rule_condition
from okta.models import user_policy_rule_condition\
    as user_policy_rule_condition


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
                              app_and_instance_policy_rule_condition.AppAndInstancePolicyRuleCondition):
                    self.app = config["app"]
                elif config["app"] is not None:
                    self.app = app_and_instance_policy_rule_condition.AppAndInstancePolicyRuleCondition(
                        config["app"]
                    )
                else:
                    self.app = None
            else:
                self.app = None
            if "apps" in config:
                if isinstance(config["apps"],
                              app_instance_policy_rule_condition.AppInstancePolicyRuleCondition):
                    self.apps = config["apps"]
                elif config["apps"] is not None:
                    self.apps = app_instance_policy_rule_condition.AppInstancePolicyRuleCondition(
                        config["apps"]
                    )
                else:
                    self.apps = None
            else:
                self.apps = None
            if "authContext" in config:
                if isinstance(config["authContext"],
                              policy_rule_auth_context_condition.PolicyRuleAuthContextCondition):
                    self.auth_context = config["authContext"]
                elif config["authContext"] is not None:
                    self.auth_context = policy_rule_auth_context_condition.PolicyRuleAuthContextCondition(
                        config["authContext"]
                    )
                else:
                    self.auth_context = None
            else:
                self.auth_context = None
            if "authProvider" in config:
                if isinstance(config["authProvider"],
                              password_policy_authentication_provider_condition.PasswordPolicyAuthenticationProviderCondition):
                    self.auth_provider = config["authProvider"]
                elif config["authProvider"] is not None:
                    self.auth_provider = password_policy_authentication_provider_condition.PasswordPolicyAuthenticationProviderCondition(
                        config["authProvider"]
                    )
                else:
                    self.auth_provider = None
            else:
                self.auth_provider = None
            if "beforeScheduledAction" in config:
                if isinstance(config["beforeScheduledAction"],
                              before_scheduled_action_policy_rule_condition.BeforeScheduledActionPolicyRuleCondition):
                    self.before_scheduled_action = config["beforeScheduledAction"]
                elif config["beforeScheduledAction"] is not None:
                    self.before_scheduled_action = before_scheduled_action_policy_rule_condition.BeforeScheduledActionPolicyRuleCondition(
                        config["beforeScheduledAction"]
                    )
                else:
                    self.before_scheduled_action = None
            else:
                self.before_scheduled_action = None
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
            if "context" in config:
                if isinstance(config["context"],
                              context_policy_rule_condition.ContextPolicyRuleCondition):
                    self.context = config["context"]
                elif config["context"] is not None:
                    self.context = context_policy_rule_condition.ContextPolicyRuleCondition(
                        config["context"]
                    )
                else:
                    self.context = None
            else:
                self.context = None
            if "device" in config:
                if isinstance(config["device"],
                              device_policy_rule_condition.DevicePolicyRuleCondition):
                    self.device = config["device"]
                elif config["device"] is not None:
                    self.device = device_policy_rule_condition.DevicePolicyRuleCondition(
                        config["device"]
                    )
                else:
                    self.device = None
            else:
                self.device = None
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
            if "groups" in config:
                if isinstance(config["groups"],
                              group_policy_rule_condition.GroupPolicyRuleCondition):
                    self.groups = config["groups"]
                elif config["groups"] is not None:
                    self.groups = group_policy_rule_condition.GroupPolicyRuleCondition(
                        config["groups"]
                    )
                else:
                    self.groups = None
            else:
                self.groups = None
            if "identityProvider" in config:
                if isinstance(config["identityProvider"],
                              identity_provider_policy_rule_condition.IdentityProviderPolicyRuleCondition):
                    self.identity_provider = config["identityProvider"]
                elif config["identityProvider"] is not None:
                    self.identity_provider = identity_provider_policy_rule_condition.IdentityProviderPolicyRuleCondition(
                        config["identityProvider"]
                    )
                else:
                    self.identity_provider = None
            else:
                self.identity_provider = None
            if "mdmEnrollment" in config:
                if isinstance(config["mdmEnrollment"],
                              mdm_enrollment_policy_rule_condition.MdmEnrollmentPolicyRuleCondition):
                    self.mdm_enrollment = config["mdmEnrollment"]
                elif config["mdmEnrollment"] is not None:
                    self.mdm_enrollment = mdm_enrollment_policy_rule_condition.MdmEnrollmentPolicyRuleCondition(
                        config["mdmEnrollment"]
                    )
                else:
                    self.mdm_enrollment = None
            else:
                self.mdm_enrollment = None
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
            if "platform" in config:
                if isinstance(config["platform"],
                              platform_policy_rule_condition.PlatformPolicyRuleCondition):
                    self.platform = config["platform"]
                elif config["platform"] is not None:
                    self.platform = platform_policy_rule_condition.PlatformPolicyRuleCondition(
                        config["platform"]
                    )
                else:
                    self.platform = None
            else:
                self.platform = None
            if "risk" in config:
                if isinstance(config["risk"],
                              risk_policy_rule_condition.RiskPolicyRuleCondition):
                    self.risk = config["risk"]
                elif config["risk"] is not None:
                    self.risk = risk_policy_rule_condition.RiskPolicyRuleCondition(
                        config["risk"]
                    )
                else:
                    self.risk = None
            else:
                self.risk = None
            if "riskScore" in config:
                if isinstance(config["riskScore"],
                              risk_score_policy_rule_condition.RiskScorePolicyRuleCondition):
                    self.risk_score = config["riskScore"]
                elif config["riskScore"] is not None:
                    self.risk_score = risk_score_policy_rule_condition.RiskScorePolicyRuleCondition(
                        config["riskScore"]
                    )
                else:
                    self.risk_score = None
            else:
                self.risk_score = None
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
            if "userIdentifier" in config:
                if isinstance(config["userIdentifier"],
                              user_identifier_policy_rule_condition.UserIdentifierPolicyRuleCondition):
                    self.user_identifier = config["userIdentifier"]
                elif config["userIdentifier"] is not None:
                    self.user_identifier = user_identifier_policy_rule_condition.UserIdentifierPolicyRuleCondition(
                        config["userIdentifier"]
                    )
                else:
                    self.user_identifier = None
            else:
                self.user_identifier = None
            if "userStatus" in config:
                if isinstance(config["userStatus"],
                              user_status_policy_rule_condition.UserStatusPolicyRuleCondition):
                    self.user_status = config["userStatus"]
                elif config["userStatus"] is not None:
                    self.user_status = user_status_policy_rule_condition.UserStatusPolicyRuleCondition(
                        config["userStatus"]
                    )
                else:
                    self.user_status = None
            else:
                self.user_status = None
            if "users" in config:
                if isinstance(config["users"],
                              user_policy_rule_condition.UserPolicyRuleCondition):
                    self.users = config["users"]
                elif config["users"] is not None:
                    self.users = user_policy_rule_condition.UserPolicyRuleCondition(
                        config["users"]
                    )
                else:
                    self.users = None
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
