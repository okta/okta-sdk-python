# ResourceServerJsonWebKey

A [JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517) is a JSON representation of a cryptographic key. Okta can use the active key to encrypt the access token minted by the authorization server. Okta supports only RSA keys with 'use: enc'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e** | **str** | The key exponent of a RSA key | [optional] 
**kid** | **str** | The unique identifier of the key | [optional] 
**kty** | [**JsonWebKeyType**](JsonWebKeyType.md) |  | [optional] 
**n** | **str** | The modulus of the RSA key | [optional] 
**status** | [**JsonWebKeyStatus**](JsonWebKeyStatus.md) |  | [optional] 
**use** | [**JsonWebKeyUse**](JsonWebKeyUse.md) |  | [optional] 

## Example

```python
from okta.models.resource_server_json_web_key import ResourceServerJsonWebKey

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceServerJsonWebKey from a JSON string
resource_server_json_web_key_instance = ResourceServerJsonWebKey.from_json(json)
# print the JSON string representation of the object
print(ResourceServerJsonWebKey.to_json())

# convert the object into a dict
resource_server_json_web_key_dict = resource_server_json_web_key_instance.to_dict()
# create an instance of ResourceServerJsonWebKey from a dict
resource_server_json_web_key_from_dict = ResourceServerJsonWebKey.from_dict(resource_server_json_web_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


