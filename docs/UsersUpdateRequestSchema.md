# UsersUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**IdentitySourceUserProfileForUpsert**](IdentitySourceUserProfileForUpsert.md) |  | [optional] 

## Example

```python
from okta.models.users_update_request_schema import UsersUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateRequestSchema from a JSON string
users_update_request_schema_instance = UsersUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateRequestSchema.to_json())

# convert the object into a dict
users_update_request_schema_dict = users_update_request_schema_instance.to_dict()
# create an instance of UsersUpdateRequestSchema from a dict
users_update_request_schema_from_dict = UsersUpdateRequestSchema.from_dict(users_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


