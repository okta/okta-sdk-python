# AndroidDeviceTrust

Android Device Trust integration provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_integrity_level** | [**DeviceIntegrity**](DeviceIntegrity.md) |  | [optional] 
**network_proxy_disabled** | **bool** | Indicates whether a device has a network proxy disabled | [optional] 
**play_protect_verdict** | [**PlayProtectVerdict**](PlayProtectVerdict.md) |  | [optional] 
**require_major_version_update** | **bool** | Indicates whether the device needs to be on the latest major version available to the device  **Note:** This option requires an &#x60;osVersion.dynamicVersionRequirement&#x60; value to be supplied with the &#x60;osVersion.dynamicVersionRequirement.type&#x60; as either &#x60;MINIMUM&#x60; or &#x60;EXACT&#x60;.  | [optional] 
**screen_lock_complexity** | [**ScreenLockComplexity**](ScreenLockComplexity.md) |  | [optional] 
**usb_debugging_disabled** | **bool** | Indicates whether Android Debug Bridge (adb) over USB is disabled | [optional] 
**wifi_secured** | **bool** | Indicates whether a device is on a password-protected Wi-Fi network | [optional] 

## Example

```python
from okta.models.android_device_trust import AndroidDeviceTrust

# TODO update the JSON string below
json = "{}"
# create an instance of AndroidDeviceTrust from a JSON string
android_device_trust_instance = AndroidDeviceTrust.from_json(json)
# print the JSON string representation of the object
print(AndroidDeviceTrust.to_json())

# convert the object into a dict
android_device_trust_dict = android_device_trust_instance.to_dict()
# create an instance of AndroidDeviceTrust from a dict
android_device_trust_from_dict = AndroidDeviceTrust.from_dict(android_device_trust_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


