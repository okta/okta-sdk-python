# OAuth2ScopeConsentGrantLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**app** | [**HrefObject**](HrefObject.md) | Link to app | [optional] 
**client** | [**HrefObject**](HrefObject.md) | Link to client | [optional] 

## Example

```python
from openapi_client.models.o_auth2_scope_consent_grant_links import OAuth2ScopeConsentGrantLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ScopeConsentGrantLinks from a JSON string
o_auth2_scope_consent_grant_links_instance = OAuth2ScopeConsentGrantLinks.from_json(json)
# print the JSON string representation of the object
print(OAuth2ScopeConsentGrantLinks.to_json())

# convert the object into a dict
o_auth2_scope_consent_grant_links_dict = o_auth2_scope_consent_grant_links_instance.to_dict()
# create an instance of OAuth2ScopeConsentGrantLinks from a dict
o_auth2_scope_consent_grant_links_form_dict = o_auth2_scope_consent_grant_links.from_dict(o_auth2_scope_consent_grant_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


