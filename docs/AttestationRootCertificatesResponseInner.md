# AttestationRootCertificatesResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x5c** | **str** | X.509 certificate chain | [optional] 
**x5t_s256** | **str** | SHA-256 hash (thumbprint) of the X.509 certificate | [optional] 
**iss** | **str** | Issuer of certificate | [optional] 
**exp** | **str** | Expiry date of certificate | [optional] 

## Example

```python
from okta.models.attestation_root_certificates_response_inner import AttestationRootCertificatesResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AttestationRootCertificatesResponseInner from a JSON string
attestation_root_certificates_response_inner_instance = AttestationRootCertificatesResponseInner.from_json(json)
# print the JSON string representation of the object
print(AttestationRootCertificatesResponseInner.to_json())

# convert the object into a dict
attestation_root_certificates_response_inner_dict = attestation_root_certificates_response_inner_instance.to_dict()
# create an instance of AttestationRootCertificatesResponseInner from a dict
attestation_root_certificates_response_inner_from_dict = AttestationRootCertificatesResponseInner.from_dict(attestation_root_certificates_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


