# ZoomUsApplicationSettingsApplication

Zoom app instance properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_domain** | **str** | Your Zoom subdomain | 

## Example

```python
from okta.models.zoom_us_application_settings_application import ZoomUsApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ZoomUsApplicationSettingsApplication from a JSON string
zoom_us_application_settings_application_instance = ZoomUsApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(ZoomUsApplicationSettingsApplication.to_json())

# convert the object into a dict
zoom_us_application_settings_application_dict = zoom_us_application_settings_application_instance.to_dict()
# create an instance of ZoomUsApplicationSettingsApplication from a dict
zoom_us_application_settings_application_from_dict = ZoomUsApplicationSettingsApplication.from_dict(zoom_us_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


