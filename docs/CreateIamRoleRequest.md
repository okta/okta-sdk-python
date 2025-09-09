# CreateIamRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the role | 
**label** | **str** | Unique label for the role | 
**permissions** | [**List[RolePermissionType]**](RolePermissionType.md) | Array of permissions that the role will grant. See [Permission Types](https://developer.okta.com/docs/concepts/role-assignment/#permission-types). | 

## Example

```python
from okta.models.create_iam_role_request import CreateIamRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIamRoleRequest from a JSON string
create_iam_role_request_instance = CreateIamRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateIamRoleRequest.to_json())

# convert the object into a dict
create_iam_role_request_dict = create_iam_role_request_instance.to_dict()
# create an instance of CreateIamRoleRequest from a dict
create_iam_role_request_from_dict = CreateIamRoleRequest.from_dict(create_iam_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


