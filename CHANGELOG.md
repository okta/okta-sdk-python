# Okta Python SDK Changelog

# 3.1.0

## OVERVIEW

This release updates the Okta Python SDK with the 5.1.0 Okta Management API specifications, introduces pagination support for list operations, and includes important changes to the SDK generation tooling.

### What's New

* **Updated API Specifications**: The SDK has been regenerated using the v5.1.0 Okta Management OpenAPI specifications, bringing support for new endpoints and enhanced functionality across the API surface.

* **Pagination Support**: List operations now support pagination for efficient handling of large result sets. For detailed usage instructions and examples, please refer to `README.md## Pagination`.

* **OpenAPI Generator Tooling Update**: The SDK generation process has transitioned from the npm-based `openapi-generator-cli` to the JAR-based version due to configuration limitations in the npm package. Contributors and maintainers should now use the OpenAPI Generator JAR file for SDK generation. Download instructions: https://openapi-generator.tech/docs/installation#jar

---

## API CHANGES FROM VERSION 3.0.0 TO 3.1.0

## SUMMARY

* **New API Files**: 66
* **Removed API Files**: 9
* **Modified API Files**: 16
* **Unchanged API Files**: 34
* **Total New Methods in Existing APIs**: 29
* **Total Removed Methods**: 99
* **Total Methods in New API Files**: 368

## NEW API FILES

### APPLICATION_CROSS_APP_ACCESS_CONNECTIONS_API
**API Class**: `ApplicationCrossAppAccessConnectionsApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_cross_app_access_connection` (NEW)
* ✓ `delete_cross_app_access_connection` (NEW)
* ✓ `get_all_cross_app_access_connections` (NEW)
* ✓ `get_cross_app_access_connection` (NEW)
* ✓ `update_cross_app_access_connection` (NEW)

### APPLICATION_SSO_CREDENTIAL_KEY_API
**API Class**: `ApplicationSsoCredentialKeyApi`
**Total Methods**: 9

**Methods**:
* ✓ `clone_application_key` (NEW)
* ✓ `generate_application_key` (NEW)
* ✓ `generate_csr_for_application` (NEW)
* ✓ `get_application_key` (NEW)
* ✓ `get_csr_for_application` (NEW)
* ✓ `list_application_keys` (NEW)
* ✓ `list_csrs_for_application` (NEW)
* ✓ `publish_csr_from_application` (NEW)
* ✓ `revoke_csr_from_application` (NEW)

### APPLICATION_SSO_FEDERATED_CLAIMS_API
**API Class**: `ApplicationSsoFederatedClaimsApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_federated_claim` (NEW)
* ✓ `delete_federated_claim` (NEW)
* ✓ `get_federated_claim` (NEW)
* ✓ `list_federated_claims` (NEW)
* ✓ `replace_federated_claim` (NEW)

### APPLICATION_SSO_PUBLIC_KEYS_API
**API Class**: `ApplicationSsoPublicKeysApi`
**Total Methods**: 12

**Methods**:
* ✓ `activate_o_auth2_client_json_web_key` (NEW)
* ✓ `activate_o_auth2_client_secret` (NEW)
* ✓ `add_jwk` (NEW)
* ✓ `create_o_auth2_client_secret` (NEW)
* ✓ `deactivate_o_auth2_client_json_web_key` (NEW)
* ✓ `deactivate_o_auth2_client_secret` (NEW)
* ✓ `delete_o_auth2_client_secret` (NEW)
* ✓ `deletejwk` (NEW)
* ✓ `get_jwk` (NEW)
* ✓ `get_o_auth2_client_secret` (NEW)
* ✓ `list_jwk` (NEW)
* ✓ `list_o_auth2_client_secrets` (NEW)

### ASSOCIATED_DOMAIN_CUSTOMIZATIONS_API
**API Class**: `AssociatedDomainCustomizationsApi`
**Total Methods**: 7

**Methods**:
* ✓ `get_all_well_known_uris` (NEW)
* ✓ `get_apple_app_site_association_well_known_uri` (NEW)
* ✓ `get_asset_links_well_known_uri` (NEW)
* ✓ `get_brand_well_known_uri` (NEW)
* ✓ `get_root_brand_well_known_uri` (NEW)
* ✓ `get_web_authn_well_known_uri` (NEW)
* ✓ `replace_brand_well_known_uri` (NEW)

### AUTHORIZATION_SERVER_ASSOC_API
**API Class**: `AuthorizationServerAssocApi`
**Total Methods**: 3

**Methods**:
* ✓ `create_associated_servers` (NEW)
* ✓ `delete_associated_server` (NEW)
* ✓ `list_associated_servers_by_trusted_type` (NEW)

### AUTHORIZATION_SERVER_CLAIMS_API
**API Class**: `AuthorizationServerClaimsApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_o_auth2_claim` (NEW)
* ✓ `delete_o_auth2_claim` (NEW)
* ✓ `get_o_auth2_claim` (NEW)
* ✓ `list_o_auth2_claims` (NEW)
* ✓ `replace_o_auth2_claim` (NEW)

### AUTHORIZATION_SERVER_CLIENTS_API
**API Class**: `AuthorizationServerClientsApi`
**Total Methods**: 5

**Methods**:
* ✓ `get_refresh_token_for_authorization_server_and_client` (NEW)
* ✓ `list_o_auth2_clients_for_authorization_server` (NEW)
* ✓ `list_refresh_tokens_for_authorization_server_and_client` (NEW)
* ✓ `revoke_refresh_token_for_authorization_server_and_client` (NEW)
* ✓ `revoke_refresh_tokens_for_authorization_server_and_client` (NEW)

### AUTHORIZATION_SERVER_KEYS_API
**API Class**: `AuthorizationServerKeysApi`
**Total Methods**: 3

**Methods**:
* ✓ `get_authorization_server_key` (NEW)
* ✓ `list_authorization_server_keys` (NEW)
* ✓ `rotate_authorization_server_keys` (NEW)

### AUTHORIZATION_SERVER_POLICIES_API
**API Class**: `AuthorizationServerPoliciesApi`
**Total Methods**: 7

**Methods**:
* ✓ `activate_authorization_server_policy` (NEW)
* ✓ `create_authorization_server_policy` (NEW)
* ✓ `deactivate_authorization_server_policy` (NEW)
* ✓ `delete_authorization_server_policy` (NEW)
* ✓ `get_authorization_server_policy` (NEW)
* ✓ `list_authorization_server_policies` (NEW)
* ✓ `replace_authorization_server_policy` (NEW)

### AUTHORIZATION_SERVER_RULES_API
**API Class**: `AuthorizationServerRulesApi`
**Total Methods**: 7

**Methods**:
* ✓ `activate_authorization_server_policy_rule` (NEW)
* ✓ `create_authorization_server_policy_rule` (NEW)
* ✓ `deactivate_authorization_server_policy_rule` (NEW)
* ✓ `delete_authorization_server_policy_rule` (NEW)
* ✓ `get_authorization_server_policy_rule` (NEW)
* ✓ `list_authorization_server_policy_rules` (NEW)
* ✓ `replace_authorization_server_policy_rule` (NEW)

### AUTHORIZATION_SERVER_SCOPES_API
**API Class**: `AuthorizationServerScopesApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_o_auth2_scope` (NEW)
* ✓ `delete_o_auth2_scope` (NEW)
* ✓ `get_o_auth2_scope` (NEW)
* ✓ `list_o_auth2_scopes` (NEW)
* ✓ `replace_o_auth2_scope` (NEW)

### BRANDS_API
**API Class**: `BrandsApi`
**Total Methods**: 6

**Methods**:
* ✓ `create_brand` (NEW)
* ✓ `delete_brand` (NEW)
* ✓ `get_brand` (NEW)
* ✓ `list_brand_domains` (NEW)
* ✓ `list_brands` (NEW)
* ✓ `replace_brand` (NEW)

### CUSTOM_PAGES_API
**API Class**: `CustomPagesApi`
**Total Methods**: 19

**Methods**:
* ✓ `delete_customized_error_page` (NEW)
* ✓ `delete_customized_sign_in_page` (NEW)
* ✓ `delete_preview_error_page` (NEW)
* ✓ `delete_preview_sign_in_page` (NEW)
* ✓ `get_customized_error_page` (NEW)
* ✓ `get_customized_sign_in_page` (NEW)
* ✓ `get_default_error_page` (NEW)
* ✓ `get_default_sign_in_page` (NEW)
* ✓ `get_error_page` (NEW)
* ✓ `get_preview_error_page` (NEW)
* ✓ `get_preview_sign_in_page` (NEW)
* ✓ `get_sign_in_page` (NEW)
* ✓ `get_sign_out_page_settings` (NEW)
* ✓ `list_all_sign_in_widget_versions` (NEW)
* ✓ `replace_customized_error_page` (NEW)
* ✓ `replace_customized_sign_in_page` (NEW)
* ✓ `replace_preview_error_page` (NEW)
* ✓ `replace_preview_sign_in_page` (NEW)
* ✓ `replace_sign_out_page_settings` (NEW)

### CUSTOM_TEMPLATES_API
**API Class**: `CustomTemplatesApi`
**Total Methods**: 14

**Methods**:
* ✓ `create_email_customization` (NEW)
* ✓ `delete_all_customizations` (NEW)
* ✓ `delete_email_customization` (NEW)
* ✓ `get_customization_preview` (NEW)
* ✓ `get_email_customization` (NEW)
* ✓ `get_email_default_content` (NEW)
* ✓ `get_email_default_preview` (NEW)
* ✓ `get_email_settings` (NEW)
* ✓ `get_email_template` (NEW)
* ✓ `list_email_customizations` (NEW)
* ✓ `list_email_templates` (NEW)
* ✓ `replace_email_customization` (NEW)
* ✓ `replace_email_settings` (NEW)
* ✓ `send_test_email` (NEW)

### DEVICE_INTEGRATIONS_API
**API Class**: `DeviceIntegrationsApi`
**Total Methods**: 4

**Methods**:
* ✓ `activate_device_integration` (NEW)
* ✓ `deactivate_device_integration` (NEW)
* ✓ `get_device_integration` (NEW)
* ✓ `list_device_integrations` (NEW)

### DEVICE_POSTURE_CHECK_API
**API Class**: `DevicePostureCheckApi`
**Total Methods**: 6

**Methods**:
* ✓ `create_device_posture_check` (NEW)
* ✓ `delete_device_posture_check` (NEW)
* ✓ `get_device_posture_check` (NEW)
* ✓ `list_default_device_posture_checks` (NEW)
* ✓ `list_device_posture_checks` (NEW)
* ✓ `replace_device_posture_check` (NEW)

### DIRECTORIES_INTEGRATION_API
**API Class**: `DirectoriesIntegrationApi`
**Total Methods**: 1

**Methods**:
* ✓ `update_ad_group_membership` (NEW)

### EMAIL_CUSTOMIZATION_API
**API Class**: `EmailCustomizationApi`
**Total Methods**: 1

**Methods**:
* ✓ `bulk_remove_email_address_bounces` (NEW)

### GOVERNANCE_BUNDLE_API
**API Class**: `GovernanceBundleApi`
**Total Methods**: 10

**Methods**:
* ✓ `create_governance_bundle` (NEW)
* ✓ `delete_governance_bundle` (NEW)
* ✓ `get_governance_bundle` (NEW)
* ✓ `get_opt_in_status` (NEW)
* ✓ `list_bundle_entitlement_values` (NEW)
* ✓ `list_bundle_entitlements` (NEW)
* ✓ `list_governance_bundles` (NEW)
* ✓ `opt_in` (NEW)
* ✓ `opt_out` (NEW)
* ✓ `replace_governance_bundle` (NEW)

### GROUP_OWNER_API
**API Class**: `GroupOwnerApi`
**Total Methods**: 3

**Methods**:
* ✓ `assign_group_owner` (NEW)
* ✓ `delete_group_owner` (NEW)
* ✓ `list_group_owners` (NEW)

### GROUP_PUSH_MAPPING_API
**API Class**: `GroupPushMappingApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_group_push_mapping` (NEW)
* ✓ `delete_group_push_mapping` (NEW)
* ✓ `get_group_push_mapping` (NEW)
* ✓ `list_group_push_mappings` (NEW)
* ✓ `update_group_push_mapping` (NEW)

### GROUP_RULE_API
**API Class**: `GroupRuleApi`
**Total Methods**: 7

**Methods**:
* ✓ `activate_group_rule` (NEW)
* ✓ `create_group_rule` (NEW)
* ✓ `deactivate_group_rule` (NEW)
* ✓ `delete_group_rule` (NEW)
* ✓ `get_group_rule` (NEW)
* ✓ `list_group_rules` (NEW)
* ✓ `replace_group_rule` (NEW)

### IDENTITY_PROVIDER_KEYS_API
**API Class**: `IdentityProviderKeysApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_identity_provider_key` (NEW)
* ✓ `delete_identity_provider_key` (NEW)
* ✓ `get_identity_provider_key` (NEW)
* ✓ `list_identity_provider_keys` (NEW)
* ✓ `replace_identity_provider_key` (NEW)

### IDENTITY_PROVIDER_SIGNING_KEYS_API
**API Class**: `IdentityProviderSigningKeysApi`
**Total Methods**: 10

**Methods**:
* ✓ `clone_identity_provider_key` (NEW)
* ✓ `generate_csr_for_identity_provider` (NEW)
* ✓ `generate_identity_provider_signing_key` (NEW)
* ✓ `get_csr_for_identity_provider` (NEW)
* ✓ `get_identity_provider_signing_key` (NEW)
* ✓ `list_active_identity_provider_signing_key` (NEW)
* ✓ `list_csrs_for_identity_provider` (NEW)
* ✓ `list_identity_provider_signing_keys` (NEW)
* ✓ `publish_csr_for_identity_provider` (NEW)
* ✓ `revoke_csr_for_identity_provider` (NEW)

### IDENTITY_PROVIDER_USERS_API
**API Class**: `IdentityProviderUsersApi`
**Total Methods**: 6

**Methods**:
* ✓ `get_identity_provider_application_user` (NEW)
* ✓ `link_user_to_identity_provider` (NEW)
* ✓ `list_identity_provider_application_users` (NEW)
* ✓ `list_social_auth_tokens` (NEW)
* ✓ `list_user_identity_providers` (NEW)
* ✓ `unlink_user_from_identity_provider` (NEW)

### O_AUTH2_RESOURCE_SERVER_CREDENTIALS_KEYS_API
**API Class**: `OAuth2ResourceServerCredentialsKeysApi`
**Total Methods**: 6

**Methods**:
* ✓ `activate_o_auth2_resource_server_json_web_key` (NEW)
* ✓ `add_o_auth2_resource_server_json_web_key` (NEW)
* ✓ `deactivate_o_auth2_resource_server_json_web_key` (NEW)
* ✓ `delete_o_auth2_resource_server_json_web_key` (NEW)
* ✓ `get_o_auth2_resource_server_json_web_key` (NEW)
* ✓ `list_o_auth2_resource_server_json_web_keys` (NEW)

### OKTA_APPLICATION_SETTINGS_API
**API Class**: `OktaApplicationSettingsApi`
**Total Methods**: 2

