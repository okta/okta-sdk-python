# AuthenticatorKeyCustomAppAllOfProviderConfigurationApns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the APNs (Apple Push Notification Service) [configurations](https://developer.okta.com/docs/reference/api/push-providers/) | [optional] 
**app_bundle_id** | **str** | AppBundleId of the APNs (Apple Push Notification Service) [configurations](https://developer.okta.com/docs/reference/api/push-providers/) | [optional] 
**debug_app_bundle_id** | **str** | DebugAppBundleId of the APNs (Apple Push Notification Service) [configurations](https://developer.okta.com/docs/reference/api/push-providers/) | [optional] 

## Example

```python
from okta.models.authenticator_key_custom_app_all_of_provider_configuration_apns import AuthenticatorKeyCustomAppAllOfProviderConfigurationApns

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyCustomAppAllOfProviderConfigurationApns from a JSON string
authenticator_key_custom_app_all_of_provider_configuration_apns_instance = AuthenticatorKeyCustomAppAllOfProviderConfigurationApns.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyCustomAppAllOfProviderConfigurationApns.to_json())

# convert the object into a dict
authenticator_key_custom_app_all_of_provider_configuration_apns_dict = authenticator_key_custom_app_all_of_provider_configuration_apns_instance.to_dict()
# create an instance of AuthenticatorKeyCustomAppAllOfProviderConfigurationApns from a dict
authenticator_key_custom_app_all_of_provider_configuration_apns_from_dict = AuthenticatorKeyCustomAppAllOfProviderConfigurationApns.from_dict(authenticator_key_custom_app_all_of_provider_configuration_apns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


