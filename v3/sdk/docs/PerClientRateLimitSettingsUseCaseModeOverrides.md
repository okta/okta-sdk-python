# PerClientRateLimitSettingsUseCaseModeOverrides

A map of Per-Client Rate Limit Use Case to the applicable PerClientRateLimitMode. Overrides the `defaultMode` property for the specified use cases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_page** | [**PerClientRateLimitMode**](PerClientRateLimitMode.md) |  | [optional] 
**oauth2_authorize** | [**PerClientRateLimitMode**](PerClientRateLimitMode.md) |  | [optional] 
**oie_app_intent** | [**PerClientRateLimitMode**](PerClientRateLimitMode.md) |  | [optional] 

## Example

```python
from okta.models.per_client_rate_limit_settings_use_case_mode_overrides import PerClientRateLimitSettingsUseCaseModeOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of PerClientRateLimitSettingsUseCaseModeOverrides from a JSON string
per_client_rate_limit_settings_use_case_mode_overrides_instance = PerClientRateLimitSettingsUseCaseModeOverrides.from_json(json)
# print the JSON string representation of the object
print(PerClientRateLimitSettingsUseCaseModeOverrides.to_json())

# convert the object into a dict
per_client_rate_limit_settings_use_case_mode_overrides_dict = per_client_rate_limit_settings_use_case_mode_overrides_instance.to_dict()
# create an instance of PerClientRateLimitSettingsUseCaseModeOverrides from a dict
per_client_rate_limit_settings_use_case_mode_overrides_from_dict = PerClientRateLimitSettingsUseCaseModeOverrides.from_dict(per_client_rate_limit_settings_use_case_mode_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


