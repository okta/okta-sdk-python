# ResourceSetResourcesLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**HrefObject**](HrefObject.md) |  | [optional] 
**resource_set** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_resources_links import ResourceSetResourcesLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetResourcesLinks from a JSON string
resource_set_resources_links_instance = ResourceSetResourcesLinks.from_json(json)
# print the JSON string representation of the object
print(ResourceSetResourcesLinks.to_json())

# convert the object into a dict
resource_set_resources_links_dict = resource_set_resources_links_instance.to_dict()
# create an instance of ResourceSetResourcesLinks from a dict
resource_set_resources_links_from_dict = ResourceSetResourcesLinks.from_dict(resource_set_resources_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


