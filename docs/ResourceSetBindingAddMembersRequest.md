# ResourceSetBindingAddMembersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | **List[str]** | A list of member resources to add to the role resource set binding | [optional] 

## Example

```python
from okta.models.resource_set_binding_add_members_request import ResourceSetBindingAddMembersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingAddMembersRequest from a JSON string
resource_set_binding_add_members_request_instance = ResourceSetBindingAddMembersRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingAddMembersRequest.to_json())

# convert the object into a dict
resource_set_binding_add_members_request_dict = resource_set_binding_add_members_request_instance.to_dict()
# create an instance of ResourceSetBindingAddMembersRequest from a dict
resource_set_binding_add_members_request_from_dict = ResourceSetBindingAddMembersRequest.from_dict(resource_set_binding_add_members_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


