# UpdateIamRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the role | 
**label** | **str** | Unique label for the role | 

## Example

```python
from openapi_client.models.update_iam_role_request import UpdateIamRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIamRoleRequest from a JSON string
update_iam_role_request_instance = UpdateIamRoleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateIamRoleRequest.to_json())

# convert the object into a dict
update_iam_role_request_dict = update_iam_role_request_instance.to_dict()
# create an instance of UpdateIamRoleRequest from a dict
update_iam_role_request_form_dict = update_iam_role_request.from_dict(update_iam_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


