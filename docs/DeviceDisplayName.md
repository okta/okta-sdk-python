# DeviceDisplayName

Display name of the device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensitive** | **bool** | Indicates whether the associated value is Personal Identifiable Information (PII) and requires masking | [optional] [default to False]
**value** | **str** | Display name of the device | [optional] 

## Example

```python
from okta.models.device_display_name import DeviceDisplayName

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDisplayName from a JSON string
device_display_name_instance = DeviceDisplayName.from_json(json)
# print the JSON string representation of the object
print(DeviceDisplayName.to_json())

# convert the object into a dict
device_display_name_dict = device_display_name_instance.to_dict()
# create an instance of DeviceDisplayName from a dict
device_display_name_from_dict = DeviceDisplayName.from_dict(device_display_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


