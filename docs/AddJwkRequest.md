# AddJwkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | Unique identifier of the JSON Web Key in the OAUth 2.0 client&#39;s JWKS | [optional] 
**status** | **str** | Status of the OAuth 2.0 client JSON Web Key | [optional] [default to 'ACTIVE']
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | [optional] 
**alg** | **str** | Algorithm used in the key | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key | [optional] 
**discriminator** | **object** |  | [optional] 
**e** | **str** | RSA key value (exponent) for key binding | [optional] 
**n** | **str** | RSA key value (modulus) for key binding | [optional] 

## Example

```python
from okta.models.add_jwk_request import AddJwkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddJwkRequest from a JSON string
add_jwk_request_instance = AddJwkRequest.from_json(json)
# print the JSON string representation of the object
print(AddJwkRequest.to_json())

# convert the object into a dict
add_jwk_request_dict = add_jwk_request_instance.to_dict()
# create an instance of AddJwkRequest from a dict
add_jwk_request_from_dict = AddJwkRequest.from_dict(add_jwk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


