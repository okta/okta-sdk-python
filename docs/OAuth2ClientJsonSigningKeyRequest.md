# OAuth2ClientJsonSigningKeyRequest

A [JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517) is a JSON representation of a cryptographic key. Okta uses signing keys to verify the signature of a JWT when provided for the `private_key_jwt` client authentication method or for a signed authorize request object. Okta supports both RSA and Elliptic Curve (EC) keys for signing tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | Unique identifier of the JSON Web Key in the OAuth 2.0 client&#39;s JWKS | [optional] 
**status** | **str** | Status of the OAuth 2.0 client JSON Web Key | [optional] [default to 'ACTIVE']
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | [optional] 
**alg** | **str** | Algorithm used in the key | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key | [optional] 
**discriminator** | **object** |  | [optional] 

## Example

```python
from okta.models.o_auth2_client_json_signing_key_request import OAuth2ClientJsonSigningKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientJsonSigningKeyRequest from a JSON string
o_auth2_client_json_signing_key_request_instance = OAuth2ClientJsonSigningKeyRequest.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientJsonSigningKeyRequest.to_json())

# convert the object into a dict
o_auth2_client_json_signing_key_request_dict = o_auth2_client_json_signing_key_request_instance.to_dict()
# create an instance of OAuth2ClientJsonSigningKeyRequest from a dict
o_auth2_client_json_signing_key_request_from_dict = OAuth2ClientJsonSigningKeyRequest.from_dict(o_auth2_client_json_signing_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


