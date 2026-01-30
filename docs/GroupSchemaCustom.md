# GroupSchemaCustom

All custom profile properties are defined in a profile subschema with the resolution scope `#custom`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The subschema name | [optional] [readonly] 
**properties** | [**Dict[str, GroupSchemaAttribute]**](GroupSchemaAttribute.md) | The &#x60;#custom&#x60; object properties | [optional] 
**required** | **List[str]** | A collection indicating required property names | [optional] [readonly] 
**type** | **str** | The object type | [optional] [readonly] 

## Example

```python
from okta.models.group_schema_custom import GroupSchemaCustom

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchemaCustom from a JSON string
group_schema_custom_instance = GroupSchemaCustom.from_json(json)
# print the JSON string representation of the object
print(GroupSchemaCustom.to_json())

# convert the object into a dict
group_schema_custom_dict = group_schema_custom_instance.to_dict()
# create an instance of GroupSchemaCustom from a dict
group_schema_custom_from_dict = GroupSchemaCustom.from_dict(group_schema_custom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


