# OAuthResourceServerKeyLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of a JSON Web Key using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources and lifecycle operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | [**HrefObjectActivateLink**](HrefObjectActivateLink.md) |  | [optional] 
**delete** | [**HrefObjectDeleteLink**](HrefObjectDeleteLink.md) |  | [optional] 

## Example

```python
from okta.models.o_auth_resource_server_key_links import OAuthResourceServerKeyLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthResourceServerKeyLinks from a JSON string
o_auth_resource_server_key_links_instance = OAuthResourceServerKeyLinks.from_json(json)
# print the JSON string representation of the object
print(OAuthResourceServerKeyLinks.to_json())

# convert the object into a dict
o_auth_resource_server_key_links_dict = o_auth_resource_server_key_links_instance.to_dict()
# create an instance of OAuthResourceServerKeyLinks from a dict
o_auth_resource_server_key_links_from_dict = OAuthResourceServerKeyLinks.from_dict(o_auth_resource_server_key_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


