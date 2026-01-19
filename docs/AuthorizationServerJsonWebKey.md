# AuthorizationServerJsonWebKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | The algorithm used with the Key. Valid value: &#x60;RS256&#x60; | [optional] 
**e** | **str** | RSA key value (public exponent) for Key binding | [optional] [readonly] 
**kid** | **str** | Unique identifier for the key | [optional] [readonly] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s keypair. Valid value: &#x60;RSA&#x60; | [optional] [readonly] 
**n** | **str** | RSA modulus value that is used by both the public and private keys and provides a link between them | [optional] 
**status** | **str** | An &#x60;ACTIVE&#x60; Key is used to sign tokens issued by the authorization server. Supported values: &#x60;ACTIVE&#x60;, &#x60;NEXT&#x60;, or &#x60;EXPIRED&#x60;&lt;br&gt; A &#x60;NEXT&#x60; Key is the next Key that the authorization server uses to sign tokens when Keys are rotated. The &#x60;NEXT&#x60; Key might not be listed if it hasn&#39;t been generated. An &#x60;EXPIRED&#x60; Key is the previous Key that the authorization server used to sign tokens. The &#x60;EXPIRED&#x60; Key might not be listed if no Key has expired or the expired Key was deleted. | [optional] 
**use** | **str** | Acceptable use of the key. Valid value: &#x60;sig&#x60; | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.authorization_server_json_web_key import AuthorizationServerJsonWebKey

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerJsonWebKey from a JSON string
authorization_server_json_web_key_instance = AuthorizationServerJsonWebKey.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerJsonWebKey.to_json())

# convert the object into a dict
authorization_server_json_web_key_dict = authorization_server_json_web_key_instance.to_dict()
# create an instance of AuthorizationServerJsonWebKey from a dict
authorization_server_json_web_key_from_dict = AuthorizationServerJsonWebKey.from_dict(authorization_server_json_web_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


