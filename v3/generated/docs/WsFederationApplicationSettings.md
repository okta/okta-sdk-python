# WsFederationApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_store_id** | **str** |  | [optional] 
**implicit_assignment** | **bool** |  | [optional] 
**inline_hook_id** | **str** |  | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 
**app** | [**WsFederationApplicationSettingsApplication**](WsFederationApplicationSettingsApplication.md) |  | [optional] 

## Example

```python
from openapi_client.models.ws_federation_application_settings import WsFederationApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WsFederationApplicationSettings from a JSON string
ws_federation_application_settings_instance = WsFederationApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(WsFederationApplicationSettings.to_json())

# convert the object into a dict
ws_federation_application_settings_dict = ws_federation_application_settings_instance.to_dict()
# create an instance of WsFederationApplicationSettings from a dict
ws_federation_application_settings_form_dict = ws_federation_application_settings.from_dict(ws_federation_application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


