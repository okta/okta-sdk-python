# AttestationRootCertificatesRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x5c** | **str** | X.509 certificate chain | [optional] 

## Example

```python
from okta.models.attestation_root_certificates_request_inner import AttestationRootCertificatesRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of AttestationRootCertificatesRequestInner from a JSON string
attestation_root_certificates_request_inner_instance = AttestationRootCertificatesRequestInner.from_json(json)
# print the JSON string representation of the object
print(AttestationRootCertificatesRequestInner.to_json())

# convert the object into a dict
attestation_root_certificates_request_inner_dict = attestation_root_certificates_request_inner_instance.to_dict()
# create an instance of AttestationRootCertificatesRequestInner from a dict
attestation_root_certificates_request_inner_from_dict = AttestationRootCertificatesRequestInner.from_dict(attestation_root_certificates_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


