# TrendMicroApexOneServiceApplicationSettingsApplication

Trend Micro Apex One as a Service app instance properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | Base Trend Micro Apex One Service URL | 

## Example

```python
from okta.models.trend_micro_apex_one_service_application_settings_application import TrendMicroApexOneServiceApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of TrendMicroApexOneServiceApplicationSettingsApplication from a JSON string
trend_micro_apex_one_service_application_settings_application_instance = TrendMicroApexOneServiceApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(TrendMicroApexOneServiceApplicationSettingsApplication.to_json())

# convert the object into a dict
trend_micro_apex_one_service_application_settings_application_dict = trend_micro_apex_one_service_application_settings_application_instance.to_dict()
# create an instance of TrendMicroApexOneServiceApplicationSettingsApplication from a dict
trend_micro_apex_one_service_application_settings_application_from_dict = TrendMicroApexOneServiceApplicationSettingsApplication.from_dict(trend_micro_apex_one_service_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


