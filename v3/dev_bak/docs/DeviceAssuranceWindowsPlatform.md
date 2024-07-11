# DeviceAssuranceWindowsPlatform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_encryption_type** | [**DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType**](DeviceAssuranceAndroidPlatformAllOfDiskEncryptionType.md) |  | [optional] 
**jailbreak** | **bool** |  | [optional] 
**os_version** | [**OSVersion**](OSVersion.md) |  | [optional] 
**screen_lock_type** | [**DeviceAssuranceAndroidPlatformAllOfScreenLockType**](DeviceAssuranceAndroidPlatformAllOfScreenLockType.md) |  | [optional] 
**secure_hardware_present** | **bool** |  | [optional] 
**third_party_signal_providers** | [**DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders**](DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_assurance_windows_platform import DeviceAssuranceWindowsPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAssuranceWindowsPlatform from a JSON string
device_assurance_windows_platform_instance = DeviceAssuranceWindowsPlatform.from_json(json)
# print the JSON string representation of the object
print(DeviceAssuranceWindowsPlatform.to_json())

# convert the object into a dict
device_assurance_windows_platform_dict = device_assurance_windows_platform_instance.to_dict()
# create an instance of DeviceAssuranceWindowsPlatform from a dict
device_assurance_windows_platform_from_dict = DeviceAssuranceWindowsPlatform.from_dict(device_assurance_windows_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


