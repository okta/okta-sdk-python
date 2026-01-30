# IdentityProviderProtocol

IdP-specific protocol settings for endpoints, bindings, and algorithms used to connect with the IdP and validate messages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithms** | [**OidcAlgorithms**](OidcAlgorithms.md) |  | [optional] 
**credentials** | [**IDVCredentials**](IDVCredentials.md) |  | [optional] 
**endpoints** | [**IDVEndpoints**](IDVEndpoints.md) |  | [optional] 
**relay_state** | [**SamlRelayState**](SamlRelayState.md) |  | [optional] 
**settings** | [**OidcSettings**](OidcSettings.md) |  | [optional] 
**type** | **str** | SAML 2.0 protocol | [optional] 
**scopes** | **List[str]** | IdP-defined permission bundles to request delegated access from the user. &gt; **Note:** The [identity provider type](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/createIdentityProvider!path&#x3D;type&amp;t&#x3D;request) table lists the scopes that are supported for each IdP. | [optional] 
**okta_idp_org_url** | **str** | URL of the IdP org | [optional] 

## Example

```python
from okta.models.identity_provider_protocol import IdentityProviderProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderProtocol from a JSON string
identity_provider_protocol_instance = IdentityProviderProtocol.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderProtocol.to_json())

# convert the object into a dict
identity_provider_protocol_dict = identity_provider_protocol_instance.to_dict()
# create an instance of IdentityProviderProtocol from a dict
identity_provider_protocol_from_dict = IdentityProviderProtocol.from_dict(identity_provider_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


