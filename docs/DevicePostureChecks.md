# DevicePostureChecks

<x-lifecycle-container><x-lifecycle class=\"ea\"></x-lifecycle></x-lifecycle-container>Represents the Device Posture Checks configuration for the device assurance policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | An array of key value pairs including Device Posture Check &#x60;variableNames&#x60; | [optional] 

## Example

```python
from okta.models.device_posture_checks import DevicePostureChecks

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePostureChecks from a JSON string
device_posture_checks_instance = DevicePostureChecks.from_json(json)
# print the JSON string representation of the object
print(DevicePostureChecks.to_json())

# convert the object into a dict
device_posture_checks_dict = device_posture_checks_instance.to_dict()
# create an instance of DevicePostureChecks from a dict
device_posture_checks_from_dict = DevicePostureChecks.from_dict(device_posture_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


