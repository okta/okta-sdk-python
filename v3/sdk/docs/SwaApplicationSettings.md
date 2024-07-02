# SwaApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_store_id** | **str** |  | [optional] 
**implicit_assignment** | **bool** |  | [optional] 
**inline_hook_id** | **str** |  | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 
**app** | [**SwaApplicationSettingsApplication**](SwaApplicationSettingsApplication.md) |  | [optional] 

## Example

```python
from openapi_client.models.swa_application_settings import SwaApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SwaApplicationSettings from a JSON string
swa_application_settings_instance = SwaApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(SwaApplicationSettings.to_json())

# convert the object into a dict
swa_application_settings_dict = swa_application_settings_instance.to_dict()
# create an instance of SwaApplicationSettings from a dict
swa_application_settings_from_dict = SwaApplicationSettings.from_dict(swa_application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


