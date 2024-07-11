# DomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_source_type** | [**DomainCertificateSourceType**](DomainCertificateSourceType.md) |  | 
**domain** | **str** | Custom domain name | 

## Example

```python
from okta.models.domain_request import DomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRequest from a JSON string
domain_request_instance = DomainRequest.from_json(json)
# print the JSON string representation of the object
print(DomainRequest.to_json())

# convert the object into a dict
domain_request_dict = domain_request_instance.to_dict()
# create an instance of DomainRequest from a dict
domain_request_from_dict = DomainRequest.from_dict(domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


