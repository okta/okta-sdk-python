# ResourceSetBindingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | &#x60;id&#x60; of the role resource set binding | [optional] 
**links** | [**ResourceSetBindingResponseLinks**](ResourceSetBindingResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_binding_response import ResourceSetBindingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingResponse from a JSON string
resource_set_binding_response_instance = ResourceSetBindingResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingResponse.to_json())

# convert the object into a dict
resource_set_binding_response_dict = resource_set_binding_response_instance.to_dict()
# create an instance of ResourceSetBindingResponse from a dict
resource_set_binding_response_from_dict = ResourceSetBindingResponse.from_dict(resource_set_binding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


