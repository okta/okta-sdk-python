# LinksNextForRoleAssignments

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**LinksNextForRoleAssignmentsNext**](LinksNextForRoleAssignmentsNext.md) |  | [optional] 

## Example

```python
from okta.models.links_next_for_role_assignments import LinksNextForRoleAssignments

# TODO update the JSON string below
json = "{}"
# create an instance of LinksNextForRoleAssignments from a JSON string
links_next_for_role_assignments_instance = LinksNextForRoleAssignments.from_json(json)
# print the JSON string representation of the object
print(LinksNextForRoleAssignments.to_json())

# convert the object into a dict
links_next_for_role_assignments_dict = links_next_for_role_assignments_instance.to_dict()
# create an instance of LinksNextForRoleAssignments from a dict
links_next_for_role_assignments_from_dict = LinksNextForRoleAssignments.from_dict(links_next_for_role_assignments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


