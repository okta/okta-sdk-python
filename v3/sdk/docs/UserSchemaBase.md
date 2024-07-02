# UserSchemaBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**properties** | [**UserSchemaBaseProperties**](UserSchemaBaseProperties.md) |  | [optional] 
**required** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_schema_base import UserSchemaBase

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaBase from a JSON string
user_schema_base_instance = UserSchemaBase.from_json(json)
# print the JSON string representation of the object
print(UserSchemaBase.to_json())

# convert the object into a dict
user_schema_base_dict = user_schema_base_instance.to_dict()
# create an instance of UserSchemaBase from a dict
user_schema_base_from_dict = UserSchemaBase.from_dict(user_schema_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


