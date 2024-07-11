# ApplicationSettingsNotifications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpn** | [**ApplicationSettingsNotificationsVpn**](ApplicationSettingsNotificationsVpn.md) |  | [optional] 

## Example

```python
from okta.models.application_settings_notifications import ApplicationSettingsNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSettingsNotifications from a JSON string
application_settings_notifications_instance = ApplicationSettingsNotifications.from_json(json)
# print the JSON string representation of the object
print(ApplicationSettingsNotifications.to_json())

# convert the object into a dict
application_settings_notifications_dict = application_settings_notifications_instance.to_dict()
# create an instance of ApplicationSettingsNotifications from a dict
application_settings_notifications_from_dict = ApplicationSettingsNotifications.from_dict(application_settings_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


