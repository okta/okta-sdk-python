# GroupSchemaBaseProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**GroupSchemaAttribute**](GroupSchemaAttribute.md) |  | [optional] 
**name** | [**GroupSchemaAttribute**](GroupSchemaAttribute.md) |  | [optional] 

## Example

```python
from okta.models.group_schema_base_properties import GroupSchemaBaseProperties

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchemaBaseProperties from a JSON string
group_schema_base_properties_instance = GroupSchemaBaseProperties.from_json(json)
# print the JSON string representation of the object
print(GroupSchemaBaseProperties.to_json())

# convert the object into a dict
group_schema_base_properties_dict = group_schema_base_properties_instance.to_dict()
# create an instance of GroupSchemaBaseProperties from a dict
group_schema_base_properties_from_dict = GroupSchemaBaseProperties.from_dict(group_schema_base_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


