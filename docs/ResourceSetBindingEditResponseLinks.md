# ResourceSetBindingEditResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**resource_set** | [**HrefObjectResourceSetLink**](HrefObjectResourceSetLink.md) |  | [optional] 
**bindings** | [**HrefObjectBindingsLink**](HrefObjectBindingsLink.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_binding_edit_response_links import ResourceSetBindingEditResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingEditResponseLinks from a JSON string
resource_set_binding_edit_response_links_instance = ResourceSetBindingEditResponseLinks.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingEditResponseLinks.to_json())

# convert the object into a dict
resource_set_binding_edit_response_links_dict = resource_set_binding_edit_response_links_instance.to_dict()
# create an instance of ResourceSetBindingEditResponseLinks from a dict
resource_set_binding_edit_response_links_from_dict = ResourceSetBindingEditResponseLinks.from_dict(resource_set_binding_edit_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


