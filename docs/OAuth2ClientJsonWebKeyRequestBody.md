# OAuth2ClientJsonWebKeyRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Algorithm used in the key | [optional] 
**e** | **str** | RSA key value (exponent) for key binding | [optional] 
**kid** | **str** | Unique identifier of the JSON Web Key in the OAUth 2.0 Client&#39;s JWKS | [optional] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | [optional] 
**n** | **str** | RSA key value (modulus) for key binding | [optional] 
**status** | **str** | Status of the OAuth 2.0 Client JSON Web Key | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key | [optional] 

## Example

```python
from okta.models.o_auth2_client_json_web_key_request_body import OAuth2ClientJsonWebKeyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientJsonWebKeyRequestBody from a JSON string
o_auth2_client_json_web_key_request_body_instance = OAuth2ClientJsonWebKeyRequestBody.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientJsonWebKeyRequestBody.to_json())

# convert the object into a dict
o_auth2_client_json_web_key_request_body_dict = o_auth2_client_json_web_key_request_body_instance.to_dict()
# create an instance of OAuth2ClientJsonWebKeyRequestBody from a dict
o_auth2_client_json_web_key_request_body_from_dict = OAuth2ClientJsonWebKeyRequestBody.from_dict(o_auth2_client_json_web_key_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


