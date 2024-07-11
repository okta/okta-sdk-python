# OAuth2ScopeConsentGrant

Grant object that represents an app consent scope grant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client ID of the app integration | [optional] [readonly] 
**created** | **datetime** | Timestamp when the Grant object was created | [optional] [readonly] 
**created_by** | [**OAuth2Actor**](OAuth2Actor.md) |  | [optional] 
**id** | **str** | ID of the Grant object | [optional] [readonly] 
**issuer** | **str** | The issuer of your org authorization server. This is typically your Okta domain. | 
**last_updated** | **datetime** | Timestamp when the Grant object was last updated | [optional] [readonly] 
**scope_id** | **str** | The name of the [Okta scope](https://developer.okta.com/docs/api/oauth2/#oauth-20-scopes) for which consent is granted | 
**source** | [**OAuth2ScopeConsentGrantSource**](OAuth2ScopeConsentGrantSource.md) |  | [optional] 
**status** | [**GrantOrTokenStatus**](GrantOrTokenStatus.md) |  | [optional] 
**user_id** | **str** | User ID that granted consent (if &#x60;source&#x60; is &#x60;END_USER&#x60;) | [optional] [readonly] 
**embedded** | [**OAuth2ScopeConsentGrantEmbedded**](OAuth2ScopeConsentGrantEmbedded.md) |  | [optional] 
**links** | [**OAuth2ScopeConsentGrantLinks**](OAuth2ScopeConsentGrantLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ScopeConsentGrant from a JSON string
o_auth2_scope_consent_grant_instance = OAuth2ScopeConsentGrant.from_json(json)
# print the JSON string representation of the object
print(OAuth2ScopeConsentGrant.to_json())

# convert the object into a dict
o_auth2_scope_consent_grant_dict = o_auth2_scope_consent_grant_instance.to_dict()
# create an instance of OAuth2ScopeConsentGrant from a dict
o_auth2_scope_consent_grant_from_dict = OAuth2ScopeConsentGrant.from_dict(o_auth2_scope_consent_grant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


