# OAuthTokenEndpoint

Endpoint for an [OAuth 2.0 Authorization Server (AS)](https://tools.ietf.org/html/rfc6749#page-18)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | [**ProtocolEndpointBinding**](ProtocolEndpointBinding.md) |  | [optional] 
**url** | **str** | URL of the IdP Authorization Server (AS) token endpoint | [optional] 

## Example

```python
from okta.models.o_auth_token_endpoint import OAuthTokenEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthTokenEndpoint from a JSON string
o_auth_token_endpoint_instance = OAuthTokenEndpoint.from_json(json)
# print the JSON string representation of the object
print(OAuthTokenEndpoint.to_json())

# convert the object into a dict
o_auth_token_endpoint_dict = o_auth_token_endpoint_instance.to_dict()
# create an instance of OAuthTokenEndpoint from a dict
o_auth_token_endpoint_from_dict = OAuthTokenEndpoint.from_dict(o_auth_token_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


