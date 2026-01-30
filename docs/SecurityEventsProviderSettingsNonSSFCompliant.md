# SecurityEventsProviderSettingsNonSSFCompliant

Security Events Provider with issuer and JWKS settings for signal ingestion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | Issuer URL | 
**jwks_url** | **str** | The public URL where the JWKS public key is uploaded | 

## Example

```python
from okta.models.security_events_provider_settings_non_ssf_compliant import SecurityEventsProviderSettingsNonSSFCompliant

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventsProviderSettingsNonSSFCompliant from a JSON string
security_events_provider_settings_non_ssf_compliant_instance = SecurityEventsProviderSettingsNonSSFCompliant.from_json(json)
# print the JSON string representation of the object
print(SecurityEventsProviderSettingsNonSSFCompliant.to_json())

# convert the object into a dict
security_events_provider_settings_non_ssf_compliant_dict = security_events_provider_settings_non_ssf_compliant_instance.to_dict()
# create an instance of SecurityEventsProviderSettingsNonSSFCompliant from a dict
security_events_provider_settings_non_ssf_compliant_from_dict = SecurityEventsProviderSettingsNonSSFCompliant.from_dict(security_events_provider_settings_non_ssf_compliant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


