# SwaApplicationSettingsApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_field** | **str** |  | [optional] 
**button_selector** | **str** |  | [optional] 
**checkbox** | **str** |  | [optional] 
**extra_field_selector** | **str** |  | [optional] 
**extra_field_value** | **str** |  | [optional] 
**login_url_regex** | **str** |  | [optional] 
**password_field** | **str** |  | [optional] 
**password_selector** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**target_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**username_field** | **str** |  | [optional] 
**user_name_selector** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.swa_application_settings_application import SwaApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of SwaApplicationSettingsApplication from a JSON string
swa_application_settings_application_instance = SwaApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(SwaApplicationSettingsApplication.to_json())

# convert the object into a dict
swa_application_settings_application_dict = swa_application_settings_application_instance.to_dict()
# create an instance of SwaApplicationSettingsApplication from a dict
swa_application_settings_application_from_dict = SwaApplicationSettingsApplication.from_dict(swa_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


