# DeviceAssuranceIOSPlatform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_encryption_type** | [**DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType**](DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType.md) |  | [optional] 
**jailbreak** | **bool** |  | [optional] 
**os_version** | [**OSVersion**](OSVersion.md) |  | [optional] 
**screen_lock_type** | [**DeviceAssuranceAndroidPlatformAllOfScreenLockType**](DeviceAssuranceAndroidPlatformAllOfScreenLockType.md) |  | [optional] 
**secure_hardware_present** | **bool** |  | [optional] 

## Example

```python
from okta.models.device_assurance_ios_platform import DeviceAssuranceIOSPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAssuranceIOSPlatform from a JSON string
device_assurance_ios_platform_instance = DeviceAssuranceIOSPlatform.from_json(json)
# print the JSON string representation of the object
print(DeviceAssuranceIOSPlatform.to_json())

# convert the object into a dict
device_assurance_ios_platform_dict = device_assurance_ios_platform_instance.to_dict()
# create an instance of DeviceAssuranceIOSPlatform from a dict
device_assurance_ios_platform_from_dict = DeviceAssuranceIOSPlatform.from_dict(device_assurance_ios_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


