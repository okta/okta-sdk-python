# CreateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**UserCredentialsWritable**](UserCredentialsWritable.md) |  | [optional] 
**group_ids** | **List[str]** | The list of group IDs of groups that the user is added to at the time of creation | [optional] 
**profile** | [**UserProfile**](UserProfile.md) |  | 
**realm_id** | **str** | The ID of the realm in which the user is residing. See [Realms](/openapi/okta-management/management/tag/Realm/). | [optional] 
**type** | [**CreateUserRequestType**](CreateUserRequestType.md) |  | [optional] 

## Example

```python
from okta.models.create_user_request import CreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequest from a JSON string
create_user_request_instance = CreateUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequest.to_json())

# convert the object into a dict
create_user_request_dict = create_user_request_instance.to_dict()
# create an instance of CreateUserRequest from a dict
create_user_request_from_dict = CreateUserRequest.from_dict(create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


