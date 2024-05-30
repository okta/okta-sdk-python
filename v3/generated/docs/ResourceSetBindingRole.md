# ResourceSetBindingRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**links** | [**ResourceSetBindingRoleLinks**](ResourceSetBindingRoleLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_set_binding_role import ResourceSetBindingRole

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingRole from a JSON string
resource_set_binding_role_instance = ResourceSetBindingRole.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingRole.to_json())

# convert the object into a dict
resource_set_binding_role_dict = resource_set_binding_role_instance.to_dict()
# create an instance of ResourceSetBindingRole from a dict
resource_set_binding_role_form_dict = resource_set_binding_role.from_dict(resource_set_binding_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


