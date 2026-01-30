# StandardRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_type** | [**RoleAssignmentType**](RoleAssignmentType.md) |  | [optional] 
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**id** | **str** | Role assignment ID | [optional] [readonly] 
**label** | **str** | Label for the role assignment | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**type** | [**RoleType**](RoleType.md) |  | 
**embedded** | [**StandardRoleEmbedded**](StandardRoleEmbedded.md) |  | [optional] 
**links** | [**LinksAssignee**](LinksAssignee.md) |  | [optional] 

## Example

```python
from okta.models.standard_role import StandardRole

# TODO update the JSON string below
json = "{}"
# create an instance of StandardRole from a JSON string
standard_role_instance = StandardRole.from_json(json)
# print the JSON string representation of the object
print(StandardRole.to_json())

# convert the object into a dict
standard_role_dict = standard_role_instance.to_dict()
# create an instance of StandardRole from a dict
standard_role_from_dict = StandardRole.from_dict(standard_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


