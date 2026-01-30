# OAuth2ResourceServerJsonWebKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | Timestamp when the JSON Web Key was created | [optional] [readonly] 
**e** | **str** | RSA key value (exponent) for key binding | [optional] 
**id** | **str** | The unique ID of the JSON Web Key | [optional] [readonly] 
**kid** | **str** | Unique identifier of the JSON Web Key in the Custom Authorization Server&#39;s Public JWKS | [optional] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s key pair | [optional] 
**last_updated** | **str** | Timestamp when the JSON Web Key was updated | [optional] [readonly] 
**n** | **str** | RSA key value (modulus) for key binding | [optional] 
**status** | **str** | The status of the encryption key. You can use only an &#x60;ACTIVE&#x60; key to encrypt tokens issued by the authorization server. | [optional] [default to 'ACTIVE']
**use** | **str** | Acceptable use of the JSON Web Key | [optional] 
**links** | [**OAuthResourceServerKeyLinks**](OAuthResourceServerKeyLinks.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_resource_server_json_web_key import OAuth2ResourceServerJsonWebKey

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ResourceServerJsonWebKey from a JSON string
o_auth2_resource_server_json_web_key_instance = OAuth2ResourceServerJsonWebKey.from_json(json)
# print the JSON string representation of the object
print(OAuth2ResourceServerJsonWebKey.to_json())

# convert the object into a dict
o_auth2_resource_server_json_web_key_dict = o_auth2_resource_server_json_web_key_instance.to_dict()
# create an instance of OAuth2ResourceServerJsonWebKey from a dict
o_auth2_resource_server_json_web_key_from_dict = OAuth2ResourceServerJsonWebKey.from_dict(o_auth2_resource_server_json_web_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


