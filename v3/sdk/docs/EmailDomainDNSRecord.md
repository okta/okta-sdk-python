# EmailDomainDNSRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** |  | [optional] 
**record_type** | [**EmailDomainDNSRecordType**](EmailDomainDNSRecordType.md) |  | [optional] 
**verification_value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.email_domain_dns_record import EmailDomainDNSRecord

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDomainDNSRecord from a JSON string
email_domain_dns_record_instance = EmailDomainDNSRecord.from_json(json)
# print the JSON string representation of the object
print(EmailDomainDNSRecord.to_json())

# convert the object into a dict
email_domain_dns_record_dict = email_domain_dns_record_instance.to_dict()
# create an instance of EmailDomainDNSRecord from a dict
email_domain_dns_record_from_dict = EmailDomainDNSRecord.from_dict(email_domain_dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


