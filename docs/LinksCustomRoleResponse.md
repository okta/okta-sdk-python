# LinksCustomRoleResponse

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**HrefObjectAssigneeLink**](HrefObjectAssigneeLink.md) |  | [optional] 
**member** | [**HrefObjectMemberLink**](HrefObjectMemberLink.md) |  | [optional] 
**permissions** | [**HrefObjectPermissionsLink**](HrefObjectPermissionsLink.md) |  | [optional] 
**resource_set** | [**HrefObjectResourceSetLink**](HrefObjectResourceSetLink.md) |  | [optional] 
**role** | [**HrefObjectRoleLink**](HrefObjectRoleLink.md) |  | [optional] 

## Example

```python
from okta.models.links_custom_role_response import LinksCustomRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinksCustomRoleResponse from a JSON string
links_custom_role_response_instance = LinksCustomRoleResponse.from_json(json)
# print the JSON string representation of the object
print(LinksCustomRoleResponse.to_json())

# convert the object into a dict
links_custom_role_response_dict = links_custom_role_response_instance.to_dict()
# create an instance of LinksCustomRoleResponse from a dict
links_custom_role_response_from_dict = LinksCustomRoleResponse.from_dict(links_custom_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


