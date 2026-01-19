# SamlTrustCredentials

Federation Trust Credentials for verifying assertions from the IdP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_kids** | **List[str]** | Additional IdP key credential reference to the Okta X.509 signature certificate | [optional] 
**audience** | **str** | URI that identifies the target Okta IdP instance (SP) for an &#x60;&lt;Assertion&gt;&#x60; | [optional] 
**issuer** | **str** | URI that identifies the issuer (IdP) of a &#x60;&lt;SAMLResponse&gt;&#x60; message &#x60;&lt;Assertion&gt;&#x60; element | [optional] 
**kid** | **str** | IdP key credential reference to the Okta X.509 signature certificate | [optional] 

## Example

```python
from okta.models.saml_trust_credentials import SamlTrustCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SamlTrustCredentials from a JSON string
saml_trust_credentials_instance = SamlTrustCredentials.from_json(json)
# print the JSON string representation of the object
print(SamlTrustCredentials.to_json())

# convert the object into a dict
saml_trust_credentials_dict = saml_trust_credentials_instance.to_dict()
# create an instance of SamlTrustCredentials from a dict
saml_trust_credentials_from_dict = SamlTrustCredentials.from_dict(saml_trust_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


