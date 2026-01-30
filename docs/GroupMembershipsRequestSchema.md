# GroupMembershipsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_external_ids** | **List[str]** | A list of app user external IDs to be inserted in this group in Okta | [optional] 

## Example

```python
from okta.models.group_memberships_request_schema import GroupMembershipsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembershipsRequestSchema from a JSON string
group_memberships_request_schema_instance = GroupMembershipsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GroupMembershipsRequestSchema.to_json())

# convert the object into a dict
group_memberships_request_schema_dict = group_memberships_request_schema_instance.to_dict()
# create an instance of GroupMembershipsRequestSchema from a dict
group_memberships_request_schema_from_dict = GroupMembershipsRequestSchema.from_dict(group_memberships_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


