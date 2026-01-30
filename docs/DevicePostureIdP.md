# DevicePostureIdP

<x-lifecycle-container><x-lifecycle class=\"oie\"></x-lifecycle></x-lifecycle-container>Device Posture IdP provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliant** | **bool** | Indicates whether the device is compliant according to the custom IDP | [optional] 
**managed** | **bool** | Indicates whether the device is managed according to the custom IDP | [optional] 

## Example

```python
from okta.models.device_posture_id_p import DevicePostureIdP

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePostureIdP from a JSON string
device_posture_id_p_instance = DevicePostureIdP.from_json(json)
# print the JSON string representation of the object
print(DevicePostureIdP.to_json())

# convert the object into a dict
device_posture_id_p_dict = device_posture_id_p_instance.to_dict()
# create an instance of DevicePostureIdP from a dict
device_posture_id_p_from_dict = DevicePostureIdP.from_dict(device_posture_id_p_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


