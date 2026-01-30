# SecurityEventsProviderSettingsResponse

Security Events Provider settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | Issuer URL | [optional] 
**jwks_url** | **str** | The public URL where the JWKS public key is uploaded | [optional] 
**well_known_url** | **str** | The well-known URL of the Security Events Provider (the SSF transmitter) | [optional] 

## Example

```python
from okta.models.security_events_provider_settings_response import SecurityEventsProviderSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventsProviderSettingsResponse from a JSON string
security_events_provider_settings_response_instance = SecurityEventsProviderSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(SecurityEventsProviderSettingsResponse.to_json())

# convert the object into a dict
security_events_provider_settings_response_dict = security_events_provider_settings_response_instance.to_dict()
# create an instance of SecurityEventsProviderSettingsResponse from a dict
security_events_provider_settings_response_from_dict = SecurityEventsProviderSettingsResponse.from_dict(security_events_provider_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


