# SamlRequestSignatureAlgorithm

XML digital Signature Algorithm settings for signing `<AuthnRequest>` messages sent to the IdP > **Note:**  The `algorithm` property is ignored when you disable request signatures (`scope` set as `NONE`).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**SamlSigningAlgorithm**](SamlSigningAlgorithm.md) |  | [optional] 
**scope** | [**ProtocolAlgorithmRequestScope**](ProtocolAlgorithmRequestScope.md) |  | [optional] 

## Example

```python
from okta.models.saml_request_signature_algorithm import SamlRequestSignatureAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of SamlRequestSignatureAlgorithm from a JSON string
saml_request_signature_algorithm_instance = SamlRequestSignatureAlgorithm.from_json(json)
# print the JSON string representation of the object
print(SamlRequestSignatureAlgorithm.to_json())

# convert the object into a dict
saml_request_signature_algorithm_dict = saml_request_signature_algorithm_instance.to_dict()
# create an instance of SamlRequestSignatureAlgorithm from a dict
saml_request_signature_algorithm_from_dict = SamlRequestSignatureAlgorithm.from_dict(saml_request_signature_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


