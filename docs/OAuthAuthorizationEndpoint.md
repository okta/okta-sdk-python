# OAuthAuthorizationEndpoint

Endpoint for an [OAuth 2.0 Authorization Server (AS)](https://tools.ietf.org/html/rfc6749#page-18)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | [**ProtocolEndpointBinding**](ProtocolEndpointBinding.md) |  | [optional] 
**url** | **str** | URL of the IdP Authorization Server (AS) authorization endpoint | [optional] 

## Example

```python
from okta.models.o_auth_authorization_endpoint import OAuthAuthorizationEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthAuthorizationEndpoint from a JSON string
o_auth_authorization_endpoint_instance = OAuthAuthorizationEndpoint.from_json(json)
# print the JSON string representation of the object
print(OAuthAuthorizationEndpoint.to_json())

# convert the object into a dict
o_auth_authorization_endpoint_dict = o_auth_authorization_endpoint_instance.to_dict()
# create an instance of OAuthAuthorizationEndpoint from a dict
o_auth_authorization_endpoint_from_dict = OAuthAuthorizationEndpoint.from_dict(o_auth_authorization_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


