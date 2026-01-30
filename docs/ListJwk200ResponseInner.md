# ListJwk200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **str** | RSA key value (exponent) for key binding | [optional] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | [optional] 
**n** | **str** | RSA key value (modulus) for key binding | [optional] 
**use** | **str** | Acceptable use of the JSON Web Key | [optional] 
**kid** | **str** | Unique identifier of the JSON Web Key in the OAUth 2.0 client&#39;s JWKS | [optional] 
**status** | **str** | Status of the OAuth 2.0 client JSON Web Key | [optional] [default to 'ACTIVE']
**created** | **str** | Timestamp when the OAuth 2.0 client JSON Web Key was created | [optional] [readonly] 
**id** | **str** | The unique ID of the OAuth Client JSON Web Key | [optional] [readonly] 
**last_updated** | **str** | Timestamp when the OAuth 2.0 client JSON Web Key was updated | [optional] [readonly] 
**links** | [**OAuthClientSecretLinks**](OAuthClientSecretLinks.md) |  | [optional] 

## Example

```python
from okta.models.list_jwk200_response_inner import ListJwk200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListJwk200ResponseInner from a JSON string
list_jwk200_response_inner_instance = ListJwk200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListJwk200ResponseInner.to_json())

# convert the object into a dict
list_jwk200_response_inner_dict = list_jwk200_response_inner_instance.to_dict()
# create an instance of ListJwk200ResponseInner from a dict
list_jwk200_response_inner_from_dict = ListJwk200ResponseInner.from_dict(list_jwk200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


