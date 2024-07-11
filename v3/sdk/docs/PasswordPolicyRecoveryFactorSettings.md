# PasswordPolicyRecoveryFactorSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_recovery_factor_settings import PasswordPolicyRecoveryFactorSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRecoveryFactorSettings from a JSON string
password_policy_recovery_factor_settings_instance = PasswordPolicyRecoveryFactorSettings.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRecoveryFactorSettings.to_json())

# convert the object into a dict
password_policy_recovery_factor_settings_dict = password_policy_recovery_factor_settings_instance.to_dict()
# create an instance of PasswordPolicyRecoveryFactorSettings from a dict
password_policy_recovery_factor_settings_from_dict = PasswordPolicyRecoveryFactorSettings.from_dict(password_policy_recovery_factor_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


