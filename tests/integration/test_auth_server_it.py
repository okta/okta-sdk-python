import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError


class TestAuthorizationServerResource:
    """
    Integration Tests for the Authorization Server Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_auth_server(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_aaPeZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        created, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(created, models.AuthorizationServer)
        assert created.name == TEST_NAME
        assert created.description == TEST_DESC
        assert created.audiences == TEST_AUDS
        assert created.audiences[0] == TEST_AUDS[0]

        # Clean up
        _, err = await client.deactivate_authorization_server(created.id)
        assert err is None
        _, err = await client.delete_authorization_server(created.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_auth_servers(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # List Auth Servers
        auth_servers, _, err = await client.list_authorization_servers()
        assert err is None
        # Assuming default Auth server instantiated
        assert auth_servers is not None
        assert len(auth_servers) > 0

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_created_auth_server(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_aaPeZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        created, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(created, models.AuthorizationServer)
        assert created.name == TEST_NAME
        assert created.description == TEST_DESC
        assert created.audiences == TEST_AUDS
        assert created.audiences[0] == TEST_AUDS[0]

        # Get Auth Server
        auth_server, _, err = await client.get_authorization_server(created.id)
        assert err is None
        assert auth_server.id == created.id
        assert auth_server.name == created.name
        assert auth_server.description == created.description

        # Clean up
        _, err = await client.deactivate_authorization_server(created.id)
        assert err is None
        _, err = await client.delete_authorization_server(created.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_auth_server(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abPeZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        created, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(created, models.AuthorizationServer)
        assert created.name == TEST_NAME
        assert created.description == TEST_DESC
        assert created.audiences == TEST_AUDS
        assert created.audiences[0] == TEST_AUDS[0]

        # Update
        UPDATED_DESC = f"{TEST_DESC}-Updated"
        created.description = UPDATED_DESC
        updated, _, err = await client.update_authorization_server(created.id,
                                                                   created)
        assert err is None
        assert updated.description == UPDATED_DESC
        assert updated.id == created.id

        # Clean up
        _, err = await client.deactivate_authorization_server(created.id)
        assert err is None
        _, err = await client.delete_authorization_server(created.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_deactivate_delete_server(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abCeZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        created, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(created, models.AuthorizationServer)
        assert created.name == TEST_NAME
        assert created.description == TEST_DESC
        assert created.audiences == TEST_AUDS
        assert created.audiences[0] == TEST_AUDS[0]

        # Get Auth Server
        auth_server, _, err = await client.get_authorization_server(created.id)
        assert err is None
        assert auth_server.id == created.id
        assert auth_server.status == "ACTIVE"

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(created.id)
        assert err is None

        # Get Auth Server
        auth_server, _, err = await client.get_authorization_server(created.id)
        assert err is None
        assert auth_server.id == created.id
        assert auth_server.status == "INACTIVE"

        # Delete Auth server
        _, err = await client.delete_authorization_server(created.id)
        assert err is None

        # Get Auth Server
        auth_server, resp, err = await\
            client.get_authorization_server(created.id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_server(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abCeZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        created, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(created, models.AuthorizationServer)
        assert created.name == TEST_NAME
        assert created.description == TEST_DESC
        assert created.audiences == TEST_AUDS
        assert created.audiences[0] == TEST_AUDS[0]

        # Get Auth Server
        auth_server, _, err = await client.get_authorization_server(created.id)
        assert err is None
        assert auth_server.id == created.id
        assert auth_server.status == "ACTIVE"

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(created.id)
        assert err is None

        # Get Auth Server
        auth_server, _, err = await client.get_authorization_server(created.id)
        assert err is None
        assert auth_server.id == created.id
        assert auth_server.status == "INACTIVE"

        # Activate Auth server
        _, err = await client.activate_authorization_server(created.id)
        assert err is None

        # Get Auth Server
        auth_server, _, err = await client.get_authorization_server(created.id)
        assert err is None
        assert auth_server.id == created.id
        assert auth_server.status == "ACTIVE"

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(created.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(created.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_auth_server_policies(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDeZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        created, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(created, models.AuthorizationServer)
        assert created.name == TEST_NAME
        assert created.description == TEST_DESC
        assert created.audiences == TEST_AUDS
        assert created.audiences[0] == TEST_AUDS[0]

        # Create Policy
        POLICY_TYPE = models.PolicyType.OAUTH_AUTHORIZATION_POLICY
        POLICY_STATUS = "ACTIVE"
        POLICY_NAME = "Test Policy"
        POLICY_DESC = "Test Policy"
        POLICY_PRIORITY = 1
        POLICY_CONDITIONS = models.PolicyRuleConditions({
            "clients": models.ClientPolicyCondition({
                "include": ["ALL_CLIENTS"]
            })
        })

        policy_obj = models.Policy({
            "type": POLICY_TYPE,
            "status": POLICY_STATUS,
            "name": POLICY_NAME,
            "description": POLICY_DESC,
            "priority": POLICY_PRIORITY,
            "conditions": POLICY_CONDITIONS
        })

        policy, _, err = await client.create_authorization_server_policy(
            created.id, policy_obj
        )
        assert err is None

        # Get Policies
        policies, _, err = await client.list_authorization_server_policies(
            created.id
        )
        assert err is None
        assert len(policies) > 0
        assert next((plcy for plcy in policies if plcy.id == policy.id))

        # Delete Policy
        _, err = await client.delete_authorization_server_policy(
            created.id, policy.id
        )
        assert err is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(created.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(created.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_auth_server_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        created, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(created, models.AuthorizationServer)
        assert created.name == TEST_NAME
        assert created.description == TEST_DESC
        assert created.audiences == TEST_AUDS
        assert created.audiences[0] == TEST_AUDS[0]

        # Create Policy
        POLICY_TYPE = models.PolicyType.OAUTH_AUTHORIZATION_POLICY
        POLICY_STATUS = "ACTIVE"
        POLICY_NAME = "Test Policy"
        POLICY_DESC = "Test Policy"
        POLICY_PRIORITY = 1
        POLICY_CONDITIONS = models.PolicyRuleConditions({
            "clients": models.ClientPolicyCondition({
                "include": ["ALL_CLIENTS"]
            })
        })

        policy_obj = models.Policy({
            "type": POLICY_TYPE,
            "status": POLICY_STATUS,
            "name": POLICY_NAME,
            "description": POLICY_DESC,
            "priority": POLICY_PRIORITY,
            "conditions": POLICY_CONDITIONS
        })

        policy, _, err = await client.create_authorization_server_policy(
            created.id, policy_obj
        )
        assert err is None

        # Get Policy
        found, _, err = await client.get_authorization_server_policy(
            created.id, policy.id
        )
        assert err is None
        assert found.id == policy.id
        assert found.name == policy.name
        assert found.description == policy.description

        # Delete Policy
        _, err = await client.delete_authorization_server_policy(
            created.id, policy.id
        )
        assert err is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(created.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(created.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_auth_server_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Create Policy
        POLICY_TYPE = models.PolicyType.OAUTH_AUTHORIZATION_POLICY
        POLICY_STATUS = "ACTIVE"
        POLICY_NAME = "Test Policy"
        POLICY_DESC = "Test Policy"
        POLICY_PRIORITY = 1
        POLICY_CONDITIONS = models.PolicyRuleConditions({
            "clients": models.ClientPolicyCondition({
                "include": ["ALL_CLIENTS"]
            })
        })

        policy_obj = models.Policy({
            "type": POLICY_TYPE,
            "status": POLICY_STATUS,
            "name": POLICY_NAME,
            "description": POLICY_DESC,
            "priority": POLICY_PRIORITY,
            "conditions": POLICY_CONDITIONS
        })

        policy, _, err = await client.create_authorization_server_policy(
            auth_server.id, policy_obj
        )
        assert err is None

        # Update policy
        UPDATED_NAME = f"{POLICY_NAME}_updated"
        UPDATED_DESC = f"{POLICY_DESC}_updated"
        policy.name = UPDATED_NAME
        policy.description = UPDATED_DESC

        updated, _, err = await client.update_authorization_server_policy(
            auth_server.id, policy.id, policy
        )
        assert err is None
        assert updated.name == UPDATED_NAME
        assert updated.description == UPDATED_DESC

        # Delete Policy
        _, err = await client.delete_authorization_server_policy(
            auth_server.id, policy.id
        )
        assert err is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_auth_server_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        created, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(created, models.AuthorizationServer)
        assert created.name == TEST_NAME
        assert created.description == TEST_DESC
        assert created.audiences == TEST_AUDS
        assert created.audiences[0] == TEST_AUDS[0]

        # Create Policy
        POLICY_TYPE = models.PolicyType.OAUTH_AUTHORIZATION_POLICY
        POLICY_STATUS = "ACTIVE"
        POLICY_NAME = "Test Policy"
        POLICY_DESC = "Test Policy"
        POLICY_PRIORITY = 1
        POLICY_CONDITIONS = models.PolicyRuleConditions({
            "clients": models.ClientPolicyCondition({
                "include": ["ALL_CLIENTS"]
            })
        })

        policy_obj = models.Policy({
            "type": POLICY_TYPE,
            "status": POLICY_STATUS,
            "name": POLICY_NAME,
            "description": POLICY_DESC,
            "priority": POLICY_PRIORITY,
            "conditions": POLICY_CONDITIONS
        })

        policy, _, err = await client.create_authorization_server_policy(
            created.id, policy_obj
        )
        assert err is None

        # Get Policy
        found, _, err = await client.get_authorization_server_policy(
            created.id, policy.id
        )
        assert err is None
        assert found is not None
        assert found.id == policy.id
        assert found.name == policy.name
        assert found.description == policy.description

        # Delete Policy
        _, err = await client.delete_authorization_server_policy(
            created.id, policy.id
        )
        assert err is None

        # Get Policy
        found, resp, err = await client.get_authorization_server_policy(
            created.id, policy.id
        )
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert found is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(created.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(created.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_oauth2_scope(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Create Oauth Scope
        SCOPE_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}:abDGz"
        scope_obj = models.OAuth2Scope({
            "name": SCOPE_NAME
        })

        oauth_scope, _, err = await client.create_o_auth_2_scope(
            auth_server.id, scope_obj
        )
        assert err is None
        assert isinstance(oauth_scope, models.OAuth2Scope)
        assert oauth_scope.name == scope_obj.name

        # Get Oauth Scope
        found, _, err = await client.get_o_auth_2_scope(
            auth_server.id, oauth_scope.id
        )
        assert err is None
        assert found.name == oauth_scope.name

        # Delete Oauth Scope
        _, err = await client.delete_o_auth_2_scope(
            auth_server.id, oauth_scope.id
        )
        assert err is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_oauth2_scopes(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDgZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Create Oauth Scope
        SCOPE_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}:abDGz"
        scope_obj = models.OAuth2Scope({
            "name": SCOPE_NAME
        })

        oauth_scope, _, err = await client.create_o_auth_2_scope(
            auth_server.id, scope_obj
        )
        assert err is None
        assert isinstance(oauth_scope, models.OAuth2Scope)
        assert oauth_scope.name == scope_obj.name

        # List Oauth Scopes
        scopes, _, err = await client.list_o_auth_2_scopes(auth_server.id)
        assert err is None
        assert len(scopes) > 0
        assert next((scope for scope in scopes if scope.id == oauth_scope.id))

        # Delete Oauth Scope
        _, err = await client.delete_o_auth_2_scope(
            auth_server.id, oauth_scope.id
        )
        assert err is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_oauth2_scope(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Create Oauth Scope
        SCOPE_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}:abDHz"
        scope_obj = models.OAuth2Scope({
            "name": SCOPE_NAME,
            "consent": "REQUIRED",
            "metadataPublish": "ALL_CLIENTS"
        })
        UPDATED_SCOPE_NAME = f"{SCOPE_NAME}updated"
        updated_obj = models.OAuth2Scope({
            "name": UPDATED_SCOPE_NAME,
            "consent": "REQUIRED",
            "metadataPublish": "ALL_CLIENTS"
        })

        oauth_scope, _, err = await client.create_o_auth_2_scope(
            auth_server.id, scope_obj
        )
        assert err is None
        assert isinstance(oauth_scope, models.OAuth2Scope)
        assert oauth_scope.name == scope_obj.name

        # Update scope
        updated_scope, _, err = await client.update_o_auth_2_scope(
            auth_server.id, oauth_scope.id, updated_obj
        )
        assert err is None
        assert updated_scope.name == UPDATED_SCOPE_NAME

        # Delete Oauth Scope
        _, err = await client.delete_o_auth_2_scope(
            auth_server.id, oauth_scope.id
        )
        assert err is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_oauth2_scope(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Create Oauth Scope
        SCOPE_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}:abDGz"
        scope_obj = models.OAuth2Scope({
            "name": SCOPE_NAME
        })

        oauth_scope, _, err = await client.create_o_auth_2_scope(
            auth_server.id, scope_obj
        )
        assert err is None
        assert isinstance(oauth_scope, models.OAuth2Scope)
        assert oauth_scope.name == scope_obj.name

        # Get Oauth Scope
        found, _, err = await client.get_o_auth_2_scope(
            auth_server.id, oauth_scope.id
        )
        assert err is None
        assert found.name == oauth_scope.name

        # Delete Oauth Scope
        _, err = await client.delete_o_auth_2_scope(
            auth_server.id, oauth_scope.id
        )
        assert err is None

        # Get Oauth Scope
        found, resp, err = await client.get_o_auth_2_scope(
            auth_server.id, oauth_scope.id
        )
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_oauth2_claim(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Create Oauth Claim
        CLAIM_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_abeIz"
        CLAIM_STATUS = "INACTIVE"
        CLAIM_TYPE = "RESOURCE"
        CLAIM_VALUE_TYPE = "EXPRESSION"
        CLAIM_VALUE = "\"driving!\""
        claim_obj = models.OAuth2Claim({
            "name": CLAIM_NAME,
            "status": CLAIM_STATUS,
            "claimType": CLAIM_TYPE,
            "valueType": CLAIM_VALUE_TYPE,
            "value": CLAIM_VALUE
        })

        oauth_claim, _, err = await client.create_o_auth_2_claim(
            auth_server.id, claim_obj
        )
        assert err is None
        assert isinstance(oauth_claim, models.OAuth2Claim)
        assert oauth_claim.name == CLAIM_NAME

        # Get Oauth claim
        found, _, err = await client.get_o_auth_2_claim(
            auth_server.id, oauth_claim.id
        )
        assert err is None
        assert found.name == oauth_claim.name

        # Delete Oauth claim
        _, err = await client.delete_o_auth_2_claim(
            auth_server.id, oauth_claim.id
        )
        assert err is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_oauth2_claims(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Create Oauth Claim
        CLAIM_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_abeIz"
        CLAIM_STATUS = "INACTIVE"
        CLAIM_TYPE = "RESOURCE"
        CLAIM_VALUE_TYPE = "EXPRESSION"
        CLAIM_VALUE = "\"driving!\""
        claim_obj = models.OAuth2Claim({
            "name": CLAIM_NAME,
            "status": CLAIM_STATUS,
            "claimType": CLAIM_TYPE,
            "valueType": CLAIM_VALUE_TYPE,
            "value": CLAIM_VALUE
        })

        oauth_claim, _, err = await client.create_o_auth_2_claim(
            auth_server.id, claim_obj
        )
        assert err is None
        assert isinstance(oauth_claim, models.OAuth2Claim)
        assert oauth_claim.name == CLAIM_NAME

        # List Oauth claims
        claims, _, err = await client.list_o_auth_2_claims(auth_server.id)
        assert err is None
        assert next((claim for claim in claims if claim.id == oauth_claim.id))

        # Delete Oauth claim
        _, err = await client.delete_o_auth_2_claim(
            auth_server.id, oauth_claim.id
        )
        assert err is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_oauth2_claim(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Create Oauth Claim
        CLAIM_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_abeIz"
        CLAIM_STATUS = "INACTIVE"
        CLAIM_TYPE = "RESOURCE"
        CLAIM_VALUE_TYPE = "EXPRESSION"
        CLAIM_VALUE = "\"driving!\""
        claim_obj = models.OAuth2Claim({
            "name": CLAIM_NAME,
            "status": CLAIM_STATUS,
            "claimType": CLAIM_TYPE,
            "valueType": CLAIM_VALUE_TYPE,
            "value": CLAIM_VALUE
        })
        UPDATED_CLAIM_NAME = f"{CLAIM_NAME}_updated"
        updated_obj = models.OAuth2Claim({
            "name": UPDATED_CLAIM_NAME,
            "status": CLAIM_STATUS,
            "claimType": CLAIM_TYPE,
            "valueType": CLAIM_VALUE_TYPE,
            "value": CLAIM_VALUE
        })

        oauth_claim, _, err = await client.create_o_auth_2_claim(
            auth_server.id, claim_obj
        )
        assert err is None
        assert isinstance(oauth_claim, models.OAuth2Claim)
        assert oauth_claim.name == CLAIM_NAME

        # Update claim
        updated_claim, _, err = await client.update_o_auth_2_claim(
            auth_server.id, oauth_claim.id, updated_obj
        )
        assert err is None
        assert isinstance(oauth_claim, models.OAuth2Claim)
        assert updated_claim.name == UPDATED_CLAIM_NAME

        # Get Oauth claim
        found, _, err = await client.get_o_auth_2_claim(
            auth_server.id, oauth_claim.id
        )
        assert err is None
        assert found.name == UPDATED_CLAIM_NAME

        # Delete Oauth claim
        _, err = await client.delete_o_auth_2_claim(
            auth_server.id, oauth_claim.id
        )
        assert err is None

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_oauth2_claim(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Create Oauth Claim
        CLAIM_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_abeIz"
        CLAIM_STATUS = "INACTIVE"
        CLAIM_TYPE = "RESOURCE"
        CLAIM_VALUE_TYPE = "EXPRESSION"
        CLAIM_VALUE = "\"driving!\""
        claim_obj = models.OAuth2Claim({
            "name": CLAIM_NAME,
            "status": CLAIM_STATUS,
            "claimType": CLAIM_TYPE,
            "valueType": CLAIM_VALUE_TYPE,
            "value": CLAIM_VALUE
        })

        oauth_claim, _, err = await client.create_o_auth_2_claim(
            auth_server.id, claim_obj
        )
        assert err is None
        assert isinstance(oauth_claim, models.OAuth2Claim)
        assert oauth_claim.name == CLAIM_NAME

        # Get Oauth claim
        found, _, err = await client.get_o_auth_2_claim(
            auth_server.id, oauth_claim.id
        )
        assert err is None
        assert found.name == oauth_claim.name

        # Delete Oauth claim
        _, err = await client.delete_o_auth_2_claim(
            auth_server.id, oauth_claim.id
        )
        assert err is None

        # Get Oauth claim
        found, resp, err = await client.get_o_auth_2_claim(
            auth_server.id, oauth_claim.id
        )
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_auth_server_keys(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # List keys
        auth_server_keys, _, err = await client.list_authorization_server_keys(
            auth_server.id
        )
        assert err is None
        assert len(auth_server_keys) > 0

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_rotate_auth_server_keys(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Auth Server
        TEST_NAME = f"{TestAuthorizationServerResource.SDK_PREFIX}_test_abDfZ"
        TEST_DESC = "Test Auth Server"
        TEST_AUDS = ["api://default"]
        auth_server_obj = models.AuthorizationServer({
            "name": TEST_NAME,
            "description": TEST_DESC,
            "audiences": TEST_AUDS
        })

        auth_server, _, err = await \
            client.create_authorization_server(auth_server_obj)
        assert err is None
        assert isinstance(auth_server, models.AuthorizationServer)
        assert auth_server.name == TEST_NAME
        assert auth_server.description == TEST_DESC
        assert auth_server.audiences == TEST_AUDS
        assert auth_server.audiences[0] == TEST_AUDS[0]

        # Make key to rotate
        rotate_key = models.JwkUse({
            "use": "sig"
        })

        # Rotate key
        keys, _, err = await client.rotate_authorization_server_keys(
            auth_server.id, rotate_key
        )
        assert err is None
        assert len(keys) > 0

        # DeActivate Auth server
        _, err = await client.deactivate_authorization_server(auth_server.id)
        assert err is None
        # Delete Auth server
        _, err = await client.delete_authorization_server(auth_server.id)
        assert err is None
