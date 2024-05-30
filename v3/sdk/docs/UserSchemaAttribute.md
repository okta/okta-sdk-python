# UserSchemaAttribute


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
**pattern** | **str** |  | [optional] 
**permissions** | [**List[UserSchemaAttributePermission]**](UserSchemaAttributePermission.md) |  | [optional] 
**required** | **bool** |  | [optional] 
**scope** | [**UserSchemaAttributeScope**](UserSchemaAttributeScope.md) |  | [optional] 
**title** | **str** |  | [optional] 
**type** | [**UserSchemaAttributeType**](UserSchemaAttributeType.md) |  | [optional] 
**union** | [**UserSchemaAttributeUnion**](UserSchemaAttributeUnion.md) |  | [optional] 
**unique** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_schema_attribute import UserSchemaAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaAttribute from a JSON string
user_schema_attribute_instance = UserSchemaAttribute.from_json(json)
# print the JSON string representation of the object
print(UserSchemaAttribute.to_json())

# convert the object into a dict
user_schema_attribute_dict = user_schema_attribute_instance.to_dict()
# create an instance of UserSchemaAttribute from a dict
user_schema_attribute_form_dict = user_schema_attribute.from_dict(user_schema_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


