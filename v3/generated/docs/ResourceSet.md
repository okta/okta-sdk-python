# ResourceSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the role was created | [optional] [readonly] 
**description** | **str** | Description of the Resource Set | [optional] 
**id** | **str** | Unique key for the role | [optional] [readonly] 
**label** | **str** | Unique label for the Resource Set | [optional] 
**last_updated** | **datetime** | Timestamp when the role was last updated | [optional] [readonly] 
**links** | [**ResourceSetLinks**](ResourceSetLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_set import ResourceSet

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSet from a JSON string
resource_set_instance = ResourceSet.from_json(json)
# print the JSON string representation of the object
print(ResourceSet.to_json())

# convert the object into a dict
resource_set_dict = resource_set_instance.to_dict()
# create an instance of ResourceSet from a dict
resource_set_form_dict = resource_set.from_dict(resource_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


