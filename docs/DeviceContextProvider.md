# DeviceContextProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the device context provider | [optional] 
**key** | **str** | Identifies the type of device context provider | 
**user_identification** | **str** | Whether or not the device context provider is used to identify the user. &#x60;IGNORE&#x60; prevents the device context provider from being used to authenticate the user. Identification of the device and device context collection happens regardless of this setting. | [optional] 

## Example

```python
from okta.models.device_context_provider import DeviceContextProvider

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceContextProvider from a JSON string
device_context_provider_instance = DeviceContextProvider.from_json(json)
# print the JSON string representation of the object
print(DeviceContextProvider.to_json())

# convert the object into a dict
device_context_provider_dict = device_context_provider_instance.to_dict()
# create an instance of DeviceContextProvider from a dict
device_context_provider_from_dict = DeviceContextProvider.from_dict(device_context_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


