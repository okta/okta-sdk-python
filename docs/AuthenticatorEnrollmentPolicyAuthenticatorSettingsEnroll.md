# AuthenticatorEnrollmentPolicyAuthenticatorSettingsEnroll

Enrollment requirements for the authenticator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**AuthenticatorEnrollmentPolicyAuthenticatorStatus**](AuthenticatorEnrollmentPolicyAuthenticatorStatus.md) |  | [optional] [default to AuthenticatorEnrollmentPolicyAuthenticatorStatus.NOT_ALLOWED]
**grace_period** | [**EnrollmentPolicyAuthenticatorGracePeriod**](EnrollmentPolicyAuthenticatorGracePeriod.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_authenticator_settings_enroll import AuthenticatorEnrollmentPolicyAuthenticatorSettingsEnroll

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyAuthenticatorSettingsEnroll from a JSON string
authenticator_enrollment_policy_authenticator_settings_enroll_instance = AuthenticatorEnrollmentPolicyAuthenticatorSettingsEnroll.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyAuthenticatorSettingsEnroll.to_json())

# convert the object into a dict
authenticator_enrollment_policy_authenticator_settings_enroll_dict = authenticator_enrollment_policy_authenticator_settings_enroll_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyAuthenticatorSettingsEnroll from a dict
authenticator_enrollment_policy_authenticator_settings_enroll_from_dict = AuthenticatorEnrollmentPolicyAuthenticatorSettingsEnroll.from_dict(authenticator_enrollment_policy_authenticator_settings_enroll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


