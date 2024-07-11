# IdentityProviderLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**acs** | [**HrefObject**](HrefObject.md) | SAML 2.0 Assertion Consumer Service URL for the Okta SP | [optional] 
**authorize** | [**HrefObject**](HrefObject.md) | OAuth 2.0 authorization endpoint for the IdP OAuth 2.0 Authorization Code flow | [optional] 
**client_redirect_uri** | [**HrefObject**](HrefObject.md) | Redirect URI for the OAuth 2.0 Authorization Code flow | [optional] 
**metadata** | [**HrefObject**](HrefObject.md) | Federation metadata document for the IdP (for example: SAML 2.0 Metadata) | [optional] 
**users** | [**HrefObject**](HrefObject.md) | IdP users | [optional] 
**deactivate** | [**HrefObject**](HrefObject.md) | Deactivate IdP | [optional] 
**activate** | [**HrefObject**](HrefObject.md) | Activate IdP | [optional] 
**keys** | [**HrefObject**](HrefObject.md) | IdP keys | [optional] 

## Example

```python
from openapi_client.models.identity_provider_links import IdentityProviderLinks

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderLinks from a JSON string
identity_provider_links_instance = IdentityProviderLinks.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderLinks.to_json())

# convert the object into a dict
identity_provider_links_dict = identity_provider_links_instance.to_dict()
# create an instance of IdentityProviderLinks from a dict
identity_provider_links_from_dict = IdentityProviderLinks.from_dict(identity_provider_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


