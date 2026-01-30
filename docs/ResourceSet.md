# ResourceSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the role was created | [optional] [readonly] 
**description** | **str** | Description of the resource set | [optional] 
**id** | **str** | Unique ID for the resource set object | [optional] [readonly] 
**label** | **str** | Unique label for the resource set | [optional] 
**last_updated** | **datetime** | Timestamp when the role was last updated | [optional] [readonly] 
**links** | [**ResourceSetLinks**](ResourceSetLinks.md) |  | [optional] 

## Example

```python
from okta.models.resource_set import ResourceSet

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSet from a JSON string
resource_set_instance = ResourceSet.from_json(json)
# print the JSON string representation of the object
print(ResourceSet.to_json())

# convert the object into a dict
resource_set_dict = resource_set_instance.to_dict()
# create an instance of ResourceSet from a dict
resource_set_from_dict = ResourceSet.from_dict(resource_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


