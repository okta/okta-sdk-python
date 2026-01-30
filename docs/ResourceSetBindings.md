# ResourceSetBindings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[ResourceSetBindingRole]**](ResourceSetBindingRole.md) | Roles associated with the resource set binding. If there are more than 100 bindings for the specified resource set, then the &#x60;_links.next&#x60; resource is returned with the next list of bindings. | [optional] 
**links** | [**ResourceSetBindingsLinks**](ResourceSetBindingsLinks.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_bindings import ResourceSetBindings

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindings from a JSON string
resource_set_bindings_instance = ResourceSetBindings.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindings.to_json())

# convert the object into a dict
resource_set_bindings_dict = resource_set_bindings_instance.to_dict()
# create an instance of ResourceSetBindings from a dict
resource_set_bindings_from_dict = ResourceSetBindings.from_dict(resource_set_bindings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


