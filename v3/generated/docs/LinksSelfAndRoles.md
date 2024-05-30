# LinksSelfAndRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**roles** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.links_self_and_roles import LinksSelfAndRoles

# TODO update the JSON string below
json = "{}"
# create an instance of LinksSelfAndRoles from a JSON string
links_self_and_roles_instance = LinksSelfAndRoles.from_json(json)
# print the JSON string representation of the object
print(LinksSelfAndRoles.to_json())

# convert the object into a dict
links_self_and_roles_dict = links_self_and_roles_instance.to_dict()
# create an instance of LinksSelfAndRoles from a dict
links_self_and_roles_form_dict = links_self_and_roles.from_dict(links_self_and_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


