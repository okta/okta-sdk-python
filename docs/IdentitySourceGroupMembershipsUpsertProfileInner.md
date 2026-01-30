# IdentitySourceGroupMembershipsUpsertProfileInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_external_id** | **str** | The external ID of the group whose memberships need to be inserted or updated in Okta | [optional] 
**member_external_ids** | **List[str]** | Array of external IDs of member profiles that need to be inserted in this group in Okta | [optional] 

## Example

```python
from okta.models.identity_source_group_memberships_upsert_profile_inner import IdentitySourceGroupMembershipsUpsertProfileInner

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitySourceGroupMembershipsUpsertProfileInner from a JSON string
identity_source_group_memberships_upsert_profile_inner_instance = IdentitySourceGroupMembershipsUpsertProfileInner.from_json(json)
# print the JSON string representation of the object
print(IdentitySourceGroupMembershipsUpsertProfileInner.to_json())

# convert the object into a dict
identity_source_group_memberships_upsert_profile_inner_dict = identity_source_group_memberships_upsert_profile_inner_instance.to_dict()
# create an instance of IdentitySourceGroupMembershipsUpsertProfileInner from a dict
identity_source_group_memberships_upsert_profile_inner_from_dict = IdentitySourceGroupMembershipsUpsertProfileInner.from_dict(identity_source_group_memberships_upsert_profile_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


