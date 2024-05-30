# CreateUpdateIamRolePermissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **object** | Conditions for further restricting a permission | [optional] 

## Example

```python
from openapi_client.models.create_update_iam_role_permission_request import CreateUpdateIamRolePermissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdateIamRolePermissionRequest from a JSON string
create_update_iam_role_permission_request_instance = CreateUpdateIamRolePermissionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUpdateIamRolePermissionRequest.to_json())

# convert the object into a dict
create_update_iam_role_permission_request_dict = create_update_iam_role_permission_request_instance.to_dict()
# create an instance of CreateUpdateIamRolePermissionRequest from a dict
create_update_iam_role_permission_request_form_dict = create_update_iam_role_permission_request.from_dict(create_update_iam_role_permission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


