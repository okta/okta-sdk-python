# UserSchemaAttributeEnum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**const** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from okta.models.user_schema_attribute_enum import UserSchemaAttributeEnum

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaAttributeEnum from a JSON string
user_schema_attribute_enum_instance = UserSchemaAttributeEnum.from_json(json)
# print the JSON string representation of the object
print(UserSchemaAttributeEnum.to_json())

# convert the object into a dict
user_schema_attribute_enum_dict = user_schema_attribute_enum_instance.to_dict()
# create an instance of UserSchemaAttributeEnum from a dict
user_schema_attribute_enum_from_dict = UserSchemaAttributeEnum.from_dict(user_schema_attribute_enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


