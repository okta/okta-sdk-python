# OidcUserInfoEndpoint

Endpoint for getting identity information about the user. For more information on the `/userinfo` endpoint, see [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | [**ProtocolEndpointBinding**](ProtocolEndpointBinding.md) |  | [optional] 
**url** | **str** | URL of the resource server&#39;s &#x60;/userinfo&#x60; endpoint | [optional] 

## Example

```python
from okta.models.oidc_user_info_endpoint import OidcUserInfoEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of OidcUserInfoEndpoint from a JSON string
oidc_user_info_endpoint_instance = OidcUserInfoEndpoint.from_json(json)
# print the JSON string representation of the object
print(OidcUserInfoEndpoint.to_json())

# convert the object into a dict
oidc_user_info_endpoint_dict = oidc_user_info_endpoint_instance.to_dict()
# create an instance of OidcUserInfoEndpoint from a dict
oidc_user_info_endpoint_from_dict = OidcUserInfoEndpoint.from_dict(oidc_user_info_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


