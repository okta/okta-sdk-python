# OAuthCredentialsClient

OAuth 2.0 and OpenID Connect Client object > **Note:** You must complete client registration with the IdP Authorization Server for your Okta IdP instance to obtain client credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The [Unique identifier](https://tools.ietf.org/html/rfc6749#section-2.2) issued by the AS for the Okta IdP instance | [optional] 
**client_secret** | **str** | The [Client secret](https://tools.ietf.org/html/rfc6749#section-2.3.1) issued by the AS for the Okta IdP instance | [optional] 
**pkce_required** | **bool** | Require Proof Key for Code Exchange (PKCE) for additional verification | [optional] 
**token_endpoint_auth_method** | **str** | Client authentication methods supported by the token endpoint | [optional] 

## Example

```python
from okta.models.o_auth_credentials_client import OAuthCredentialsClient

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthCredentialsClient from a JSON string
o_auth_credentials_client_instance = OAuthCredentialsClient.from_json(json)
# print the JSON string representation of the object
print(OAuthCredentialsClient.to_json())

# convert the object into a dict
o_auth_credentials_client_dict = o_auth_credentials_client_instance.to_dict()
# create an instance of OAuthCredentialsClient from a dict
o_auth_credentials_client_from_dict = OAuthCredentialsClient.from_dict(o_auth_credentials_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


