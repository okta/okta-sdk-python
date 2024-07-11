# DNSRecord

DNS TXT and CNAME records to be registered for the Domain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | **str** | DNS TXT record expiration | [optional] 
**fqdn** | **str** | DNS record name | [optional] 
**record_type** | [**DNSRecordType**](DNSRecordType.md) |  | [optional] 
**values** | **List[str]** | DNS record value | [optional] 

## Example

```python
from okta.models.dns_record import DNSRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DNSRecord from a JSON string
dns_record_instance = DNSRecord.from_json(json)
# print the JSON string representation of the object
print(DNSRecord.to_json())

# convert the object into a dict
dns_record_dict = dns_record_instance.to_dict()
# create an instance of DNSRecord from a dict
dns_record_from_dict = DNSRecord.from_dict(dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


