# GroupSchemaBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The subschema name | [optional] [readonly] 
**properties** | [**GroupSchemaBaseProperties**](GroupSchemaBaseProperties.md) | The &#x60;#base&#x60; object properties | [optional] 
**required** | **List[str]** | A collection indicating required property names | [optional] [readonly] 
**type** | **str** | The object type | [optional] [readonly] 

## Example

```python
from okta.models.group_schema_base import GroupSchemaBase

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchemaBase from a JSON string
group_schema_base_instance = GroupSchemaBase.from_json(json)
# print the JSON string representation of the object
print(GroupSchemaBase.to_json())

# convert the object into a dict
group_schema_base_dict = group_schema_base_instance.to_dict()
# create an instance of GroupSchemaBase from a dict
group_schema_base_from_dict = GroupSchemaBase.from_dict(group_schema_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


