# Embedded

The Public Key Details are defined in the `_embedded` property of the Key object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Algorithm used in the key | [optional] [readonly] 
**e** | **str** | RSA key value (exponent) for key binding | [optional] [readonly] 
**kid** | **str** | Unique identifier for the certificate | [optional] [readonly] 
**kty** | **str** | Cryptographic algorithm family for the certificate&#39;s keypair | [optional] [readonly] 
**n** | **str** | RSA key value (modulus) for key binding | [optional] [readonly] 
**use** | **str** | Acceptable use of the certificate | [optional] [readonly] 

## Example

```python
from okta.models.embedded import Embedded

# TODO update the JSON string below
json = "{}"
# create an instance of Embedded from a JSON string
embedded_instance = Embedded.from_json(json)
# print the JSON string representation of the object
print(Embedded.to_json())

# convert the object into a dict
embedded_dict = embedded_instance.to_dict()
# create an instance of Embedded from a dict
embedded_from_dict = Embedded.from_dict(embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


