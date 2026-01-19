# ProtocolOidc

Protocol settings for authentication using the [OpenID Connect Protocol](http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithms** | [**OidcAlgorithms**](OidcAlgorithms.md) |  | [optional] 
**credentials** | [**OAuthCredentials**](OAuthCredentials.md) |  | [optional] 
**endpoints** | [**OAuthEndpoints**](OAuthEndpoints.md) |  | [optional] 
**okta_idp_org_url** | **str** | URL of the IdP org | [optional] 
**scopes** | **List[str]** | OpenID Connect and IdP-defined permission bundles to request delegated access from the user &gt; **Note:** The [IdP type](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/createIdentityProvider!path&#x3D;type&amp;t&#x3D;request) table lists the scopes that are supported for each IdP. | [optional] 
**settings** | [**OidcSettings**](OidcSettings.md) |  | [optional] 
**type** | **str** | OpenID Connect Authorization Code flow | [optional] 

## Example

```python
from okta.models.protocol_oidc import ProtocolOidc

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolOidc from a JSON string
protocol_oidc_instance = ProtocolOidc.from_json(json)
# print the JSON string representation of the object
print(ProtocolOidc.to_json())

# convert the object into a dict
protocol_oidc_dict = protocol_oidc_instance.to_dict()
# create an instance of ProtocolOidc from a dict
protocol_oidc_from_dict = ProtocolOidc.from_dict(protocol_oidc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


