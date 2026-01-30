# ResourceSetResourcePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**ResourceConditions**](ResourceConditions.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_resource_put_request import ResourceSetResourcePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetResourcePutRequest from a JSON string
resource_set_resource_put_request_instance = ResourceSetResourcePutRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceSetResourcePutRequest.to_json())

# convert the object into a dict
resource_set_resource_put_request_dict = resource_set_resource_put_request_instance.to_dict()
# create an instance of ResourceSetResourcePutRequest from a dict
resource_set_resource_put_request_from_dict = ResourceSetResourcePutRequest.from_dict(resource_set_resource_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


