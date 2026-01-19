# SecurityEventsProviderSettingsSSFCompliant

Security Events Provider with well-known URL setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**well_known_url** | **str** | The published well-known URL of the Security Events Provider (the SSF transmitter) | 

## Example

```python
from okta.models.security_events_provider_settings_ssf_compliant import SecurityEventsProviderSettingsSSFCompliant

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventsProviderSettingsSSFCompliant from a JSON string
security_events_provider_settings_ssf_compliant_instance = SecurityEventsProviderSettingsSSFCompliant.from_json(json)
# print the JSON string representation of the object
print(SecurityEventsProviderSettingsSSFCompliant.to_json())

# convert the object into a dict
security_events_provider_settings_ssf_compliant_dict = security_events_provider_settings_ssf_compliant_instance.to_dict()
# create an instance of SecurityEventsProviderSettingsSSFCompliant from a dict
security_events_provider_settings_ssf_compliant_from_dict = SecurityEventsProviderSettingsSSFCompliant.from_dict(security_events_provider_settings_ssf_compliant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


