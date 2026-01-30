# GroupsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The external ID of the identity source group to be created | [optional] 
**profile** | [**IdentitySourceGroupProfileForUpsert**](IdentitySourceGroupProfileForUpsert.md) |  | [optional] 

## Example

```python
from okta.models.groups_request_schema import GroupsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsRequestSchema from a JSON string
groups_request_schema_instance = GroupsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GroupsRequestSchema.to_json())

# convert the object into a dict
groups_request_schema_dict = groups_request_schema_instance.to_dict()
# create an instance of GroupsRequestSchema from a dict
groups_request_schema_from_dict = GroupsRequestSchema.from_dict(groups_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


