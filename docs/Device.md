# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the device was created | [optional] [readonly] 
**id** | **str** | Unique key for the device | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the device record was last updated. Updates occur when Okta collects and saves device signals during authentication, and when the lifecycle state of the device changes. | [optional] [readonly] 
**profile** | [**DeviceProfile**](DeviceProfile.md) |  | [optional] 
**resource_alternate_id** | **str** |  | [optional] [readonly] 
**resource_display_name** | [**DeviceDisplayName**](DeviceDisplayName.md) |  | [optional] 
**resource_id** | **str** | Alternate key for the &#x60;id&#x60; | [optional] [readonly] 
**resource_type** | **str** |  | [optional] [readonly] [default to 'UDDevice']
**status** | [**DeviceStatus**](DeviceStatus.md) |  | [optional] 
**links** | [**LinksSelfAndFullUsersLifecycle**](LinksSelfAndFullUsersLifecycle.md) |  | [optional] 

## Example

```python
from okta.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


