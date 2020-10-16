import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError


class TestPoliciesResource:
    """
    Integration Tests for the Policies Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_sign_on_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Retrieve
        retrieved_policy, _, err = await client.get_policy(created_policy.id)
        assert err is None
        assert retrieved_policy.id == created_policy.id
        assert retrieved_policy.name == created_policy.name
        assert retrieved_policy.description == created_policy.description
        assert retrieved_policy.status == created_policy.status
        assert retrieved_policy.type == created_policy.type

        # Delete
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_password_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.PasswordPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Password",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.PasswordPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.PASSWORD

        # Retrieve
        retrieved_policy, _, err = await client.get_policy(created_policy.id)
        assert err is None
        assert retrieved_policy.id == created_policy.id
        assert retrieved_policy.name == created_policy.name
        assert retrieved_policy.description == created_policy.description
        assert retrieved_policy.status == created_policy.status
        assert retrieved_policy.type == created_policy.type

        # Delete
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.Policy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "type": models.PolicyType.OKTA_SIGN_ON,
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Retrieve
        retrieved_policy, _, err = await client.get_policy(created_policy.id)
        assert err is None
        assert retrieved_policy.id == created_policy.id
        assert retrieved_policy.name == created_policy.name
        assert retrieved_policy.description == created_policy.description
        assert retrieved_policy.status == created_policy.status
        assert retrieved_policy.type == created_policy.type

        # Delete
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_sign_on_policy_with_group_conditions(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Group
        GROUP_NAME = "Group-Target-Test"
        group_obj = models.Group({
            "profile": models.GroupProfile({
                "name": GROUP_NAME
            })
        })
        created_group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(created_group, models.Group)

        # Create Policy & Conditions
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        policy_conditions = models.OktaSignOnPolicyConditions({
            "people": models.PolicyPeopleCondition({
                "groups": models.GroupCondition({
                    "include": [created_group.id]
                })
            })
        })

        policy_model.conditions = policy_conditions

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON
        assert len(created_policy.conditions.people.groups.include) == 1
        assert created_group.id in \
            created_policy.conditions.people.groups.include

        # Retrieve
        retrieved_policy, _, err = await client.get_policy(created_policy.id)
        assert err is None
        assert retrieved_policy.id == created_policy.id
        assert retrieved_policy.name == created_policy.name
        assert retrieved_policy.description == created_policy.description
        assert retrieved_policy.status == created_policy.status
        assert retrieved_policy.type == created_policy.type
        assert len(retrieved_policy.conditions.people.groups.include) == 1
        assert created_group.id in \
            retrieved_policy.conditions.people.groups.include

        # Delete Policy + Group
        _, err = await client.delete_policy(created_policy.id)
        assert err is None
        _, err = await client.delete_group(created_group.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_policies_by_type(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policies
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test sign on policy applies for tests only"
        })

        policy_model_2 = models.PasswordPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Password",
            "status": "ACTIVE",
            "description": "Test password policy applies for tests only"
        })

        created_oss_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_oss_policy, models.OktaSignOnPolicy)
        assert created_oss_policy.name == policy_model.name
        assert created_oss_policy.description == policy_model.description
        assert created_oss_policy.status == "ACTIVE"
        assert created_oss_policy.type == models.PolicyType.OKTA_SIGN_ON

        created_pw_policy, _, err = await client.create_policy(policy_model_2)
        assert err is None
        assert isinstance(created_pw_policy, models.PasswordPolicy)
        assert created_pw_policy.name == policy_model_2.name
        assert created_pw_policy.description == policy_model_2.description
        assert created_pw_policy.status == "ACTIVE"
        assert created_pw_policy.type == models.PolicyType.PASSWORD

        # List by type
        query_params_list_sign_on = {"type": "OKTA_SIGN_ON"}
        sign_on_policies, _, err = await \
            client.list_policies(query_params_list_sign_on)
        assert err is None
        assert isinstance(sign_on_policies, list)
        assert next((plcy for plcy in sign_on_policies
                     if plcy.id == created_oss_policy.id))

        query_params_list_pw = {"type": "PASSWORD"}
        sign_on_policies, _, err = await \
            client.list_policies(query_params_list_pw)
        assert err is None
        assert isinstance(sign_on_policies, list)
        assert next((plcy for plcy in sign_on_policies
                     if plcy.id == created_pw_policy.id))

        # Delete
        _, err = await client.delete_policy(created_oss_policy.id)
        assert err is None
        _, err = await client.delete_policy(created_pw_policy.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Retrieve
        retrieved_policy, _, err = await client.get_policy(created_policy.id)
        assert err is None
        assert retrieved_policy.id == created_policy.id
        assert retrieved_policy.name == created_policy.name
        assert retrieved_policy.description == created_policy.description
        assert retrieved_policy.status == created_policy.status
        assert retrieved_policy.type == created_policy.type

        # Delete
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

        # Retrieve
        retrieved_policy, resp, err = await \
            client.get_policy(created_policy.id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_policy is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Retrieve
        retrieved_policy, _, err = await client.get_policy(created_policy.id)
        assert err is None
        assert retrieved_policy.id == created_policy.id
        assert retrieved_policy.name == created_policy.name
        assert retrieved_policy.description == created_policy.description
        assert retrieved_policy.status == created_policy.status
        assert retrieved_policy.type == created_policy.type

        # Update
        NEW_NAME = policy_model.name + "UPDATED"
        NEW_DESC = policy_model.description + "UPDATED"
        created_policy.name = NEW_NAME
        created_policy.description = NEW_DESC
        updated_policy, _, err = await client.update_policy(
            created_policy.id, created_policy
        )
        assert err is None
        assert updated_policy.id == created_policy.id
        assert updated_policy.name == NEW_NAME
        assert updated_policy.description == NEW_DESC

        # Retrieve
        retrieved_policy, _, err = await client.get_policy(created_policy.id)
        assert err is None
        assert retrieved_policy.id == created_policy.id
        assert retrieved_policy.name == NEW_NAME
        assert retrieved_policy.description == NEW_DESC
        assert retrieved_policy.status == created_policy.status
        assert retrieved_policy.type == created_policy.type

        # Delete
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_deactivate_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Deactivate
        _, err = await client.deactivate_policy(created_policy.id)
        assert err is None

        # Retrieve
        retrieved_policy, _, err = await client.get_policy(created_policy.id)
        assert err is None
        assert retrieved_policy.id == created_policy.id
        assert retrieved_policy.name == created_policy.name
        assert retrieved_policy.description == created_policy.description
        assert retrieved_policy.status == "INACTIVE"
        assert retrieved_policy.type == created_policy.type

        # Reactivate
        _, err = await client.activate_policy(created_policy.id)
        assert err is None

        # Delete
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

    """
    POLICY RULES TESTS BELOW
    """
    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_sign_on_policy_rule(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Create Policy Rule
        policy_rule_model = models.OktaSignOnPolicyRule({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On-Rule",
            "actions": models.OktaSignOnPolicyRuleActions({
                "signon": models.OktaSignOnPolicyRuleSignonActions({
                    "access": "ALLOW",
                    "requireFactor": "false",
                    "rememberDeviceByDefault": "false",
                    "session":
                    models.OktaSignOnPolicyRuleSignonSessionActions({
                        "usePersistentCookie": "false",
                        "maxSessionIdleMinutes": 720,
                        "maxSessionLifetimeMinutes": 0
                    })
                })
            }),
            "conditions": models.OktaSignOnPolicyRuleConditions({
                "authContext": models.PolicyRuleAuthContextCondition({
                    "authType": "ANY"
                })
            })
        })
        created_policy_rule, _, err = await client.create_policy_rule(
            created_policy.id, policy_rule_model
        )
        assert err is None
        assert isinstance(created_policy_rule, models.OktaSignOnPolicyRule)
        assert created_policy_rule.name == policy_rule_model.name
        assert created_policy_rule.type == "SIGN_ON"
        assert created_policy_rule.actions.signon.access == "ALLOW"
        assert created_policy_rule.actions.signon.require_factor is False
        assert created_policy_rule.actions.signon.remember_device_by_default\
            is False
        assert created_policy_rule.actions.signon.session.\
            use_persistent_cookie is False
        assert created_policy_rule.actions.signon.session.\
            max_session_idle_minutes == 720
        assert created_policy_rule.actions.signon.session.\
            max_session_lifetime_minutes == 0
        assert created_policy_rule.conditions.auth_context.auth_type == "ANY"

        # Retrieve
        retrieved_policy_rule, _, err = await client.get_policy_rule(
            created_policy.id, created_policy_rule.id)
        assert err is None
        assert retrieved_policy_rule.id == created_policy_rule.id
        assert retrieved_policy_rule.name == created_policy_rule.name
        assert isinstance(retrieved_policy_rule, models.OktaSignOnPolicyRule)

        # Delete
        _, err = await \
            client.delete_policy_rule(
                created_policy.id, created_policy_rule.id)
        assert err is None
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_password_policy_rule(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.PasswordPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Password",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.PasswordPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.PASSWORD

        # Create Policy Rule
        policy_rule_model = models.PasswordPolicyRule({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Password-Rule",
            "actions": models.PasswordPolicyRuleActions({
                "passwordChange": models.PasswordPolicyRuleAction({
                    "access": "ALLOW"
                }),
                "selfServicePasswordReset": models.PasswordPolicyRuleAction({
                    "access": "ALLOW"
                }),
                "selfServiceUnlock": models.PasswordPolicyRuleAction({
                    "access": "ALLOW"
                })
            }),
            "conditions": models.PasswordPolicyRuleConditions({
                "people": models.PolicyPeopleCondition({
                    "users": models.UserCondition({
                        "exclude": []
                    })
                }),
                "network": models.PolicyNetworkCondition({
                    "connection": "ANYWHERE"
                })
            })
        })
        created_policy_rule, _, err = await client.create_policy_rule(
            created_policy.id, policy_rule_model
        )
        assert err is None
        assert isinstance(created_policy_rule, models.PasswordPolicyRule)
        assert created_policy_rule.name == policy_rule_model.name
        assert created_policy_rule.type == "PASSWORD"
        assert created_policy_rule.status == "ACTIVE"
        assert created_policy_rule.conditions.people.users.exclude == []
        assert created_policy_rule.conditions.network.connection ==\
            "ANYWHERE"
        assert created_policy_rule.actions.password_change.access == "ALLOW"
        assert created_policy_rule.actions.self_service_password_reset\
            .access == "ALLOW"
        assert created_policy_rule.actions.self_service_unlock\
            .access == "ALLOW"

        # Retrieve
        retrieved_policy_rule, _, err = await client.get_policy_rule(
            created_policy.id, created_policy_rule.id)
        assert err is None
        assert retrieved_policy_rule.id == created_policy_rule.id
        assert retrieved_policy_rule.name == created_policy_rule.name
        assert isinstance(retrieved_policy_rule, models.PasswordPolicyRule)

        # Delete
        _, err = await \
            client.delete_policy_rule(
                created_policy.id, created_policy_rule.id)
        assert err is None
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_policy_rule(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Create Policy Rule
        policy_rule_model = models.OktaSignOnPolicyRule({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On-Rule",
            "actions": models.OktaSignOnPolicyRuleActions({
                "signon": models.OktaSignOnPolicyRuleSignonActions({
                    "access": "ALLOW",
                    "requireFactor": "false",
                    "rememberDeviceByDefault": "false",
                    "session":
                    models.OktaSignOnPolicyRuleSignonSessionActions({
                        "usePersistentCookie": "false",
                        "maxSessionIdleMinutes": 720,
                        "maxSessionLifetimeMinutes": 0
                    })
                })
            }),
            "conditions": models.OktaSignOnPolicyRuleConditions({
                "authContext": models.PolicyRuleAuthContextCondition({
                    "authType": "ANY"
                })
            })
        })
        created_policy_rule, _, err = await client.create_policy_rule(
            created_policy.id, policy_rule_model
        )
        assert err is None
        assert isinstance(created_policy_rule, models.OktaSignOnPolicyRule)
        assert created_policy_rule.name == policy_rule_model.name
        assert created_policy_rule.type == "SIGN_ON"
        assert created_policy_rule.actions.signon.access == "ALLOW"
        assert created_policy_rule.actions.signon.require_factor is False
        assert created_policy_rule.actions.signon.remember_device_by_default\
            is False
        assert created_policy_rule.actions.signon.session.\
            use_persistent_cookie is False
        assert created_policy_rule.actions.signon.session.\
            max_session_idle_minutes == 720
        assert created_policy_rule.actions.signon.session.\
            max_session_lifetime_minutes == 0
        assert created_policy_rule.conditions.auth_context.auth_type == "ANY"

        # Retrieve
        retrieved_policy_rule, _, err = await client.get_policy_rule(
            created_policy.id, created_policy_rule.id)
        assert err is None
        assert retrieved_policy_rule.id == created_policy_rule.id
        assert retrieved_policy_rule.name == created_policy_rule.name
        assert isinstance(retrieved_policy_rule, models.OktaSignOnPolicyRule)

        # Update
        created_policy_rule.name = policy_rule_model.name + "UPDATED"
        created_policy_rule.conditions.network.connection = "ANYWHERE"
        updated_policy_rule, _, err = await client.update_policy_rule(
            created_policy.id, created_policy_rule.id, created_policy_rule
        )
        assert err is None
        assert isinstance(updated_policy_rule, models.OktaSignOnPolicyRule)
        assert updated_policy_rule.name == created_policy_rule.name
        assert updated_policy_rule.conditions.network.connection ==\
            created_policy_rule.conditions.network.connection

        # Retrieve
        retrieved_policy_rule, _, err = await client.get_policy_rule(
            created_policy.id, created_policy_rule.id)
        assert err is None
        assert retrieved_policy_rule.id == created_policy_rule.id
        assert retrieved_policy_rule.name == created_policy_rule.name
        assert retrieved_policy_rule.conditions.network.connection ==\
            created_policy_rule.conditions.network.connection
        assert isinstance(retrieved_policy_rule, models.OktaSignOnPolicyRule)

        # Delete
        _, err = await \
            client.delete_policy_rule(
                created_policy.id, created_policy_rule.id)
        assert err is None
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_policy_rules(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Create Policy Rule
        policy_rule_model = models.OktaSignOnPolicyRule({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On-Rule",
            "actions": models.OktaSignOnPolicyRuleActions({
                "signon": models.OktaSignOnPolicyRuleSignonActions({
                    "access": "ALLOW",
                    "requireFactor": "false",
                    "rememberDeviceByDefault": "false",
                    "session":
                    models.OktaSignOnPolicyRuleSignonSessionActions({
                        "usePersistentCookie": "false",
                        "maxSessionIdleMinutes": 720,
                        "maxSessionLifetimeMinutes": 0
                    })
                })
            }),
            "conditions": models.OktaSignOnPolicyRuleConditions({
                "authContext": models.PolicyRuleAuthContextCondition({
                    "authType": "ANY"
                })
            })
        })
        created_policy_rule, _, err = await client.create_policy_rule(
            created_policy.id, policy_rule_model
        )
        assert err is None
        assert isinstance(created_policy_rule, models.OktaSignOnPolicyRule)
        assert created_policy_rule.name == policy_rule_model.name
        assert created_policy_rule.type == "SIGN_ON"
        assert created_policy_rule.actions.signon.access == "ALLOW"
        assert created_policy_rule.actions.signon.require_factor is False
        assert created_policy_rule.actions.signon.remember_device_by_default\
            is False
        assert created_policy_rule.actions.signon.session.\
            use_persistent_cookie is False
        assert created_policy_rule.actions.signon.session.\
            max_session_idle_minutes == 720
        assert created_policy_rule.actions.signon.session.\
            max_session_lifetime_minutes == 0
        assert created_policy_rule.conditions.auth_context.auth_type == "ANY"

        # List
        policy_rules, _, err = await \
            client.list_policy_rules(created_policy.id)
        assert err is None
        assert isinstance(policy_rules, list)
        assert next((plcy_rule for plcy_rule in policy_rules
                     if plcy_rule.id == created_policy_rule.id))
        assert len(policy_rules) == 1

        # Delete
        _, err = await \
            client.delete_policy_rule(
                created_policy.id, created_policy_rule.id)
        assert err is None
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_policy_rules(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Create Policy Rule
        policy_rule_model = models.OktaSignOnPolicyRule({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On-Rule",
            "actions": models.OktaSignOnPolicyRuleActions({
                "signon": models.OktaSignOnPolicyRuleSignonActions({
                    "access": "ALLOW",
                    "requireFactor": "false",
                    "rememberDeviceByDefault": "false",
                    "session":
                    models.OktaSignOnPolicyRuleSignonSessionActions({
                        "usePersistentCookie": "false",
                        "maxSessionIdleMinutes": 720,
                        "maxSessionLifetimeMinutes": 0
                    })
                })
            }),
            "conditions": models.OktaSignOnPolicyRuleConditions({
                "authContext": models.PolicyRuleAuthContextCondition({
                    "authType": "ANY"
                })
            })
        })
        created_policy_rule, _, err = await client.create_policy_rule(
            created_policy.id, policy_rule_model
        )
        assert err is None
        assert isinstance(created_policy_rule, models.OktaSignOnPolicyRule)
        assert created_policy_rule.name == policy_rule_model.name
        assert created_policy_rule.type == "SIGN_ON"
        assert created_policy_rule.actions.signon.access == "ALLOW"
        assert created_policy_rule.actions.signon.require_factor is False
        assert created_policy_rule.actions.signon.remember_device_by_default\
            is False
        assert created_policy_rule.actions.signon.session.\
            use_persistent_cookie is False
        assert created_policy_rule.actions.signon.session.\
            max_session_idle_minutes == 720
        assert created_policy_rule.actions.signon.session.\
            max_session_lifetime_minutes == 0
        assert created_policy_rule.conditions.auth_context.auth_type == "ANY"

        # Retrieve
        retrieved_policy_rule, _, err = await client.get_policy_rule(
            created_policy.id, created_policy_rule.id)
        assert err is None
        assert retrieved_policy_rule.id == created_policy_rule.id
        assert retrieved_policy_rule.name == created_policy_rule.name
        assert isinstance(retrieved_policy_rule, models.OktaSignOnPolicyRule)

        # Delete
        _, err = await \
            client.delete_policy_rule(
                created_policy.id, created_policy_rule.id)
        assert err is None
        _, err = await client.delete_policy(created_policy.id)
        assert err is None

        # Retrieve
        retrieved_policy_rule, resp, err = await client.get_policy_rule(
            created_policy.id, created_policy_rule.id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_policy_rule is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_deactivate_policy_rule(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Policy
        policy_model = models.OktaSignOnPolicy({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On",
            "status": "ACTIVE",
            "description": "Test policy applies for tests only"
        })

        created_policy, _, err = await client.create_policy(policy_model)
        assert err is None
        assert isinstance(created_policy, models.OktaSignOnPolicy)
        assert created_policy.name == policy_model.name
        assert created_policy.description == policy_model.description
        assert created_policy.status == "ACTIVE"
        assert created_policy.type == models.PolicyType.OKTA_SIGN_ON

        # Create Policy Rule
        policy_rule_model = models.OktaSignOnPolicyRule({
            "name": f"{TestPoliciesResource.SDK_PREFIX} Test-Sign-On-Rule",
            "actions": models.OktaSignOnPolicyRuleActions({
                "signon": models.OktaSignOnPolicyRuleSignonActions({
                    "access": "ALLOW",
                    "requireFactor": "false",
                    "rememberDeviceByDefault": "false",
                    "session":
                    models.OktaSignOnPolicyRuleSignonSessionActions({
                        "usePersistentCookie": "false",
                        "maxSessionIdleMinutes": 720,
                        "maxSessionLifetimeMinutes": 0
                    })
                })
            }),
            "conditions": models.OktaSignOnPolicyRuleConditions({
                "authContext": models.PolicyRuleAuthContextCondition({
                    "authType": "ANY"
                })
            })
        })
        created_policy_rule, _, err = await client.create_policy_rule(
            created_policy.id, policy_rule_model
        )
        assert err is None
        assert isinstance(created_policy_rule, models.OktaSignOnPolicyRule)
        assert created_policy_rule.name == policy_rule_model.name
        assert created_policy_rule.type == "SIGN_ON"
        assert created_policy_rule.status == "ACTIVE"
        assert created_policy_rule.actions.signon.access == "ALLOW"
        assert created_policy_rule.actions.signon.require_factor is False
        assert created_policy_rule.actions.signon.remember_device_by_default\
            is False
        assert created_policy_rule.actions.signon.session.\
            use_persistent_cookie is False
        assert created_policy_rule.actions.signon.session.\
            max_session_idle_minutes == 720
        assert created_policy_rule.actions.signon.session.\
            max_session_lifetime_minutes == 0
        assert created_policy_rule.conditions.auth_context.auth_type == "ANY"

        # Retrieve
        retrieved_policy_rule, _, err = await client.get_policy_rule(
            created_policy.id, created_policy_rule.id)
        assert err is None
        assert retrieved_policy_rule.id == created_policy_rule.id
        assert retrieved_policy_rule.name == created_policy_rule.name
        assert retrieved_policy_rule.status == "ACTIVE"
        assert isinstance(retrieved_policy_rule, models.OktaSignOnPolicyRule)

        # Deactivate
        _, err = await client.deactivate_policy_rule(
            created_policy.id, created_policy_rule.id
        )
        assert err is None

        # Retrieve
        retrieved_policy_rule, _, err = await client.get_policy_rule(
            created_policy.id, created_policy_rule.id)
        assert err is None
        assert retrieved_policy_rule.id == created_policy_rule.id
        assert retrieved_policy_rule.name == created_policy_rule.name
        assert retrieved_policy_rule.status == "INACTIVE"
        assert isinstance(retrieved_policy_rule, models.OktaSignOnPolicyRule)

        # Reactivate
        _, err = await client.activate_policy_rule(
            created_policy.id, created_policy_rule.id
        )
        assert err is None

        # Retrieve
        retrieved_policy_rule, _, err = await client.get_policy_rule(
            created_policy.id, created_policy_rule.id)
        assert err is None
        assert retrieved_policy_rule.id == created_policy_rule.id
        assert retrieved_policy_rule.name == created_policy_rule.name
        assert retrieved_policy_rule.status == "ACTIVE"
        assert isinstance(retrieved_policy_rule, models.OktaSignOnPolicyRule)

        # Delete
        _, err = await \
            client.delete_policy_rule(
                created_policy.id, created_policy_rule.id)
        assert err is None
        _, err = await client.delete_policy(created_policy.id)
        assert err is None
