# DeviceAssurance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] [readonly] 
**created_date** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**last_updated_by** | **str** |  | [optional] [readonly] 
**last_updated_date** | **str** |  | [optional] [readonly] 
**name** | **str** | Display name of the Device Assurance Policy | [optional] 
**platform** | [**Platform**](Platform.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.device_assurance import DeviceAssurance

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAssurance from a JSON string
device_assurance_instance = DeviceAssurance.from_json(json)
# print the JSON string representation of the object
print(DeviceAssurance.to_json())

# convert the object into a dict
device_assurance_dict = device_assurance_instance.to_dict()
# create an instance of DeviceAssurance from a dict
device_assurance_from_dict = DeviceAssurance.from_dict(device_assurance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


