# ResourceSetBindingMembersLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**HrefObject**](HrefObject.md) |  | [optional] 
**binding** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_set_binding_members_links import ResourceSetBindingMembersLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingMembersLinks from a JSON string
resource_set_binding_members_links_instance = ResourceSetBindingMembersLinks.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingMembersLinks.to_json())

# convert the object into a dict
resource_set_binding_members_links_dict = resource_set_binding_members_links_instance.to_dict()
# create an instance of ResourceSetBindingMembersLinks from a dict
resource_set_binding_members_links_from_dict = ResourceSetBindingMembersLinks.from_dict(resource_set_binding_members_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


