# DomainResponse

The properties that define an individual domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_id** | **str** | The ID number of the brand | [optional] 
**certificate_source_type** | [**DomainCertificateSourceType**](DomainCertificateSourceType.md) |  | [optional] 
**dns_records** | [**List[DNSRecord]**](DNSRecord.md) |  | [optional] 
**domain** | **str** | Custom domain name | [optional] 
**id** | **str** | Unique ID of the domain | [optional] 
**public_certificate** | [**DomainCertificateMetadata**](DomainCertificateMetadata.md) |  | [optional] 
**validation_status** | [**DomainValidationStatus**](DomainValidationStatus.md) |  | [optional] 
**links** | [**DomainLinks**](DomainLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.domain_response import DomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponse from a JSON string
domain_response_instance = DomainResponse.from_json(json)
# print the JSON string representation of the object
print(DomainResponse.to_json())

# convert the object into a dict
domain_response_dict = domain_response_instance.to_dict()
# create an instance of DomainResponse from a dict
domain_response_form_dict = domain_response.from_dict(domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


