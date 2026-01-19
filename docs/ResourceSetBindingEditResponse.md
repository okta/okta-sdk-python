# ResourceSetBindingEditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ResourceSetBindingEditResponseLinks**](ResourceSetBindingEditResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.resource_set_binding_edit_response import ResourceSetBindingEditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingEditResponse from a JSON string
resource_set_binding_edit_response_instance = ResourceSetBindingEditResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingEditResponse.to_json())

# convert the object into a dict
resource_set_binding_edit_response_dict = resource_set_binding_edit_response_instance.to_dict()
# create an instance of ResourceSetBindingEditResponse from a dict
resource_set_binding_edit_response_from_dict = ResourceSetBindingEditResponse.from_dict(resource_set_binding_edit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


