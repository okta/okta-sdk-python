# GroupSchemaDefinitions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**GroupSchemaBase**](GroupSchemaBase.md) |  | [optional] 
**custom** | [**GroupSchemaCustom**](GroupSchemaCustom.md) |  | [optional] 

## Example

```python
from openapi_client.models.group_schema_definitions import GroupSchemaDefinitions

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchemaDefinitions from a JSON string
group_schema_definitions_instance = GroupSchemaDefinitions.from_json(json)
# print the JSON string representation of the object
print(GroupSchemaDefinitions.to_json())

# convert the object into a dict
group_schema_definitions_dict = group_schema_definitions_instance.to_dict()
# create an instance of GroupSchemaDefinitions from a dict
group_schema_definitions_from_dict = GroupSchemaDefinitions.from_dict(group_schema_definitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


