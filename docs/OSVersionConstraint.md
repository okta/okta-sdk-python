# OSVersionConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_version_requirement** | [**OSVersionConstraintDynamicVersionRequirement**](OSVersionConstraintDynamicVersionRequirement.md) |  | [optional] 
**major_version_constraint** | **str** | Indicates the Windows major version | 
**minimum** | **str** | The Windows device version must be equal to or newer than the specified version | [optional] 

## Example

```python
from okta.models.os_version_constraint import OSVersionConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of OSVersionConstraint from a JSON string
os_version_constraint_instance = OSVersionConstraint.from_json(json)
# print the JSON string representation of the object
print(OSVersionConstraint.to_json())

# convert the object into a dict
os_version_constraint_dict = os_version_constraint_instance.to_dict()
# create an instance of OSVersionConstraint from a dict
os_version_constraint_from_dict = OSVersionConstraint.from_dict(os_version_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


