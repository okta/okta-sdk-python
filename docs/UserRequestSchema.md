# UserRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The external ID of the user in the identity source | [optional] 
**profile** | [**IdentitySourceUserProfileForUpsert**](IdentitySourceUserProfileForUpsert.md) |  | [optional] 

## Example

```python
from okta.models.user_request_schema import UserRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UserRequestSchema from a JSON string
user_request_schema_instance = UserRequestSchema.from_json(json)
# print the JSON string representation of the object
print(UserRequestSchema.to_json())

# convert the object into a dict
user_request_schema_dict = user_request_schema_instance.to_dict()
# create an instance of UserRequestSchema from a dict
user_request_schema_from_dict = UserRequestSchema.from_dict(user_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


