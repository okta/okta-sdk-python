# PasswordPolicyAuthenticationProviderCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** |  | [optional] 
**provider** | [**PasswordPolicyAuthenticationProviderType**](PasswordPolicyAuthenticationProviderType.md) |  | [optional] 

## Example

```python
from openapi_client.models.password_policy_authentication_provider_condition import PasswordPolicyAuthenticationProviderCondition

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyAuthenticationProviderCondition from a JSON string
password_policy_authentication_provider_condition_instance = PasswordPolicyAuthenticationProviderCondition.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyAuthenticationProviderCondition.to_json())

# convert the object into a dict
password_policy_authentication_provider_condition_dict = password_policy_authentication_provider_condition_instance.to_dict()
# create an instance of PasswordPolicyAuthenticationProviderCondition from a dict
password_policy_authentication_provider_condition_form_dict = password_policy_authentication_provider_condition.from_dict(password_policy_authentication_provider_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


