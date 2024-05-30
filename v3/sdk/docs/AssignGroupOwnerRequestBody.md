# AssignGroupOwnerRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &#x60;id&#x60; of the group owner | [optional] 
**type** | [**GroupOwnerType**](GroupOwnerType.md) |  | [optional] 

## Example

```python
from openapi_client.models.assign_group_owner_request_body import AssignGroupOwnerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AssignGroupOwnerRequestBody from a JSON string
assign_group_owner_request_body_instance = AssignGroupOwnerRequestBody.from_json(json)
# print the JSON string representation of the object
print(AssignGroupOwnerRequestBody.to_json())

# convert the object into a dict
assign_group_owner_request_body_dict = assign_group_owner_request_body_instance.to_dict()
# create an instance of AssignGroupOwnerRequestBody from a dict
assign_group_owner_request_body_form_dict = assign_group_owner_request_body.from_dict(assign_group_owner_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


