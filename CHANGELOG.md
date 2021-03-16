# Okta Python SDK Changelog

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
