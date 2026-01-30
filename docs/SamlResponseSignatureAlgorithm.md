# SamlResponseSignatureAlgorithm

XML digital Signature Algorithm settings for verifying `<SAMLResponse>` messages and `<Assertion>` elements from the IdP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**SamlSigningAlgorithm**](SamlSigningAlgorithm.md) |  | [optional] 
**scope** | [**ProtocolAlgorithmResponseScope**](ProtocolAlgorithmResponseScope.md) |  | [optional] 

## Example

```python
from okta.models.saml_response_signature_algorithm import SamlResponseSignatureAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of SamlResponseSignatureAlgorithm from a JSON string
saml_response_signature_algorithm_instance = SamlResponseSignatureAlgorithm.from_json(json)
# print the JSON string representation of the object
print(SamlResponseSignatureAlgorithm.to_json())

# convert the object into a dict
saml_response_signature_algorithm_dict = saml_response_signature_algorithm_instance.to_dict()
# create an instance of SamlResponseSignatureAlgorithm from a dict
saml_response_signature_algorithm_from_dict = SamlResponseSignatureAlgorithm.from_dict(saml_response_signature_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


