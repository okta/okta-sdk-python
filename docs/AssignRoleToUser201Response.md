# AssignRoleToUser201Response


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
from okta.models.assign_role_to_user201_response import AssignRoleToUser201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRoleToUser201Response from a JSON string
assign_role_to_user201_response_instance = AssignRoleToUser201Response.from_json(json)
# print the JSON string representation of the object
print(AssignRoleToUser201Response.to_json())

# convert the object into a dict
assign_role_to_user201_response_dict = assign_role_to_user201_response_instance.to_dict()
# create an instance of AssignRoleToUser201Response from a dict
assign_role_to_user201_response_from_dict = AssignRoleToUser201Response.from_dict(assign_role_to_user201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


