# ResourceSetBindingsLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**next** | [**ResourceSetBindingsLinksAllOfNext**](ResourceSetBindingsLinksAllOfNext.md) |  | [optional] 
**resource_set** | [**HrefObjectResourceSetLink**](HrefObjectResourceSetLink.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_bindings_links import ResourceSetBindingsLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingsLinks from a JSON string
resource_set_bindings_links_instance = ResourceSetBindingsLinks.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingsLinks.to_json())

# convert the object into a dict
resource_set_bindings_links_dict = resource_set_bindings_links_instance.to_dict()
# create an instance of ResourceSetBindingsLinks from a dict
resource_set_bindings_links_from_dict = ResourceSetBindingsLinks.from_dict(resource_set_bindings_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


