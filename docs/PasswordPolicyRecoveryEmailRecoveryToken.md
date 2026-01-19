# PasswordPolicyRecoveryEmailRecoveryToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_lifetime_minutes** | **int** | Lifetime (in minutes) of the recovery token | [optional] [default to 10080]

## Example

```python
from okta.models.password_policy_recovery_email_recovery_token import PasswordPolicyRecoveryEmailRecoveryToken

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRecoveryEmailRecoveryToken from a JSON string
password_policy_recovery_email_recovery_token_instance = PasswordPolicyRecoveryEmailRecoveryToken.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRecoveryEmailRecoveryToken.to_json())

# convert the object into a dict
password_policy_recovery_email_recovery_token_dict = password_policy_recovery_email_recovery_token_instance.to_dict()
# create an instance of PasswordPolicyRecoveryEmailRecoveryToken from a dict
password_policy_recovery_email_recovery_token_from_dict = PasswordPolicyRecoveryEmailRecoveryToken.from_dict(password_policy_recovery_email_recovery_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


