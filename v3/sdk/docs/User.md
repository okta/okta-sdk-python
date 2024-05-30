# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated** | **datetime** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**credentials** | [**UserCredentials**](UserCredentials.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_login** | **datetime** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**password_changed** | **datetime** |  | [optional] [readonly] 
**profile** | [**UserProfile**](UserProfile.md) |  | [optional] 
**realm_id** | **str** | The ID of the realm in which the user is residing | [optional] [readonly] 
**status** | [**UserStatus**](UserStatus.md) |  | [optional] 
**status_changed** | **datetime** |  | [optional] [readonly] 
**transitioning_to_status** | [**UserStatus**](UserStatus.md) |  | [optional] 
**type** | [**UserType**](UserType.md) |  | [optional] 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


