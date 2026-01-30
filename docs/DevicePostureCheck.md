# DevicePostureCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | User who created the device posture check | [optional] [readonly] 
**created_date** | **str** | Time the device posture check was created | [optional] [readonly] 
**description** | **str** | Description of the device posture check | [optional] 
**id** | **str** | The ID of the device posture check | [optional] [readonly] 
**last_update** | **str** | Time the device posture check was updated | [optional] [readonly] 
**last_updated_by** | **str** | User who updated the device posture check | [optional] [readonly] 
**mapping_type** | [**DevicePostureChecksMappingType**](DevicePostureChecksMappingType.md) |  | [optional] 
**name** | **str** | Display name of the device posture check | [optional] 
**platform** | [**DevicePostureChecksPlatform**](DevicePostureChecksPlatform.md) |  | [optional] 
**query** | **str** | OSQuery for the device posture check | [optional] 
**remediation_settings** | [**DevicePostureChecksRemediationSettings**](DevicePostureChecksRemediationSettings.md) |  | [optional] 
**type** | [**DevicePostureChecksType**](DevicePostureChecksType.md) |  | [optional] 
**variable_name** | **str** | Unique name of the device posture check | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.device_posture_check import DevicePostureCheck

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePostureCheck from a JSON string
device_posture_check_instance = DevicePostureCheck.from_json(json)
# print the JSON string representation of the object
print(DevicePostureCheck.to_json())

# convert the object into a dict
device_posture_check_dict = device_posture_check_instance.to_dict()
# create an instance of DevicePostureCheck from a dict
device_posture_check_from_dict = DevicePostureCheck.from_dict(device_posture_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


