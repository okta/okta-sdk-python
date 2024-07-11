# DeviceProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_encryption_type** | [**DiskEncryptionTypeDef**](DiskEncryptionTypeDef.md) |  | [optional] 
**display_name** | **str** | Display name of the device | 
**imei** | **str** | International Mobile Equipment Identity (IMEI) of the device | [optional] 
**integrity_jailbreak** | **bool** | Indicates if the device is jailbroken or rooted. Only applicable to &#x60;IOS&#x60; and &#x60;ANDROID&#x60; platforms | [optional] 
**manufacturer** | **str** | Name of the manufacturer of the device | [optional] 
**meid** | **str** | Mobile equipment identifier of the device | [optional] 
**model** | **str** | Model of the device | [optional] 
**os_version** | **str** | Version of the device OS | [optional] 
**platform** | [**DevicePlatform**](DevicePlatform.md) |  | 
**registered** | **bool** | Indicates if the device is registered at Okta | 
**secure_hardware_present** | **bool** | Indicates if the device contains a secure hardware functionality | [optional] 
**serial_number** | **str** | Serial number of the device | [optional] 
**sid** | **str** | Windows Security identifier of the device | [optional] 
**tpm_public_key_hash** | **str** | Windows Trsted Platform Module hash value | [optional] 
**udid** | **str** | macOS Unique Device identifier of the device | [optional] 

## Example

```python
from okta.models.device_profile import DeviceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceProfile from a JSON string
device_profile_instance = DeviceProfile.from_json(json)
# print the JSON string representation of the object
print(DeviceProfile.to_json())

# convert the object into a dict
device_profile_dict = device_profile_instance.to_dict()
# create an instance of DeviceProfile from a dict
device_profile_from_dict = DeviceProfile.from_dict(device_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


