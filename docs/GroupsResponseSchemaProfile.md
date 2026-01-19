# GroupsResponseSchemaProfile

The profile information of the group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**IdentitySourceGroupProfileForUpsert**](IdentitySourceGroupProfileForUpsert.md) |  | [optional] 

## Example

```python
from okta.models.groups_response_schema_profile import GroupsResponseSchemaProfile

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsResponseSchemaProfile from a JSON string
groups_response_schema_profile_instance = GroupsResponseSchemaProfile.from_json(json)
# print the JSON string representation of the object
print(GroupsResponseSchemaProfile.to_json())

# convert the object into a dict
groups_response_schema_profile_dict = groups_response_schema_profile_instance.to_dict()
# create an instance of GroupsResponseSchemaProfile from a dict
groups_response_schema_profile_from_dict = GroupsResponseSchemaProfile.from_dict(groups_response_schema_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


