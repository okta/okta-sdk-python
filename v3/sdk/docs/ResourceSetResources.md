# ResourceSetResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[ResourceSetResource]**](ResourceSetResource.md) |  | [optional] 
**links** | [**ResourceSetResourcesLinks**](ResourceSetResourcesLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_set_resources import ResourceSetResources

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetResources from a JSON string
resource_set_resources_instance = ResourceSetResources.from_json(json)
# print the JSON string representation of the object
print(ResourceSetResources.to_json())

# convert the object into a dict
resource_set_resources_dict = resource_set_resources_instance.to_dict()
# create an instance of ResourceSetResources from a dict
resource_set_resources_form_dict = resource_set_resources.from_dict(resource_set_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


