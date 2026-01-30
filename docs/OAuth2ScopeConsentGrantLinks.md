# OAuth2ScopeConsentGrantLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**app** | [**AppResourceHrefObject**](AppResourceHrefObject.md) | Link to the app resource | [optional] 
**client** | [**AppResourceHrefObject**](AppResourceHrefObject.md) | Link to the client resource | [optional] 
**scope** | [**ScopeResourceHrefObject**](ScopeResourceHrefObject.md) | Link to the scope resource | [optional] 
**user** | [**UserResourceHrefObject**](UserResourceHrefObject.md) | Link to the user resource | [optional] 
**authorization_server** | [**AuthorizationServerResourceHrefObject**](AuthorizationServerResourceHrefObject.md) | Link to the authorization server resource | [optional] 

## Example

```python
from okta.models.o_auth2_scope_consent_grant_links import OAuth2ScopeConsentGrantLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ScopeConsentGrantLinks from a JSON string
o_auth2_scope_consent_grant_links_instance = OAuth2ScopeConsentGrantLinks.from_json(json)
# print the JSON string representation of the object
print(OAuth2ScopeConsentGrantLinks.to_json())

# convert the object into a dict
o_auth2_scope_consent_grant_links_dict = o_auth2_scope_consent_grant_links_instance.to_dict()
# create an instance of OAuth2ScopeConsentGrantLinks from a dict
o_auth2_scope_consent_grant_links_from_dict = OAuth2ScopeConsentGrantLinks.from_dict(o_auth2_scope_consent_grant_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