**Methods**:
* ✓ `get_first_party_app_settings` (NEW)
* ✓ `replace_first_party_app_settings` (NEW)

### OKTA_PERSONAL_SETTINGS_API
**API Class**: `OktaPersonalSettingsApi`
**Total Methods**: 3

**Methods**:
* ✓ `list_personal_apps_export_block_list` (NEW)
* ✓ `replace_blocked_email_domains` (NEW)
* ✓ `replace_okta_personal_admin_settings` (NEW)

### ORG_CREATOR_API
**API Class**: `OrgCreatorApi`
**Total Methods**: 1

**Methods**:
* ✓ `create_child_org` (NEW)

### ORG_SETTING_ADMIN_API
**API Class**: `OrgSettingAdminApi`
**Total Methods**: 6

**Methods**:
* ✓ `assign_client_privileges_setting` (NEW)
* ✓ `get_auto_assign_admin_app_setting` (NEW)
* ✓ `get_client_privileges_setting` (NEW)
* ✓ `get_third_party_admin_setting` (NEW)
* ✓ `update_auto_assign_admin_app_setting` (NEW)
* ✓ `update_third_party_admin_setting` (NEW)

### ORG_SETTING_COMMUNICATION_API
**API Class**: `OrgSettingCommunicationApi`
**Total Methods**: 3

**Methods**:
* ✓ `get_okta_communication_settings` (NEW)
* ✓ `opt_in_users_to_okta_communication_emails` (NEW)
* ✓ `opt_out_users_from_okta_communication_emails` (NEW)

### ORG_SETTING_CONTACT_API
**API Class**: `OrgSettingContactApi`
**Total Methods**: 3

**Methods**:
* ✓ `get_org_contact_user` (NEW)
* ✓ `list_org_contact_types` (NEW)
* ✓ `replace_org_contact_user` (NEW)

### ORG_SETTING_CUSTOMIZATION_API
**API Class**: `OrgSettingCustomizationApi`
**Total Methods**: 3

**Methods**:
* ✓ `get_org_preferences` (NEW)
* ✓ `set_org_hide_okta_ui_footer` (NEW)
* ✓ `set_org_show_okta_ui_footer` (NEW)

### ORG_SETTING_GENERAL_API
**API Class**: `OrgSettingGeneralApi`
**Total Methods**: 3

**Methods**:
* ✓ `get_org_settings` (NEW)
* ✓ `replace_org_settings` (NEW)
* ✓ `update_org_settings` (NEW)

### ORG_SETTING_METADATA_API
**API Class**: `OrgSettingMetadataApi`
**Total Methods**: 1

**Methods**:
* ✓ `get_wellknown_org_metadata` (NEW)

### ORG_SETTING_SUPPORT_API
**API Class**: `OrgSettingSupportApi`
**Total Methods**: 9

**Methods**:
* ✓ `extend_okta_support` (NEW)
* ✓ `get_aerial_consent` (NEW)
* ✓ `get_org_okta_support_settings` (NEW)
* ✓ `grant_aerial_consent` (NEW)
* ✓ `grant_okta_support` (NEW)
* ✓ `list_okta_support_cases` (NEW)
* ✓ `revoke_aerial_consent` (NEW)
* ✓ `revoke_okta_support` (NEW)
* ✓ `update_okta_support_case` (NEW)

### REALM_ASSIGNMENT_API
**API Class**: `RealmAssignmentApi`
**Total Methods**: 9

**Methods**:
* ✓ `activate_realm_assignment` (NEW)
* ✓ `create_realm_assignment` (NEW)
* ✓ `deactivate_realm_assignment` (NEW)
* ✓ `delete_realm_assignment` (NEW)
* ✓ `execute_realm_assignment` (NEW)
* ✓ `get_realm_assignment` (NEW)
* ✓ `list_realm_assignment_operations` (NEW)
* ✓ `list_realm_assignments` (NEW)
* ✓ `replace_realm_assignment` (NEW)

### ROLE_ASSIGNMENT_A_USER_API
**API Class**: `RoleAssignmentAUserApi`
**Total Methods**: 8

**Methods**:
* ✓ `assign_role_to_user` (NEW)
* ✓ `get_role_assignment_governance_grant` (NEW)
* ✓ `get_role_assignment_governance_grant_resources` (NEW)
* ✓ `get_user_assigned_role` (NEW)
* ✓ `get_user_assigned_role_governance` (NEW)
* ✓ `list_assigned_roles_for_user` (NEW)
* ✓ `list_users_with_role_assignments` (NEW)
* ✓ `unassign_role_from_user` (NEW)

### ROLE_ASSIGNMENT_B_GROUP_API
**API Class**: `RoleAssignmentBGroupApi`
**Total Methods**: 4

**Methods**:
* ✓ `assign_role_to_group` (NEW)
* ✓ `get_group_assigned_role` (NEW)
* ✓ `list_group_assigned_roles` (NEW)
* ✓ `unassign_role_from_group` (NEW)

### ROLE_ASSIGNMENT_CLIENT_API
**API Class**: `RoleAssignmentClientApi`
**Total Methods**: 4

**Methods**:
* ✓ `assign_role_to_client` (NEW)
* ✓ `delete_role_from_client` (NEW)
* ✓ `list_roles_for_client` (NEW)
* ✓ `retrieve_client_role` (NEW)

### ROLE_B_TARGET_ADMIN_API
**API Class**: `RoleBTargetAdminApi`
**Total Methods**: 10

**Methods**:
* ✓ `assign_all_apps_as_target_to_role_for_user` (NEW)
* ✓ `assign_app_instance_target_to_app_admin_role_for_user` (NEW)
* ✓ `assign_app_target_to_admin_role_for_user` (NEW)
* ✓ `assign_group_target_to_user_role` (NEW)
* ✓ `get_role_targets_by_user_id_and_role_id` (NEW)
* ✓ `list_application_targets_for_application_administrator_role_for_user` (NEW)
* ✓ `list_group_targets_for_role` (NEW)
* ✓ `unassign_app_instance_target_from_admin_role_for_user` (NEW)
* ✓ `unassign_app_target_from_app_admin_role_for_user` (NEW)
* ✓ `unassign_group_target_from_user_admin_role` (NEW)

### ROLE_B_TARGET_B_GROUP_API
**API Class**: `RoleBTargetBGroupApi`
**Total Methods**: 8

**Methods**:
* ✓ `assign_app_instance_target_to_app_admin_role_for_group` (NEW)
* ✓ `assign_app_target_to_admin_role_for_group` (NEW)
* ✓ `assign_group_target_to_group_admin_role` (NEW)
* ✓ `list_application_targets_for_application_administrator_role_for_group` (NEW)
* ✓ `list_group_targets_for_group_role` (NEW)
* ✓ `unassign_app_instance_target_to_app_admin_role_for_group` (NEW)
* ✓ `unassign_app_target_to_admin_role_for_group` (NEW)
* ✓ `unassign_group_target_from_group_admin_role` (NEW)

### ROLE_B_TARGET_CLIENT_API
**API Class**: `RoleBTargetClientApi`
**Total Methods**: 8

**Methods**:
* ✓ `assign_app_target_instance_role_for_client` (NEW)
* ✓ `assign_app_target_role_to_client` (NEW)
* ✓ `assign_group_target_role_for_client` (NEW)
* ✓ `list_app_target_role_to_client` (NEW)
* ✓ `list_group_target_role_for_client` (NEW)
* ✓ `remove_app_target_instance_role_for_client` (NEW)
* ✓ `remove_app_target_role_from_client` (NEW)
* ✓ `remove_group_target_role_from_client` (NEW)

### ROLE_C_RESOURCE_SET_API
**API Class**: `RoleCResourceSetApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_resource_set` (NEW)
* ✓ `delete_resource_set` (NEW)
* ✓ `get_resource_set` (NEW)
* ✓ `list_resource_sets` (NEW)
* ✓ `replace_resource_set` (NEW)

### ROLE_C_RESOURCE_SET_RESOURCE_API
**API Class**: `RoleCResourceSetResourceApi`
**Total Methods**: 6

**Methods**:
* ✓ `add_resource_set_resource` (NEW)
* ✓ `add_resource_set_resources` (NEW)
* ✓ `delete_resource_set_resource` (NEW)
* ✓ `get_resource_set_resource` (NEW)
* ✓ `list_resource_set_resources` (NEW)
* ✓ `replace_resource_set_resource` (NEW)

### ROLE_D_RESOURCE_SET_BINDING_API
**API Class**: `RoleDResourceSetBindingApi`
**Total Methods**: 4

**Methods**:
* ✓ `create_resource_set_binding` (NEW)
* ✓ `delete_binding` (NEW)
* ✓ `get_binding` (NEW)
* ✓ `list_bindings` (NEW)

### ROLE_D_RESOURCE_SET_BINDING_MEMBER_API
**API Class**: `RoleDResourceSetBindingMemberApi`
**Total Methods**: 4

**Methods**:
* ✓ `add_members_to_binding` (NEW)
* ✓ `get_member_of_binding` (NEW)
* ✓ `list_members_of_binding` (NEW)
* ✓ `unassign_member_from_binding` (NEW)

### ROLE_E_CUSTOM_API
**API Class**: `RoleECustomApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_role` (NEW)
* ✓ `delete_role` (NEW)
* ✓ `get_role` (NEW)
* ✓ `list_roles` (NEW)
* ✓ `replace_role` (NEW)

### ROLE_E_CUSTOM_PERMISSION_API
**API Class**: `RoleECustomPermissionApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_role_permission` (NEW)
* ✓ `delete_role_permission` (NEW)
* ✓ `get_role_permission` (NEW)
* ✓ `list_role_permissions` (NEW)
* ✓ `replace_role_permission` (NEW)

### SERVICE_ACCOUNT_API
**API Class**: `ServiceAccountApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_app_service_account` (NEW)
* ✓ `delete_app_service_account` (NEW)
* ✓ `get_app_service_account` (NEW)
* ✓ `list_app_service_accounts` (NEW)
* ✓ `update_app_service_account` (NEW)

### SSF_RECEIVER_API
**API Class**: `SsfReceiverApi`
**Total Methods**: 7

**Methods**:
* ✓ `activate_security_events_provider_instance` (NEW)
* ✓ `create_security_events_provider_instance` (NEW)
* ✓ `deactivate_security_events_provider_instance` (NEW)
* ✓ `delete_security_events_provider_instance` (NEW)
* ✓ `get_security_events_provider_instance` (NEW)
* ✓ `list_security_events_provider_instances` (NEW)
* ✓ `replace_security_events_provider_instance` (NEW)

### SSF_SECURITY_EVENT_TOKEN_API
**API Class**: `SsfSecurityEventTokenApi`
**Total Methods**: 1

**Methods**:
* ✓ `publish_security_event_tokens` (NEW)

### SSF_TRANSMITTER_API
**API Class**: `SsfTransmitterApi`
**Total Methods**: 8

**Methods**:
* ✓ `create_ssf_stream` (NEW)
* ✓ `delete_ssf_stream` (NEW)
* ✓ `get_ssf_stream_status` (NEW)
* ✓ `get_ssf_streams` (NEW)
* ✓ `get_wellknown_ssf_metadata` (NEW)
* ✓ `replace_ssf_stream` (NEW)
* ✓ `update_ssf_stream` (NEW)
* ✓ `verify_ssf_stream` (NEW)

### THEMES_API
**API Class**: `ThemesApi`
**Total Methods**: 9

**Methods**:
* ✓ `delete_brand_theme_background_image` (NEW)
* ✓ `delete_brand_theme_favicon` (NEW)
* ✓ `delete_brand_theme_logo` (NEW)
* ✓ `get_brand_theme` (NEW)
* ✓ `list_brand_themes` (NEW)
* ✓ `replace_brand_theme` (NEW)
* ✓ `upload_brand_theme_background_image` (NEW)
* ✓ `upload_brand_theme_favicon` (NEW)
* ✓ `upload_brand_theme_logo` (NEW)

### USER_AUTHENTICATOR_ENROLLMENTS_API
**API Class**: `UserAuthenticatorEnrollmentsApi`
**Total Methods**: 5

**Methods**:
* ✓ `create_authenticator_enrollment` (NEW)
* ✓ `create_tac_authenticator_enrollment` (NEW)
* ✓ `delete_authenticator_enrollment` (NEW)
* ✓ `get_authenticator_enrollment` (NEW)
* ✓ `list_authenticator_enrollments` (NEW)

### USER_CLASSIFICATION_API
**API Class**: `UserClassificationApi`
**Total Methods**: 2

**Methods**:
* ✓ `get_user_classification` (NEW)
* ✓ `replace_user_classification` (NEW)

### USER_CRED_API
**API Class**: `UserCredApi`
**Total Methods**: 7

**Methods**:
* ✓ `change_password` (NEW)
* ✓ `change_recovery_question` (NEW)
* ✓ `expire_password` (NEW)
* ✓ `expire_password_with_temp_password` (NEW)
* ✓ `forgot_password` (NEW)
* ✓ `forgot_password_set_new_password` (NEW)
* ✓ `reset_password` (NEW)

### USER_GRANT_API
**API Class**: `UserGrantApi`
**Total Methods**: 6

**Methods**:
* ✓ `get_user_grant` (NEW)
* ✓ `list_grants_for_user_and_client` (NEW)
* ✓ `list_user_grants` (NEW)
* ✓ `revoke_grants_for_user_and_client` (NEW)
* ✓ `revoke_user_grant` (NEW)
* ✓ `revoke_user_grants` (NEW)

### USER_LIFECYCLE_API
**API Class**: `UserLifecycleApi`
**Total Methods**: 7

**Methods**:
* ✓ `activate_user` (NEW)
* ✓ `deactivate_user` (NEW)
* ✓ `reactivate_user` (NEW)
* ✓ `reset_factors` (NEW)
* ✓ `suspend_user` (NEW)
* ✓ `unlock_user` (NEW)
* ✓ `unsuspend_user` (NEW)

### USER_LINKED_OBJECT_API
**API Class**: `UserLinkedObjectApi`
**Total Methods**: 3

**Methods**:
* ✓ `assign_linked_object_value_for_primary` (NEW)
* ✓ `delete_linked_object_for_user` (NEW)
* ✓ `list_linked_objects_for_user` (NEW)

### USER_O_AUTH_API
**API Class**: `UserOAuthApi`
**Total Methods**: 4

**Methods**:
* ✓ `get_refresh_token_for_user_and_client` (NEW)
* ✓ `list_refresh_tokens_for_user_and_client` (NEW)
* ✓ `revoke_token_for_user_and_client` (NEW)
* ✓ `revoke_tokens_for_user_and_client` (NEW)

### USER_RESOURCES_API
**API Class**: `UserResourcesApi`
**Total Methods**: 4

**Methods**:
* ✓ `list_app_links` (NEW)
* ✓ `list_user_clients` (NEW)
* ✓ `list_user_devices` (NEW)
* ✓ `list_user_groups` (NEW)

### USER_RISK_API
**API Class**: `UserRiskApi`
**Total Methods**: 2

**Methods**:
* ✓ `get_user_risk` (NEW)
* ✓ `upsert_user_risk` (NEW)

