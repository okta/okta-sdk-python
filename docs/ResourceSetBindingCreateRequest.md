# ResourceSetBindingCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** |  | [optional] 
**role** | **str** | Unique key for the role | [optional] 

## Example

```python
from okta.models.resource_set_binding_create_request import ResourceSetBindingCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingCreateRequest from a JSON string
resource_set_binding_create_request_instance = ResourceSetBindingCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingCreateRequest.to_json())

# convert the object into a dict
resource_set_binding_create_request_dict = resource_set_binding_create_request_instance.to_dict()
# create an instance of ResourceSetBindingCreateRequest from a dict
resource_set_binding_create_request_from_dict = ResourceSetBindingCreateRequest.from_dict(resource_set_binding_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


