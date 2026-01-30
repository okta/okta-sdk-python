# DNSRecordAuthenticators

DNS TXT record that must be registered for an RP ID domain that requires verification. This is used to verify the domain ownership for the WebAuthn RP ID configuration. After the domain ownership is verified, the `DNSRecord` isn't returned in the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | The DNS record name | [optional] 
**record_type** | [**DNSRecordTypeAuthenticators**](DNSRecordTypeAuthenticators.md) |  | [optional] 
**verification_value** | **str** | The DNS record verification value | [optional] 

## Example

```python
from okta.models.dns_record_authenticators import DNSRecordAuthenticators

# TODO update the JSON string below
json = "{}"
# create an instance of DNSRecordAuthenticators from a JSON string
dns_record_authenticators_instance = DNSRecordAuthenticators.from_json(json)
# print the JSON string representation of the object
print(DNSRecordAuthenticators.to_json())

# convert the object into a dict
dns_record_authenticators_dict = dns_record_authenticators_instance.to_dict()
# create an instance of DNSRecordAuthenticators from a dict
dns_record_authenticators_from_dict = DNSRecordAuthenticators.from_dict(dns_record_authenticators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


