# RoleAssignedUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RoleAssignedUser]**](RoleAssignedUser.md) |  | [optional] 
**links** | [**LinksNextForRoleAssignments**](LinksNextForRoleAssignments.md) |  | [optional] 

## Example

```python
from okta.models.role_assigned_users import RoleAssignedUsers

# TODO update the JSON string below
json = "{}"
# create an instance of RoleAssignedUsers from a JSON string
role_assigned_users_instance = RoleAssignedUsers.from_json(json)
# print the JSON string representation of the object
print(RoleAssignedUsers.to_json())

# convert the object into a dict
role_assigned_users_dict = role_assigned_users_instance.to_dict()
# create an instance of RoleAssignedUsers from a dict
role_assigned_users_from_dict = RoleAssignedUsers.from_dict(role_assigned_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


