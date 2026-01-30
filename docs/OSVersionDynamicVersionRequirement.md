# OSVersionDynamicVersionRequirement

<x-lifecycle-container><x-lifecycle class=\"ea\"></x-lifecycle></x-lifecycle-container>Contains the necessary properties for a dynamic version requirement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates the type of the dynamic OS version requirement | [optional] 
**distance_from_latest_major** | **int** | Indicates the distance from the latest major version | [optional] 
**latest_security_patch** | **bool** | Indicates whether the device needs to be on the latest security patch | [optional] 

## Example

```python
from okta.models.os_version_dynamic_version_requirement import OSVersionDynamicVersionRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of OSVersionDynamicVersionRequirement from a JSON string
os_version_dynamic_version_requirement_instance = OSVersionDynamicVersionRequirement.from_json(json)
# print the JSON string representation of the object
print(OSVersionDynamicVersionRequirement.to_json())

# convert the object into a dict
os_version_dynamic_version_requirement_dict = os_version_dynamic_version_requirement_instance.to_dict()
# create an instance of OSVersionDynamicVersionRequirement from a dict
os_version_dynamic_version_requirement_from_dict = OSVersionDynamicVersionRequirement.from_dict(os_version_dynamic_version_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


