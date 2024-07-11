# UserSchemaAttributeItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enum** | **List[str]** |  | [optional] 
**one_of** | [**List[UserSchemaAttributeEnum]**](UserSchemaAttributeEnum.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_schema_attribute_items import UserSchemaAttributeItems

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaAttributeItems from a JSON string
user_schema_attribute_items_instance = UserSchemaAttributeItems.from_json(json)
# print the JSON string representation of the object
print(UserSchemaAttributeItems.to_json())

# convert the object into a dict
user_schema_attribute_items_dict = user_schema_attribute_items_instance.to_dict()
# create an instance of UserSchemaAttributeItems from a dict
user_schema_attribute_items_from_dict = UserSchemaAttributeItems.from_dict(user_schema_attribute_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


