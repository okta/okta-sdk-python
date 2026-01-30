# GroupSchemaBaseProperties

All Okta-defined profile properties are defined in a profile subschema with the resolution scope `#base`. These properties can't be removed or edited, regardless of any attempt to do so.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**GroupSchemaAttribute**](GroupSchemaAttribute.md) | Human readable description of the group | [optional] 
**name** | [**GroupSchemaAttribute**](GroupSchemaAttribute.md) | Unique identifier for the group | [optional] 

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


