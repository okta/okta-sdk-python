# PasswordPolicySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegation** | [**PasswordPolicyDelegationSettings**](PasswordPolicyDelegationSettings.md) |  | [optional] 
**password** | [**PasswordPolicyPasswordSettings**](PasswordPolicyPasswordSettings.md) |  | [optional] 
**recovery** | [**PasswordPolicyRecoverySettings**](PasswordPolicyRecoverySettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.password_policy_settings import PasswordPolicySettings

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicySettings from a JSON string
password_policy_settings_instance = PasswordPolicySettings.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicySettings.to_json())

# convert the object into a dict
password_policy_settings_dict = password_policy_settings_instance.to_dict()
# create an instance of PasswordPolicySettings from a dict
password_policy_settings_from_dict = PasswordPolicySettings.from_dict(password_policy_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


