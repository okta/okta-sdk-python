# DomainCertificateMetadata

Certificate metadata for the domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | **str** | Certificate expiration | [optional] 
**fingerprint** | **str** | Certificate fingerprint | [optional] 
**subject** | **str** | Certificate subject | [optional] 

## Example

```python
from okta.models.domain_certificate_metadata import DomainCertificateMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCertificateMetadata from a JSON string
domain_certificate_metadata_instance = DomainCertificateMetadata.from_json(json)
# print the JSON string representation of the object
print(DomainCertificateMetadata.to_json())

# convert the object into a dict
domain_certificate_metadata_dict = domain_certificate_metadata_instance.to_dict()
# create an instance of DomainCertificateMetadata from a dict
domain_certificate_metadata_from_dict = DomainCertificateMetadata.from_dict(domain_certificate_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


