# PasswordPolicyDelegationSettingsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_unlock** | **bool** |  | [optional] 

## Example

```python
from okta.models.password_policy_delegation_settings_options import PasswordPolicyDelegationSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyDelegationSettingsOptions from a JSON string
password_policy_delegation_settings_options_instance = PasswordPolicyDelegationSettingsOptions.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyDelegationSettingsOptions.to_json())

# convert the object into a dict
password_policy_delegation_settings_options_dict = password_policy_delegation_settings_options_instance.to_dict()
# create an instance of PasswordPolicyDelegationSettingsOptions from a dict
password_policy_delegation_settings_options_from_dict = PasswordPolicyDelegationSettingsOptions.from_dict(password_policy_delegation_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


