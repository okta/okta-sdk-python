# flake8: noqa
# The Okta software accompanied by this notice is provided pursuant to the following terms:
# Copyright © 2025-Present, Okta, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
# License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
# coding: utf-8

import pytest

import okta.models as models
from tests.mocks import MockOktaClient


class TestAuthorizationServerRulesResource:
    """
    Integration Tests for the Authorization Server Rules Resource

    This test suite provides comprehensive integration testing for the Authorization Server Rules API
    within the Okta Python SDK. The tests validate real API interactions using VCR for recording
    and replaying HTTP requests/responses.

    API Methods Tested:
    1. create_authorization_server_policy_rule() - Create a policy rule
    2. get_authorization_server_policy_rule() - Get a specific rule
    3. list_authorization_server_policy_rules() - List all rules for a policy
    4. replace_authorization_server_policy_rule() - Replace/update a rule
    5. activate_authorization_server_policy_rule() - Activate a rule
    6. deactivate_authorization_server_policy_rule() - Deactivate a rule
    7. delete_authorization_server_policy_rule() - Delete a rule
    """

    SDK_PREFIX = "python_sdk_rules"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_policy_rules_lifecycle(self, fs):
        """
        Test the complete lifecycle of Authorization Server Policy Rules operations

        This test covers:
        - Creating a temporary authorization server
        - Creating a policy within the auth server
        - Creating a policy rule
        - Getting and listing rules
        - Replacing/updating a rule
        - Activating and deactivating a rule
        - Deleting the rule
        - Cleaning up temporary resources
        """
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        auth_server_id = None
        policy_id = None
        rule_id = None

        try:
            # ===== CREATE AUTHORIZATION SERVER =====
            print("\n=== Creating Authorization Server ===")

            auth_server_name = f"{TestAuthorizationServerRulesResource.SDK_PREFIX}_server"
            auth_server = models.AuthorizationServer(
                name=auth_server_name,
                description="Test Auth Server for Rules API",
                audiences=["api://test_rules"]
            )

            created_auth_server, _, err = await client.create_authorization_server(auth_server)

            assert err is None, f"Failed to create authorization server: {err}"
            assert created_auth_server is not None
            assert isinstance(created_auth_server, models.AuthorizationServer)

            auth_server_id = created_auth_server.id
            print(f"Created auth server: {auth_server_id}")

            # ===== CREATE POLICY =====
            print("\n=== Creating Policy ===")

            policy_name = f"{TestAuthorizationServerRulesResource.SDK_PREFIX}_policy"
            policy = models.AuthorizationServerPolicy(
                name=policy_name,
                description="Test Policy for Rules",
                priority=1,
                type="OAUTH_AUTHORIZATION_POLICY"
            )

            created_policy, _, err = await client.create_authorization_server_policy(
                auth_server_id, policy
            )

            assert err is None, f"Failed to create policy: {err}"
            assert created_policy is not None
            assert isinstance(created_policy, models.AuthorizationServerPolicy)

            policy_id = created_policy.id
            print(f"Created policy: {policy_id}")

            # ===== CREATE POLICY RULE =====
            print("\n=== Creating Policy Rule ===")

            rule_name = f"{TestAuthorizationServerRulesResource.SDK_PREFIX}_rule"

            # Create rule conditions
            rule_conditions = models.AuthorizationServerPolicyRuleConditions(
                people=models.AuthorizationServerPolicyPeopleCondition(
                    groups=models.AuthorizationServerPolicyRuleGroupCondition(
                        include=["EVERYONE"]
                    )
                ),
                grant_types=models.GrantTypePolicyRuleCondition(
                    include=["authorization_code", "client_credentials"]
                ),
                scopes=models.OAuth2ScopesMediationPolicyRuleCondition(
                    include=["*"]
                )
            )

            # Create rule actions
            rule_actions = models.AuthorizationServerPolicyRuleActions(
                token=models.TokenAuthorizationServerPolicyRuleAction(
                    access_token_lifetime_minutes=60,
                    refresh_token_lifetime_minutes=0,
                    refresh_token_window_minutes=10080
                )
            )

            rule_request = models.AuthorizationServerPolicyRuleRequest(
                name=rule_name,
                priority=1,
                type="RESOURCE_ACCESS",
                conditions=rule_conditions,
                actions=rule_actions
            )

            created_rule, _, err = await client.create_authorization_server_policy_rule(
                auth_server_id, policy_id, rule_request
            )

            assert err is None, f"Failed to create policy rule: {err}"
            assert created_rule is not None
            assert isinstance(created_rule, models.AuthorizationServerPolicyRule)
            assert created_rule.name == rule_name

            rule_id = created_rule.id
            print(f"Created policy rule: {rule_id}")
            print(f"  Name: {created_rule.name}")
            print(f"  Priority: {created_rule.priority}")
            print(f"  Status: {created_rule.status}")

            # ===== GET POLICY RULE =====
            print("\n=== Getting Policy Rule ===")

            retrieved_rule, _, err = await client.get_authorization_server_policy_rule(
                auth_server_id, policy_id, rule_id
            )

            assert err is None, f"Failed to get policy rule: {err}"
            assert retrieved_rule is not None
            assert retrieved_rule.id == rule_id
            assert retrieved_rule.name == rule_name

            print(f"Retrieved policy rule: {retrieved_rule.id}")

            # ===== LIST POLICY RULES =====
            print("\n=== Listing Policy Rules ===")

            rules_list, _, err = await client.list_authorization_server_policy_rules(
                auth_server_id, policy_id
            )

            assert err is None, f"Failed to list policy rules: {err}"
            assert rules_list is not None
            assert isinstance(rules_list, list)
            assert len(rules_list) > 0

            # Verify our created rule is in the list
            rule_ids = [rule.id for rule in rules_list]
            assert rule_id in rule_ids, f"Created rule {rule_id} not found in list"

            print(f"Found {len(rules_list)} policy rule(s)")

            # ===== REPLACE (UPDATE) POLICY RULE =====
            print("\n=== Replacing Policy Rule ===")

            updated_name = f"{rule_name}_updated"

            # Create updated rule with modified name and priority
            updated_rule_request = models.AuthorizationServerPolicyRuleRequest(
                name=updated_name,
                priority=2,  # Changed priority
                type="RESOURCE_ACCESS",
                conditions=rule_conditions,
                actions=rule_actions
            )

            replaced_rule, _, err = await client.replace_authorization_server_policy_rule(
                auth_server_id, policy_id, rule_id, updated_rule_request
            )

            assert err is None, f"Failed to replace policy rule: {err}"
            assert replaced_rule is not None
            assert replaced_rule.id == rule_id
            assert replaced_rule.name == updated_name

            print(f"Replaced policy rule successfully")
            print(f"  New name: {replaced_rule.name}")
            print(f"  Priority: {replaced_rule.priority}")

            # ===== DEACTIVATE POLICY RULE =====
            print("\n=== Deactivating Policy Rule ===")

            # Check current status
            current_status = replaced_rule.status
            print(f"Current status: {current_status}")

            if current_status == "ACTIVE":
                _, _, err = await client.deactivate_authorization_server_policy_rule(
                    auth_server_id, policy_id, rule_id
                )

                assert err is None, f"Failed to deactivate policy rule: {err}"
                print(f"Successfully deactivated policy rule")
            else:
                print(f"Rule already INACTIVE, skipping deactivation")

            # ===== ACTIVATE POLICY RULE =====
            print("\n=== Activating Policy Rule ===")

            _, _, err = await client.activate_authorization_server_policy_rule(
                auth_server_id, policy_id, rule_id
            )

            assert err is None, f"Failed to activate policy rule: {err}"
            print(f"Successfully activated policy rule")

            # ===== DEACTIVATE AGAIN BEFORE DELETION =====
            print("\n=== Deactivating Rule Before Deletion ===")

            _, _, err = await client.deactivate_authorization_server_policy_rule(
                auth_server_id, policy_id, rule_id
            )

            assert err is None, f"Failed to deactivate policy rule before deletion: {err}"
            print(f"Deactivated rule for deletion")

            # ===== DELETE POLICY RULE =====
            print("\n=== Deleting Policy Rule ===")

            _, _, err = await client.delete_authorization_server_policy_rule(
                auth_server_id, policy_id, rule_id
            )

            assert err is None, f"Failed to delete policy rule: {err}"
            print(f"Successfully deleted policy rule")

            # ===== VERIFY RULE IS DELETED =====
            print("\n=== Verifying Rule Deletion ===")

            verify_list, _, verify_err = await client.list_authorization_server_policy_rules(
                auth_server_id, policy_id
            )

            if verify_err is None:
                verify_ids = [rule.id for rule in verify_list]
                assert rule_id not in verify_ids, f"Rule {rule_id} still exists after deletion"
                print(f"Verified rule is deleted")

            print("\n=== Test completed successfully ===")

        except Exception as e:
            print(f"\n!!! Test failed with error: {e}")
            raise

        finally:
            # ===== CLEANUP: DELETE POLICY AND AUTH SERVER =====
            print("\n=== Cleanup: Deleting Resources ===")

            if rule_id:
                try:
                    print(f"Attempting to delete rule: {rule_id}")
                    # Try to deactivate and delete if it still exists
                    await client.deactivate_authorization_server_policy_rule(
                        auth_server_id, policy_id, rule_id
                    )
                    _, _, err = await client.delete_authorization_server_policy_rule(
                        auth_server_id, policy_id, rule_id
                    )
                    if not err:
                        print(f"Deleted rule in cleanup")
                except Exception as e:
                    print(f"Rule cleanup (already deleted or error): {e}")

            if policy_id and auth_server_id:
                try:
                    print(f"Deleting policy: {policy_id}")
                    _, _, err = await client.delete_authorization_server_policy(
                        auth_server_id, policy_id
                    )
                    if err:
                        print(f"Warning: Could not delete policy: {err}")
                    else:
                        print(f"Deleted policy successfully")
                except Exception as e:
                    print(f"Exception deleting policy: {e}")

            if auth_server_id:
                try:
                    print(f"Deleting authorization server: {auth_server_id}")
                    _, _, err = await client.delete_authorization_server(auth_server_id)
                    if err:
                        print(f"Warning: Could not delete auth server: {err}")
                    else:
                        print(f"Deleted auth server successfully")
                except Exception as e:
                    print(f"Exception deleting auth server: {e}")

            print("=== Cleanup completed ===")

