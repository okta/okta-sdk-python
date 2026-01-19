# UserResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The timestamp when the user was created in the identity source | [optional] [readonly] 
**external_id** | **str** | The external ID of the user in the identity source | [optional] [readonly] 
**id** | **str** | The ID of the user in the identity source | [optional] [readonly] 
**last_updated** | **datetime** | The timestamp when the user was last updated in the identity source | [optional] [readonly] 
**profile** | [**IdentitySourceUserProfileForUpsert**](IdentitySourceUserProfileForUpsert.md) |  | [optional] 

## Example

```python
from okta.models.user_response_schema import UserResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponseSchema from a JSON string
user_response_schema_instance = UserResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UserResponseSchema.to_json())

# convert the object into a dict
user_response_schema_dict = user_response_schema_instance.to_dict()
# create an instance of UserResponseSchema from a dict
user_response_schema_from_dict = UserResponseSchema.from_dict(user_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


