# StandardRoleEmbeddedTargets

Targets configured for the role assignment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[Group]**](Group.md) | Group targets | [optional] 
**catalog** | [**StandardRoleEmbeddedTargetsCatalog**](StandardRoleEmbeddedTargetsCatalog.md) |  | [optional] 

## Example

```python
from okta.models.standard_role_embedded_targets import StandardRoleEmbeddedTargets

# TODO update the JSON string below
json = "{}"
# create an instance of StandardRoleEmbeddedTargets from a JSON string
standard_role_embedded_targets_instance = StandardRoleEmbeddedTargets.from_json(json)
# print the JSON string representation of the object
print(StandardRoleEmbeddedTargets.to_json())

# convert the object into a dict
standard_role_embedded_targets_dict = standard_role_embedded_targets_instance.to_dict()
# create an instance of StandardRoleEmbeddedTargets from a dict
standard_role_embedded_targets_from_dict = StandardRoleEmbeddedTargets.from_dict(standard_role_embedded_targets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


