# ResourceSetBindings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[ResourceSetBindingRole]**](ResourceSetBindingRole.md) |  | [optional] 
**links** | [**ResourceSetBindingResponseLinks**](ResourceSetBindingResponseLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_set_bindings import ResourceSetBindings

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindings from a JSON string
resource_set_bindings_instance = ResourceSetBindings.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindings.to_json())

# convert the object into a dict
resource_set_bindings_dict = resource_set_bindings_instance.to_dict()
# create an instance of ResourceSetBindings from a dict
resource_set_bindings_form_dict = resource_set_bindings.from_dict(resource_set_bindings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


