# ApplicationSettingsNotificationsVpn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**help_url** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**network** | [**ApplicationSettingsNotificationsVpnNetwork**](ApplicationSettingsNotificationsVpnNetwork.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_settings_notifications_vpn import ApplicationSettingsNotificationsVpn

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSettingsNotificationsVpn from a JSON string
application_settings_notifications_vpn_instance = ApplicationSettingsNotificationsVpn.from_json(json)
# print the JSON string representation of the object
print(ApplicationSettingsNotificationsVpn.to_json())

# convert the object into a dict
application_settings_notifications_vpn_dict = application_settings_notifications_vpn_instance.to_dict()
# create an instance of ApplicationSettingsNotificationsVpn from a dict
application_settings_notifications_vpn_from_dict = ApplicationSettingsNotificationsVpn.from_dict(application_settings_notifications_vpn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


