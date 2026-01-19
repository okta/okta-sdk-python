# ResourceSetResourcePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**ResourceConditions**](ResourceConditions.md) |  | 
**resource_orn_or_url** | **str** | Resource in ORN or REST API URL format | 

## Example

```python
from okta.models.resource_set_resource_post_request import ResourceSetResourcePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetResourcePostRequest from a JSON string
resource_set_resource_post_request_instance = ResourceSetResourcePostRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceSetResourcePostRequest.to_json())

# convert the object into a dict
resource_set_resource_post_request_dict = resource_set_resource_post_request_instance.to_dict()
# create an instance of ResourceSetResourcePostRequest from a dict
resource_set_resource_post_request_from_dict = ResourceSetResourcePostRequest.from_dict(resource_set_resource_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


