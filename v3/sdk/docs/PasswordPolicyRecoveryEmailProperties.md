# PasswordPolicyRecoveryEmailProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_token** | [**PasswordPolicyRecoveryEmailRecoveryToken**](PasswordPolicyRecoveryEmailRecoveryToken.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_recovery_email_properties import PasswordPolicyRecoveryEmailProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRecoveryEmailProperties from a JSON string
password_policy_recovery_email_properties_instance = PasswordPolicyRecoveryEmailProperties.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRecoveryEmailProperties.to_json())

# convert the object into a dict
password_policy_recovery_email_properties_dict = password_policy_recovery_email_properties_instance.to_dict()
# create an instance of PasswordPolicyRecoveryEmailProperties from a dict
password_policy_recovery_email_properties_from_dict = PasswordPolicyRecoveryEmailProperties.from_dict(password_policy_recovery_email_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


