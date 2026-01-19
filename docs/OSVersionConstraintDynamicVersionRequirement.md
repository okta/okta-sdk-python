# OSVersionConstraintDynamicVersionRequirement

Contains the necessary properties for a dynamic Windows version requirement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates the type of the dynamic Windows version requirement | [optional] 
**distance_from_latest_major** | **int** | Indicates the distance from the latest Windows major version | [optional] 
**latest_security_patch** | **bool** | Indicates whether the policy requires Windows devices to be on the latest security patch | [optional] 

## Example

```python
from okta.models.os_version_constraint_dynamic_version_requirement import OSVersionConstraintDynamicVersionRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of OSVersionConstraintDynamicVersionRequirement from a JSON string
os_version_constraint_dynamic_version_requirement_instance = OSVersionConstraintDynamicVersionRequirement.from_json(json)
# print the JSON string representation of the object
print(OSVersionConstraintDynamicVersionRequirement.to_json())

# convert the object into a dict
os_version_constraint_dynamic_version_requirement_dict = os_version_constraint_dynamic_version_requirement_instance.to_dict()
# create an instance of OSVersionConstraintDynamicVersionRequirement from a dict
os_version_constraint_dynamic_version_requirement_from_dict = OSVersionConstraintDynamicVersionRequirement.from_dict(os_version_constraint_dynamic_version_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


