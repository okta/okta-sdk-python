# PasswordPolicyRecoveryEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**PasswordPolicyRecoveryEmailProperties**](PasswordPolicyRecoveryEmailProperties.md) |  | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.password_policy_recovery_email import PasswordPolicyRecoveryEmail

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyRecoveryEmail from a JSON string
password_policy_recovery_email_instance = PasswordPolicyRecoveryEmail.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicyRecoveryEmail.to_json())

# convert the object into a dict
password_policy_recovery_email_dict = password_policy_recovery_email_instance.to_dict()
# create an instance of PasswordPolicyRecoveryEmail from a dict
password_policy_recovery_email_from_dict = PasswordPolicyRecoveryEmail.from_dict(password_policy_recovery_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


