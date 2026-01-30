# ResourceSetResourceLinksResource


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
from okta.models.resource_set_resource_links_resource import ResourceSetResourceLinksResource

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetResourceLinksResource from a JSON string
resource_set_resource_links_resource_instance = ResourceSetResourceLinksResource.from_json(json)
# print the JSON string representation of the object
print(ResourceSetResourceLinksResource.to_json())

# convert the object into a dict
resource_set_resource_links_resource_dict = resource_set_resource_links_resource_instance.to_dict()
# create an instance of ResourceSetResourceLinksResource from a dict
resource_set_resource_links_resource_from_dict = ResourceSetResourceLinksResource.from_dict(resource_set_resource_links_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


