# ProtocolOAuth

Protocol settings for authentication using the [OAuth 2.0 Authorization Code flow](https://tools.ietf.org/html/rfc6749#section-4.1)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**OAuthCredentials**](OAuthCredentials.md) |  | [optional] 
**endpoints** | [**OAuthEndpoints**](OAuthEndpoints.md) |  | [optional] 
**scopes** | **List[str]** | IdP-defined permission bundles to request delegated access from the user. &gt; **Note:** The [identity provider type](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/createIdentityProvider!path&#x3D;type&amp;t&#x3D;request) table lists the scopes that are supported for each IdP. | [optional] 
**type** | **str** | OAuth 2.0 Authorization Code flow | [optional] 

## Example

```python
from okta.models.protocol_o_auth import ProtocolOAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolOAuth from a JSON string
protocol_o_auth_instance = ProtocolOAuth.from_json(json)
# print the JSON string representation of the object
print(ProtocolOAuth.to_json())

# convert the object into a dict
protocol_o_auth_dict = protocol_o_auth_instance.to_dict()
# create an instance of ProtocolOAuth from a dict
protocol_o_auth_from_dict = ProtocolOAuth.from_dict(protocol_o_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


