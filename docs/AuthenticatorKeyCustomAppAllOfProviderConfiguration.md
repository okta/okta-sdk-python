# AuthenticatorKeyCustomAppAllOfProviderConfiguration

The configuration of the provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apns** | [**AuthenticatorKeyCustomAppAllOfProviderConfigurationApns**](AuthenticatorKeyCustomAppAllOfProviderConfigurationApns.md) |  | [optional] 
**fcm** | [**AuthenticatorKeyCustomAppAllOfProviderConfigurationFcm**](AuthenticatorKeyCustomAppAllOfProviderConfigurationFcm.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_custom_app_all_of_provider_configuration import AuthenticatorKeyCustomAppAllOfProviderConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyCustomAppAllOfProviderConfiguration from a JSON string
authenticator_key_custom_app_all_of_provider_configuration_instance = AuthenticatorKeyCustomAppAllOfProviderConfiguration.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyCustomAppAllOfProviderConfiguration.to_json())

# convert the object into a dict
authenticator_key_custom_app_all_of_provider_configuration_dict = authenticator_key_custom_app_all_of_provider_configuration_instance.to_dict()
# create an instance of AuthenticatorKeyCustomAppAllOfProviderConfiguration from a dict
authenticator_key_custom_app_all_of_provider_configuration_from_dict = AuthenticatorKeyCustomAppAllOfProviderConfiguration.from_dict(authenticator_key_custom_app_all_of_provider_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


