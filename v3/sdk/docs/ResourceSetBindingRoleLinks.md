# ResourceSetBindingRoleLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**members** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.resource_set_binding_role_links import ResourceSetBindingRoleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceSetBindingRoleLinks from a JSON string
resource_set_binding_role_links_instance = ResourceSetBindingRoleLinks.from_json(json)
# print the JSON string representation of the object
print(ResourceSetBindingRoleLinks.to_json())

# convert the object into a dict
resource_set_binding_role_links_dict = resource_set_binding_role_links_instance.to_dict()
# create an instance of ResourceSetBindingRoleLinks from a dict
resource_set_binding_role_links_from_dict = ResourceSetBindingRoleLinks.from_dict(resource_set_binding_role_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


