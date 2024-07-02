# PerClientRateLimitSettings



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_mode** | [**PerClientRateLimitMode**](PerClientRateLimitMode.md) |  | 
**use_case_mode_overrides** | [**PerClientRateLimitSettingsUseCaseModeOverrides**](PerClientRateLimitSettingsUseCaseModeOverrides.md) |  | [optional] 

## Example

```python
from openapi_client.models.per_client_rate_limit_settings import PerClientRateLimitSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PerClientRateLimitSettings from a JSON string
per_client_rate_limit_settings_instance = PerClientRateLimitSettings.from_json(json)
# print the JSON string representation of the object
print(PerClientRateLimitSettings.to_json())

# convert the object into a dict
per_client_rate_limit_settings_dict = per_client_rate_limit_settings_instance.to_dict()
# create an instance of PerClientRateLimitSettings from a dict
per_client_rate_limit_settings_from_dict = PerClientRateLimitSettings.from_dict(per_client_rate_limit_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


