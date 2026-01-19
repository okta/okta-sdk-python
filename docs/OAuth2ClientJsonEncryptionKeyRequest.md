# OAuth2ClientJsonEncryptionKeyRequest

<x-lifecycle-container><x-lifecycle class=\"ea\"></x-lifecycle></x-lifecycle-container>A [JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517) is a JSON representation of a cryptographic key. Okta uses an encryption key to encrypt an ID token JWT minted by the org authorization server or custom authorization server. Okta supports only RSA keys for encrypting tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **str** | RSA key value (exponent) for key binding | [optional] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | [optional] 
**n** | **str** | RSA key value (modulus) for key binding | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key | [optional] 
**kid** | **str** | Unique identifier of the JSON Web Key in the OAUth 2.0 client&#39;s JWKS | [optional] 
**status** | **str** | Status of the OAuth 2.0 client JSON Web Key | [optional] [default to 'ACTIVE']

## Example

```python
from okta.models.o_auth2_client_json_encryption_key_request import OAuth2ClientJsonEncryptionKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientJsonEncryptionKeyRequest from a JSON string
o_auth2_client_json_encryption_key_request_instance = OAuth2ClientJsonEncryptionKeyRequest.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientJsonEncryptionKeyRequest.to_json())

# convert the object into a dict
o_auth2_client_json_encryption_key_request_dict = o_auth2_client_json_encryption_key_request_instance.to_dict()
# create an instance of OAuth2ClientJsonEncryptionKeyRequest from a dict
o_auth2_client_json_encryption_key_request_from_dict = OAuth2ClientJsonEncryptionKeyRequest.from_dict(o_auth2_client_json_encryption_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


