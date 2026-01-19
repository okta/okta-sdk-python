# SamlSigningCredentials

Key used for signing requests to the IdP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | IdP key credential reference to the Okta X.509 signature certificate | [optional] 

## Example

```python
from okta.models.saml_signing_credentials import SamlSigningCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SamlSigningCredentials from a JSON string
saml_signing_credentials_instance = SamlSigningCredentials.from_json(json)
# print the JSON string representation of the object
print(SamlSigningCredentials.to_json())

# convert the object into a dict
saml_signing_credentials_dict = saml_signing_credentials_instance.to_dict()
# create an instance of SamlSigningCredentials from a dict
saml_signing_credentials_from_dict = SamlSigningCredentials.from_dict(saml_signing_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


