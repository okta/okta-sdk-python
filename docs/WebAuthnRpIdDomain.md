# WebAuthnRpIdDomain

The RP domain object for the WebAuthn configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_record** | [**WebAuthnRpIdDomainDnsRecord**](WebAuthnRpIdDomainDnsRecord.md) |  | [optional] 
**name** | **str** | The [RP ID](https://www.w3.org/TR/webauthn/#relying-party-identifier) domain value to be used for all WebAuthn operations.  If it isn&#39;t specified, the &#x60;domain&#x60; object isn&#39;t included in the request, and the domain value defaults to the domain of the current page (the domain of your org or a custom domain, for example).  &gt; **Note:** If you don&#39;t use a custom RP ID (the default behavior), the domain value defaults to the end user&#39;s current page. The domain value defaults to the full domain name of the page that the end user is on when they&#39;re attempting the WebAuthn credential operation (enrollment or verification). | [optional] 
**validation_status** | **str** | Indicates the validation status of the domain | [optional] [readonly] 

## Example

```python
from okta.models.web_authn_rp_id_domain import WebAuthnRpIdDomain

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnRpIdDomain from a JSON string
web_authn_rp_id_domain_instance = WebAuthnRpIdDomain.from_json(json)
# print the JSON string representation of the object
print(WebAuthnRpIdDomain.to_json())

# convert the object into a dict
web_authn_rp_id_domain_dict = web_authn_rp_id_domain_instance.to_dict()
# create an instance of WebAuthnRpIdDomain from a dict
web_authn_rp_id_domain_from_dict = WebAuthnRpIdDomain.from_dict(web_authn_rp_id_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


