# LinksSelf

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of an application using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources and lifecycle operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 

## Example

```python
from openapi_client.models.links_self import LinksSelf

# TODO update the JSON string below
json = "{}"
# create an instance of LinksSelf from a JSON string
links_self_instance = LinksSelf.from_json(json)
# print the JSON string representation of the object
print(LinksSelf.to_json())

# convert the object into a dict
links_self_dict = links_self_instance.to_dict()
# create an instance of LinksSelf from a dict
links_self_form_dict = links_self.from_dict(links_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