### USER_SESSIONS_API
**API Class**: `UserSessionsApi`
**Total Methods**: 1

**Methods**:
* ✓ `revoke_user_sessions` (NEW)

### WEB_AUTHN_PREREGISTRATION_API
**API Class**: `WebAuthnPreregistrationApi`
**Total Methods**: 7

**Methods**:
* ✓ `activate_preregistration_enrollment` (NEW)
* ✓ `assign_fulfillment_error_web_authn_preregistration_factor` (NEW)
* ✓ `delete_web_authn_preregistration_factor` (NEW)
* ✓ `enroll_preregistration_enrollment` (NEW)
* ✓ `generate_fulfillment_request` (NEW)
* ✓ `list_web_authn_preregistration_factors` (NEW)
* ✓ `send_pin` (NEW)

## REMOVED API FILES

### APPLICATION_CREDENTIALS_API
**API Class**: `ApplicationCredentialsApi`
**Total Methods Removed**: 9

**Removed Methods**:
* ✗ `clone_application_key` (REMOVED)
* ✗ `generate_application_key` (REMOVED)
* ✗ `generate_csr_for_application` (REMOVED)
* ✗ `get_application_key` (REMOVED)
* ✗ `get_csr_for_application` (REMOVED)
* ✗ `list_application_keys` (REMOVED)
* ✗ `list_csrs_for_application` (REMOVED)
* ✗ `publish_csr_from_application` (REMOVED)
* ✗ `revoke_csr_from_application` (REMOVED)

### CUSTOMIZATION_API
**API Class**: `CustomizationApi`
**Total Methods Removed**: 48

**Removed Methods**:
* ✗ `create_brand` (REMOVED)
* ✗ `create_email_customization` (REMOVED)
* ✗ `delete_all_customizations` (REMOVED)
* ✗ `delete_brand` (REMOVED)
* ✗ `delete_brand_theme_background_image` (REMOVED)
* ✗ `delete_brand_theme_favicon` (REMOVED)
* ✗ `delete_brand_theme_logo` (REMOVED)
* ✗ `delete_customized_error_page` (REMOVED)
* ✗ `delete_customized_sign_in_page` (REMOVED)
* ✗ `delete_email_customization` (REMOVED)
* ✗ `delete_preview_error_page` (REMOVED)
* ✗ `delete_preview_sign_in_page` (REMOVED)
* ✗ `get_brand` (REMOVED)
* ✗ `get_brand_theme` (REMOVED)
* ✗ `get_customization_preview` (REMOVED)
* ✗ `get_customized_error_page` (REMOVED)
* ✗ `get_customized_sign_in_page` (REMOVED)
* ✗ `get_default_error_page` (REMOVED)
* ✗ `get_default_sign_in_page` (REMOVED)
* ✗ `get_email_customization` (REMOVED)
* ✗ `get_email_default_content` (REMOVED)
* ✗ `get_email_default_preview` (REMOVED)
* ✗ `get_email_settings` (REMOVED)
* ✗ `get_email_template` (REMOVED)
* ✗ `get_error_page` (REMOVED)
* ✗ `get_preview_error_page` (REMOVED)
* ✗ `get_preview_sign_in_page` (REMOVED)
* ✗ `get_sign_in_page` (REMOVED)
* ✗ `get_sign_out_page_settings` (REMOVED)
* ✗ `list_all_sign_in_widget_versions` (REMOVED)
* ✗ `list_brand_domains` (REMOVED)
* ✗ `list_brand_themes` (REMOVED)
* ✗ `list_brands` (REMOVED)
* ✗ `list_email_customizations` (REMOVED)
* ✗ `list_email_templates` (REMOVED)
* ✗ `replace_brand` (REMOVED)
* ✗ `replace_brand_theme` (REMOVED)
* ✗ `replace_customized_error_page` (REMOVED)
* ✗ `replace_customized_sign_in_page` (REMOVED)
* ✗ `replace_email_customization` (REMOVED)
* ✗ `replace_email_settings` (REMOVED)
* ✗ `replace_preview_error_page` (REMOVED)
* ✗ `replace_preview_sign_in_page` (REMOVED)
* ✗ `replace_sign_out_page_settings` (REMOVED)
* ✗ `send_test_email` (REMOVED)
* ✗ `upload_brand_theme_background_image` (REMOVED)
* ✗ `upload_brand_theme_favicon` (REMOVED)
* ✗ `upload_brand_theme_logo` (REMOVED)

### ORG_SETTING_API
**API Class**: `OrgSettingApi`
**Total Methods Removed**: 19

**Removed Methods**:
* ✗ `bulk_remove_email_address_bounces` (REMOVED)
* ✗ `extend_okta_support` (REMOVED)
* ✗ `get_okta_communication_settings` (REMOVED)
* ✗ `get_org_contact_types` (REMOVED)
* ✗ `get_org_contact_user` (REMOVED)
* ✗ `get_org_okta_support_settings` (REMOVED)
* ✗ `get_org_preferences` (REMOVED)
* ✗ `get_org_settings` (REMOVED)
* ✗ `get_wellknown_org_metadata` (REMOVED)
* ✗ `grant_okta_support` (REMOVED)
* ✗ `opt_in_users_to_okta_communication_emails` (REMOVED)
* ✗ `opt_out_users_from_okta_communication_emails` (REMOVED)
* ✗ `replace_org_contact_user` (REMOVED)
* ✗ `replace_org_settings` (REMOVED)
* ✗ `revoke_okta_support` (REMOVED)
* ✗ `update_org_hide_okta_ui_footer` (REMOVED)
* ✗ `update_org_settings` (REMOVED)
* ✗ `update_org_show_okta_ui_footer` (REMOVED)
* ✗ `upload_org_logo` (REMOVED)

### RESOURCE_SET_API
**API Class**: `ResourceSetApi`
**Total Methods Removed**: 16

**Removed Methods**:
* ✗ `add_members_to_binding` (REMOVED)
* ✗ `add_resource_set_resource` (REMOVED)
* ✗ `create_resource_set` (REMOVED)
* ✗ `create_resource_set_binding` (REMOVED)
* ✗ `delete_binding` (REMOVED)
* ✗ `delete_resource_set` (REMOVED)
* ✗ `delete_resource_set_resource` (REMOVED)
* ✗ `get_binding` (REMOVED)
* ✗ `get_member_of_binding` (REMOVED)
* ✗ `get_resource_set` (REMOVED)
* ✗ `list_bindings` (REMOVED)
* ✗ `list_members_of_binding` (REMOVED)
* ✗ `list_resource_set_resources` (REMOVED)
* ✗ `list_resource_sets` (REMOVED)
* ✗ `replace_resource_set` (REMOVED)
* ✗ `unassign_member_from_binding` (REMOVED)

### RISK_EVENT_API
**API Class**: `RiskEventApi`
**Total Methods Removed**: 1

**Removed Methods**:
* ✗ `send_risk_events` (REMOVED)

### RISK_PROVIDER_API
**API Class**: `RiskProviderApi`
**Total Methods Removed**: 5

**Removed Methods**:
* ✗ `create_risk_provider` (REMOVED)
* ✗ `delete_risk_provider` (REMOVED)
* ✗ `get_risk_provider` (REMOVED)
* ✗ `list_risk_providers` (REMOVED)
* ✗ `replace_risk_provider` (REMOVED)

### ROLE_API
**API Class**: `RoleApi`
**Total Methods Removed**: 10

**Removed Methods**:
* ✗ `create_role` (REMOVED)
* ✗ `create_role_permission` (REMOVED)
* ✗ `delete_role` (REMOVED)
* ✗ `delete_role_permission` (REMOVED)
* ✗ `get_role` (REMOVED)
* ✗ `get_role_permission` (REMOVED)
* ✗ `list_role_permissions` (REMOVED)
* ✗ `list_roles` (REMOVED)
* ✗ `replace_role` (REMOVED)
* ✗ `replace_role_permission` (REMOVED)

### ROLE_ASSIGNMENT_API
**API Class**: `RoleAssignmentApi`
**Total Methods Removed**: 9

**Removed Methods**:
* ✗ `assign_role_to_group` (REMOVED)
* ✗ `assign_role_to_user` (REMOVED)
* ✗ `get_group_assigned_role` (REMOVED)
* ✗ `get_user_assigned_role` (REMOVED)
* ✗ `list_assigned_roles_for_user` (REMOVED)
* ✗ `list_group_assigned_roles` (REMOVED)
* ✗ `list_users_with_role_assignments` (REMOVED)
* ✗ `unassign_role_from_group` (REMOVED)
* ✗ `unassign_role_from_user` (REMOVED)

### ROLE_TARGET_API
**API Class**: `RoleTargetApi`
**Total Methods Removed**: 17

**Removed Methods**:
* ✗ `assign_all_apps_as_target_to_role_for_user` (REMOVED)
* ✗ `assign_app_instance_target_to_app_admin_role_for_group` (REMOVED)
* ✗ `assign_app_instance_target_to_app_admin_role_for_user` (REMOVED)
* ✗ `assign_app_target_to_admin_role_for_group` (REMOVED)
* ✗ `assign_app_target_to_admin_role_for_user` (REMOVED)
* ✗ `assign_group_target_to_group_admin_role` (REMOVED)
* ✗ `assign_group_target_to_user_role` (REMOVED)
* ✗ `list_application_targets_for_application_administrator_role_for_group` (REMOVED)
* ✗ `list_application_targets_for_application_administrator_role_for_user` (REMOVED)
* ✗ `list_group_targets_for_group_role` (REMOVED)
* ✗ `list_group_targets_for_role` (REMOVED)
* ✗ `unassign_app_instance_target_from_admin_role_for_user` (REMOVED)
* ✗ `unassign_app_instance_target_to_app_admin_role_for_group` (REMOVED)
* ✗ `unassign_app_target_from_app_admin_role_for_user` (REMOVED)
* ✗ `unassign_app_target_to_admin_role_for_group` (REMOVED)
* ✗ `unassign_group_target_from_group_admin_role` (REMOVED)
* ✗ `unassign_group_target_from_user_admin_role` (REMOVED)

## MODIFIED API FILES

### API_TOKEN_API
**API Class**: `ApiTokenApi`
**Added Methods**: 1
**Removed Methods**: 0
**Unchanged Methods**: 4

**New Methods**:
* ✓ `upsert_api_token` (NEW)

### APPLICATION_CONNECTIONS_API
**API Class**: `ApplicationConnectionsApi`
**Added Methods**: 2
**Removed Methods**: 0
**Unchanged Methods**: 4

**New Methods**:
* ✓ `get_user_provisioning_connection_jwks` (NEW)
* ✓ `verify_provisioning_connection_for_application` (NEW)

### APPLICATION_GROUPS_API
**API Class**: `ApplicationGroupsApi`
**Added Methods**: 1
**Removed Methods**: 0
**Unchanged Methods**: 4

**New Methods**:
* ✓ `update_group_assignment_to_application` (NEW)

### ATTACK_PROTECTION_API
**API Class**: `AttackProtectionApi`
**Added Methods**: 2
**Removed Methods**: 0
**Unchanged Methods**: 2

**New Methods**:
* ✓ `get_authenticator_settings` (NEW)
* ✓ `replace_authenticator_settings` (NEW)

### AUTHENTICATOR_API
**API Class**: `AuthenticatorApi`
**Added Methods**: 7
**Removed Methods**: 0
**Unchanged Methods**: 12

**New Methods**:
* ✓ `create_custom_aaguid` (NEW)
* ✓ `delete_custom_aaguid` (NEW)
* ✓ `get_custom_aaguid` (NEW)
* ✓ `list_all_custom_aaguids` (NEW)
* ✓ `replace_custom_aaguid` (NEW)
* ✓ `update_custom_aaguid` (NEW)
* ✓ `verify_rp_id_domain` (NEW)

### AUTHORIZATION_SERVER_API
**API Class**: `AuthorizationServerApi`
**Added Methods**: 0
**Removed Methods**: 34
**Unchanged Methods**: 7

**Removed Methods**:
* ✗ `activate_authorization_server_policy` (REMOVED)
* ✗ `activate_authorization_server_policy_rule` (REMOVED)
* ✗ `create_associated_servers` (REMOVED)
* ✗ `create_authorization_server_policy` (REMOVED)
* ✗ `create_authorization_server_policy_rule` (REMOVED)
* ✗ `create_o_auth2_claim` (REMOVED)
* ✗ `create_o_auth2_scope` (REMOVED)
* ✗ `deactivate_authorization_server_policy` (REMOVED)
* ✗ `deactivate_authorization_server_policy_rule` (REMOVED)
* ✗ `delete_associated_server` (REMOVED)
* ✗ `delete_authorization_server_policy` (REMOVED)
* ✗ `delete_authorization_server_policy_rule` (REMOVED)
* ✗ `delete_o_auth2_claim` (REMOVED)
* ✗ `delete_o_auth2_scope` (REMOVED)
* ✗ `get_authorization_server_policy` (REMOVED)
* ✗ `get_authorization_server_policy_rule` (REMOVED)
* ✗ `get_o_auth2_claim` (REMOVED)
* ✗ `get_o_auth2_scope` (REMOVED)
* ✗ `get_refresh_token_for_authorization_server_and_client` (REMOVED)
* ✗ `list_associated_servers_by_trusted_type` (REMOVED)
* ✗ `list_authorization_server_keys` (REMOVED)
* ✗ `list_authorization_server_policies` (REMOVED)
* ✗ `list_authorization_server_policy_rules` (REMOVED)
* ✗ `list_o_auth2_claims` (REMOVED)
* ✗ `list_o_auth2_clients_for_authorization_server` (REMOVED)
* ✗ `list_o_auth2_scopes` (REMOVED)
* ✗ `list_refresh_tokens_for_authorization_server_and_client` (REMOVED)
* ✗ `replace_authorization_server_policy` (REMOVED)
* ✗ `replace_authorization_server_policy_rule` (REMOVED)
* ✗ `replace_o_auth2_claim` (REMOVED)
* ✗ `replace_o_auth2_scope` (REMOVED)
* ✗ `revoke_refresh_token_for_authorization_server_and_client` (REMOVED)
* ✗ `revoke_refresh_tokens_for_authorization_server_and_client` (REMOVED)
* ✗ `rotate_authorization_server_keys` (REMOVED)

### CUSTOM_DOMAIN_API
**API Class**: `CustomDomainApi`
**Added Methods**: 1
**Removed Methods**: 0
**Unchanged Methods**: 6

**New Methods**:
* ✓ `create_custom_domain` (NEW)

### GROUP_API
**API Class**: `GroupApi`
**Added Methods**: 1
**Removed Methods**: 11
**Unchanged Methods**: 8

**New Methods**:
* ✓ `add_group` (NEW)

**Removed Methods**:
* ✗ `activate_group_rule` (REMOVED)
* ✗ `assign_group_owner` (REMOVED)
* ✗ `create_group` (REMOVED)
* ✗ `create_group_rule` (REMOVED)
* ✗ `deactivate_group_rule` (REMOVED)
* ✗ `delete_group_owner` (REMOVED)
* ✗ `delete_group_rule` (REMOVED)
* ✗ `get_group_rule` (REMOVED)
* ✗ `list_group_owners` (REMOVED)
* ✗ `list_group_rules` (REMOVED)
* ✗ `replace_group_rule` (REMOVED)

