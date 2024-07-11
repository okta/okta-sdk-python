# GroupSchemaAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**enum** | **List[str]** |  | [optional] 
**external_name** | **str** |  | [optional] 
**external_namespace** | **str** |  | [optional] 
**items** | [**UserSchemaAttributeItems**](UserSchemaAttributeItems.md) |  | [optional] 
**master** | [**UserSchemaAttributeMaster**](UserSchemaAttributeMaster.md) |  | [optional] 
**max_length** | **int** |  | [optional] 
**min_length** | **int** |  | [optional] 
**mutability** | **str** |  | [optional] 
**one_of** | [**List[UserSchemaAttributeEnum]**](UserSchemaAttributeEnum.md) |  | [optional] 
**permissions** | [**List[UserSchemaAttributePermission]**](UserSchemaAttributePermission.md) |  | [optional] 
**required** | **bool** |  | [optional] 
**scope** | [**UserSchemaAttributeScope**](UserSchemaAttributeScope.md) |  | [optional] 
**title** | **str** |  | [optional] 
**type** | [**UserSchemaAttributeType**](UserSchemaAttributeType.md) |  | [optional] 
**union** | [**UserSchemaAttributeUnion**](UserSchemaAttributeUnion.md) |  | [optional] 
**unique** | **str** |  | [optional] 

## Example

```python
from okta.models.group_schema_attribute import GroupSchemaAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSchemaAttribute from a JSON string
group_schema_attribute_instance = GroupSchemaAttribute.from_json(json)
# print the JSON string representation of the object
print(GroupSchemaAttribute.to_json())

# convert the object into a dict
group_schema_attribute_dict = group_schema_attribute_instance.to_dict()
# create an instance of GroupSchemaAttribute from a dict
group_schema_attribute_from_dict = GroupSchemaAttribute.from_dict(group_schema_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


