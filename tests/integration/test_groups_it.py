import pytest
from tests.mocks import MockOktaClient
from http import HTTPStatus
import okta.models as models


class TestGroupsResource:
    """
    Integration Tests for the Groups Resource
    """

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_create_get_group(self, fs):
        # Instantiate Mock Client
        client = MockOktaClient()

        # Create Group Object
        GROUP_NAME = "Group-Target-Test"
        group_profile = models.GroupProfile({
            "name": GROUP_NAME
        })
        group_obj = models.Group({
            "profile": group_profile
        })

        # Create Group
        group, _, err = await client.create_group(group_obj)
        assert err is None
        assert isinstance(group, models.Group)

        found_group, _, err = await client.get_group(group.id)
        assert err is None
        assert found_group.id == group.id

        _, err = await client.delete_group(group.id)
        assert err is None

        found_group, resp, err = await client.get_group(group.id)
        assert err is not None
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert found_group is None
