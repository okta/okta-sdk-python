# ZscalerbyzApplicationSettingsApplication

Zscaler app instance properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_domain** | **str** | Your Zscaler domain | [optional] 

## Example

```python
from okta.models.zscalerbyz_application_settings_application import ZscalerbyzApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ZscalerbyzApplicationSettingsApplication from a JSON string
zscalerbyz_application_settings_application_instance = ZscalerbyzApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(ZscalerbyzApplicationSettingsApplication.to_json())

# convert the object into a dict
zscalerbyz_application_settings_application_dict = zscalerbyz_application_settings_application_instance.to_dict()
# create an instance of ZscalerbyzApplicationSettingsApplication from a dict
zscalerbyz_application_settings_application_from_dict = ZscalerbyzApplicationSettingsApplication.from_dict(zscalerbyz_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


