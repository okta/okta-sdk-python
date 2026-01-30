# ListGroupAssignedRoles200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_type** | [**RoleAssignmentType**](RoleAssignmentType.md) |  | [optional] 
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**id** | **str** | Binding object ID | [optional] [readonly] 
**label** | **str** | Label for the role assignment | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**type** | [**RoleType**](RoleType.md) |  | 
**embedded** | [**StandardRoleEmbedded**](StandardRoleEmbedded.md) |  | [optional] 
**links** | [**LinksCustomRoleResponse**](LinksCustomRoleResponse.md) |  | [optional] 
**resource_set** | **str** | Resource set ID | [optional] [readonly] 
**role** | **str** | Role ID | [optional] [readonly] 

## Example

```python
from okta.models.list_group_assigned_roles200_response_inner import ListGroupAssignedRoles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListGroupAssignedRoles200ResponseInner from a JSON string
list_group_assigned_roles200_response_inner_instance = ListGroupAssignedRoles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListGroupAssignedRoles200ResponseInner.to_json())

# convert the object into a dict
list_group_assigned_roles200_response_inner_dict = list_group_assigned_roles200_response_inner_instance.to_dict()
# create an instance of ListGroupAssignedRoles200ResponseInner from a dict
list_group_assigned_roles200_response_inner_from_dict = ListGroupAssignedRoles200ResponseInner.from_dict(list_group_assigned_roles200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