### IDENTITY_PROVIDER_API
**API Class**: `IdentityProviderApi`
**Added Methods**: 0
**Removed Methods**: 18
**Unchanged Methods**: 7

**Removed Methods**:
* ✗ `clone_identity_provider_key` (REMOVED)
* ✗ `create_identity_provider_key` (REMOVED)
* ✗ `delete_identity_provider_key` (REMOVED)
* ✗ `generate_csr_for_identity_provider` (REMOVED)
* ✗ `generate_identity_provider_signing_key` (REMOVED)
* ✗ `get_csr_for_identity_provider` (REMOVED)
* ✗ `get_identity_provider_application_user` (REMOVED)
* ✗ `get_identity_provider_key` (REMOVED)
* ✗ `get_identity_provider_signing_key` (REMOVED)
* ✗ `link_user_to_identity_provider` (REMOVED)
* ✗ `list_csrs_for_identity_provider` (REMOVED)
* ✗ `list_identity_provider_application_users` (REMOVED)
* ✗ `list_identity_provider_keys` (REMOVED)
* ✗ `list_identity_provider_signing_keys` (REMOVED)
* ✗ `list_social_auth_tokens` (REMOVED)
* ✗ `publish_csr_for_identity_provider` (REMOVED)
* ✗ `revoke_csr_for_identity_provider` (REMOVED)
* ✗ `unlink_user_from_identity_provider` (REMOVED)

### IDENTITY_SOURCE_API
**API Class**: `IdentitySourceApi`
**Added Methods**: 9
**Removed Methods**: 0
**Unchanged Methods**: 7

**New Methods**:
* ✓ `create_identity_source_user` (NEW)
* ✓ `delete_identity_source_user` (NEW)
* ✓ `get_identity_source_user` (NEW)
* ✓ `replace_existing_identity_source_user` (NEW)
* ✓ `update_identity_source_users` (NEW)
* ✓ `upload_identity_source_group_memberships_for_delete` (NEW)
* ✓ `upload_identity_source_group_memberships_for_upsert` (NEW)
* ✓ `upload_identity_source_groups_data_for_delete` (NEW)
* ✓ `upload_identity_source_groups_for_upsert` (NEW)

### INLINE_HOOK_API
**API Class**: `InlineHookApi`
**Added Methods**: 1
**Removed Methods**: 0
**Unchanged Methods**: 8

**New Methods**:
* ✓ `update_inline_hook` (NEW)

### REALM_API
**API Class**: `RealmApi`
**Added Methods**: 1
**Removed Methods**: 1
**Unchanged Methods**: 4

**New Methods**:
* ✓ `replace_realm` (NEW)

**Removed Methods**:
* ✗ `update_realm` (REMOVED)

### SCHEMA_API
**API Class**: `SchemaApi`
**Added Methods**: 0
**Removed Methods**: 2
**Unchanged Methods**: 8

**Removed Methods**:
* ✗ `get_app_ui_schema` (REMOVED)
* ✗ `get_app_ui_schema_links` (REMOVED)

### SESSION_API
**API Class**: `SessionApi`
**Added Methods**: 0
**Removed Methods**: 1
**Unchanged Methods**: 3

**Removed Methods**:
* ✗ `create_session` (REMOVED)

### USER_API
**API Class**: `UserApi`
**Added Methods**: 0
**Removed Methods**: 32
**Unchanged Methods**: 7

**Removed Methods**:
* ✗ `activate_user` (REMOVED)
* ✗ `change_password` (REMOVED)
* ✗ `change_recovery_question` (REMOVED)
* ✗ `deactivate_user` (REMOVED)
* ✗ `delete_linked_object_for_user` (REMOVED)
* ✗ `expire_password` (REMOVED)
* ✗ `expire_password_and_get_temporary_password` (REMOVED)
* ✗ `forgot_password` (REMOVED)
* ✗ `forgot_password_set_new_password` (REMOVED)
* ✗ `generate_reset_password_token` (REMOVED)
* ✗ `get_refresh_token_for_user_and_client` (REMOVED)
* ✗ `get_user_grant` (REMOVED)
* ✗ `list_app_links` (REMOVED)
* ✗ `list_grants_for_user_and_client` (REMOVED)
* ✗ `list_linked_objects_for_user` (REMOVED)
* ✗ `list_refresh_tokens_for_user_and_client` (REMOVED)
* ✗ `list_user_clients` (REMOVED)
* ✗ `list_user_grants` (REMOVED)
* ✗ `list_user_groups` (REMOVED)
* ✗ `list_user_identity_providers` (REMOVED)
* ✗ `reactivate_user` (REMOVED)
* ✗ `reset_factors` (REMOVED)
* ✗ `revoke_grants_for_user_and_client` (REMOVED)
* ✗ `revoke_token_for_user_and_client` (REMOVED)
* ✗ `revoke_tokens_for_user_and_client` (REMOVED)
* ✗ `revoke_user_grant` (REMOVED)
* ✗ `revoke_user_grants` (REMOVED)
* ✗ `revoke_user_sessions` (REMOVED)
* ✗ `set_linked_object_for_user` (REMOVED)
* ✗ `suspend_user` (REMOVED)
* ✗ `unlock_user` (REMOVED)
* ✗ `unsuspend_user` (REMOVED)

### USER_FACTOR_API
**API Class**: `UserFactorApi`
**Added Methods**: 3
**Removed Methods**: 0
**Unchanged Methods**: 10

**New Methods**:
* ✓ `get_yubikey_otp_token_by_id` (NEW)
* ✓ `list_yubikey_otp_tokens` (NEW)
* ✓ `upload_yubikey_otp_token_seed` (NEW)

# 3.0.0

## OKTA SDK PYTHON COMPREHENSIVE API MIGRATION REPORT

## EXECUTIVE SUMMARY

This summary documents ALL METHOD CHANGES across the complete set of 350 operations
between the older `resource_clients` directory and the newer `api` directory in the
Okta Python SDK.

## COMPLETE METHOD MIGRATION MAPPING


### 1. `APPLICATION_CLIENT.PY` → MULTIPLE APIs (53 METHODS)


**FROM**: `application_client.py` (53 methods)
**TO**: Multiple specialized APIs

**CORE APPLICATION METHODS (Retained in `application_api.py`)**:
* ✓ `list_applications` → `list_applications` (KEPT)
* ✓ `create_application` → `create_application` (KEPT)
* ✓ `delete_application` → `delete_application` (KEPT)
* ✓ `get_application` → `get_application` (KEPT)
* ✓ `activate_application` → `activate_application` (KEPT)
* ✓ `deactivate_application` → `deactivate_application` (KEPT)
* ✗ `update_application` → `replace_application` (RENAMED)

**APPLICATION CONNECTION METHODS (→ `application_connections_api.py`)**:
* ✗ `get_default_provisioning_connection_for_application` → MOVED
* ✗ `set_default_provisioning_connection_for_application` → MOVED
* ✗ `activate_default_provisioning_connection_for_application` → MOVED
* ✗ `deactivate_default_provisioning_connection_for_application` → MOVED

**CERTIFICATE/CSR METHODS (REMOVED - No direct equivalent)**:
* ✗ `list_csrs_for_application` → REMOVED
* ✗ `generate_csr_for_application` → REMOVED
* ✗ `revoke_csr_from_application` → REMOVED
* ✗ `get_csr_for_application` → REMOVED
* ✗ `publish_cer_cert` → REMOVED
* ✗ `publish_binary_cer_cert` → REMOVED
* ✗ `publish_der_cert` → REMOVED
* ✗ `publish_binary_der_cert` → REMOVED
* ✗ `publish_binary_pem_cert` → REMOVED

**APPLICATION KEYS METHODS (REMOVED - No direct equivalent)**:
* ✗ `list_application_keys` → REMOVED
* ✗ `generate_application_key` → REMOVED
* ✗ `get_application_key` → REMOVED
* ✗ `clone_application_key` → REMOVED

**CLIENT SECRETS METHODS (→ `application_credentials_api.py`)**:
* ✗ `list_client_secrets_for_application` → MOVED
* ✗ `create_new_client_secret_for_application` → MOVED
* ✗ `delete_client_secret_for_application` → MOVED
* ✗ `get_client_secret_for_application` → MOVED
* ✗ `activate_client_secret_for_application` → MOVED
* ✗ `deactivate_client_secret_for_application` → MOVED

**FEATURES METHODS (→ `application_features_api.py`)**:
* ✗ `list_features_for_application` → MOVED
* ✗ `get_feature_for_application` → MOVED
* ✗ `update_feature_for_application` → MOVED

**SCOPE GRANTS METHODS (→ `application_grants_api.py`)**:
* ✗ `list_scope_consent_grants` → MOVED
* ✗ `grant_consent_to_scope` → MOVED
* ✗ `revoke_scope_consent_grant` → MOVED
* ✗ `get_scope_consent_grant` → MOVED

**GROUP ASSIGNMENTS METHODS (→ `application_groups_api.py`)**:
* ✗ `list_application_group_assignments` → MOVED
* ✗ `delete_application_group_assignment` → MOVED
* ✗ `get_application_group_assignment` → MOVED
* ✗ `create_application_group_assignment` → MOVED

**LOGO METHODS (→ `application_logos_api.py`)**:
* ✗ `upload_application_logo` → MOVED

**POLICY METHODS (→ `application_policies_api.py`)**:
* ✗ `update_application_policy` → MOVED

**SSO/SAML METHODS (→ `application_sso_api.py`)**:
* ✗ `preview_saml_app_metadata` → MOVED

**TOKEN METHODS (→ `application_tokens_api.py`)**:
* ✗ `revoke_o_auth_2_tokens_for_application` → MOVED
* ✗ `list_o_auth_2_tokens_for_application` → MOVED
* ✗ `revoke_o_auth_2_token_for_application` → MOVED
* ✗ `get_o_auth_2_token_for_application` → MOVED

**USER ASSIGNMENT METHODS (→ `application_users_api.py`)**:
* ✗ `list_application_users` → MOVED
* ✗ `assign_user_to_application` → MOVED
* ✗ `delete_application_user` → MOVED
* ✗ `get_application_user` → MOVED
* ✗ `update_application_user` → MOVED

### 2. `USER_CLIENT.PY` → `USER_API.PY` + ROLE APIs (53 METHODS)


**FROM**: `user_client.py` (53 methods)
**TO**: `user_api.py` + `role_api.py` + `subscription_api.py`

**CORE USER METHODS (Retained in `user_api.py`)**:
* ✓ `list_users` → `list_users` (KEPT)
* ✓ `create_user` → `create_user` (KEPT)
* ✓ `get_user` → `get_user` (KEPT)
* ✓ `update_user` → `update_user` (KEPT)
* ✗ `deactivate_or_delete_user` → SPLIT into `deactivate_user` + `delete_user`
* ✗ `partial_update_user` → `replace_user` (RENAMED)

**USER LIFECYCLE METHODS**:
* ✓ `activate_user` → `activate_user` (KEPT)
* ✓ `deactivate_user` → `deactivate_user` (KEPT)
* ✓ `suspend_user` → `suspend_user` (KEPT)
* ✓ `unsuspend_user` → `unsuspend_user` (KEPT)
* ✓ `unlock_user` → `unlock_user` (KEPT)
* ✓ `expire_password` → `expire_password` (KEPT)
* ✓ `expire_password_and_get_temporary_password` → `expire_password_and_get_temporary_password` (KEPT)

**CREDENTIAL METHODS**:
* ✓ `change_password` → `change_password` (KEPT)
* ✓ `change_recovery_question` → `change_recovery_question` (KEPT)
* ✗ `forgot_password_generate_one_time_token` → `generate_reset_password_token` (RENAMED)
* ✓ `forgot_password_set_new_password` → `forgot_password_set_new_password` (KEPT)
* ✗ `reset_password` → `forgot_password` (RENAMED)

**SESSION METHODS**:
* ✗ `clear_user_sessions` → `revoke_user_sessions` (RENAMED)

**LINKED OBJECTS METHODS**:
* ✓ `set_linked_object_for_user` → `set_linked_object_for_user` (KEPT)
* ✗ `get_linked_objects_for_user` → `list_linked_objects_for_user` (RENAMED)
* ✗ `remove_linked_object_for_user` → `delete_linked_object_for_user` (RENAMED)

**APP LINKS AND OAUTH METHODS**:
* ✓ `list_app_links` → `list_app_links` (KEPT)
* ✓ `list_user_clients` → `list_user_clients` (KEPT)
* ✓ `revoke_grants_for_user_and_client` → `revoke_grants_for_user_and_client` (KEPT)
* ✓ `list_grants_for_user_and_client` → `list_grants_for_user_and_client` (KEPT)
* ✓ `revoke_tokens_for_user_and_client` → `revoke_tokens_for_user_and_client` (KEPT)
* ✓ `list_refresh_tokens_for_user_and_client` → `list_refresh_tokens_for_user_and_client` (KEPT)
* ✓ `revoke_token_for_user_and_client` → `revoke_token_for_user_and_client` (KEPT)
* ✓ `get_refresh_token_for_user_and_client` → `get_refresh_token_for_user_and_client` (KEPT)

**GROUP MEMBERSHIP METHODS**:
* ✓ `list_user_groups` → `list_user_groups` (KEPT)

**IDENTITY PROVIDER METHODS**:
* ✓ `list_user_identity_providers` → `list_user_identity_providers` (KEPT)

**NEW METHODS ADDED TO `user_api.py`**:
* + `delete_user` (split from `deactivate_or_delete_user`)
* + `replace_user` (replaces `partial_update_user`)
* + `forgot_password` (replaces `reset_password`)
* + `generate_reset_password_token` (replaces `forgot_password_generate_one_time_token`)
* + `list_linked_objects_for_user` (replaces `get_linked_objects_for_user`)
* + `delete_linked_object_for_user` (replaces `remove_linked_object_for_user`)
* + `revoke_user_sessions` (replaces `clear_user_sessions`)
* + `list_user_blocks` (NEW functionality)


### 3. `AUTHORIZATION_SERVER_CLIENT.PY` → `AUTHORIZATION_SERVER_API.PY` (38 METHODS)


**FROM**: `authorization_server_client.py` (38 methods)
**TO**: `authorization_server_api.py` (41 methods)

**CORE AUTHORIZATION SERVER METHODS**:
* ✓ `list_authorization_servers` → `list_authorization_servers` (KEPT)
* ✓ `create_authorization_server` → `create_authorization_server` (KEPT)
* ✓ `delete_authorization_server` → `delete_authorization_server` (KEPT)
* ✓ `get_authorization_server` → `get_authorization_server` (KEPT)
* ✗ `update_authorization_server` → `replace_authorization_server` (RENAMED)
* ✓ `activate_authorization_server` → `activate_authorization_server` (KEPT)
* ✓ `deactivate_authorization_server` → `deactivate_authorization_server` (KEPT)

