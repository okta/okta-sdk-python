# MultifactorEnrollmentPolicySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticators** | [**List[MultifactorEnrollmentPolicyAuthenticatorSettings]**](MultifactorEnrollmentPolicyAuthenticatorSettings.md) |  | [optional] 
**type** | [**MultifactorEnrollmentPolicySettingsType**](MultifactorEnrollmentPolicySettingsType.md) |  | [optional] 

## Example

```python
from openapi_client.models.multifactor_enrollment_policy_settings import MultifactorEnrollmentPolicySettings

# TODO update the JSON string below
json = "{}"
# create an instance of MultifactorEnrollmentPolicySettings from a JSON string
multifactor_enrollment_policy_settings_instance = MultifactorEnrollmentPolicySettings.from_json(json)
# print the JSON string representation of the object
print(MultifactorEnrollmentPolicySettings.to_json())

# convert the object into a dict
multifactor_enrollment_policy_settings_dict = multifactor_enrollment_policy_settings_instance.to_dict()
# create an instance of MultifactorEnrollmentPolicySettings from a dict
multifactor_enrollment_policy_settings_form_dict = multifactor_enrollment_policy_settings.from_dict(multifactor_enrollment_policy_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


