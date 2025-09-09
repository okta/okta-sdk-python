# MultifactorEnrollmentPolicyAuthenticatorSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**MultifactorEnrollmentPolicyAuthenticatorSettingsConstraints**](MultifactorEnrollmentPolicyAuthenticatorSettingsConstraints.md) |  | [optional] 
**enroll** | [**MultifactorEnrollmentPolicyAuthenticatorSettingsEnroll**](MultifactorEnrollmentPolicyAuthenticatorSettingsEnroll.md) |  | [optional] 
**key** | [**MultifactorEnrollmentPolicyAuthenticatorType**](MultifactorEnrollmentPolicyAuthenticatorType.md) |  | [optional] 

## Example

```python
from okta.models.multifactor_enrollment_policy_authenticator_settings import MultifactorEnrollmentPolicyAuthenticatorSettings

# TODO update the JSON string below
json = "{}"
# create an instance of MultifactorEnrollmentPolicyAuthenticatorSettings from a JSON string
multifactor_enrollment_policy_authenticator_settings_instance = MultifactorEnrollmentPolicyAuthenticatorSettings.from_json(json)
# print the JSON string representation of the object
print(MultifactorEnrollmentPolicyAuthenticatorSettings.to_json())

# convert the object into a dict
multifactor_enrollment_policy_authenticator_settings_dict = multifactor_enrollment_policy_authenticator_settings_instance.to_dict()
# create an instance of MultifactorEnrollmentPolicyAuthenticatorSettings from a dict
multifactor_enrollment_policy_authenticator_settings_from_dict = MultifactorEnrollmentPolicyAuthenticatorSettings.from_dict(multifactor_enrollment_policy_authenticator_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


