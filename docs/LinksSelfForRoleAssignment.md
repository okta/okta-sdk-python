# LinksSelfForRoleAssignment

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 

## Example

```python
from okta.models.links_self_for_role_assignment import LinksSelfForRoleAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of LinksSelfForRoleAssignment from a JSON string
links_self_for_role_assignment_instance = LinksSelfForRoleAssignment.from_json(json)
# print the JSON string representation of the object
print(LinksSelfForRoleAssignment.to_json())

# convert the object into a dict
links_self_for_role_assignment_dict = links_self_for_role_assignment_instance.to_dict()
# create an instance of LinksSelfForRoleAssignment from a dict
links_self_for_role_assignment_from_dict = LinksSelfForRoleAssignment.from_dict(links_self_for_role_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


