# DeviceUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | Timestamp when device was created | [optional] 
**management_status** | **str** | The management status of the device | [optional] 
**screen_lock_type** | **str** | Screen lock type of the device | [optional] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from okta.models.device_user import DeviceUser

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUser from a JSON string
device_user_instance = DeviceUser.from_json(json)
# print the JSON string representation of the object
print(DeviceUser.to_json())

# convert the object into a dict
device_user_dict = device_user_instance.to_dict()
# create an instance of DeviceUser from a dict
device_user_from_dict = DeviceUser.from_dict(device_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


