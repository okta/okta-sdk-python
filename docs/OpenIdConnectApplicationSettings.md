# OpenIdConnectApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**em_opt_in_status** | **str** | The entitlement management opt-in status for the app | [optional] [readonly] 
**identity_store_id** | **str** | Identifies an additional identity store app, if your app supports it. The &#x60;identityStoreId&#x60; value must be a valid identity store app ID. This identity store app must be created in the same org as your app. | [optional] 
**implicit_assignment** | **bool** | Controls whether Okta automatically assigns users to the app based on the user&#39;s role or group membership. | [optional] 
**inline_hook_id** | **str** | Identifier of an inline hook. Inline hooks are outbound calls from Okta to your own custom code, triggered at specific points in Okta process flows. They allow you to integrate custom functionality into those flows. See [Inline hooks](/openapi/okta-management/management/tag/InlineHook/). | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 
**oauth_client** | [**OpenIdConnectApplicationSettingsClient**](OpenIdConnectApplicationSettingsClient.md) |  | [optional] 

## Example

```python
from okta.models.open_id_connect_application_settings import OpenIdConnectApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectApplicationSettings from a JSON string
open_id_connect_application_settings_instance = OpenIdConnectApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectApplicationSettings.to_json())

# convert the object into a dict
open_id_connect_application_settings_dict = open_id_connect_application_settings_instance.to_dict()
# create an instance of OpenIdConnectApplicationSettings from a dict
open_id_connect_application_settings_from_dict = OpenIdConnectApplicationSettings.from_dict(open_id_connect_application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


