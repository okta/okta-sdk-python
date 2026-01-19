# DNSRecordDomains

DNS TXT and CNAME records to be registered for the Domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | **str** | DNS TXT record expiration | [optional] 
**fqdn** | **str** | DNS record name | [optional] 
**record_type** | [**DNSRecordTypeDomains**](DNSRecordTypeDomains.md) |  | [optional] 
**values** | **List[str]** | DNS record value | [optional] 

## Example

```python
from okta.models.dns_record_domains import DNSRecordDomains

# TODO update the JSON string below
json = "{}"
# create an instance of DNSRecordDomains from a JSON string
dns_record_domains_instance = DNSRecordDomains.from_json(json)
# print the JSON string representation of the object
print(DNSRecordDomains.to_json())

# convert the object into a dict
dns_record_domains_dict = dns_record_domains_instance.to_dict()
# create an instance of DNSRecordDomains from a dict
dns_record_domains_from_dict = DNSRecordDomains.from_dict(dns_record_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