**OAUTH2 CLAIMS METHODS (Naming pattern change `o_auth_2_` → `o_auth2_`)**:
* ✗ `create_o_auth_2_claim` → `create_o_auth2_claim` (RENAMED)
* ✗ `delete_o_auth_2_claim` → `delete_o_auth2_claim` (RENAMED)
* ✗ `get_o_auth_2_claim` → `get_o_auth2_claim` (RENAMED)
* ✗ `list_o_auth_2_claims` → `list_o_auth2_claims` (RENAMED)
* ✗ `update_o_auth_2_claim` → `replace_o_auth2_claim` (RENAMED)

**OAUTH2 SCOPES METHODS (Naming pattern change `o_auth_2_` → `o_auth2_`)**:
* ✗ `create_o_auth_2_scope` → `create_o_auth2_scope` (RENAMED)
* ✗ `delete_o_auth_2_scope` → `delete_o_auth2_scope` (RENAMED)
* ✗ `get_o_auth_2_scope` → `get_o_auth2_scope` (RENAMED)
* ✗ `list_o_auth_2_scopes` → `list_o_auth2_scopes` (RENAMED)
* ✗ `update_o_auth_2_scope` → `replace_o_auth2_scope` (RENAMED)

**OAUTH2 CLIENTS METHODS**:
* ✗ `list_o_auth_2_clients_for_authorization_server` → `list_o_auth2_clients_for_authorization_server` (RENAMED)

**POLICY METHODS**:
* ✓ `list_authorization_server_policies` → `list_authorization_server_policies` (KEPT)
* ✓ `create_authorization_server_policy` → `create_authorization_server_policy` (KEPT)
* ✓ `delete_authorization_server_policy` → `delete_authorization_server_policy` (KEPT)
* ✓ `get_authorization_server_policy` → `get_authorization_server_policy` (KEPT)
* ✗ `update_authorization_server_policy` → `replace_authorization_server_policy` (RENAMED)
* ✓ `activate_authorization_server_policy` → `activate_authorization_server_policy` (KEPT)
* ✓ `deactivate_authorization_server_policy` → `deactivate_authorization_server_policy` (KEPT)

**POLICY RULE METHODS**:
* ✓ `list_authorization_server_policy_rules` → `list_authorization_server_policy_rules` (KEPT)
* ✓ `create_authorization_server_policy_rule` → `create_authorization_server_policy_rule` (KEPT)
* ✓ `delete_authorization_server_policy_rule` → `delete_authorization_server_policy_rule` (KEPT)
* ✓ `get_authorization_server_policy_rule` → `get_authorization_server_policy_rule` (KEPT)
* ✗ `update_authorization_server_policy_rule` → `replace_authorization_server_policy_rule` (RENAMED)
* ✓ `activate_authorization_server_policy_rule` → `activate_authorization_server_policy_rule` (KEPT)
* ✓ `deactivate_authorization_server_policy_rule` → `deactivate_authorization_server_policy_rule` (KEPT)

**KEYS METHODS**:
* ✓ `list_authorization_server_keys` → `list_authorization_server_keys` (KEPT)
* ✓ `rotate_authorization_server_keys` → `rotate_authorization_server_keys` (KEPT)

**NEW METHODS ADDED**:
* + `create_associated_servers` (NEW)
* + `delete_associated_server` (NEW)
* + `list_associated_servers_by_trusted_type` (NEW)


### 4. `GROUP_CLIENT.PY` → `GROUP_API.PY` (28 METHODS)


**FROM**: `group_client.py` (28 methods)
**TO**: `group_api.py`

**CORE GROUP METHODS (Retained in `group_api.py`)**:
* ✓ `list_groups` → `list_groups` (KEPT)
* ✓ `create_group` → `create_group` (KEPT)
* ✓ `delete_group` → `delete_group` (KEPT)
* ✓ `get_group` → `get_group` (KEPT)
* ✗ `update_group` → `replace_group` (RENAMED)

**GROUP RULE METHODS**:
* ✓ `list_group_rules` → `list_group_rules` (KEPT)
* ✓ `create_group_rule` → `create_group_rule` (KEPT)
* ✓ `delete_group_rule` → `delete_group_rule` (KEPT)
* ✓ `get_group_rule` → `get_group_rule` (KEPT)
* ✗ `update_group_rule` → `replace_group_rule` (RENAMED)
* ✓ `activate_group_rule` → `activate_group_rule` (KEPT)
* ✓ `deactivate_group_rule` → `deactivate_group_rule` (KEPT)

**GROUP APPLICATIONS**:
* ✓ `list_assigned_applications_for_group` → `list_assigned_applications_for_group` (KEPT)

**USER MEMBERSHIP METHODS**:
* ✓ `list_group_users` → `list_group_users` (KEPT)
* ✗ `add_user_to_group` → `assign_user_to_group` (RENAMED)
* ✗ `remove_user_from_group` → `unassign_user_from_group` (RENAMED)

**ROLE MANAGEMENT METHODS (→ `role_api.py` + `role_assignment_api.py`)**:
* ✗ `list_group_assigned_roles` → MOVED to `role_api.py`
* ✗ `assign_role_to_group` → MOVED to `role_assignment_api.py`
* ✗ `remove_role_from_group` → MOVED to `role_api.py`
* ✗ `get_role` → MOVED to `role_api.py`
* ✗ `list_app_targets_for_application_admin_role_for_group` → MOVED to `role_api.py`
* ✗ `remove_app_target_from_application_admin_role_given_to_group` → MOVED to `role_api.py`
* ✗ `add_application_target_to_admin_role_given_to_group` → MOVED to `role_api.py`
* ✗ `remove_app_target_from_admin_role_given_to_group` → MOVED to `role_api.py`
* ✗ `add_app_instance_target_to_app_admin_role_given_to_group` → MOVED to `role_api.py`
* ✗ `list_group_targets_for_group_role` → MOVED to `role_api.py`
* ✗ `remove_group_target_from_group_admin_role_given_to_group` → MOVED to `role_api.py`
* ✗ `add_group_target_to_group_administrator_role_for_group` → MOVED to `role_api.py`

**NEW METHODS ADDED TO `group_api.py`**:
* + `assign_group_owner` (NEW)
* + `assign_user_to_group` (replaces `add_user_to_group`)
* + `delete_group_owner` (NEW)
* + `list_group_owners` (NEW)
* + `replace_group` (replaces `update_group`)
* + `replace_group_rule` (replaces `update_group_rule`)
* + `unassign_user_from_group` (replaces `remove_user_from_group`)

### 5. `POLICY_CLIENT.PY` → `POLICY_API.PY` (14 METHODS)


**FROM**: `policy_client.py` (14 methods)
**TO**: `policy_api.py` (21 methods)

**CORE POLICY METHODS**:
* ✓ `list_policies` → `list_policies` (KEPT)
* ✓ `create_policy` → `create_policy` (KEPT)
* ✓ `delete_policy` → `delete_policy` (KEPT)
* ✓ `get_policy` → `get_policy` (KEPT)
* ✗ `update_policy` → `replace_policy` (RENAMED)
* ✓ `activate_policy` → `activate_policy` (KEPT)
* ✓ `deactivate_policy` → `deactivate_policy` (KEPT)

**POLICY RULE METHODS**:
* ✓ `list_policy_rules` → `list_policy_rules` (KEPT)
* ✓ `create_policy_rule` → `create_policy_rule` (KEPT)
* ✓ `delete_policy_rule` → `delete_policy_rule` (KEPT)
* ✓ `get_policy_rule` → `get_policy_rule` (KEPT)
* ✗ `update_policy_rule` → `replace_policy_rule` (RENAMED)
* ✓ `activate_policy_rule` → `activate_policy_rule` (KEPT)
* ✓ `deactivate_policy_rule` → `deactivate_policy_rule` (KEPT)

**NEW METHODS ADDED TO `policy_api.py`**:
* + `clone_policy` (NEW)
* + `create_policy_simulation` (NEW)
* + `delete_policy_resource_mapping` (NEW)
* + `get_policy_mapping` (NEW)
* + `list_policy_apps` (NEW)
* + `list_policy_mappings` (NEW)
* + `map_resource_to_policy` (NEW)
* + `replace_policy` (replaces `update_policy`)
* + `replace_policy_rule` (replaces `update_policy_rule`)

### 6. `IDENTITY_PROVIDER_CLIENT.PY` → `IDENTITY_PROVIDER_API.PY` (29 METHODS)


**FROM**: `identity_provider_client.py` (29 methods)
**TO**: `identity_provider_api.py` (25 methods)

**CORE IDENTITY PROVIDER METHODS**:
* ✓ `list_identity_providers` → `list_identity_providers` (KEPT)
* ✓ `create_identity_provider` → `create_identity_provider` (KEPT)
* ✓ `delete_identity_provider` → `delete_identity_provider` (KEPT)
* ✓ `get_identity_provider` → `get_identity_provider` (KEPT)
* ✗ `update_identity_provider` → `replace_identity_provider` (RENAMED)
* ✓ `activate_identity_provider` → `activate_identity_provider` (KEPT)
* ✓ `deactivate_identity_provider` → `deactivate_identity_provider` (KEPT)

**IDENTITY PROVIDER KEYS**:
* ✓ `list_identity_provider_keys` → `list_identity_provider_keys` (KEPT)
* ✓ `generate_identity_provider_signing_key` → `generate_identity_provider_signing_key` (KEPT)
* ✓ `get_identity_provider_signing_key` → `get_identity_provider_signing_key` (KEPT)
* ✓ `clone_identity_provider_key` → `clone_identity_provider_key` (KEPT)

**CSR METHODS**:
* ✓ `list_csrs_for_identity_provider` → `list_csrs_for_identity_provider` (KEPT)
* ✓ `generate_csr_for_identity_provider` → `generate_csr_for_identity_provider` (KEPT)
* ✓ `revoke_csr_for_identity_provider` → `revoke_csr_for_identity_provider` (KEPT)
* ✓ `get_csr_for_identity_provider` → `get_csr_for_identity_provider` (KEPT)

**CERTIFICATE PUBLISHING METHODS (REMOVED - Pattern changed)**:
* ✗ `publish_cer_cert_for_identity_provider` → REMOVED
* ✗ `publish_binary_cer_cert_for_identity_provider` → REMOVED
* ✗ `publish_der_cert_for_identity_provider` → REMOVED
* ✗ `publish_binary_der_cert_for_identity_provider` → REMOVED
* ✗ `publish_binary_pem_cert_for_identity_provider` → REMOVED

**USER OPERATIONS**:
* ✓ `list_identity_provider_application_users` → `list_identity_provider_application_users` (KEPT)
* ✓ `unlink_user_from_identity_provider` → `unlink_user_from_identity_provider` (KEPT)
* ✓ `get_identity_provider_application_user` → `get_identity_provider_application_user` (KEPT)
* ✓ `link_user_to_identity_provider` → `link_user_to_identity_provider` (KEPT)
* ✓ `list_social_auth_tokens` → `list_social_auth_tokens` (KEPT)

**NEW METHODS ADDED TO `identity_provider_api.py`**:
* + `publish_csr_for_identity_provider` (NEW - replaces old cert publishing)
* + `replace_identity_provider` (replaces `update_identity_provider`)

### 7. `AUTHENTICATOR_CLIENT.PY` → `AUTHENTICATOR_API.PY` (6 METHODS)


**FROM**: `authenticator_client.py` (6 methods)
**TO**: `authenticator_api.py` (12 methods)

**CORE AUTHENTICATOR METHODS**:
* ✓ `list_authenticators` → `list_authenticators` (KEPT)
* ✓ `create_authenticator` → `create_authenticator` (KEPT)
* ✓ `delete_authenticator` → `delete_authenticator` (KEPT)
* ✓ `get_authenticator` → `get_authenticator` (KEPT)
* ✗ `update_authenticator` → `replace_authenticator` (RENAMED)
* ✓ `activate_authenticator` → `activate_authenticator` (KEPT)
* ✓ `deactivate_authenticator` → `deactivate_authenticator` (KEPT)

**NEW METHODS ADDED TO `authenticator_api.py`**:
* + `activate_authenticator_method` (NEW)
* + `deactivate_authenticator_method` (NEW)
* + `get_authenticator_method` (NEW)
* + `get_well_known_app_authenticator_configuration` (NEW)
* + `list_authenticator_methods` (NEW)
* + `replace_authenticator` (replaces `update_authenticator`)
* + `replace_authenticator_method` (NEW)

### 8. `TRUSTED_ORIGIN_CLIENT.PY` → `TRUSTED_ORIGIN_API.PY` (7 METHODS)


**FROM**: `trusted_origin_client.py` (7 methods)
**TO**: `trusted_origin_api.py` (7 methods)

**COMPLETE NAMING PATTERN CHANGE (All methods renamed)**:
* ✗ `list_origins` → `list_trusted_origins` (RENAMED)
* ✗ `create_origin` → `create_trusted_origin` (RENAMED)
* ✗ `delete_origin` → `delete_trusted_origin` (RENAMED)
* ✗ `get_origin` → `get_trusted_origin` (RENAMED)
* ✗ `update_origin` → `replace_trusted_origin` (RENAMED)
* ✗ `activate_origin` → `activate_trusted_origin` (RENAMED)
* ✗ `deactivate_origin` → `deactivate_trusted_origin` (RENAMED)

### 9. `EVENT_HOOK_CLIENT.PY` → `EVENT_HOOK_API.PY` (8 METHODS)


**FROM**: `event_hook_client.py` (8 methods)
**TO**: `event_hook_api.py` (8 methods)

**CORE EVENT HOOK METHODS**:
* ✓ `list_event_hooks` → `list_event_hooks` (KEPT)
* ✓ `create_event_hook` → `create_event_hook` (KEPT)
* ✓ `delete_event_hook` → `delete_event_hook` (KEPT)
* ✓ `get_event_hook` → `get_event_hook` (KEPT)
* ✗ `update_event_hook` → `replace_event_hook` (RENAMED)
* ✓ `activate_event_hook` → `activate_event_hook` (KEPT)
* ✓ `deactivate_event_hook` → `deactivate_event_hook` (KEPT)
* ✓ `verify_event_hook` → `verify_event_hook` (KEPT)

**NEW METHODS ADDED TO `event_hook_api.py`**:
* + `replace_event_hook` (replaces `update_event_hook`)

### 10. `INLINE_HOOK_CLIENT.PY` → `INLINE_HOOK_API.PY` (8 METHODS)


**FROM**: `inline_hook_client.py` (8 methods)
**TO**: `inline_hook_api.py` (8 methods)

**CORE INLINE HOOK METHODS**:
* ✓ `list_inline_hooks` → `list_inline_hooks` (KEPT)
* ✓ `create_inline_hook` → `create_inline_hook` (KEPT)
* ✓ `delete_inline_hook` → `delete_inline_hook` (KEPT)
* ✓ `get_inline_hook` → `get_inline_hook` (KEPT)
* ✗ `update_inline_hook` → `replace_inline_hook` (RENAMED)
* ✓ `activate_inline_hook` → `activate_inline_hook` (KEPT)
* ✓ `deactivate_inline_hook` → `deactivate_inline_hook` (KEPT)
* ✓ `execute_inline_hook` → `execute_inline_hook` (KEPT)

**NEW METHODS ADDED TO `inline_hook_api.py`**:
* + `replace_inline_hook` (replaces `update_inline_hook`)

