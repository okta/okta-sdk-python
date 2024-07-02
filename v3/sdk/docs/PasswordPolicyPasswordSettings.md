# PasswordPolicyPasswordSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | [**PasswordPolicyPasswordSettingsAge**](PasswordPolicyPasswordSettingsAge.md) |  | [optional] 
**complexity** | [**PasswordPolicyPasswordSettingsComplexity**](PasswordPolicyPasswordSettingsComplexity.md) |  | [optional] 
**lockout** | [**PasswordPolicyPasswordSettingsLockout**](PasswordPolicyPasswordSettingsLockout.md) |  | [optional] 

## Example

```python
from openapi_client.models.password_policy_password_settings import PasswordPolicyPasswordSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyPasswordSettings from a JSON string
password_policy_password_settings_instance = PasswordPolicyPasswordSettings.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyPasswordSettings.to_json())

# convert the object into a dict
password_policy_password_settings_dict = password_policy_password_settings_instance.to_dict()
# create an instance of PasswordPolicyPasswordSettings from a dict
password_policy_password_settings_from_dict = PasswordPolicyPasswordSettings.from_dict(password_policy_password_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


