# LinkedObjectLinksSelf

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of an application using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources and lifecycle operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**LinkedHrefObject**](LinkedHrefObject.md) |  | [optional] 

## Example

```python
from okta.models.linked_object_links_self import LinkedObjectLinksSelf

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedObjectLinksSelf from a JSON string
linked_object_links_self_instance = LinkedObjectLinksSelf.from_json(json)
# print the JSON string representation of the object
print(LinkedObjectLinksSelf.to_json())

# convert the object into a dict
linked_object_links_self_dict = linked_object_links_self_instance.to_dict()
# create an instance of LinkedObjectLinksSelf from a dict
linked_object_links_self_from_dict = LinkedObjectLinksSelf.from_dict(linked_object_links_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


