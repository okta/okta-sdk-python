# PasswordPolicyPasswordSettingsLockout

Lockout settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_unlock_minutes** | **int** | Specifies the time interval (in minutes) a locked account remains locked before it is automatically unlocked: &#x60;0&#x60; indicates no limit | [optional] [default to 0]
**max_attempts** | **int** | Specifies the number of times Users can attempt to sign in to their accounts with an invalid password before their accounts are locked: &#x60;0&#x60; indicates no limit | [optional] [default to 10]
**show_lockout_failures** | **bool** | Indicates if the User should be informed when their account is locked | [optional] [default to False]
**user_lockout_notification_channels** | **List[str]** | How the user is notified when their account becomes locked. The only acceptable values are &#x60;[]&#x60; and &#x60;[&#39;EMAIL&#39;]&#x60;. | [optional] [default to []]

## Example

```python
from okta.models.password_policy_password_settings_lockout import PasswordPolicyPasswordSettingsLockout

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


