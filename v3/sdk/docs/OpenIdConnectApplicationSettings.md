# OpenIdConnectApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_store_id** | **str** |  | [optional] 
**implicit_assignment** | **bool** |  | [optional] 
**inline_hook_id** | **str** |  | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 
**oauth_client** | [**OpenIdConnectApplicationSettingsClient**](OpenIdConnectApplicationSettingsClient.md) |  | [optional] 

## Example

```python
from openapi_client.models.open_id_connect_application_settings import OpenIdConnectApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectApplicationSettings from a JSON string
open_id_connect_application_settings_instance = OpenIdConnectApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectApplicationSettings.to_json())

# convert the object into a dict
open_id_connect_application_settings_dict = open_id_connect_application_settings_instance.to_dict()
# create an instance of OpenIdConnectApplicationSettings from a dict
open_id_connect_application_settings_form_dict = open_id_connect_application_settings.from_dict(open_id_connect_application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


