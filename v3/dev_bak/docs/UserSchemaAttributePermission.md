# UserSchemaAttributePermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_schema_attribute_permission import UserSchemaAttributePermission

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaAttributePermission from a JSON string
user_schema_attribute_permission_instance = UserSchemaAttributePermission.from_json(json)
# print the JSON string representation of the object
print(UserSchemaAttributePermission.to_json())

# convert the object into a dict
user_schema_attribute_permission_dict = user_schema_attribute_permission_instance.to_dict()
# create an instance of UserSchemaAttributePermission from a dict
user_schema_attribute_permission_from_dict = UserSchemaAttributePermission.from_dict(user_schema_attribute_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


