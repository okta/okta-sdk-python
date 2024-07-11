# DomainCertificate

Defines the properties of the certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Certificate content | 
**certificate_chain** | **str** | Certificate chain | 
**private_key** | **str** | Certificate private key | 
**type** | [**DomainCertificateType**](DomainCertificateType.md) |  | 

## Example

```python
from openapi_client.models.domain_certificate import DomainCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCertificate from a JSON string
domain_certificate_instance = DomainCertificate.from_json(json)
# print the JSON string representation of the object
print(DomainCertificate.to_json())

# convert the object into a dict
domain_certificate_dict = domain_certificate_instance.to_dict()
# create an instance of DomainCertificate from a dict
domain_certificate_from_dict = DomainCertificate.from_dict(domain_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


