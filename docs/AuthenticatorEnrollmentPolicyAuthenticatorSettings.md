# AuthenticatorEnrollmentPolicyAuthenticatorSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**AuthenticatorEnrollmentPolicyAuthenticatorSettingsConstraints**](AuthenticatorEnrollmentPolicyAuthenticatorSettingsConstraints.md) |  | [optional] 
**enroll** | [**AuthenticatorEnrollmentPolicyAuthenticatorSettingsEnroll**](AuthenticatorEnrollmentPolicyAuthenticatorSettingsEnroll.md) |  | [optional] 
**key** | [**AuthenticatorEnrollmentPolicyAuthenticatorType**](AuthenticatorEnrollmentPolicyAuthenticatorType.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_policy_authenticator_settings import AuthenticatorEnrollmentPolicyAuthenticatorSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentPolicyAuthenticatorSettings from a JSON string
authenticator_enrollment_policy_authenticator_settings_instance = AuthenticatorEnrollmentPolicyAuthenticatorSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentPolicyAuthenticatorSettings.to_json())

# convert the object into a dict
authenticator_enrollment_policy_authenticator_settings_dict = authenticator_enrollment_policy_authenticator_settings_instance.to_dict()
# create an instance of AuthenticatorEnrollmentPolicyAuthenticatorSettings from a dict
authenticator_enrollment_policy_authenticator_settings_from_dict = AuthenticatorEnrollmentPolicyAuthenticatorSettings.from_dict(authenticator_enrollment_policy_authenticator_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


