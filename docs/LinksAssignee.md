# LinksAssignee

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**HrefObjectAssigneeLink**](HrefObjectAssigneeLink.md) |  | [optional] 

## Example

```python
from okta.models.links_assignee import LinksAssignee

# TODO update the JSON string below
json = "{}"
# create an instance of LinksAssignee from a JSON string
links_assignee_instance = LinksAssignee.from_json(json)
# print the JSON string representation of the object
print(LinksAssignee.to_json())

# convert the object into a dict
links_assignee_dict = links_assignee_instance.to_dict()
# create an instance of LinksAssignee from a dict
links_assignee_from_dict = LinksAssignee.from_dict(links_assignee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


