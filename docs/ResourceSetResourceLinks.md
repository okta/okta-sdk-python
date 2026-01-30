# ResourceSetResourceLinks

Related discoverable resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**ResourceSetResourceLinksSelf**](ResourceSetResourceLinksSelf.md) |  | [optional] 
**resource** | [**ResourceSetResourceLinksResource**](ResourceSetResourceLinksResource.md) |  | [optional] 
**groups** | [**ResourceSetResourceLinksGroups**](ResourceSetResourceLinksGroups.md) |  | [optional] 
**users** | [**ResourceSetResourceLinksUsers**](ResourceSetResourceLinksUsers.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_resource_links import ResourceSetResourceLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetResourceLinks from a JSON string
resource_set_resource_links_instance = ResourceSetResourceLinks.from_json(json)
# print the JSON string representation of the object
print(ResourceSetResourceLinks.to_json())

# convert the object into a dict
resource_set_resource_links_dict = resource_set_resource_links_instance.to_dict()
# create an instance of ResourceSetResourceLinks from a dict
resource_set_resource_links_from_dict = ResourceSetResourceLinks.from_dict(resource_set_resource_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


