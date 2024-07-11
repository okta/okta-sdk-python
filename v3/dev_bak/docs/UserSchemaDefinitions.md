# UserSchemaDefinitions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**UserSchemaBase**](UserSchemaBase.md) |  | [optional] 
**custom** | [**UserSchemaPublic**](UserSchemaPublic.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_schema_definitions import UserSchemaDefinitions

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaDefinitions from a JSON string
user_schema_definitions_instance = UserSchemaDefinitions.from_json(json)
# print the JSON string representation of the object
print(UserSchemaDefinitions.to_json())

# convert the object into a dict
user_schema_definitions_dict = user_schema_definitions_instance.to_dict()
# create an instance of UserSchemaDefinitions from a dict
user_schema_definitions_from_dict = UserSchemaDefinitions.from_dict(user_schema_definitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


