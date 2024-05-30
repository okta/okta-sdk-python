import pytest
from tests.mocks import MockOktaClient
import okta.models as models
from http import HTTPStatus
from okta.errors.okta_api_error import OktaAPIError


class TestUserSchemaResource:
    """
    Integration Tests for the User Schema Resource
    """
    SDK_PREFIX = "python_sdk"

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_user_schema(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        # Get User Schema
        user_schema, resp, err = await client.get_user_schema('default')
        assert err is None

        # Validate schema attributes
        assert user_schema.definitions.base.id == '#base'
        assert user_schema.definitions.base.type == 'object'
        assert 'login' in user_schema.definitions.base.required
        assert user_schema.definitions.base.properties.login.title == 'Username'
        assert user_schema.definitions.base.properties.login.type == 'string'
        assert user_schema.definitions.base.properties.login.required is True
        assert user_schema.definitions.base.properties.login.mutability == 'READ_WRITE'
        assert user_schema.definitions.base.properties.login.scope == 'NONE'
        assert user_schema.definitions.base.properties.login.min_length == 5
        assert user_schema.definitions.base.properties.login.max_length == 100
        assert user_schema.definitions.base.properties.login.permissions[0].principal == 'SELF'
        assert user_schema.definitions.base.properties.login.permissions[0].action == 'READ_ONLY'

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_update_user_profile(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient(fs)

        try:
            # Get User Schema
            user_schema, _, err = await client.get_user_schema("default")
            assert err is None

            # Add custom attribute
            attr_config = {
                'title': 'Test Custom User Attribute',
                'type': 'string',
                'description': 'test custom user attribute',
                'minLength': 1,
                'maxLength': 20,
                'permissions': [models.UserSchemaAttributePermission({
                                   'action': 'READ_WRITE',
                                   'principal': 'SELF'
                               })]
            }

            custom_attr = models.UserSchemaAttribute(attr_config)
            user_schema.definitions.custom.properties = {'testCustomAttribute': custom_attr.as_dict()}

            # Update user schema
            updated_user_schema, _, err = await client.update_user_profile('default', user_schema)
            assert err is None

            # Check custom attribute
            assert updated_user_schema.definitions.custom.properties['testCustomAttribute']['title'] == 'Test Custom User Attribute'
        finally:
            errors = []
            try:
                # Remove custom attribute
                updated_user_schema.definitions.custom.properties['testCustomAttribute'] = None
                # Update user schema
                updated_user_schema, _, err = await client.update_user_profile('default', updated_user_schema)
                assert err is None
            except Exception as exc:
                errors.append(exc)

            assert len(errors) == 0
