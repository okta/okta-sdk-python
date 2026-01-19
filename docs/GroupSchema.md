# GroupSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | JSON schema version identifier | [optional] [readonly] 
**created** | **str** | Timestamp when the schema was created | [optional] [readonly] 
**definitions** | [**GroupSchemaDefinitions**](GroupSchemaDefinitions.md) |  | [optional] 
**description** | **str** | Description for the schema | [optional] 
**id** | **str** | URI of group schema | [optional] [readonly] 
**last_updated** | **str** | Timestamp when the schema was last updated | [optional] [readonly] 
**name** | **str** | Name of the schema | [optional] [readonly] 
**properties** | [**UserSchemaProperties**](UserSchemaProperties.md) |  | [optional] 
**title** | **str** | User-defined display name for the schema | [optional] 
**type** | **str** | Type of [root schema](https://tools.ietf.org/html/draft-zyp-json-schema-04#section-3.4) | [optional] [readonly] 
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


