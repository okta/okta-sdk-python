# ApplicationSettingsNotificationsVpnNetwork

Defines network zones for VPN notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | **str** | Specifies the VPN connection details required to access the app | [optional] 
**exclude** | **List[str]** | Defines the IP addresses or network ranges that are excluded from the VPN requirement | [optional] 
**include** | **List[str]** | Defines the IP addresses or network ranges that are required to use the VPN | [optional] 

## Example

```python
from okta.models.application_settings_notifications_vpn_network import ApplicationSettingsNotificationsVpnNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSettingsNotificationsVpnNetwork from a JSON string
application_settings_notifications_vpn_network_instance = ApplicationSettingsNotificationsVpnNetwork.from_json(json)
# print the JSON string representation of the object
print(ApplicationSettingsNotificationsVpnNetwork.to_json())

# convert the object into a dict
application_settings_notifications_vpn_network_dict = application_settings_notifications_vpn_network_instance.to_dict()
# create an instance of ApplicationSettingsNotificationsVpnNetwork from a dict
application_settings_notifications_vpn_network_from_dict = ApplicationSettingsNotificationsVpnNetwork.from_dict(application_settings_notifications_vpn_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


