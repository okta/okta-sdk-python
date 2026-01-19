# SamlAssertionEncryption

Determines if the app supports encrypted assertions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates whether Okta encrypts the assertions that it sends to the Service Provider | [optional] 
**encryption_algorithm** | **str** | The encryption algorithm used to encrypt the SAML assertion | [optional] 
**key_transport_algorithm** | **str** | The key transport algorithm used to encrypt the SAML assertion | [optional] 
**x5c** | **List[str]** | A list that contains exactly one x509 encoded certificate which Okta uses to encrypt the SAML assertion with | [optional] 

## Example

```python
from okta.models.saml_assertion_encryption import SamlAssertionEncryption

# TODO update the JSON string below
json = "{}"
# create an instance of SamlAssertionEncryption from a JSON string
saml_assertion_encryption_instance = SamlAssertionEncryption.from_json(json)
# print the JSON string representation of the object
print(SamlAssertionEncryption.to_json())

# convert the object into a dict
saml_assertion_encryption_dict = saml_assertion_encryption_instance.to_dict()
# create an instance of SamlAssertionEncryption from a dict
saml_assertion_encryption_from_dict = SamlAssertionEncryption.from_dict(saml_assertion_encryption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


