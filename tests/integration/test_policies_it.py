import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError
from okta.client import Client


class TestPoliciesResource:
    """
    Integration Tests for the Policies Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_sign_on_policy(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

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
