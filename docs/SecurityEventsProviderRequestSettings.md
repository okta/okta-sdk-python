# SecurityEventsProviderRequestSettings

Information about the Security Events Provider for signal ingestion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**well_known_url** | **str** | The published well-known URL of the Security Events Provider (the SSF transmitter) | 
**issuer** | **str** | Issuer URL | 
**jwks_url** | **str** | The public URL where the JWKS public key is uploaded | 

## Example

```python
from okta.models.security_events_provider_request_settings import SecurityEventsProviderRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventsProviderRequestSettings from a JSON string
security_events_provider_request_settings_instance = SecurityEventsProviderRequestSettings.from_json(json)
# print the JSON string representation of the object
print(SecurityEventsProviderRequestSettings.to_json())

# convert the object into a dict
security_events_provider_request_settings_dict = security_events_provider_request_settings_instance.to_dict()
# create an instance of SecurityEventsProviderRequestSettings from a dict
security_events_provider_request_settings_from_dict = SecurityEventsProviderRequestSettings.from_dict(security_events_provider_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


