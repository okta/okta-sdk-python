# DeviceAssuranceMacOSPlatform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_encryption_type** | [**DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType**](DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType.md) |  | [optional] 
**jailbreak** | **bool** |  | [optional] 
**os_version** | [**OSVersion**](OSVersion.md) |  | [optional] 
**screen_lock_type** | [**DeviceAssuranceAndroidPlatformAllOfScreenLockType**](DeviceAssuranceAndroidPlatformAllOfScreenLockType.md) |  | [optional] 
**secure_hardware_present** | **bool** |  | [optional] 
**third_party_signal_providers** | [**DeviceAssuranceMacOSPlatformAllOfThirdPartySignalProviders**](DeviceAssuranceMacOSPlatformAllOfThirdPartySignalProviders.md) |  | [optional] 

## Example

```python
from okta.models.device_assurance_mac_os_platform import DeviceAssuranceMacOSPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAssuranceMacOSPlatform from a JSON string
device_assurance_mac_os_platform_instance = DeviceAssuranceMacOSPlatform.from_json(json)
# print the JSON string representation of the object
print(DeviceAssuranceMacOSPlatform.to_json())

# convert the object into a dict
device_assurance_mac_os_platform_dict = device_assurance_mac_os_platform_instance.to_dict()
# create an instance of DeviceAssuranceMacOSPlatform from a dict
device_assurance_mac_os_platform_from_dict = DeviceAssuranceMacOSPlatform.from_dict(device_assurance_mac_os_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


