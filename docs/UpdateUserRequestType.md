# UpdateUserRequestType

The ID of the user type. Add this value if you want to create a user with a non-default [User Type](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserType/). The user type determines which [schema](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Schema/) applies to that user. After a user has been created, the user can only be assigned a different user type by an admin through a full replacement (`PUT`) operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the user type | [optional] 

## Example

```python
from okta.models.update_user_request_type import UpdateUserRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestType from a JSON string
update_user_request_type_instance = UpdateUserRequestType.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestType.to_json())

# convert the object into a dict
update_user_request_type_dict = update_user_request_type_instance.to_dict()
# create an instance of UpdateUserRequestType from a dict
update_user_request_type_from_dict = UpdateUserRequestType.from_dict(update_user_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


