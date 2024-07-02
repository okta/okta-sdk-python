# LinksNext

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of an application using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. Use the `LinksNext` object for dynamic discovery of related resources and lifecycle operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from openapi_client.models.links_next import LinksNext

# TODO update the JSON string below
json = "{}"
# create an instance of LinksNext from a JSON string
links_next_instance = LinksNext.from_json(json)
# print the JSON string representation of the object
print(LinksNext.to_json())

# convert the object into a dict
links_next_dict = links_next_instance.to_dict()
# create an instance of LinksNext from a dict
links_next_from_dict = LinksNext.from_dict(links_next_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


