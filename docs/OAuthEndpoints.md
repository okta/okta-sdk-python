# OAuthEndpoints

The `OAUTH2` and `OIDC` protocols support the `authorization` and `token` endpoints. Also, the `OIDC` protocol supports the `userInfo` and `jwks` endpoints.  The IdP Authorization Server (AS) endpoints are currently defined as part of the [IdP provider]((https://developer.okta.com/docs/api/openapi/okta-management/management/tag/IdentityProvider/#tag/IdentityProvider/operation/createIdentityProvider!path=type&t=request)) and are read-only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**OAuthAuthorizationEndpoint**](OAuthAuthorizationEndpoint.md) |  | [optional] 
**jwks** | [**OidcJwksEndpoint**](OidcJwksEndpoint.md) |  | [optional] 
**slo** | [**OidcSloEndpoint**](OidcSloEndpoint.md) |  | [optional] 
**token** | [**OAuthTokenEndpoint**](OAuthTokenEndpoint.md) |  | [optional] 
**user_info** | [**OidcUserInfoEndpoint**](OidcUserInfoEndpoint.md) |  | [optional] 

## Example

```python
from okta.models.o_auth_endpoints import OAuthEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthEndpoints from a JSON string
o_auth_endpoints_instance = OAuthEndpoints.from_json(json)
# print the JSON string representation of the object
print(OAuthEndpoints.to_json())

# convert the object into a dict
o_auth_endpoints_dict = o_auth_endpoints_instance.to_dict()
# create an instance of OAuthEndpoints from a dict
o_auth_endpoints_from_dict = OAuthEndpoints.from_dict(o_auth_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


