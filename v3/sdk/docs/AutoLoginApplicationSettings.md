# AutoLoginApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_store_id** | **str** |  | [optional] 
**implicit_assignment** | **bool** |  | [optional] 
**inline_hook_id** | **str** |  | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 
**sign_on** | [**AutoLoginApplicationSettingsSignOn**](AutoLoginApplicationSettingsSignOn.md) |  | [optional] 

## Example

```python
from okta.models.auto_login_application_settings import AutoLoginApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AutoLoginApplicationSettings from a JSON string
auto_login_application_settings_instance = AutoLoginApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(AutoLoginApplicationSettings.to_json())

# convert the object into a dict
auto_login_application_settings_dict = auto_login_application_settings_instance.to_dict()
# create an instance of AutoLoginApplicationSettings from a dict
auto_login_application_settings_from_dict = AutoLoginApplicationSettings.from_dict(auto_login_application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