### 11. `NETWORK_ZONE_CLIENT.PY` → `NETWORK_ZONE_API.PY` (7 METHODS)


**FROM**: `network_zone_client.py` (7 methods)
**TO**: `network_zone_api.py` (7 methods)

**CORE NETWORK ZONE METHODS**:
* ✓ `list_network_zones` → `list_network_zones` (KEPT)
* ✓ `create_network_zone` → `create_network_zone` (KEPT)
* ✓ `delete_network_zone` → `delete_network_zone` (KEPT)
* ✓ `get_network_zone` → `get_network_zone` (KEPT)
* ✗ `update_network_zone` → `replace_network_zone` (RENAMED)
* ✓ `activate_network_zone` → `activate_network_zone` (KEPT)
* ✓ `deactivate_network_zone` → `deactivate_network_zone` (KEPT)

**NEW METHODS ADDED TO `network_zone_api.py`**:
* + `replace_network_zone` (replaces `update_network_zone`)

### 12. `LINKED_OBJECT_CLIENT.PY` → `LINKED_OBJECT_API.PY` (4 METHODS)


**FROM**: `linked_object_client.py` (4 methods)
**TO**: `linked_object_api.py` (4 methods)

**LINKED OBJECT METHODS**:
* ✓ `list_linked_object_definitions` → `list_linked_object_definitions` (KEPT)
* ✗ `add_linked_object_definition` → `create_linked_object_definition` (RENAMED)
* ✓ `delete_linked_object_definition` → `delete_linked_object_definition` (KEPT)
* ✓ `get_linked_object_definition` → `get_linked_object_definition` (KEPT)

**NEW METHODS ADDED TO `linked_object_api.py`**:
* + `create_linked_object_definition` (replaces `add_linked_object_definition`)

### 13. `SESSION_CLIENT.PY` → `SESSION_API.PY` (4 METHODS)


**FROM**: `session_client.py` (4 methods)
**TO**: `session_api.py` (4 methods)

**SESSION METHODS**:
* ✓ `create_session` → `create_session` (KEPT)
* ✓ `get_session` → `get_session` (KEPT)
* ✓ `refresh_session` → `refresh_session` (KEPT)
* ✗ `end_session` → `revoke_session` (RENAMED)

**NEW METHODS ADDED TO `session_api.py`**:
* + `revoke_session` (replaces `end_session`)

### 14. `SUBSCRIPTION_CLIENT.PY` → `SUBSCRIPTION_API.PY` (6 METHODS)


**FROM**: `subscription_client.py` (6 methods)
**TO**: `subscription_api.py` (8 methods)

**COMPLETE METHOD RESTRUCTURING**:

**OLD METHODS (ALL REMOVED)**:
* ✗ `get_role_subscription_by_notification_type` → REMOVED
* ✗ `list_role_subscriptions` → REMOVED
* ✗ `subscribe_role_subscription_by_notification_type` → REMOVED
* ✗ `subscribe_user_subscription_by_notification_type` → REMOVED
* ✗ `unsubscribe_role_subscription_by_notification_type` → REMOVED
* ✗ `unsubscribe_user_subscription_by_notification_type` → REMOVED

**NEW METHODS ADDED TO `subscription_api.py`**:
* + `get_subscriptions_notification_type_role` (NEW)
* + `get_subscriptions_notification_type_user` (NEW)
* + `list_subscriptions_role` (NEW)
* + `list_subscriptions_user` (NEW)
* + `subscribe_by_notification_type_role` (NEW)
* + `subscribe_by_notification_type_user` (NEW)
* + `unsubscribe_by_notification_type_role` (NEW)
* + `unsubscribe_by_notification_type_user` (NEW)

### 15. `USER_FACTOR_CLIENT.PY` → `USER_FACTOR_API.PY` (9 METHODS)


**FROM**: `user_factor_client.py` (9 methods)
**TO**: `user_factor_api.py` (10 methods)

**USER FACTOR METHODS**:
* ✓ `list_factors` → `list_factors` (KEPT)
* ✓ `enroll_factor` → `enroll_factor` (KEPT)
* ✗ `delete_factor` → `unenroll_factor` (RENAMED)
* ✓ `get_factor` → `get_factor` (KEPT)
* ✓ `activate_factor` → `activate_factor` (KEPT)
* ✓ `verify_factor` → `verify_factor` (KEPT)
* ✓ `list_supported_factors` → `list_supported_factors` (KEPT)
* ✓ `list_supported_security_questions` → `list_supported_security_questions` (KEPT)
* ✓ `get_factor_transaction_status` → `get_factor_transaction_status` (KEPT)

**NEW METHODS ADDED TO `user_factor_api.py`**:
* + `resend_enroll_factor` (NEW)
* + `unenroll_factor` (replaces `delete_factor`)

### 16. `THREAT_INSIGHT_CLIENT.PY` → `THREAT_INSIGHT_API.PY` (2 METHODS)


**FROM**: `threat_insight_client.py` (2 methods)
**TO**: `threat_insight_api.py` (2 methods)

**THREAT INSIGHT METHODS (NO CHANGES)**:
* ✓ `get_current_configuration` → `get_current_configuration` (KEPT)
* ✓ `update_configuration` → `update_configuration` (KEPT)

### 17. `FEATURE_CLIENT.PY` → `FEATURE_API.PY` (5 METHODS)


**FROM**: `feature_client.py` (5 methods)
**TO**: `feature_api.py` (5 methods)

**FEATURE METHODS (NO CHANGES)**:
* ✓ `list_features` → `list_features` (KEPT)
* ✓ `get_feature` → `get_feature` (KEPT)
* ✓ `update_feature_lifecycle` → `update_feature_lifecycle` (KEPT)
* ✓ `list_feature_dependencies` → `list_feature_dependencies` (KEPT)
* ✓ `list_feature_dependents` → `list_feature_dependents` (KEPT)

### 18. `PROFILE_MAPPING_CLIENT.PY` → `PROFILE_MAPPING_API.PY` (3 METHODS)


**FROM**: `profile_mapping_client.py` (3 methods)
**TO**: `profile_mapping_api.py` (3 methods)

**PROFILE MAPPING METHODS (NO CHANGES)**:
* ✓ `list_profile_mappings` → `list_profile_mappings` (KEPT)
* ✓ `get_profile_mapping` → `get_profile_mapping` (KEPT)
* ✓ `update_profile_mapping` → `update_profile_mapping` (KEPT)

### 19. `USER_TYPE_CLIENT.PY` → `USER_TYPE_API.PY` (6 METHODS)


**FROM**: `user_type_client.py` (6 methods)
**TO**: `user_type_api.py` (6 methods)

**USER TYPE METHODS (NO CHANGES)**:
* ✓ `list_user_types` → `list_user_types` (KEPT)
* ✓ `create_user_type` → `create_user_type` (KEPT)
* ✓ `delete_user_type` → `delete_user_type` (KEPT)
* ✓ `get_user_type` → `get_user_type` (KEPT)
* ✓ `update_user_type` → `update_user_type` (KEPT)
* ✓ `replace_user_type` → `replace_user_type` (KEPT)

## CLIENT FILES WITHOUT DIRECT API EQUIVALENTS (8 FILES - 54 METHODS)


### 20. `BRAND_CLIENT.PY` (5 METHODS) → NO DIRECT EQUIVALENT

* ✗ `list_brands` → CONSOLIDATED into `customization_api.py`
* ✗ `get_brand` → CONSOLIDATED into `customization_api.py`
* ✗ `update_brand` → CONSOLIDATED into `customization_api.py`
* ✗ `list_brand_themes` → CONSOLIDATED into `customization_api.py`
* ✗ `get_brand_theme` → CONSOLIDATED into `customization_api.py`

### 21. `DOMAIN_CLIENT.PY` (8 METHODS) → NO DIRECT EQUIVALENT

* ✗ `list_domains` → CONSOLIDATED into `custom_domain_api.py`
* ✗ `create_domain` → CONSOLIDATED into `custom_domain_api.py`
* ✗ `delete_domain` → CONSOLIDATED into `custom_domain_api.py`
* ✗ `get_domain` → CONSOLIDATED into `custom_domain_api.py`
* ✗ `create_certificate` → CONSOLIDATED into `custom_domain_api.py`
* ✗ `list_certificates` → CONSOLIDATED into `custom_domain_api.py`
* ✗ `verify_domain` → CONSOLIDATED into `custom_domain_api.py`
* ✗ `update_domain` → CONSOLIDATED into `custom_domain_api.py`

### 22. `GROUP_SCHEMA_CLIENT.PY` (6 METHODS) → NO DIRECT EQUIVALENT

* ✗ `get_group_schema` → CONSOLIDATED into `schema_api.py`
* ✗ `update_group_schema` → CONSOLIDATED into `schema_api.py`
* ✗ `list_group_schema_custom_attributes` → CONSOLIDATED into `schema_api.py`
* ✗ `add_group_schema_custom_attribute` → CONSOLIDATED into `schema_api.py`
* ✗ `remove_group_schema_custom_attribute` → CONSOLIDATED into `schema_api.py`
* ✗ `get_group_schema_custom_attribute` → CONSOLIDATED into `schema_api.py`

### 23. `LOG_EVENT_CLIENT.PY` (1 METHOD) → NO DIRECT EQUIVALENT

* ✗ `get_logs` → CONSOLIDATED into `system_log_api.py`

### 24. `ORG_CLIENT.PY` (15 METHODS) → NO DIRECT EQUIVALENT

* ✗ `get_org_settings` → CONSOLIDATED into `org_setting_api.py`
* ✗ `partial_update_org_setting` → CONSOLIDATED into `org_setting_api.py`
* ✗ `update_org_settings` → CONSOLIDATED into `org_setting_api.py`
* ✗ `upload_org_logo` → CONSOLIDATED into `org_setting_api.py`
* ✗ `get_org_preferences` → CONSOLIDATED into `org_setting_api.py`
* ✗ `hide_okta_ui_footer` → CONSOLIDATED into `org_setting_api.py`
* ✗ `show_okta_ui_footer` → CONSOLIDATED into `org_setting_api.py`
* ✗ `get_okta_communication_settings` → CONSOLIDATED into `org_setting_api.py`
* ✗ `opt_in_users_to_okta_communication_emails` → CONSOLIDATED into `org_setting_api.py`
* ✗ `opt_out_users_from_okta_communication_emails` → CONSOLIDATED into `org_setting_api.py`
* ✗ `extend_org_setting` → CONSOLIDATED into `org_setting_api.py`
* ✗ `grant_okta_support` → CONSOLIDATED into `org_setting_api.py`
* ✗ `revoke_okta_support` → CONSOLIDATED into `org_setting_api.py`
* ✗ `get_well_known_org_metadata` → CONSOLIDATED into `org_setting_api.py`
* ✗ `get_org_contact_types` → CONSOLIDATED into `org_setting_api.py`

### 25. `SMS_TEMPLATE_CLIENT.PY` (7 METHODS) → NO DIRECT EQUIVALENT

* ✗ `list_sms_templates` → CONSOLIDATED into `template_api.py`
* ✗ `create_sms_template` → CONSOLIDATED into `template_api.py`
* ✗ `delete_sms_template` → CONSOLIDATED into `template_api.py`
* ✗ `get_sms_template` → CONSOLIDATED into `template_api.py`
* ✗ `partial_update_sms_template` → CONSOLIDATED into `template_api.py`
* ✗ `update_sms_template` → CONSOLIDATED into `template_api.py`
* ✗ `get_sms_template_translations` → CONSOLIDATED into `template_api.py`

### 26. `USER_SCHEMA_CLIENT.PY` (6 METHODS) → NO DIRECT EQUIVALENT

* ✗ `get_user_schema` → CONSOLIDATED into `schema_api.py`
* ✗ `update_user_profile` → CONSOLIDATED into `schema_api.py`
* ✗ `list_user_schema_custom_attributes` → CONSOLIDATED into `schema_api.py`
* ✗ `add_user_schema_custom_attribute` → CONSOLIDATED into `schema_api.py`
* ✗ `remove_user_schema_custom_attribute` → CONSOLIDATED into `schema_api.py`
* ✗ `get_user_schema_custom_attribute` → CONSOLIDATED into `schema_api.py`

### 27. `USER_CLIENT.PY`

**FROM**: `user_client.py` (Additional methods not previously documented)
**TO**: `user_api.py` + `subscription_api.py`

**GRANT MANAGEMENT METHODS (→ `subscription_api.py` or `user_api.py`)**:
* ✗ `list_user_grants` → MOVED to `subscription_api.py`
* ✗ `revoke_user_grant` → MOVED to `subscription_api.py`
* ✗ `get_user_grant` → MOVED to `subscription_api.py`
* ✗ `revoke_user_grants` → MOVED to `subscription_api.py`

**USER LIFECYCLE METHODS (Retained in `user_api.py`)**:
* ✗ `reactivate_user` → `reactivate_user` (KEPT in `user_api.py`)
* ✗ `reset_factors` → `reset_factors` (KEPT in `user_api.py`)

**DETAILED METHOD DESCRIPTIONS**:
- `list_user_grants`: Lists all grants for the specified user
- `revoke_user_grant`: Revokes one grant for a specified user
- `get_user_grant`: Gets a grant for the specified user
- `revoke_user_grants`: Revokes all grants for a specified user
- `reactivate_user`: Reactivates a user (can only be performed on users with PROVISIONED status)
- `reset_factors`: Resets all factors for the specified user

### 28. `AUTHORIZATION_SERVER_CLIENT.PY`
**FROM**: `authorization_server_client.py` (Additional methods not previously documented)
**TO**: `authorization_server_api.py`

**REFRESH TOKEN MANAGEMENT METHODS (Retained in `authorization_server_api.py`)**:
* ✗ `revoke_refresh_tokens_for_authorization_server_and_client` → KEPT
* ✗ `list_refresh_tokens_for_authorization_server_and_client` → KEPT
* ✗ `revoke_refresh_token_for_authorization_server_and_client` → KEPT
* ✗ `get_refresh_token_for_authorization_server_and_client` → KEPT

**DETAILED METHOD DESCRIPTIONS**:
- `revoke_refresh_tokens_for_authorization_server_and_client`: Revokes all refresh tokens for authorization server and client
- `list_refresh_tokens_for_authorization_server_and_client`: Lists refresh tokens for authorization server and client
- `revoke_refresh_token_for_authorization_server_and_client`: Revokes specific refresh token for authorization server and client
- `get_refresh_token_for_authorization_server_and_client`: Gets specific refresh token for authorization server and client

### 29. `ORG_CLIENT.PY`
**FROM**: `org_client.py` (Additional methods not previously documented)
**TO**: `org_setting_api.py`

**ORGANIZATION CONTACT MANAGEMENT (→ `org_setting_api.py`)**:
* ✗ `get_org_contact_user` → MOVED
* ✗ `update_org_contact_user` → MOVED

**ORGANIZATION BRANDING/LOGO (→ `org_setting_api.py`)**:
* ✗ `update_org_logo` → MOVED (different from `upload_org_logo`)

**OKTA SUPPORT SETTINGS (→ `org_setting_api.py`)**:
* ✗ `get_org_okta_support_settings` → MOVED
* ✗ `extend_okta_support` → MOVED (different from `extend_org_setting`)

