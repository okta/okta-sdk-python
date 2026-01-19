# LogIssuer

Describes the issuer of the authorization server when the authentication is performed through OAuth. This is the location where well-known resources regarding the details of the authorization servers are published.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Varies depending on the type of authentication. If authentication is SAML 2.0, &#x60;id&#x60; is the issuer in the SAML assertion. For social login, &#x60;id&#x60; is the issuer of the token. | [optional] [readonly] 
**type** | **str** | Information on the &#x60;issuer&#x60; and source of the SAML assertion or token | [optional] [readonly] 

## Example

```python
from okta.models.log_issuer import LogIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of LogIssuer from a JSON string
log_issuer_instance = LogIssuer.from_json(json)
# print the JSON string representation of the object
print(LogIssuer.to_json())

# convert the object into a dict
log_issuer_dict = log_issuer_instance.to_dict()
# create an instance of LogIssuer from a dict
log_issuer_from_dict = LogIssuer.from_dict(log_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


