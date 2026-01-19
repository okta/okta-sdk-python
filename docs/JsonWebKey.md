# JsonWebKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**e** | **str** | RSA key value (public exponent) for Key binding | [optional] [readonly] 
**expires_at** | **datetime** | Timestamp when the certificate expires | [optional] [readonly] 
**kid** | **str** | Unique identifier for the certificate | [optional] [readonly] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s keypair. Valid value: &#x60;RSA&#x60; | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**n** | **str** | RSA modulus value that is used by both the public and private keys and provides a link between them | [optional] 
**use** | **str** | Acceptable use of the certificate. Valid value: &#x60;sig&#x60; | [optional] [readonly] 
**x5c** | **List[str]** | X.509 certificate chain that contains a chain of one or more certificates | [optional] [readonly] 
**x5t_s256** | **str** | X.509 certificate SHA-256 thumbprint, which is the base64url-encoded SHA-256 thumbprint (digest) of the DER encoding of an X.509 certificate | [optional] [readonly] 

## Example

```python
from okta.models.json_web_key import JsonWebKey

# TODO update the JSON string below
json = "{}"
# create an instance of JsonWebKey from a JSON string
json_web_key_instance = JsonWebKey.from_json(json)
# print the JSON string representation of the object
print(JsonWebKey.to_json())

# convert the object into a dict
json_web_key_dict = json_web_key_instance.to_dict()
# create an instance of JsonWebKey from a dict
json_web_key_from_dict = JsonWebKey.from_dict(json_web_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


