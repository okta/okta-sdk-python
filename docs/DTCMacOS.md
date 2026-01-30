# DTCMacOS

Google Chrome Device Trust Connector provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_version** | [**ChromeBrowserVersion**](ChromeBrowserVersion.md) |  | [optional] 
**built_in_dns_client_enabled** | **bool** | Indicates if a software stack is used to communicate with the DNS server | [optional] 
**chrome_remote_desktop_app_blocked** | **bool** | Indicates whether access to the Chrome Remote Desktop application is blocked through a policy | [optional] 
**device_enrollment_domain** | **str** | Enrollment domain of the customer that is currently managing the device | [optional] 
**disk_encrypted** | **bool** | Indicates whether the main disk is encrypted | [optional] 
**key_trust_level** | [**KeyTrustLevelBrowserKey**](KeyTrustLevelBrowserKey.md) |  | [optional] 
**os_firewall** | **bool** | Indicates whether a firewall is enabled at the OS-level on the device | [optional] 
**os_version** | [**OSVersionThreeComponents**](OSVersionThreeComponents.md) |  | [optional] 
**password_protection_warning_trigger** | [**PasswordProtectionWarningTrigger**](PasswordProtectionWarningTrigger.md) |  | [optional] 
**realtime_url_check_mode** | **bool** | Indicates whether enterprise-grade (custom) unsafe URL scanning is enabled | [optional] 
**safe_browsing_protection_level** | [**SafeBrowsingProtectionLevel**](SafeBrowsingProtectionLevel.md) |  | [optional] 
**screen_lock_secured** | **bool** | Indicates whether the device is password-protected | [optional] 
**site_isolation_enabled** | **bool** | Indicates whether the Site Isolation (also known as **Site Per Process**) setting is enabled | [optional] 

## Example

```python
from okta.models.dtc_mac_os import DTCMacOS

# TODO update the JSON string below
json = "{}"
# create an instance of DTCMacOS from a JSON string
dtc_mac_os_instance = DTCMacOS.from_json(json)
# print the JSON string representation of the object
print(DTCMacOS.to_json())

# convert the object into a dict
dtc_mac_os_dict = dtc_mac_os_instance.to_dict()
# create an instance of DTCMacOS from a dict
dtc_mac_os_from_dict = DTCMacOS.from_dict(dtc_mac_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


