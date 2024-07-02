# DTCChromeOS

Google Chrome Device Trust Connector provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_screen_lock** | **bool** | Indicates whether the AllowScreenLock enterprise policy is enabled | [optional] 
**browser_version** | [**ChromeBrowserVersion**](ChromeBrowserVersion.md) |  | [optional] 
**built_in_dns_client_enabled** | **bool** | Indicates if a software stack is used to communicate with the DNS server | [optional] 
**chrome_remote_desktop_app_blocked** | **bool** | Indicates whether access to the Chrome Remote Desktop application is blocked through a policy | [optional] 
**device_enrollment_domain** | **str** | Enrollment domain of the customer that is currently managing the device | [optional] 
**disk_enrypted** | **bool** | Indicates whether the main disk is encrypted | [optional] 
**key_trust_level** | [**KeyTrustLevelOSMode**](KeyTrustLevelOSMode.md) |  | [optional] 
**os_firewall** | **bool** | Indicates whether a firewall is enabled at the OS-level on the device | [optional] 
**os_version** | [**OSVersion**](OSVersion.md) |  | [optional] 
**password_protection_warning_trigger** | [**PasswordProtectionWarningTrigger**](PasswordProtectionWarningTrigger.md) |  | [optional] 
**realtime_url_check_mode** | **bool** | Indicates whether enterprise-grade (custom) unsafe URL scanning is enabled | [optional] 
**safe_browsing_protection_level** | [**SafeBrowsingProtectionLevel**](SafeBrowsingProtectionLevel.md) |  | [optional] 
**screen_lock_secured** | **bool** | Indicates whether the device is password-protected | [optional] 
**site_isolation_enabled** | **bool** | Indicates whether the Site Isolation (also known as **Site Per Process**) setting is enabled | [optional] 

## Example

```python
from openapi_client.models.dtc_chrome_os import DTCChromeOS

# TODO update the JSON string below
json = "{}"
# create an instance of DTCChromeOS from a JSON string
dtc_chrome_os_instance = DTCChromeOS.from_json(json)
# print the JSON string representation of the object
print(DTCChromeOS.to_json())

# convert the object into a dict
dtc_chrome_os_dict = dtc_chrome_os_instance.to_dict()
# create an instance of DTCChromeOS from a dict
dtc_chrome_os_from_dict = DTCChromeOS.from_dict(dtc_chrome_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


