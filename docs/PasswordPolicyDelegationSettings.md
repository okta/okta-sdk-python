# PasswordPolicyDelegationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**PasswordPolicyDelegationSettingsOptions**](PasswordPolicyDelegationSettingsOptions.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_delegation_settings import PasswordPolicyDelegationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyDelegationSettings from a JSON string
password_policy_delegation_settings_instance = PasswordPolicyDelegationSettings.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyDelegationSettings.to_json())

# convert the object into a dict
password_policy_delegation_settings_dict = password_policy_delegation_settings_instance.to_dict()
# create an instance of PasswordPolicyDelegationSettings from a dict
password_policy_delegation_settings_from_dict = PasswordPolicyDelegationSettings.from_dict(password_policy_delegation_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


