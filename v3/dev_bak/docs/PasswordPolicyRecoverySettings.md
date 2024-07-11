# PasswordPolicyRecoverySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factors** | [**PasswordPolicyRecoveryFactors**](PasswordPolicyRecoveryFactors.md) |  | [optional] 

## Example

```python
from openapi_client.models.password_policy_recovery_settings import PasswordPolicyRecoverySettings

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRecoverySettings from a JSON string
password_policy_recovery_settings_instance = PasswordPolicyRecoverySettings.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRecoverySettings.to_json())

# convert the object into a dict
password_policy_recovery_settings_dict = password_policy_recovery_settings_instance.to_dict()
# create an instance of PasswordPolicyRecoverySettings from a dict
password_policy_recovery_settings_from_dict = PasswordPolicyRecoverySettings.from_dict(password_policy_recovery_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


