import pytest
import okta.models as models
from tests.mocks import MockOktaClient


"""
Testing Okta Models Instantiation in different scenarios
"""


@pytest.mark.vcr()
@pytest.mark.asyncio
@ pytest.mark.parametrize("group_obj",
                          [
                              {  # No Okta Model included
                                  'profile': {
                                      'name': 'GroupName',
                                      'description': 'Group Description'
                                  }
                              },
                              models.Group({  # Parent Okta model included
                                  "profile": {
                                      'name': 'GroupName',
                                      'description': 'Group Description'
                                  }
                              }),
                              models.Group({  # Parent + Nested models included
                                  "profile": models.GroupProfile({
                                      "name": "GroupName",
                                      "description": "Group Description"
                                  })
                              })
                          ])
async def test_create_group_different_inputs(fs, group_obj):
    # Instantiate Mock Client
    client = MockOktaClient(fs)

    # Create Group
    group, _, err = await client.create_group(group_obj)
    assert err is None
    assert isinstance(group, models.Group)
    if isinstance(group_obj, dict):
        assert group.profile.name == group_obj["profile"]["name"]
        assert group.profile.description == group_obj["profile"]["description"]
    else:
        assert group.profile.name == group_obj.profile.name
        assert group.profile.description == group_obj.profile.description

    # Delete created group
    _, err = await client.delete_group(group.id)
    assert err is None