**ORGANIZATION METADATA (→ `org_setting_api.py`)**:
* ✗ `get_well_known_org_metadata` → MOVED
* ✗ `update_org_well_known_metadata` → MOVED

**CONTACT TYPE MANAGEMENT (→ `org_setting_api.py`)**:
* ✗ `list_org_contact_types` → MOVED
* ✗ `get_org_contact_type` → MOVED
* ✗ `update_org_contact_type` → MOVED
* ✗ `delete_org_contact_type` → MOVED
* ✗ `create_org_contact_type` → MOVED

**SECURITY AND NOTIFICATION SETTINGS (→ `org_setting_api.py`)**:
* ✗ `get_org_security_notification_emails_settings` → MOVED
* ✗ `update_org_security_notification_emails_settings` → MOVED
* ✗ `get_org_third_party_admin_settings` → MOVED
* ✗ `update_org_third_party_admin_settings` → MOVED

**BULK OPERATIONS (→ `org_setting_api.py`)**:
* ✗ `bulk_upsert_org_contacts` → MOVED
* ✗ `bulk_delete_org_contacts` → MOVED

**DETAILED METHOD DESCRIPTIONS**:
- `get_org_contact_user`: Retrieves the URL of the User associated with the specified Contact Type
- `update_org_contact_user`: Updates the User associated with the specified Contact Type
- `update_org_logo`: Updates the logo for your organization (different from `upload_org_logo`)
- `get_org_okta_support_settings`: Gets Okta Support Settings of your organization
- `extend_okta_support`: Extends the length of time that Okta Support can access your org by 24 hours
- `get_well_known_org_metadata`: Gets well-known organization metadata
- `list_org_contact_types`: Lists contact types
- `get_org_contact_type`: Gets specific contact type
- `update_org_contact_type`: Updates specific contact type
- `delete_org_contact_type`: Deletes specific contact type
- `create_org_contact_type`: Creates new contact type
- `get_org_security_notification_emails_settings`: Gets security notification email settings
- `update_org_security_notification_emails_settings`: Updates security notification email settings
- `get_org_third_party_admin_settings`: Gets third party admin settings
- `update_org_third_party_admin_settings`: Updates third party admin settings
- `bulk_upsert_org_contacts`: Bulk upsert organization contacts
- `bulk_delete_org_contacts`: Bulk delete organization contacts
- `update_org_well_known_metadata`: Updates well-known organization metadata

### 30. `BRAND_CLIENT.PY`
**FROM**: `brand_client.py` (Additional methods not previously documented)
**TO**: `customization_api.py`

**BRAND THEME MANAGEMENT (→ `customization_api.py`)**:
* ✗ `update_brand_theme` → MOVED
* ✗ `delete_brand_theme` → MOVED
* ✗ `create_brand_theme` → MOVED
* ✗ `list_brand_theme_background_images` → MOVED

**DETAILED METHOD DESCRIPTIONS**:
- `update_brand_theme`: Updates brand theme configuration
- `delete_brand_theme`: Deletes brand theme
- `create_brand_theme`: Creates new brand theme
- `list_brand_theme_background_images`: Lists brand theme background images

## 2.9.13
* Expire and renew the access token when using OAuth 2.0

## 2.9.12
* Reduce JWT Token Expiration time

## 2.9.11
* Allow latest aenum release
* Add missing OAuthGrantType enum values
* Add data_type parameter for OktaAPIResponse

## 2.9.8
* Add signed_nonce UserFactor type

## 2.9.7
* Remove ecdsa dependency

## 2.9.5
* Clear access token from cache on call to OAuth.clear_access_token()

## 2.9.4
* Add optional parameter to api_response.next() to include response object as a third tuple value.

## 2.9.3
* Add missing properties to applicationsettingsapplication per the reference docs: https://developer.okta.com/docs/reference/api/apps/#settings-4
* Add signed_nonce factor type per the reference docs: https://developer.okta.com/docs/reference/api/factors/#factor-type

## 2.9.2
* Add missing dependency in setup.py by @justinabrokwah-okta in https://github.com/okta/okta-sdk-python/pull/351
* Update __init__.py by @bretterer in https://github.com/okta/okta-sdk-python/pull/352

## 2.9.1
* fixing okta icon image url by @BarondeCharlus in https://github.com/okta/okta-sdk-python/pull/323
* Update README.md by @omidraha in https://github.com/okta/okta-sdk-python/pull/310
* Update README.md by @glebinsky in https://github.com/okta/okta-sdk-python/pull/321
* Update README.md by @scheblein in https://github.com/okta/okta-sdk-python/pull/300
* update HTTPError, OktaAPIError to call Error base class constructor by @andyj29 in https://github.com/okta/okta-sdk-python/pull/319
* Update type checking in jwt.py to use isinstance synxtax for consistency by @andyj29 in https://github.com/okta/okta-sdk-python/pull/320
* pagination should be easier by @gabrielsroka in https://github.com/okta/okta-sdk-python/pull/328
* Update next by @bretterer in https://github.com/okta/okta-sdk-python/pull/348
* Update version number by @bretterer in https://github.com/okta/okta-sdk-python/pull/349

## v2.9.0
* Addressed a number of open issues regarding SDK
  * Allow overwriting of default HTTP headers
  * Prevent automatic camel casing when using pagination to retrieve next set of results
  * Allow key ID (kid) to be specified when providing JWT
  * Allow log level to be set by user
* Using `pycryptodomex` dependency instead of `pycryptodome` to prevent clash in import statements
* Upgraded to latest version of API spec. Includes following changes:
  * Added support for MFA Enroll policy type
  * Added custom role type
  * Added dynamic issuer mode for open id connect applications
  * Added failed to verify and domain taken as domain validation statuses
  * Added Okta managed as domain certificate source type
  * Added create authenticator endpoint
  * Added endpoint to preview SAML app metadata

_New models:_
* ClientSecret
* ClientSecretMetadata
* MultifactorEnrollmentPolicy
* MultifactorEnrollmentPolicySettings
* MultifactorEnrollmentPolicySettingsType
* MultifactorEnrollmentPolicyAuthenticatorType
* MultifactorEnrollmentPolicyAuthenticatorStatus
* MultifactorEnrollmentPolicyAuthenticatorSettings

## v2.7.0
_What's Changed_
* Regenerated and added pkce_requried to app oauth credentials by @drewcarmichael-okta in https://github.com/okta/okta-sdk-python/pull/313

_New Contributors_
* @drewcarmichael-okta made their first contribution in https://github.com/okta/okta-sdk-python/pull/313

