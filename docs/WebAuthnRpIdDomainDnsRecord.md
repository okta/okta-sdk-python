# WebAuthnRpIdDomainDnsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | The DNS record name | [optional] 
**record_type** | [**DNSRecordTypeAuthenticators**](DNSRecordTypeAuthenticators.md) |  | [optional] 
**verification_value** | **str** | The DNS record verification value | [optional] 

## Example

```python
from okta.models.web_authn_rp_id_domain_dns_record import WebAuthnRpIdDomainDnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnRpIdDomainDnsRecord from a JSON string
web_authn_rp_id_domain_dns_record_instance = WebAuthnRpIdDomainDnsRecord.from_json(json)
# print the JSON string representation of the object
print(WebAuthnRpIdDomainDnsRecord.to_json())

# convert the object into a dict
web_authn_rp_id_domain_dns_record_dict = web_authn_rp_id_domain_dns_record_instance.to_dict()
# create an instance of WebAuthnRpIdDomainDnsRecord from a dict
web_authn_rp_id_domain_dns_record_from_dict = WebAuthnRpIdDomainDnsRecord.from_dict(web_authn_rp_id_domain_dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


