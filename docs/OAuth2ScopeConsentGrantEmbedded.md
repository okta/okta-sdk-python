# OAuth2ScopeConsentGrantEmbedded

Embedded resources related to the Grant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**OAuth2ScopeConsentGrantEmbeddedScope**](OAuth2ScopeConsentGrantEmbeddedScope.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_scope_consent_grant_embedded import OAuth2ScopeConsentGrantEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ScopeConsentGrantEmbedded from a JSON string
o_auth2_scope_consent_grant_embedded_instance = OAuth2ScopeConsentGrantEmbedded.from_json(json)
# print the JSON string representation of the object
print(OAuth2ScopeConsentGrantEmbedded.to_json())

# convert the object into a dict
o_auth2_scope_consent_grant_embedded_dict = o_auth2_scope_consent_grant_embedded_instance.to_dict()
# create an instance of OAuth2ScopeConsentGrantEmbedded from a dict
o_auth2_scope_consent_grant_embedded_from_dict = OAuth2ScopeConsentGrantEmbedded.from_dict(o_auth2_scope_consent_grant_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


