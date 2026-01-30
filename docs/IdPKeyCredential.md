# IdPKeyCredential

A [JSON Web Key](https://tools.ietf.org/html/rfc7517) for a signature or encryption credential for an IdP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**e** | **str** | The exponent value for the RSA public key | [optional] 
**expires_at** | **datetime** | Timestamp when the object expires | [optional] [readonly] 
**kid** | **str** | Unique identifier for the key | [optional] 
**kty** | **str** | Identifies the cryptographic algorithm family used with the key | [optional] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**n** | **str** | The modulus value for the RSA public key | [optional] 
**use** | **str** | Intended use of the public key | [optional] 
**x5c** | **List[str]** | Base64-encoded X.509 certificate chain with DER encoding | [optional] 
**x5t_s256** | **str** | Base64url-encoded SHA-256 thumbprint of the DER encoding of an X.509 certificate | [optional] 

## Example

```python
from okta.models.id_p_key_credential import IdPKeyCredential

# TODO update the JSON string below
json = "{}"
# create an instance of IdPKeyCredential from a JSON string
id_p_key_credential_instance = IdPKeyCredential.from_json(json)
# print the JSON string representation of the object
print(IdPKeyCredential.to_json())

# convert the object into a dict
id_p_key_credential_dict = id_p_key_credential_instance.to_dict()
# create an instance of IdPKeyCredential from a dict
id_p_key_credential_from_dict = IdPKeyCredential.from_dict(id_p_key_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


