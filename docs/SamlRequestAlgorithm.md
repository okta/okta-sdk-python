# SamlRequestAlgorithm

Algorithm settings used to secure an `<AuthnRequest>` message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | [**SamlRequestSignatureAlgorithm**](SamlRequestSignatureAlgorithm.md) |  | [optional] 

## Example

```python
from okta.models.saml_request_algorithm import SamlRequestAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of SamlRequestAlgorithm from a JSON string
saml_request_algorithm_instance = SamlRequestAlgorithm.from_json(json)
# print the JSON string representation of the object
print(SamlRequestAlgorithm.to_json())

# convert the object into a dict
saml_request_algorithm_dict = saml_request_algorithm_instance.to_dict()
# create an instance of SamlRequestAlgorithm from a dict
saml_request_algorithm_from_dict = SamlRequestAlgorithm.from_dict(saml_request_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


