# GroupMembershipsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_external_ids** | **List[str]** | A list of app user external IDs that are members of the group in Okta | [optional] 

## Example

```python
from okta.models.group_memberships_response_schema import GroupMembershipsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembershipsResponseSchema from a JSON string
group_memberships_response_schema_instance = GroupMembershipsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GroupMembershipsResponseSchema.to_json())

# convert the object into a dict
group_memberships_response_schema_dict = group_memberships_response_schema_instance.to_dict()
# create an instance of GroupMembershipsResponseSchema from a dict
group_memberships_response_schema_from_dict = GroupMembershipsResponseSchema.from_dict(group_memberships_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


