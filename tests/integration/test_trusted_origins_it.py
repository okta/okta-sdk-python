import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError


class TestTrustedOriginsResource:
    """
    Integration Tests for the Trusted Origins Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_origin(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Trusted Origin
        TO_NAME = f"{TestTrustedOriginsResource.SDK_PREFIX}_test_TO"
        TO_ORIGIN = "http://example.com"
        trusted_origin_model = models.TrustedOrigin({
            "name": TO_NAME,
            "origin": TO_ORIGIN,
            "scopes": [
                models.Scope({
                    "type": models.ScopeType.CORS
                }),
                models.Scope({
                    "type": models.ScopeType.REDIRECT
                }),
            ]
        })

        created_trusted_origin, _, err = await \
            client.create_origin(trusted_origin_model)
        assert err is None
        assert isinstance(created_trusted_origin, models.TrustedOrigin)

        # Retrieve
        retrieved_origin, _, err = await \
            client.get_origin(created_trusted_origin.id)
        assert err is None
        assert isinstance(retrieved_origin, models.TrustedOrigin)
        assert retrieved_origin.name == created_trusted_origin.name
        assert len(retrieved_origin.scopes) == 2

        # Delete
        _, err = await client.delete_origin(created_trusted_origin.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_origins(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Trusted Origin
        TO_NAME = f"{TestTrustedOriginsResource.SDK_PREFIX}_test_TO"
        TO_ORIGIN = "http://example.com"
        trusted_origin_model = models.TrustedOrigin({
            "name": TO_NAME,
            "origin": TO_ORIGIN,
            "scopes": [
                models.Scope({
                    "type": models.ScopeType.CORS
                }),
                models.Scope({
                    "type": models.ScopeType.REDIRECT
                }),
            ]
        })

        created_trusted_origin, _, err = await \
            client.create_origin(trusted_origin_model)
        assert err is None
        assert isinstance(created_trusted_origin, models.TrustedOrigin)

        # List
        trusted_origins, _, err = await client.list_origins()
        assert err is None
        assert isinstance(trusted_origins, list)
        assert len(trusted_origins) > 0
        assert isinstance(trusted_origins[0], models.TrustedOrigin)
        assert next((to for to in trusted_origins
                     if to.name == created_trusted_origin.name), None) \
            is not None

        # Delete
        _, err = await client.delete_origin(created_trusted_origin.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_delete_origin(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Trusted Origin
        TO_NAME = f"{TestTrustedOriginsResource.SDK_PREFIX}_test_TO"
        TO_ORIGIN = "http://example.com"
        trusted_origin_model = models.TrustedOrigin({
            "name": TO_NAME,
            "origin": TO_ORIGIN,
            "scopes": [
                models.Scope({
                    "type": models.ScopeType.CORS
                }),
                models.Scope({
                    "type": models.ScopeType.REDIRECT
                }),
            ]
        })

        created_trusted_origin, _, err = await \
            client.create_origin(trusted_origin_model)
        assert err is None
        assert isinstance(created_trusted_origin, models.TrustedOrigin)

        # Retrieve
        retrieved_origin, _, err = await \
            client.get_origin(created_trusted_origin.id)
        assert err is None
        assert isinstance(retrieved_origin, models.TrustedOrigin)
        assert retrieved_origin.name == created_trusted_origin.name
        assert len(retrieved_origin.scopes) == 2

        # Delete
        _, err = await client.delete_origin(created_trusted_origin.id)

        # Retrieve to validate
        retrieved_origin, resp, err = await \
            client.get_origin(created_trusted_origin.id)
        assert err is not None
        assert isinstance(err, OktaAPIError)
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert retrieved_origin is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_origin(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Trusted Origin
        TO_NAME = f"{TestTrustedOriginsResource.SDK_PREFIX}_test_TO"
        TO_ORIGIN = "http://example.com"
        trusted_origin_model = models.TrustedOrigin({
            "name": TO_NAME,
            "origin": TO_ORIGIN,
            "scopes": [
                models.Scope({
                    "type": models.ScopeType.CORS
                }),
                models.Scope({
                    "type": models.ScopeType.REDIRECT
                }),
            ]
        })

        created_trusted_origin, _, err = await \
            client.create_origin(trusted_origin_model)
        assert err is None
        assert isinstance(created_trusted_origin, models.TrustedOrigin)

        # Retrieve
        retrieved_origin, _, err = await \
            client.get_origin(created_trusted_origin.id)
        assert err is None
        assert isinstance(retrieved_origin, models.TrustedOrigin)
        assert retrieved_origin.name == created_trusted_origin.name
        assert len(retrieved_origin.scopes) == 2

        # Update
        updated_trusted_origin_model = models.TrustedOrigin({
            "name": TO_NAME + "_updated",
            "origin": TO_ORIGIN,
            "scopes": [
                models.Scope({
                    "type": models.ScopeType.CORS
                }),
                models.Scope({
                    "type": models.ScopeType.REDIRECT
                }),
            ]
        })
        updated_origin, _, err = await \
            client.update_origin(created_trusted_origin.id,
                                 updated_trusted_origin_model)
        assert err is None
        assert isinstance(updated_origin, models.TrustedOrigin)
        assert updated_origin.id == created_trusted_origin.id
        assert updated_origin.name == updated_trusted_origin_model.name

        # Retrieve to validate
        retrieved_origin, resp, err = await \
            client.get_origin(created_trusted_origin.id)
        assert retrieved_origin.id == created_trusted_origin.id
        assert retrieved_origin.name == updated_origin.name

        # Delete
        _, err = await client.delete_origin(created_trusted_origin.id)

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_deactivate_origin(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Create Trusted Origin
        TO_NAME = f"{TestTrustedOriginsResource.SDK_PREFIX}_test_TO"
        TO_ORIGIN = "http://example.com"
        trusted_origin_model = models.TrustedOrigin({
            "name": TO_NAME,
            "origin": TO_ORIGIN,
            "scopes": [
                models.Scope({
                    "type": models.ScopeType.CORS
                }),
                models.Scope({
                    "type": models.ScopeType.REDIRECT
                }),
            ]
        })

        created_trusted_origin, _, err = await \
            client.create_origin(trusted_origin_model)
        assert err is None
        assert isinstance(created_trusted_origin, models.TrustedOrigin)
        assert created_trusted_origin.status == "ACTIVE"

        # Deactivate
        deactivated_origin, _, err = await \
            client.deactivate_origin(created_trusted_origin.id)
        assert err is None
        assert deactivated_origin.status == "INACTIVE"

        # Retrieve to validate
        retrieved_origin, resp, err = await \
            client.get_origin(created_trusted_origin.id)
        assert retrieved_origin.id == created_trusted_origin.id
        assert retrieved_origin.status == "INACTIVE"

        # Reactivate
        reactivated_origin, _, err = await \
            client.activate_origin(created_trusted_origin.id)
        assert err is None
        assert reactivated_origin.status == "ACTIVE"

        # Retrieve to validate
        retrieved_origin, resp, err = await \
            client.get_origin(created_trusted_origin.id)
        assert retrieved_origin.id == created_trusted_origin.id
        assert retrieved_origin.status == "ACTIVE"

        # Delete
        _, err = await client.delete_origin(created_trusted_origin.id)
