# DTCWindows

Google Chrome Device Trust Connector provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser_version** | [**ChromeBrowserVersion**](ChromeBrowserVersion.md) |  | [optional] 
**built_in_dns_client_enabled** | **bool** | Indicates if a software stack is used to communicate with the DNS server | [optional] 
**chrome_remote_desktop_app_blocked** | **bool** | Indicates whether access to the Chrome Remote Desktop application is blocked through a policy | [optional] 
**crowd_strike_agent_id** | **str** | Agent ID of an installed CrowdStrike agent | [optional] 
**crowd_strike_customer_id** | **str** | Customer ID of an installed CrowdStrike agent | [optional] 
**device_enrollment_domain** | **str** | Enrollment domain of the customer that is currently managing the device | [optional] 
**disk_enrypted** | **bool** | Indicates whether the main disk is encrypted | [optional] 
**key_trust_level** | [**KeyTrustLevelBrowserKey**](KeyTrustLevelBrowserKey.md) |  | [optional] 
**os_firewall** | **bool** | Indicates whether a firewall is enabled at the OS-level on the device | [optional] 
**os_version** | [**OSVersion**](OSVersion.md) |  | [optional] 
**password_protection_warning_trigger** | [**PasswordProtectionWarningTrigger**](PasswordProtectionWarningTrigger.md) |  | [optional] 
**realtime_url_check_mode** | **bool** | Indicates whether enterprise-grade (custom) unsafe URL scanning is enabled | [optional] 
**safe_browsing_protection_level** | [**SafeBrowsingProtectionLevel**](SafeBrowsingProtectionLevel.md) |  | [optional] 
**screen_lock_secured** | **bool** | Indicates whether the device is password-protected | [optional] 
**secure_boot_enabled** | **bool** | Indicates whether the device&#39;s startup software has its Secure Boot feature enabled | [optional] 
**site_isolation_enabled** | **bool** | Indicates whether the Site Isolation (also known as **Site Per Process**) setting is enabled | [optional] 
**third_party_blocking_enabled** | **bool** | Indicates whether Chrome is blocking third-party software injection | [optional] 
**windows_machine_domain** | **str** | Windows domain that the current machine has joined | [optional] 
**windows_user_domain** | **str** | Windows domain for the current OS user | [optional] 

## Example

```python
from openapi_client.models.dtc_windows import DTCWindows

# TODO update the JSON string below
json = "{}"
# create an instance of DTCWindows from a JSON string
dtc_windows_instance = DTCWindows.from_json(json)
# print the JSON string representation of the object
print(DTCWindows.to_json())

# convert the object into a dict
dtc_windows_dict = dtc_windows_instance.to_dict()
# create an instance of DTCWindows from a dict
dtc_windows_from_dict = DTCWindows.from_dict(dtc_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