## v2.6.0
- Manage custom group profile attributes (Fixes #279)
## v2.5.0
- Regenerate code using the [open API spec v2.11.1](https://github.com/okta/okta-management-openapi-spec/releases/tag/openapi-2.11.1)
- Updates client template to persist aiohttp and related logic
- Fixed copyright headers which had the incorrect starting year

_New resources:_
* Brand

_New models:_
* EmailTemplate
* EmailTemplateContent
* EmailTemplateCustomization
* EmailTemplateCustomizationRequest
* EmailTemplateTestTrequest
* IdpPolicyRuleAction
* IdpPolicyRuleActionProvider
## v2.4.0
- Regenerate code using the [open API spec v2.10.0](https://github.com/okta/okta-management-openapi-spec/releases/tag/openapi-2.10.0).
- Allow possibility to re-use http session.

_New resources:_
* Subscription

_New models:_
* ApplicationFeature
* CapabilitiesCreateObject
* CapabilitiesObject
* CapabilitiesUpdateObject
* ChangeEnum
* LifecycleCreateSettingObject
* LifecycleDeactivateSettingObject
* NotificationType
* Org2OrgApplication
* Org2OrgApplicationSettings
* Org2OrgApplicationSettingsApp
* PasswordSettingObject
* ProfileSettingObject
* ProvisioningConnection
* ProvisioningConnectionAuthScheme
* ProvisioningConnectionProfile
* ProvisioningConnectionRequest
* ProvisioningConnectionStatus
* SeedEnum
* Subscription
* SubscriptionStatus

_New features:_
Reuse http session to improve performance using client as a context manager:
```py
import asyncio
import aiohttp

from okta.client import Client as OktaClient


async def main():
    async with OktaClient() as client:
        # perform all queries within same session
        users, okta_resp, err = await client.list_users()
        user, okta_resp, err = await client.get_user(users[0].id)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## v2.3.1
- Regenerate code using the [open API spec v2.9.2](https://github.com/okta/okta-management-openapi-spec/releases/tag/openapi-2.9.2).
- Make DevicePolicyRuleCondition model parent for DeviceAccessPolicyRuleCondition

## v2.3.0
- Regenerate code using the [open API spec v2.9.1](https://github.com/okta/okta-management-openapi-spec/releases/tag/openapi-2.9.1).
- Allow next for all requests
- Allow upload files within FormData
- Add updateOrgLogo operation to Org resource (Org appeared in v2.2.0)
- Allow custom SSL Context settings

_New resources:_
* Brand

_New models:_
AccessPolicy
AccessPolicyConstraint
AccessPolicyConstraints
AccessPolicyRule
AccessPolicyRuleActions
AccessPolicyRuleApplicationSignOn
AccessPolicyRuleConditions
AccessPolicyRuleCustomCondition
AuthenticatorProvider
AuthenticatorProviderConfiguration
AuthenticatorProviderConfigurationUserNamePlate
Brand
ChannelBinding
Compliance
DeviceAccessPolicyRuleCondition
EmailTemplateTouchPointVariant
EndUserDashboardTouchPointVariant
ErrorPageTouchPointVariant
FipsEnum
ImageUploadResponse
KnowledgeConstraint
PossessionConstraint
PreRegistrationInlineHook
ProfileEnrollmentPolicy
ProfileEnrollmentPolicyRule
ProfileEnrollmentPolicyRuleAction
ProfileEnrollmentPolicyRuleActions
ProfileEnrollmentPolicyRuleActivationRequirement
ProfileEnrollmentPolicyRuleProfileAttribute
RequiredEnum
SignInPageTouchPointVariant
Theme
ThemeResponse
UserTypeCondition
UserVerificationEnum
VerificationMethod

## v2.2.0
- Regenerate code using the [open API spec v2.7.0](https://github.com/okta/okta-management-openapi-spec/releases/tag/openapi-2.7.0).
- Allow Bearer auth
- Support Python 3.9

_New resources:_
* Authenticator
* GroupSchema
* Org

_New models:_
* AllowedForEnum
* Authenticator
* AuthenticatorSettings
* AuthenticatorStatus
* AuthenticatorType
* GroupSchema
* GroupSchemaBase
* GroupSchemaCustom
* GroupSchemaAttribute
* GroupSchemaDefinitions
* GroupSchemaBaseProperties
* OrgContactType
* OrgContactTypeObj
* OrgContactUser
* OrgOktaCommunicationSetting
* OrgOktaSupportSetting
* OrgOktaSupportSettingsObj
* OrgPreferences
* OrgSetting

## v2.1.0
- Regenerate code using the [open API spec v2.6.0](https://github.com/okta/okta-management-openapi-spec/releases/tag/openapi-2.6.0).
- Expose parameter `keep_empty_params` to all user interfaces.

_New models:_
* ApplicationSettingsNotes
* SignOnInlineHook
* TokenAuthorizationServerPolicyRuleActionInlineHook

## v2.0.0
- Regenerate code using the [open API spec v2.5.0](https://github.com/okta/okta-management-openapi-spec/releases/tag/openapi-2.5.0).
- Make sign_on_mode of all apps instance of enum, issue #198 (this change might be not compatible with custom clients code, although probability is low)
- Add response headers to OktaAPIResponse object, issue #218

_New resources:_
* Domain
* UserSchema

_New models:_
* DnsRecord
* DnsRecordType
* Domain
* DomainCertificate
* DomainCertificateMetadata
* DomainCertificateSourceType
* DomainCertificateType
* DomainListResponse
* DomainValidationStatus
* UserSchemaAttributeEnum
* UserSchemaAttributeItems
* UserSchemaAttributeMasterPriority
* UserSchemaAttributeMasterType
* UserSchemaAttributeScope
* UserSchemaAttributeType
* UserSchemaAttributeUnion
* UserSchemaProperties
* UserSchemaPropertiesProfile
* UserSchemaPropertiesProfileItem

### Breaking changes
Previously, the type of `sign_on_mode` attribute was inconsistent among different applications. While some applications, including the generic application, defined this attribute as string, others defined it as `ApplicationSignOnMode`.

We have now standardized the sign_on_mode attribute making its type an ApplicationSignOnMode. Thus, code like the following, which was working previously, won't provide desired result:

```py
# if sign_on_mode is not an ApplicationSignOnMode type, then it should be string; but now all sign_on_modes are of type ApplicationSignOnMode
if not isinstance(app.sign_on_mode, ApplicationSignOnMode):
    do_some_stuff()
```

## v1.7.0
- Regenerate code using the [open API spec v2.4.0](https://github.com/okta/okta-management-openapi-spec/releases/tag/openapi-2.4.0).
- Fix case issue with user custom attributes, issue #202.
- Fix UserProfile serializing, PR #207.
- Fix inconsistent responses within pagination, issue #210.

_New resources:_
* ThreatInsight
* NetworkZone
* ProfileMapping

_New models:_
* NetworkZone
* NetworkZoneAddress
* NetworkZoneAddressType
* NetworkZoneLocation
* NetworkZoneStatus
* NetworkZoneType
* NetworkZoneUsage
* PolicyRuleActions
* PolicyRuleActionsEnroll
* PolicyRuleActionsEnrollSelf
* ProfileMapping
* ProfileMappingProperty
* ProfileMappingPropertyPushStatus
* ProfileMappingSource
* ThreatInsightConfiguration

### Breaking changes
Custom attributes, set on instances of the `UserProfile` model, will now no longer be automatically converted to lower camel case.

## v1.6.0
- Update SDK according to openapi spec v2.3.0.
- Fix custom user attributes.

## v1.5.1
- Fix request headers serializing.
- Fix retry logic.
- Log wait time when hit rate limit.

## v1.5.0
- Fix return access_token when it already exists.
- Small README updates.
- Add logging facility for easier debugging.

## v1.4.1
- Fix unknown signOnMode issue
- Handle aiohttp errors
- Fix unused custom HTTPClient implementation

## v1.4.0
- Update env variables to match conventions

## v1.3.2
- Fix outdated date format which comes from header "Date"

## v1.3.1
- Fix application mapping

## v1.3.0
- Add custom http headers to client
- Fix installation requirements

## v1.2.1
- Exclude tests from packaging

## v1.2.0
- Add possibility to create user with custom attributes in profile

## v1.1.0
- Add exceptions and option `raiseException` to OktaClient

## v1.0.5
- Fix construction of http request

## v1.0.4
- Fix cyclic imports for Python3.6
- Update according to openapi 2.1.6
- Fix logs pagination.

## v1.0.3
- Fix construction of async http request, fix method not allowed issue.

## v1.0.2
- Update setup.py, fix python_requires parameter

## v1.0.1
- Add `__init__.py` files for all modules so imports work correctly during publish

## v1.0.0
- Initial Release

## v1.0.0-alpha.1

- Official Release of v1.0.0-alpha.1 Okta Python Management SDK

### Python Versions Supported:

- 3.6
- 3.7
- 3.8
- Removed support for Python 2.7, 3.3, 3.4

### Functional Files Added:

- okta/cache
  - okta/cache/cache.py
  - okta/cache/no_op_cache.py
  - okta/cache/okta_cache.py
- okta/config
  - okta/config/config_setter.py
  - okta/config/config_validator.py
- okta/errors
  - okta/errors/error.py
  - okta/errors/http_error.py
  - okta/errors/okta_api_error.py
- okta/resource_clients
- okta/\_\_init\_\_.py
- okta/api_client.py
- okta/api_response.py
- okta/client.py
- okta/constants.py
- okta/error_messages.py
- okta/http_client.py
- okta/jwt.py
- okta/oauth.py
- okta/okta_object.py
- okta/request_executor.py
- okta/user_agent.py
- okta/utils.py

### Functional Files Deleted

- N/A

### Test Files Added:

- Unit Tests
  - Python Tests
  - Sample YAML files for client configuration
  - HTTP VCR recordings for tests which connect to API
- Integration Tests
  - Python Tests
  - HTTP VCR recordings for tests which connect to API
- Testing configuration files
  - .travis.yml
  - tox.ini
  - tests/conftest.py

### Test Files Deleted:

- N/A

### Other files added:

- Python packaging files
  - setup.py
  - setup.cfg
  - MANIFEST.in
  - requirements.txt
- Repository Docs
  - README.md
  - CHANGELOG.md
  - CONTRIBUTING.md
  - LICENSE.md
  - LONG_DESCRIPTION.md

### Other files deleted:

- N/A

### Added Models:

- okta/models/\_\_init\_\_.py
- okta/models/activate_factor_request.py
- okta/models/app_and_instance_condition_evaluator_app_or_instance.py
- okta/models/app_and_instance_policy_rule_condition.py
- okta/models/app_instance_policy_rule_condition.py
- okta/models/app_link.py
- okta/models/app_user.py
- okta/models/app_user_credentials.py
- okta/models/app_user_password_credential.py
- okta/models/application.py
- okta/models/application_accessibility.py
- okta/models/application_credentials.py
- okta/models/application_credentials_o_auth_client.py
- okta/models/application_credentials_scheme.py
- okta/models/application_credentials_signing.py
- okta/models/application_credentials_signing_use.py
- okta/models/application_credentials_username_template.py
- okta/models/application_group_assignment.py
- okta/models/application_licensing.py
- okta/models/application_settings.py
- okta/models/application_settings_application.py
- okta/models/application_settings_notifications.py
- okta/models/application_settings_notifications_vpn.py
- okta/models/application_settings_notifications_vpn_network.py
- okta/models/application_sign_on_mode.py
- okta/models/application_visibility.py
- okta/models/application_visibility_hide.py
- okta/models/assign_role_request.py
- okta/models/authentication_provider.py
- okta/models/authentication_provider_type.py
- okta/models/authorization_server.py
- okta/models/authorization_server_credentials.py
- okta/models/authorization_server_credentials_rotation_mode.py
- okta/models/authorization_server_credentials_signing_config.py
- okta/models/authorization_server_credentials_use.py
- okta/models/auto_login_application.py
- okta/models/auto_login_application_settings.py
- okta/models/auto_login_application_settings_sign_on.py
- okta/models/basic_application_settings.py
- okta/models/basic_application_settings_application.py
- okta/models/basic_auth_application.py
- okta/models/before_scheduled_action_policy_rule_condition.py
- okta/models/bookmark_application.py
- okta/models/bookmark_application_settings.py
- okta/models/bookmark_application_settings_application.py
- okta/models/browser_plugin_application.py
- okta/models/call_user_factor.py
- okta/models/call_user_factor_profile.py
- okta/models/catalog_application.py
- okta/models/catalog_application_status.py
- okta/models/change_password_request.py
- okta/models/client_policy_condition.py
- okta/models/context_policy_rule_condition.py
- okta/models/create_session_request.py
- okta/models/create_user_request.py
- okta/models/csr.py
- okta/models/csr_metadata.py
- okta/models/csr_metadata_subject.py
- okta/models/csr_metadata_subject_alt_names.py
- okta/models/device_policy_rule_condition.py
- okta/models/device_policy_rule_condition_platform.py
- okta/models/duration.py
- okta/models/email_user_factor.py
- okta/models/email_user_factor_profile.py
- okta/models/enabled_status.py
- okta/models/event_hook.py
- okta/models/event_hook_channel.py
- okta/models/event_hook_channel_config.py
- okta/models/event_hook_channel_config_auth_scheme.py
- okta/models/event_hook_channel_config_auth_scheme_type.py
- okta/models/event_hook_channel_config_header.py
- okta/models/event_subscriptions.py
- okta/models/factor_provider.py
- okta/models/factor_result_type.py
- okta/models/factor_status.py
- okta/models/factor_type.py
- okta/models/feature.py
- okta/models/feature_stage.py
- okta/models/feature_stage_state.py
- okta/models/feature_stage_value.py
- okta/models/feature_type.py
- okta/models/forgot_password_response.py
- okta/models/grant_type_policy_rule_condition.py
- okta/models/group.py
- okta/models/group_condition.py
- okta/models/group_policy_rule_condition.py
- okta/models/group_profile.py
- okta/models/group_rule.py
- okta/models/group_rule_action.py
- okta/models/group_rule_conditions.py
- okta/models/group_rule_expression.py
- okta/models/group_rule_group_assignment.py
- okta/models/group_rule_group_condition.py
- okta/models/group_rule_people_condition.py
- okta/models/group_rule_status.py
- okta/models/group_rule_user_condition.py
- okta/models/group_type.py
- okta/models/hardware_user_factor.py
- okta/models/hardware_user_factor_profile.py
- okta/models/identity_provider.py
- okta/models/identity_provider_application_user.py
- okta/models/identity_provider_credentials.py
- okta/models/identity_provider_credentials_client.py
- okta/models/identity_provider_credentials_signing.py
- okta/models/identity_provider_credentials_trust.py
- okta/models/identity_provider_policy.py
- okta/models/identity_provider_policy_rule_condition.py
- okta/models/inactivity_policy_rule_condition.py
- okta/models/inline_hook.py
- okta/models/inline_hook_channel.py
- okta/models/inline_hook_channel_config.py
- okta/models/inline_hook_channel_config_auth_scheme.py
- okta/models/inline_hook_channel_config_headers.py
- okta/models/inline_hook_payload.py
- okta/models/inline_hook_response.py
- okta/models/inline_hook_response_command_value.py
- okta/models/inline_hook_response_commands.py
- okta/models/inline_hook_status.py
- okta/models/inline_hook_type.py
- okta/models/ion_field.py
- okta/models/ion_form.py
- okta/models/json_web_key.py
- okta/models/jwk_use.py
- okta/models/lifecycle_expiration_policy_rule_condition.py
- okta/models/linked_object.py
- okta/models/linked_object_details.py
- okta/models/linked_object_details_type.py
- okta/models/log_actor.py
- okta/models/log_authentication_context.py
- okta/models/log_authentication_provider.py
- okta/models/log_client.py
- okta/models/log_credential_provider.py
- okta/models/log_credential_type.py
- okta/models/log_debug_context.py
- okta/models/log_event.py
- okta/models/log_geographical_context.py
- okta/models/log_geolocation.py
- okta/models/log_ip_address.py
- okta/models/log_issuer.py
- okta/models/log_outcome.py
- okta/models/log_request.py
- okta/models/log_security_context.py
- okta/models/log_severity.py
- okta/models/log_target.py
- okta/models/log_transaction.py
- okta/models/log_user_agent.py
- okta/models/mdm_enrollment_policy_rule_condition.py
- okta/models/o_auth_2_actor.py
- okta/models/o_auth_2_claim.py
- okta/models/o_auth_2_claim_conditions.py
- okta/models/o_auth_2_client.py
- okta/models/o_auth_2_refresh_token.py
- okta/models/o_auth_2_scope.py
- okta/models/o_auth_2_scope_consent_grant.py
- okta/models/o_auth_2_scope_consent_grant_source.py
- okta/models/o_auth_2_scope_consent_grant_status.py
- okta/models/o_auth_2_scopes_mediation_policy_rule_condition.py
- okta/models/o_auth_2_token.py
- okta/models/o_auth_application_credentials.py
- okta/models/o_auth_authorization_policy.py
- okta/models/o_auth_endpoint_authentication_method.py
- okta/models/o_auth_grant_type.py
- okta/models/o_auth_response_type.py
- okta/models/okta_sign_on_policy.py
- okta/models/okta_sign_on_policy_conditions.py
- okta/models/okta_sign_on_policy_rule.py
- okta/models/okta_sign_on_policy_rule_actions.py
- okta/models/okta_sign_on_policy_rule_conditions.py
- okta/models/okta_sign_on_policy_rule_signon_actions.py
- okta/models/okta_sign_on_policy_rule_signon_session_actions.py
- okta/models/open_id_connect_application.py
- okta/models/open_id_connect_application_consent_method.py
- okta/models/open_id_connect_application_issuer_mode.py
- okta/models/open_id_connect_application_settings.py
- okta/models/open_id_connect_application_settings_client.py
- okta/models/open_id_connect_application_type.py
- okta/models/password_credential.py
- okta/models/password_credential_hash.py
- okta/models/password_credential_hash_algorithm.py
- okta/models/password_credential_hook.py
- okta/models/password_dictionary.py
- okta/models/password_dictionary_common.py
- okta/models/password_expiration_policy_rule_condition.py
- okta/models/password_policy.py
- okta/models/password_policy_authentication_provider_condition.py
- okta/models/password_policy_conditions.py
- okta/models/password_policy_delegation_settings.py
- okta/models/password_policy_delegation_settings_options.py
- okta/models/password_policy_password_settings.py
- okta/models/password_policy_password_settings_age.py
- okta/models/password_policy_password_settings_complexity.py
- okta/models/password_policy_password_settings_lockout.py
- okta/models/password_policy_recovery_email.py
- okta/models/password_policy_recovery_email_properties.py
- okta/models/password_policy_recovery_email_recovery_token.py
- okta/models/password_policy_recovery_factor_settings.py
- okta/models/password_policy_recovery_factors.py
- okta/models/password_policy_recovery_question.py
- okta/models/password_policy_recovery_question_complexity.py
- okta/models/password_policy_recovery_question_properties.py
- okta/models/password_policy_recovery_settings.py
- okta/models/password_policy_rule.py
- okta/models/password_policy_rule_action.py
- okta/models/password_policy_rule_actions.py
- okta/models/password_policy_rule_conditions.py
- okta/models/password_policy_settings.py
- okta/models/platform_condition_evaluator_platform.py
- okta/models/platform_condition_evaluator_platform_operating_system.py
- okta/models/platform_condition_evaluator_platform_operating_system_version.py
- okta/models/platform_policy_rule_condition.py
- okta/models/policy.py
- okta/models/policy_account_link.py
- okta/models/policy_account_link_filter.py
- okta/models/policy_account_link_filter_groups.py
- okta/models/policy_network_condition.py
- okta/models/policy_people_condition.py
- okta/models/policy_rule.py
- okta/models/policy_rule_auth_context_condition.py
- okta/models/policy_rule_conditions.py
- okta/models/policy_subject.py
- okta/models/policy_subject_match_type.py
- okta/models/policy_type.py
- okta/models/policy_user_name_template.py
- okta/models/protocol.py
- okta/models/protocol_algorithm_type.py
- okta/models/protocol_algorithm_type_signature.py
- okta/models/protocol_algorithms.py
- okta/models/protocol_endpoint.py
- okta/models/protocol_endpoints.py
- okta/models/protocol_relay_state.py
- okta/models/protocol_relay_state_format.py
- okta/models/protocol_settings.py
- okta/models/provisioning.py
- okta/models/provisioning_conditions.py
- okta/models/provisioning_deprovisioned_condition.py
- okta/models/provisioning_groups.py
- okta/models/provisioning_suspended_condition.py
- okta/models/push_user_factor.py
- okta/models/push_user_factor_profile.py
- okta/models/recovery_question_credential.py
- okta/models/reset_password_token.py
- okta/models/response_links.py
- okta/models/risk_policy_rule_condition.py
- okta/models/risk_score_policy_rule_condition.py
- okta/models/role.py
- okta/models/role_assignment_type.py
- okta/models/role_status.py
- okta/models/role_type.py
- okta/models/saml_application.py
- okta/models/saml_application_settings.py
- okta/models/saml_application_settings_sign_on.py
- okta/models/saml_attribute_statement.py
- okta/models/scheduled_user_lifecycle_action.py
- okta/models/scheme_application_credentials.py
- okta/models/scope.py
- okta/models/scope_type.py
- okta/models/secure_password_store_application.py
- okta/models/secure_password_store_application_settings.py
- okta/models/secure_password_store_application_settings_application.py
- okta/models/security_question.py
- okta/models/security_question_user_factor.py
- okta/models/security_question_user_factor_profile.py
- okta/models/session.py
- okta/models/session_authentication_method.py
- okta/models/session_identity_provider.py
- okta/models/session_identity_provider_type.py
- okta/models/session_status.py
- okta/models/sms_template.py
- okta/models/sms_template_translations.py
- okta/models/sms_template_type.py
- okta/models/sms_user_factor.py
- okta/models/sms_user_factor_profile.py
- okta/models/social_auth_token.py
- okta/models/swa_application.py
- okta/models/swa_application_settings.py
- okta/models/swa_application_settings_application.py
- okta/models/swa_three_field_application.py
- okta/models/swa_three_field_application_settings.py
- okta/models/swa_three_field_application_settings_application.py
- okta/models/temp_password.py
- okta/models/token_user_factor.py
- okta/models/token_user_factor_profile.py
- okta/models/totp_user_factor.py
- okta/models/totp_user_factor_profile.py
- okta/models/trusted_origin.py
- okta/models/u_2_f_user_factor.py
- okta/models/u_2_f_user_factor_profile.py
- okta/models/user.py
- okta/models/user_activation_token.py
- okta/models/user_condition.py
- okta/models/user_credentials.py
- okta/models/user_factor.py
- okta/models/user_identifier_condition_evaluator_pattern.py
- okta/models/user_identifier_policy_rule_condition.py
- okta/models/user_identity_provider_link_request.py
- okta/models/user_lifecycle_attribute_policy_rule_condition.py
- okta/models/user_next_login.py
- okta/models/user_policy_rule_condition.py
- okta/models/user_profile.py
- okta/models/user_status.py
- okta/models/user_status_policy_rule_condition.py
- okta/models/user_type.py
- okta/models/verify_factor_request.py
- okta/models/verify_user_factor_response.py
- okta/models/web_authn_user_factor.py
- okta/models/web_authn_user_factor_profile.py
- okta/models/web_user_factor.py
- okta/models/web_user_factor_profile.py
- okta/models/ws_federation_application.py
- okta/models/ws_federation_application_settings.py
- okta/models/ws_federation_application_settings_application.py

### Deleted Models:

- N/A
