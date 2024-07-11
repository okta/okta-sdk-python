# GroupSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] [readonly] 
**created** | **str** |  | [optional] [readonly] 
**definitions** | [**GroupSchemaDefinitions**](GroupSchemaDefinitions.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**properties** | [**UserSchemaProperties**](UserSchemaProperties.md) |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.group_schema import GroupSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchema from a JSON string
group_schema_instance = GroupSchema.from_json(json)
# print the JSON string representation of the object
print(GroupSchema.to_json())

# convert the object into a dict
group_schema_dict = group_schema_instance.to_dict()
# create an instance of GroupSchema from a dict
group_schema_from_dict = GroupSchema.from_dict(group_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


