# PasswordPolicyRecoveryFactors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**okta_call** | [**PasswordPolicyRecoveryFactorSettings**](PasswordPolicyRecoveryFactorSettings.md) |  | [optional] 
**okta_email** | [**PasswordPolicyRecoveryEmail**](PasswordPolicyRecoveryEmail.md) |  | [optional] 
**okta_sms** | [**PasswordPolicyRecoveryFactorSettings**](PasswordPolicyRecoveryFactorSettings.md) |  | [optional] 
**recovery_question** | [**PasswordPolicyRecoveryQuestion**](PasswordPolicyRecoveryQuestion.md) |  | [optional] 

## Example

```python
from openapi_client.models.password_policy_recovery_factors import PasswordPolicyRecoveryFactors

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRecoveryFactors from a JSON string
password_policy_recovery_factors_instance = PasswordPolicyRecoveryFactors.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRecoveryFactors.to_json())

# convert the object into a dict
password_policy_recovery_factors_dict = password_policy_recovery_factors_instance.to_dict()
# create an instance of PasswordPolicyRecoveryFactors from a dict
password_policy_recovery_factors_from_dict = PasswordPolicyRecoveryFactors.from_dict(password_policy_recovery_factors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


