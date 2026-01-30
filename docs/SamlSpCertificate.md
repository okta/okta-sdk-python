# SamlSpCertificate

The certificate that Okta uses to validate Single Logout (SLO) requests and responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x5c** | **List[str]** | A list that contains exactly one x509 encoded certificate | [optional] 

## Example

```python
from okta.models.saml_sp_certificate import SamlSpCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of SamlSpCertificate from a JSON string
saml_sp_certificate_instance = SamlSpCertificate.from_json(json)
# print the JSON string representation of the object
print(SamlSpCertificate.to_json())

# convert the object into a dict
saml_sp_certificate_dict = saml_sp_certificate_instance.to_dict()
# create an instance of SamlSpCertificate from a dict
saml_sp_certificate_from_dict = SamlSpCertificate.from_dict(saml_sp_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


