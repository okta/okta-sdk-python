# IdPCsr

Defines a CSR for a signature or decryption credential for an IdP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**csr** | **str** | Base64-encoded CSR in DER format | [optional] [readonly] 
**id** | **str** | Unique identifier for the CSR | [optional] [readonly] 
**kty** | **str** | Cryptographic algorithm family for the CSR&#39;s keypair | [optional] 
**links** | [**IdPCsrLinks**](IdPCsrLinks.md) |  | [optional] 

## Example

```python
from okta.models.id_p_csr import IdPCsr

# TODO update the JSON string below
json = "{}"
# create an instance of IdPCsr from a JSON string
id_p_csr_instance = IdPCsr.from_json(json)
# print the JSON string representation of the object
print(IdPCsr.to_json())

# convert the object into a dict
id_p_csr_dict = id_p_csr_instance.to_dict()
# create an instance of IdPCsr from a dict
id_p_csr_from_dict = IdPCsr.from_dict(id_p_csr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


