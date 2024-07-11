# AutoLoginApplicationSettingsSignOn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_url** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 

## Example

```python
from okta.models.auto_login_application_settings_sign_on import AutoLoginApplicationSettingsSignOn

# TODO update the JSON string below
json = "{}"
# create an instance of AutoLoginApplicationSettingsSignOn from a JSON string
auto_login_application_settings_sign_on_instance = AutoLoginApplicationSettingsSignOn.from_json(json)
# print the JSON string representation of the object
print(AutoLoginApplicationSettingsSignOn.to_json())

# convert the object into a dict
auto_login_application_settings_sign_on_dict = auto_login_application_settings_sign_on_instance.to_dict()
# create an instance of AutoLoginApplicationSettingsSignOn from a dict
auto_login_application_settings_sign_on_from_dict = AutoLoginApplicationSettingsSignOn.from_dict(auto_login_application_settings_sign_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


