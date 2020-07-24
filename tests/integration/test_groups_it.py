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

        # Get group using ID
        found_group, _, err = await client.get_group(group.id)
        assert err is None
        assert found_group.id == group.id

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None

        # Ensure group cannot be found again
        found_group, resp, err = await client.get_group(group.id)
        assert err is not None
        assert resp.get_status() == HTTPStatus.NOT_FOUND
        assert found_group is None

    @pytest.mark.vcr()
    @pytest.mark.asyncio
    async def test_list_groups(self, fs):
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

        groups_list, resp, err = await client.list_groups()
        assert err is None
        assert not resp.has_next()
        assert next((grp for grp in groups_list if grp.id == group.id))

        # Delete created group
        _, err = await client.delete_group(group.id)
        assert err is None
