# SamlCredentials

Federation Trust Credentials for verifying assertions from the IdP and signing requests to the IdP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing** | [**SamlSigningCredentials**](SamlSigningCredentials.md) |  | [optional] 
**trust** | [**SamlTrustCredentials**](SamlTrustCredentials.md) |  | [optional] 

## Example

```python
from okta.models.saml_credentials import SamlCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SamlCredentials from a JSON string
saml_credentials_instance = SamlCredentials.from_json(json)
# print the JSON string representation of the object
print(SamlCredentials.to_json())

# convert the object into a dict
saml_credentials_dict = saml_credentials_instance.to_dict()
# create an instance of SamlCredentials from a dict
saml_credentials_from_dict = SamlCredentials.from_dict(saml_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


