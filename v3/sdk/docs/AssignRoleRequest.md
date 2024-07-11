# AssignRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RoleType**](RoleType.md) |  | [optional] 

## Example

```python
from okta.models.assign_role_request import AssignRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRoleRequest from a JSON string
assign_role_request_instance = AssignRoleRequest.from_json(json)
# print the JSON string representation of the object
print(AssignRoleRequest.to_json())

# convert the object into a dict
assign_role_request_dict = assign_role_request_instance.to_dict()
# create an instance of AssignRoleRequest from a dict
assign_role_request_from_dict = AssignRoleRequest.from_dict(assign_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


