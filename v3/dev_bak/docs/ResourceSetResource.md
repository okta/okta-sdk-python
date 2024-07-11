# ResourceSetResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the role was created | [optional] [readonly] 
**description** | **str** | Description of the Resource Set | [optional] 
**id** | **str** | Unique key for the role | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the role was last updated | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_set_resource import ResourceSetResource

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetResource from a JSON string
resource_set_resource_instance = ResourceSetResource.from_json(json)
# print the JSON string representation of the object
print(ResourceSetResource.to_json())

# convert the object into a dict
resource_set_resource_dict = resource_set_resource_instance.to_dict()
# create an instance of ResourceSetResource from a dict
resource_set_resource_from_dict = ResourceSetResource.from_dict(resource_set_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


