# OAuth2ClientJsonWebKeyECRequest

An EC signing key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | [optional] 
**x** | **str** | The public x coordinate for the elliptic curve point | 
**y** | **str** | The public y coordinate for the elliptic curve point | 
**crv** | **str** | The cryptographic curve used with the key | 
**kid** | **str** | Unique identifier of the JSON Web Key in the OAuth 2.0 client&#39;s JWKS | [optional] 
**status** | **str** | Status of the OAuth 2.0 client JSON Web Key | [optional] [default to 'ACTIVE']
**alg** | **str** | Algorithm used in the key | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key | [optional] 
**discriminator** | **object** |  | [optional] 

## Example

```python
from okta.models.o_auth2_client_json_web_key_ec_request import OAuth2ClientJsonWebKeyECRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientJsonWebKeyECRequest from a JSON string
o_auth2_client_json_web_key_ec_request_instance = OAuth2ClientJsonWebKeyECRequest.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientJsonWebKeyECRequest.to_json())

# convert the object into a dict
o_auth2_client_json_web_key_ec_request_dict = o_auth2_client_json_web_key_ec_request_instance.to_dict()
# create an instance of OAuth2ClientJsonWebKeyECRequest from a dict
o_auth2_client_json_web_key_ec_request_from_dict = OAuth2ClientJsonWebKeyECRequest.from_dict(o_auth2_client_json_web_key_ec_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


