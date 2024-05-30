# ResourceSetBindingResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**bindings** | [**HrefObject**](HrefObject.md) |  | [optional] 
**resource_set** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_set_binding_response_links import ResourceSetBindingResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingResponseLinks from a JSON string
resource_set_binding_response_links_instance = ResourceSetBindingResponseLinks.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingResponseLinks.to_json())

# convert the object into a dict
resource_set_binding_response_links_dict = resource_set_binding_response_links_instance.to_dict()
# create an instance of ResourceSetBindingResponseLinks from a dict
resource_set_binding_response_links_form_dict = resource_set_binding_response_links.from_dict(resource_set_binding_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


