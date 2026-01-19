# ResourceSetResourceLinksGroups


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
from okta.models.resource_set_resource_links_groups import ResourceSetResourceLinksGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetResourceLinksGroups from a JSON string
resource_set_resource_links_groups_instance = ResourceSetResourceLinksGroups.from_json(json)
# print the JSON string representation of the object
print(ResourceSetResourceLinksGroups.to_json())

# convert the object into a dict
resource_set_resource_links_groups_dict = resource_set_resource_links_groups_instance.to_dict()
# create an instance of ResourceSetResourceLinksGroups from a dict
resource_set_resource_links_groups_from_dict = ResourceSetResourceLinksGroups.from_dict(resource_set_resource_links_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


