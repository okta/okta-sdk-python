# CustomRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_type** | [**RoleAssignmentType**](RoleAssignmentType.md) |  | [optional] 
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**id** | **str** | Binding object ID | [optional] [readonly] 
**label** | **str** | Label for the role assignment | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**resource_set** | **str** | Resource set ID | [optional] [readonly] 
**role** | **str** | Role ID | [optional] [readonly] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**type** | [**RoleType**](RoleType.md) |  | 
**links** | [**LinksCustomRoleResponse**](LinksCustomRoleResponse.md) |  | [optional] 

## Example

```python
from okta.models.custom_role import CustomRole

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRole from a JSON string
custom_role_instance = CustomRole.from_json(json)
# print the JSON string representation of the object
print(CustomRole.to_json())

# convert the object into a dict
custom_role_dict = custom_role_instance.to_dict()
# create an instance of CustomRole from a dict
custom_role_from_dict = CustomRole.from_dict(custom_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


