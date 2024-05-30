# UserSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] [readonly] 
**created** | **str** |  | [optional] [readonly] 
**definitions** | [**UserSchemaDefinitions**](UserSchemaDefinitions.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**properties** | [**UserSchemaProperties**](UserSchemaProperties.md) |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.user_schema import UserSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchema from a JSON string
user_schema_instance = UserSchema.from_json(json)
# print the JSON string representation of the object
print(UserSchema.to_json())

# convert the object into a dict
user_schema_dict = user_schema_instance.to_dict()
# create an instance of UserSchema from a dict
user_schema_form_dict = user_schema.from_dict(user_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


