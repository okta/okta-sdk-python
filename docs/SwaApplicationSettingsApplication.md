# SwaApplicationSettingsApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_field** | **str** | CSS selector for the **Sign-In** button in the sign-in form (for SWA apps with the &#x60;template_swa&#x60; app name definition) | 
**button_selector** | **str** | CSS selector for the **Sign-In**  button in the sign-in form (for three-field SWA apps with the &#x60;template_swa3field&#x60; app name definition) | [optional] 
**extra_field_selector** | **str** | Enter the CSS selector for the extra field (for three-field SWA apps with the &#x60;template_swa3field&#x60; app name definition). | [optional] 
**extra_field_value** | **str** | Enter the value for the extra field in the form (for three-field SWA apps with the &#x60;template_swa3field&#x60; app name definition). | [optional] 
**login_url_regex** | **str** | A regular expression that further restricts targetURL to the specified regular expression | [optional] 
**password_field** | **str** | CSS selector for the **Password** field in the sign-in form (for SWA apps with the &#x60;template_swa&#x60; app name definition) | 
**password_selector** | **str** | CSS selector for the **Password** field in the sign-in form (for three-field SWA apps with the &#x60;template_swa3field&#x60; app name definition) | [optional] 
**target_url** | **str** | The URL of the sign-in page for this app (for three-field SWA apps with the &#x60;template_swa3field&#x60; app name definition) | [optional] 
**url** | **str** | The URL of the sign-in page for this app (for SWA apps with the &#x60;template_swa&#x60; app name definition) | 
**username_field** | **str** | CSS selector for the **Username** field in the sign-in form (for SWA apps with the &#x60;template_swa&#x60; app name definition) | 
**user_name_selector** | **str** | CSS selector for the **Username** field in the sign-in form (for three-field SWA apps with the &#x60;template_swa3field&#x60; app name definition) | [optional] 

## Example

```python
from okta.models.swa_application_settings_application import SwaApplicationSettingsApplication

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


