# ResourceSetBindingMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[ResourceSetBindingMember]**](ResourceSetBindingMember.md) | The members of the role resource set binding. If there are more than 100 members for the binding, then the &#x60;_links.next&#x60; resource is returned with the next list of members. | [optional] 
**links** | [**ResourceSetBindingMembersLinks**](ResourceSetBindingMembersLinks.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_binding_members import ResourceSetBindingMembers

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


