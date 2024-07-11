# UserLockoutSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prevent_brute_force_lockout_from_unknown_devices** | **bool** | Prevents brute-force lockout from unknown devices for the password authenticator. | [optional] 

## Example

```python
from okta.models.user_lockout_settings import UserLockoutSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UserLockoutSettings from a JSON string
user_lockout_settings_instance = UserLockoutSettings.from_json(json)
# print the JSON string representation of the object
print(UserLockoutSettings.to_json())

# convert the object into a dict
user_lockout_settings_dict = user_lockout_settings_instance.to_dict()
# create an instance of UserLockoutSettings from a dict
user_lockout_settings_from_dict = UserLockoutSettings.from_dict(user_lockout_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


