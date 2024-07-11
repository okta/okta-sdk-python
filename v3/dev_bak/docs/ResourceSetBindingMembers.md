# ResourceSetBindingMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[ResourceSetBindingMember]**](ResourceSetBindingMember.md) |  | [optional] 
**links** | [**ResourceSetBindingMembersLinks**](ResourceSetBindingMembersLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_set_binding_members import ResourceSetBindingMembers

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingMembers from a JSON string
resource_set_binding_members_instance = ResourceSetBindingMembers.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingMembers.to_json())

# convert the object into a dict
resource_set_binding_members_dict = resource_set_binding_members_instance.to_dict()
# create an instance of ResourceSetBindingMembers from a dict
resource_set_binding_members_from_dict = ResourceSetBindingMembers.from_dict(resource_set_binding_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


