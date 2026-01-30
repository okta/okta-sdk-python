# ResourceSetBindingMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the member was created | [optional] [readonly] 
**id** | **str** | Role resource set binding member ID | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the member was last updated | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_binding_member import ResourceSetBindingMember

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingMember from a JSON string
resource_set_binding_member_instance = ResourceSetBindingMember.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingMember.to_json())

# convert the object into a dict
resource_set_binding_member_dict = resource_set_binding_member_instance.to_dict()
# create an instance of ResourceSetBindingMember from a dict
resource_set_binding_member_from_dict = ResourceSetBindingMember.from_dict(resource_set_binding_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


