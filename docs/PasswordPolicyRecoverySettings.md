# PasswordPolicyRecoverySettings

Specifies the password recovery settings for the policy > **Note:** With Identity Engine, you can specify recovery factors inside the password policy rule instead of in the policy settings object. Recovery factors for the rule are defined inside the [`selfServicePasswordReset` action](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Policy/#tag/Policy/operation/createPolicyRule!path=1/actions/selfServicePasswordReset&t=request).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factors** | [**PasswordPolicyRecoveryFactors**](PasswordPolicyRecoveryFactors.md) |  | [optional] 

## Example

```python
from okta.models.password_policy_recovery_settings import PasswordPolicyRecoverySettings

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


