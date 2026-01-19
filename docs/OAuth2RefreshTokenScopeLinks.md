# OAuth2RefreshTokenScopeLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of an application using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources and lifecycle operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**OfflineAccessScopeResourceHrefObject**](OfflineAccessScopeResourceHrefObject.md) | Link to Scope resource | [optional] 

## Example

```python
from okta.models.o_auth2_refresh_token_scope_links import OAuth2RefreshTokenScopeLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2RefreshTokenScopeLinks from a JSON string
o_auth2_refresh_token_scope_links_instance = OAuth2RefreshTokenScopeLinks.from_json(json)
# print the JSON string representation of the object
print(OAuth2RefreshTokenScopeLinks.to_json())

# convert the object into a dict
o_auth2_refresh_token_scope_links_dict = o_auth2_refresh_token_scope_links_instance.to_dict()
# create an instance of OAuth2RefreshTokenScopeLinks from a dict
o_auth2_refresh_token_scope_links_from_dict = OAuth2RefreshTokenScopeLinks.from_dict(o_auth2_refresh_token_scope_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


