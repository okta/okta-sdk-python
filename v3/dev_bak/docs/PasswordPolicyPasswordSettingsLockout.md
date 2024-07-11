# PasswordPolicyPasswordSettingsLockout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_unlock_minutes** | **int** |  | [optional] 
**max_attempts** | **int** |  | [optional] 
**show_lockout_failures** | **bool** |  | [optional] 
**user_lockout_notification_channels** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.password_policy_password_settings_lockout import PasswordPolicyPasswordSettingsLockout

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyPasswordSettingsLockout from a JSON string
password_policy_password_settings_lockout_instance = PasswordPolicyPasswordSettingsLockout.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyPasswordSettingsLockout.to_json())

# convert the object into a dict
password_policy_password_settings_lockout_dict = password_policy_password_settings_lockout_instance.to_dict()
# create an instance of PasswordPolicyPasswordSettingsLockout from a dict
password_policy_password_settings_lockout_from_dict = PasswordPolicyPasswordSettingsLockout.from_dict(password_policy_password_settings_lockout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


