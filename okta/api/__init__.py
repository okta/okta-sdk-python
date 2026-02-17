# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

# flake8: noqa

import importlib as _importlib

# Lazy import mapping: attribute name -> module path
_LAZY_IMPORT_MAP = {
    "AgentPoolsApi": "okta.api.agent_pools_api",
    "ApiServiceIntegrationsApi": "okta.api.api_service_integrations_api",
    "ApiTokenApi": "okta.api.api_token_api",
    "ApplicationApi": "okta.api.application_api",
    "ApplicationConnectionsApi": "okta.api.application_connections_api",
    "ApplicationCrossAppAccessConnectionsApi": "okta.api.application_cross_app_access_connections_api",
    "ApplicationFeaturesApi": "okta.api.application_features_api",
    "ApplicationGrantsApi": "okta.api.application_grants_api",
    "ApplicationGroupsApi": "okta.api.application_groups_api",
    "ApplicationLogosApi": "okta.api.application_logos_api",
    "ApplicationPoliciesApi": "okta.api.application_policies_api",
    "ApplicationSSOApi": "okta.api.application_sso_api",
    "ApplicationSSOCredentialKeyApi": "okta.api.application_sso_credential_key_api",
    "ApplicationSSOFederatedClaimsApi": "okta.api.application_sso_federated_claims_api",
    "ApplicationSSOPublicKeysApi": "okta.api.application_sso_public_keys_api",
    "ApplicationTokensApi": "okta.api.application_tokens_api",
    "ApplicationUsersApi": "okta.api.application_users_api",
    "AssociatedDomainCustomizationsApi": "okta.api.associated_domain_customizations_api",
    "AttackProtectionApi": "okta.api.attack_protection_api",
    "AuthenticatorApi": "okta.api.authenticator_api",
    "AuthorizationServerApi": "okta.api.authorization_server_api",
    "AuthorizationServerAssocApi": "okta.api.authorization_server_assoc_api",
    "AuthorizationServerClaimsApi": "okta.api.authorization_server_claims_api",
    "AuthorizationServerClientsApi": "okta.api.authorization_server_clients_api",
    "AuthorizationServerKeysApi": "okta.api.authorization_server_keys_api",
    "AuthorizationServerPoliciesApi": "okta.api.authorization_server_policies_api",
    "AuthorizationServerRulesApi": "okta.api.authorization_server_rules_api",
    "AuthorizationServerScopesApi": "okta.api.authorization_server_scopes_api",
    "BehaviorApi": "okta.api.behavior_api",
    "BrandsApi": "okta.api.brands_api",
    "CAPTCHAApi": "okta.api.captcha_api",
    "CustomDomainApi": "okta.api.custom_domain_api",
    "CustomPagesApi": "okta.api.custom_pages_api",
    "CustomTemplatesApi": "okta.api.custom_templates_api",
    "DeviceApi": "okta.api.device_api",
    "DeviceAssuranceApi": "okta.api.device_assurance_api",
    "DeviceIntegrationsApi": "okta.api.device_integrations_api",
    "DevicePostureCheckApi": "okta.api.device_posture_check_api",
    "DirectoriesIntegrationApi": "okta.api.directories_integration_api",
    "EmailCustomizationApi": "okta.api.email_customization_api",
    "EmailDomainApi": "okta.api.email_domain_api",
    "EmailServerApi": "okta.api.email_server_api",
    "EventHookApi": "okta.api.event_hook_api",
    "FeatureApi": "okta.api.feature_api",
    "GovernanceBundleApi": "okta.api.governance_bundle_api",
    "GroupApi": "okta.api.group_api",
    "GroupOwnerApi": "okta.api.group_owner_api",
    "GroupPushMappingApi": "okta.api.group_push_mapping_api",
    "GroupRuleApi": "okta.api.group_rule_api",
    "HookKeyApi": "okta.api.hook_key_api",
    "IdentityProviderApi": "okta.api.identity_provider_api",
    "IdentityProviderKeysApi": "okta.api.identity_provider_keys_api",
    "IdentityProviderSigningKeysApi": "okta.api.identity_provider_signing_keys_api",
    "IdentityProviderUsersApi": "okta.api.identity_provider_users_api",
    "IdentitySourceApi": "okta.api.identity_source_api",
    "InlineHookApi": "okta.api.inline_hook_api",
    "LinkedObjectApi": "okta.api.linked_object_api",
    "LogStreamApi": "okta.api.log_stream_api",
    "NetworkZoneApi": "okta.api.network_zone_api",
    "OAuth2ResourceServerCredentialsKeysApi": "okta.api.o_auth2_resource_server_credentials_keys_api",
    "OktaApplicationSettingsApi": "okta.api.okta_application_settings_api",
    "OktaPersonalSettingsApi": "okta.api.okta_personal_settings_api",
    "OrgCreatorApi": "okta.api.org_creator_api",
    "OrgSettingAdminApi": "okta.api.org_setting_admin_api",
    "OrgSettingCommunicationApi": "okta.api.org_setting_communication_api",
    "OrgSettingContactApi": "okta.api.org_setting_contact_api",
    "OrgSettingCustomizationApi": "okta.api.org_setting_customization_api",
    "OrgSettingGeneralApi": "okta.api.org_setting_general_api",
    "OrgSettingMetadataApi": "okta.api.org_setting_metadata_api",
    "OrgSettingSupportApi": "okta.api.org_setting_support_api",
    "PolicyApi": "okta.api.policy_api",
    "PrincipalRateLimitApi": "okta.api.principal_rate_limit_api",
    "ProfileMappingApi": "okta.api.profile_mapping_api",
    "PushProviderApi": "okta.api.push_provider_api",
    "RateLimitSettingsApi": "okta.api.rate_limit_settings_api",
    "RealmApi": "okta.api.realm_api",
    "RealmAssignmentApi": "okta.api.realm_assignment_api",
    "RoleAssignmentAUserApi": "okta.api.role_assignment_a_user_api",
    "RoleAssignmentBGroupApi": "okta.api.role_assignment_b_group_api",
    "RoleAssignmentClientApi": "okta.api.role_assignment_client_api",
    "RoleBTargetAdminApi": "okta.api.role_b_target_admin_api",
    "RoleBTargetBGroupApi": "okta.api.role_b_target_b_group_api",
    "RoleBTargetClientApi": "okta.api.role_b_target_client_api",
    "RoleCResourceSetApi": "okta.api.role_c_resource_set_api",
    "RoleCResourceSetResourceApi": "okta.api.role_c_resource_set_resource_api",
    "RoleDResourceSetBindingApi": "okta.api.role_d_resource_set_binding_api",
    "RoleDResourceSetBindingMemberApi": "okta.api.role_d_resource_set_binding_member_api",
    "RoleECustomApi": "okta.api.role_e_custom_api",
    "RoleECustomPermissionApi": "okta.api.role_e_custom_permission_api",
    "SSFReceiverApi": "okta.api.ssf_receiver_api",
    "SSFSecurityEventTokenApi": "okta.api.ssf_security_event_token_api",
    "SSFTransmitterApi": "okta.api.ssf_transmitter_api",
    "SchemaApi": "okta.api.schema_api",
    "ServiceAccountApi": "okta.api.service_account_api",
    "SessionApi": "okta.api.session_api",
    "SubscriptionApi": "okta.api.subscription_api",
    "SystemLogApi": "okta.api.system_log_api",
    "TemplateApi": "okta.api.template_api",
    "ThemesApi": "okta.api.themes_api",
    "ThreatInsightApi": "okta.api.threat_insight_api",
    "TrustedOriginApi": "okta.api.trusted_origin_api",
    "UISchemaApi": "okta.api.ui_schema_api",
    "UserApi": "okta.api.user_api",
    "UserAuthenticatorEnrollmentsApi": "okta.api.user_authenticator_enrollments_api",
    "UserClassificationApi": "okta.api.user_classification_api",
    "UserCredApi": "okta.api.user_cred_api",
    "UserFactorApi": "okta.api.user_factor_api",
    "UserGrantApi": "okta.api.user_grant_api",
    "UserLifecycleApi": "okta.api.user_lifecycle_api",
    "UserLinkedObjectApi": "okta.api.user_linked_object_api",
    "UserOAuthApi": "okta.api.user_o_auth_api",
    "UserResourcesApi": "okta.api.user_resources_api",
    "UserRiskApi": "okta.api.user_risk_api",
    "UserSessionsApi": "okta.api.user_sessions_api",
    "UserTypeApi": "okta.api.user_type_api",
    "WebAuthnPreregistrationApi": "okta.api.web_authn_preregistration_api",
}


def __getattr__(name):
    if name in _LAZY_IMPORT_MAP:
        module = _importlib.import_module(_LAZY_IMPORT_MAP[name])
        attr = getattr(module, name)
        globals()[name] = attr
        return attr
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(_LAZY_IMPORT_MAP.keys()) + list(globals().keys())
