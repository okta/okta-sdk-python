# ECKeyJWK

Elliptic curve key in JSON Web Key (JWK) format. It's used during enrollment to encrypt fulfillment requests to Yubico, or during activation to verify Yubico's JWS (JSON Web Signature) objects in fulfillment responses. The currently agreed protocol uses P-384.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crv** | **str** | The elliptic curve protocol | 
**kid** | **str** | The unique identifier of the key | 
**kty** | **str** | The type of public key | 
**use** | **str** | The intended use for the key. This value is either &#x60;enc&#x60; (encryption) during enrollment, when Okta uses the ECKeyJWK to encrypt requests to Yubico. Or it&#39;s &#x60;sig&#x60; (signature) during activation, when Okta uses the ECKeyJWK to verify the responses from Yubico. | 
**x** | **str** | The public x coordinate for the elliptic curve point | 
**y** | **str** | The public y coordinate for the elliptic curve point | 

## Example

```python
from okta.models.ec_key_jwk import ECKeyJWK

# TODO update the JSON string below
json = "{}"
# create an instance of ECKeyJWK from a JSON string
ec_key_jwk_instance = ECKeyJWK.from_json(json)
# print the JSON string representation of the object
print(ECKeyJWK.to_json())

# convert the object into a dict
ec_key_jwk_dict = ec_key_jwk_instance.to_dict()
# create an instance of ECKeyJWK from a dict
ec_key_jwk_from_dict = ECKeyJWK.from_dict(ec_key_jwk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


