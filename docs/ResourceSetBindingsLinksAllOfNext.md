# ResourceSetBindingsLinksAllOfNext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.resource_set_bindings_links_all_of_next import ResourceSetBindingsLinksAllOfNext

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingsLinksAllOfNext from a JSON string
resource_set_bindings_links_all_of_next_instance = ResourceSetBindingsLinksAllOfNext.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingsLinksAllOfNext.to_json())

# convert the object into a dict
resource_set_bindings_links_all_of_next_dict = resource_set_bindings_links_all_of_next_instance.to_dict()
# create an instance of ResourceSetBindingsLinksAllOfNext from a dict
resource_set_bindings_links_all_of_next_from_dict = ResourceSetBindingsLinksAllOfNext.from_dict(resource_set_bindings_links_all_of_next_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


