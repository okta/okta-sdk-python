# ResourceSetResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**ResourceConditions**](ResourceConditions.md) |  | [optional] 
**created** | **datetime** | Timestamp when the resource set resource object was created | [optional] [readonly] 
**id** | **str** | Unique ID of the resource set resource object | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when this object was last updated | [optional] [readonly] 
**orn** | **str** | The Okta Resource Name (ORN) of the resource | [optional] 
**links** | [**ResourceSetResourceLinks**](ResourceSetResourceLinks.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_resource import ResourceSetResource

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


