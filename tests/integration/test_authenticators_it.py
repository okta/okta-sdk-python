import pytest
from tests.mocks import MockOktaClient
import okta.models as models


class TestAuthenticatorsResource:
    """
    Integration Tests for the Authenticators Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_authenticators(self, fs):
        client = MockOktaClient(fs)
        resp, _, err = await client.list_authenticators()
        assert err is None
        assert len(resp) > 0
        assert all([isinstance(elem, models.Authenticator) for elem in resp])
        assert all([isinstance(elem.type, models.AuthenticatorType) for elem in resp])

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_get_authenticator(self, fs):
        client = MockOktaClient(fs)
        authenticators_list, _, err = await client.list_authenticators()
        assert err is None

        resp, _, err = await client.get_authenticator(authenticators_list[0].id)
        assert err is None
        assert isinstance(resp, models.Authenticator)
        assert resp.as_dict() == authenticators_list[0].as_dict()

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_activate_and_deactivate_authenticator(self, fs):
        client = MockOktaClient(fs)
        authenticators_list, _, err = await client.list_authenticators()
        assert err is None

        app_authenticator = [a for a in authenticators_list if a.type == 'phone'][0]
        try:
            _, err = await client.activate_authenticator(app_authenticator.id)
            assert err is None
        finally:
            _, err = await client.deactivate_authenticator(app_authenticator.id)
            assert err is None
