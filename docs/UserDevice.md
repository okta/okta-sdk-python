# UserDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the device was created | [optional] [readonly] 
**device** | [**Device**](Device.md) |  | [optional] 
**device_user_id** | **str** | Unique key for the user device link | [optional] 

## Example

```python
from okta.models.user_device import UserDevice

# TODO update the JSON string below
json = "{}"
# create an instance of UserDevice from a JSON string
user_device_instance = UserDevice.from_json(json)
# print the JSON string representation of the object
print(UserDevice.to_json())

# convert the object into a dict
user_device_dict = user_device_instance.to_dict()
# create an instance of UserDevice from a dict
user_device_from_dict = UserDevice.from_dict(user_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


