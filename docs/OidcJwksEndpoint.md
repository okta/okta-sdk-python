# OidcJwksEndpoint

Endpoint for the JSON Web Key Set (JWKS) document. This document contains signing keys that are used to validate the signatures from the provider. For more information on JWKS, see [JSON Web Key](https://tools.ietf.org/html/rfc7517).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | [**ProtocolEndpointBinding**](ProtocolEndpointBinding.md) |  | [optional] 
**url** | **str** | URL of the endpoint to the JWK Set | [optional] 

## Example

```python
from okta.models.oidc_jwks_endpoint import OidcJwksEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of OidcJwksEndpoint from a JSON string
oidc_jwks_endpoint_instance = OidcJwksEndpoint.from_json(json)
# print the JSON string representation of the object
print(OidcJwksEndpoint.to_json())

# convert the object into a dict
oidc_jwks_endpoint_dict = oidc_jwks_endpoint_instance.to_dict()
# create an instance of OidcJwksEndpoint from a dict
oidc_jwks_endpoint_from_dict = OidcJwksEndpoint.from_dict(oidc_jwks_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


