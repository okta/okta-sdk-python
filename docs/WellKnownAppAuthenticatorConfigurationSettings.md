# WellKnownAppAuthenticatorConfigurationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_verification** | [**CustomAppUserVerificationEnum**](CustomAppUserVerificationEnum.md) |  | [optional] 

## Example

```python
from okta.models.well_known_app_authenticator_configuration_settings import WellKnownAppAuthenticatorConfigurationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownAppAuthenticatorConfigurationSettings from a JSON string
well_known_app_authenticator_configuration_settings_instance = WellKnownAppAuthenticatorConfigurationSettings.from_json(json)
# print the JSON string representation of the object
print(WellKnownAppAuthenticatorConfigurationSettings.to_json())

# convert the object into a dict
well_known_app_authenticator_configuration_settings_dict = well_known_app_authenticator_configuration_settings_instance.to_dict()
# create an instance of WellKnownAppAuthenticatorConfigurationSettings from a dict
well_known_app_authenticator_configuration_settings_from_dict = WellKnownAppAuthenticatorConfigurationSettings.from_dict(well_known_app_authenticator_configuration_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


