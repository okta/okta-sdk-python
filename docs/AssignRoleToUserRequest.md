# AssignRoleToUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Specify a [standard admin role](/openapi/okta-management/guides/roles/#standard-roles), an [IAM-based standard role](/openapi/okta-management/guides/roles/#iam-based-standard-roles), or &#x60;CUSTOM&#x60; for a custom role type: | 
**resource_set** | **str** | Resource set ID | 
**role** | **str** | Custom role ID | 

## Example

```python
from okta.models.assign_role_to_user_request import AssignRoleToUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignRoleToUserRequest from a JSON string
assign_role_to_user_request_instance = AssignRoleToUserRequest.from_json(json)
# print the JSON string representation of the object
print(AssignRoleToUserRequest.to_json())

# convert the object into a dict
assign_role_to_user_request_dict = assign_role_to_user_request_instance.to_dict()
# create an instance of AssignRoleToUserRequest from a dict
assign_role_to_user_request_from_dict = AssignRoleToUserRequest.from_dict(assign_role_to_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


