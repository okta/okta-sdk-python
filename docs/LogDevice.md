# LogDevice

The entity that describes a device enrolled with passwordless authentication using Okta Verify.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_integrator** | **object** | The integration platform or software used with the device | [optional] [readonly] 
**disk_encryption_type** | [**LogDiskEncryptionType**](LogDiskEncryptionType.md) |  | [optional] 
**id** | **str** | ID of the device | [optional] [readonly] 
**jailbreak** | **bool** | If the device has removed software restrictions | [optional] [readonly] 
**managed** | **bool** | Indicates if the device is configured for device management and is registered with Okta | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**os_platform** | **str** |  | [optional] [readonly] 
**os_version** | **str** |  | [optional] [readonly] 
**registered** | **bool** | Indicates if the device is registered with an Okta org and is bound to an Okta Verify instance on the device | [optional] [readonly] 
**screen_lock_type** | [**LogScreenLockType**](LogScreenLockType.md) |  | [optional] 
**secure_hardware_present** | **bool** | The availability of hardware security on the device | [optional] [readonly] 

## Example

```python
from okta.models.log_device import LogDevice

# TODO update the JSON string below
json = "{}"
# create an instance of LogDevice from a JSON string
log_device_instance = LogDevice.from_json(json)
# print the JSON string representation of the object
print(LogDevice.to_json())

# convert the object into a dict
log_device_dict = log_device_instance.to_dict()
# create an instance of LogDevice from a dict
log_device_from_dict = LogDevice.from_dict(log_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


