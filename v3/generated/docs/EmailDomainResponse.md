# EmailDomainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_validation_records** | [**List[EmailDomainDNSRecord]**](EmailDomainDNSRecord.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**validation_status** | [**EmailDomainStatus**](EmailDomainStatus.md) |  | [optional] 
**display_name** | **str** |  | 
**user_name** | **str** |  | 

## Example

```python
from openapi_client.models.email_domain_response import EmailDomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomainResponse from a JSON string
email_domain_response_instance = EmailDomainResponse.from_json(json)
# print the JSON string representation of the object
print(EmailDomainResponse.to_json())

# convert the object into a dict
email_domain_response_dict = email_domain_response_instance.to_dict()
# create an instance of EmailDomainResponse from a dict
email_domain_response_form_dict = email_domain_response.from_dict(email_domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


