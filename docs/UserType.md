# UserType

The user type that determines the schema for the user's profile. The `type` property is a map that identifies the [User Types](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/#tag/UserType).  Currently it contains a single element, `id`. It can be specified when creating a new user, and can be updated by an admin on a full replace of an existing user (but not a partial update).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the user type | [optional] 

## Example

```python
from okta.models.user_type import UserType

# TODO update the JSON string below
json = "{}"
# create an instance of UserType from a JSON string
user_type_instance = UserType.from_json(json)
# print the JSON string representation of the object
print(UserType.to_json())

# convert the object into a dict
user_type_dict = user_type_instance.to_dict()
# create an instance of UserType from a dict
user_type_from_dict = UserType.from_dict(user_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


