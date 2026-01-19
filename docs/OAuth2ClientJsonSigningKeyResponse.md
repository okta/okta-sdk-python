# OAuth2ClientJsonSigningKeyResponse

A [JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517) is a JSON representation of a cryptographic key. Okta uses signing keys to verify the signature of a JWT when provided for the `private_key_jwt` client authentication method or for a signed authorize request object. Okta supports both RSA and Elliptic Curve (EC) keys for signing tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the OAuth Client JSON Web Key | [readonly] 
**created** | **str** | Timestamp when the OAuth 2.0 client JSON Web Key was created | [readonly] 
**last_updated** | **str** | Timestamp when the OAuth 2.0 client JSON Web Key was updated | [readonly] 
**links** | [**OAuthClientSecretLinks**](OAuthClientSecretLinks.md) |  | [optional] 
**kid** | **str** | Unique identifier of the JSON Web Key in the OAuth 2.0 client&#39;s JWKS | [optional] 
**status** | **str** | Status of the OAuth 2.0 client JSON Web Key | [optional] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | 
**alg** | **str** | Algorithm used in the key | 
**use** | **str** | Acceptable use of the JSON Web Key | 

## Example

```python
from okta.models.o_auth2_client_json_signing_key_response import OAuth2ClientJsonSigningKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientJsonSigningKeyResponse from a JSON string
o_auth2_client_json_signing_key_response_instance = OAuth2ClientJsonSigningKeyResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientJsonSigningKeyResponse.to_json())

# convert the object into a dict
o_auth2_client_json_signing_key_response_dict = o_auth2_client_json_signing_key_response_instance.to_dict()
# create an instance of OAuth2ClientJsonSigningKeyResponse from a dict
o_auth2_client_json_signing_key_response_from_dict = OAuth2ClientJsonSigningKeyResponse.from_dict(o_auth2_client_json_signing_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


