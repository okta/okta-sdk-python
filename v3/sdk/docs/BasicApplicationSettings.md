# BasicApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_store_id** | **str** |  | [optional] 
**implicit_assignment** | **bool** |  | [optional] 
**inline_hook_id** | **str** |  | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 
**app** | [**BasicApplicationSettingsApplication**](BasicApplicationSettingsApplication.md) |  | [optional] 

## Example

```python
from openapi_client.models.basic_application_settings import BasicApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BasicApplicationSettings from a JSON string
basic_application_settings_instance = BasicApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(BasicApplicationSettings.to_json())

# convert the object into a dict
basic_application_settings_dict = basic_application_settings_instance.to_dict()
# create an instance of BasicApplicationSettings from a dict
basic_application_settings_from_dict = BasicApplicationSettings.from_dict(basic_application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


