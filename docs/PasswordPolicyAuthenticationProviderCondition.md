# PasswordPolicyAuthenticationProviderCondition

Specifies an authentication provider that's the source of some or all users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**provider** | [**PasswordPolicyAuthenticationProviderType**](PasswordPolicyAuthenticationProviderType.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_authentication_provider_condition import PasswordPolicyAuthenticationProviderCondition

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyAuthenticationProviderCondition from a JSON string
password_policy_authentication_provider_condition_instance = PasswordPolicyAuthenticationProviderCondition.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyAuthenticationProviderCondition.to_json())

# convert the object into a dict
password_policy_authentication_provider_condition_dict = password_policy_authentication_provider_condition_instance.to_dict()
# create an instance of PasswordPolicyAuthenticationProviderCondition from a dict
password_policy_authentication_provider_condition_from_dict = PasswordPolicyAuthenticationProviderCondition.from_dict(password_policy_authentication_provider_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


