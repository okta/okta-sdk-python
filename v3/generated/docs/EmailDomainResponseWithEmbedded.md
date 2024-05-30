# EmailDomainResponseWithEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | **object** |  | [optional] [readonly] 
**dns_validation_records** | [**List[EmailDomainDNSRecord]**](EmailDomainDNSRecord.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**validation_status** | [**EmailDomainStatus**](EmailDomainStatus.md) |  | [optional] 
**display_name** | **str** |  | 
**user_name** | **str** |  | 

## Example

```python
from openapi_client.models.email_domain_response_with_embedded import EmailDomainResponseWithEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomainResponseWithEmbedded from a JSON string
email_domain_response_with_embedded_instance = EmailDomainResponseWithEmbedded.from_json(json)
# print the JSON string representation of the object
print(EmailDomainResponseWithEmbedded.to_json())

# convert the object into a dict
email_domain_response_with_embedded_dict = email_domain_response_with_embedded_instance.to_dict()
# create an instance of EmailDomainResponseWithEmbedded from a dict
email_domain_response_with_embedded_form_dict = email_domain_response_with_embedded.from_dict(email_domain_response_with_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


