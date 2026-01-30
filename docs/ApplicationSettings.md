# ApplicationSettings

App settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**em_opt_in_status** | **str** | The entitlement management opt-in status for the app | [optional] [readonly] 
**identity_store_id** | **str** | Identifies an additional identity store app, if your app supports it. The &#x60;identityStoreId&#x60; value must be a valid identity store app ID. This identity store app must be created in the same org as your app. | [optional] 
**implicit_assignment** | **bool** | Controls whether Okta automatically assigns users to the app based on the user&#39;s role or group membership. | [optional] 
**inline_hook_id** | **str** | Identifier of an inline hook. Inline hooks are outbound calls from Okta to your own custom code, triggered at specific points in Okta process flows. They allow you to integrate custom functionality into those flows. See [Inline hooks](/openapi/okta-management/management/tag/InlineHook/). | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 

## Example

```python
from okta.models.application_settings import ApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSettings from a JSON string
application_settings_instance = ApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(ApplicationSettings.to_json())

# convert the object into a dict
application_settings_dict = application_settings_instance.to_dict()
# create an instance of ApplicationSettings from a dict
application_settings_from_dict = ApplicationSettings.from_dict(application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


