# RoleAssignedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the user | [optional] [readonly] 
**orn** | **str** | ORN representing the assignee | [optional] [readonly] 
**links** | [**LinksSelfAndRoles**](LinksSelfAndRoles.md) |  | [optional] 

## Example

```python
from okta.models.role_assigned_user import RoleAssignedUser

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignedUser from a JSON string
role_assigned_user_instance = RoleAssignedUser.from_json(json)
# print the JSON string representation of the object
print(RoleAssignedUser.to_json())

# convert the object into a dict
role_assigned_user_dict = role_assigned_user_instance.to_dict()
# create an instance of RoleAssignedUser from a dict
role_assigned_user_from_dict = RoleAssignedUser.from_dict(role_assigned_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


