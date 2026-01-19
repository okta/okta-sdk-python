# ResourceSetLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**resources** | [**HrefObjectResourceSetResourcesLink**](HrefObjectResourceSetResourcesLink.md) |  | [optional] 
**bindings** | [**HrefObjectBindingsLink**](HrefObjectBindingsLink.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_links import ResourceSetLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetLinks from a JSON string
resource_set_links_instance = ResourceSetLinks.from_json(json)
# print the JSON string representation of the object
print(ResourceSetLinks.to_json())

# convert the object into a dict
resource_set_links_dict = resource_set_links_instance.to_dict()
# create an instance of ResourceSetLinks from a dict
resource_set_links_from_dict = ResourceSetLinks.from_dict(resource_set_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


