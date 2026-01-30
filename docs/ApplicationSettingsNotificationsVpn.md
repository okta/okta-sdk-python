# ApplicationSettingsNotificationsVpn

Sends customizable messages with conditions to end users when a VPN connection is required

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**help_url** | **str** | An optional URL to a help page to assist your end users in signing in to your company VPN | [optional] 
**message** | **str** | A VPN requirement message that&#39;s displayed to users | [optional] 
**network** | [**ApplicationSettingsNotificationsVpnNetwork**](ApplicationSettingsNotificationsVpnNetwork.md) |  | 

## Example

```python
from okta.models.application_settings_notifications_vpn import ApplicationSettingsNotificationsVpn

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


