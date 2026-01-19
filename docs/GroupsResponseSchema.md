# GroupsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The external ID of the identity source group | [optional] 
**id** | **str** | The Okta group ID of the identity source group | [optional] [readonly] 
**profile** | [**GroupsResponseSchemaProfile**](GroupsResponseSchemaProfile.md) |  | [optional] 

## Example

```python
from okta.models.groups_response_schema import GroupsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsResponseSchema from a JSON string
groups_response_schema_instance = GroupsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GroupsResponseSchema.to_json())

# convert the object into a dict
groups_response_schema_dict = groups_response_schema_instance.to_dict()
# create an instance of GroupsResponseSchema from a dict
groups_response_schema_from_dict = GroupsResponseSchema.from_dict(groups_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


