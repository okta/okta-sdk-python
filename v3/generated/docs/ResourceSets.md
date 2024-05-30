# ResourceSets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_sets** | [**List[ResourceSet]**](ResourceSet.md) |  | [optional] 
**links** | [**LinksNext**](LinksNext.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_sets import ResourceSets

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSets from a JSON string
resource_sets_instance = ResourceSets.from_json(json)
# print the JSON string representation of the object
print(ResourceSets.to_json())

# convert the object into a dict
resource_sets_dict = resource_sets_instance.to_dict()
# create an instance of ResourceSets from a dict
resource_sets_form_dict = resource_sets.from_dict(resource_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


