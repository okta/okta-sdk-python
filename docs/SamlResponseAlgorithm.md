# SamlResponseAlgorithm

Algorithm settings for verifying `<SAMLResponse>` messages and `<Assertion>` elements from the IdP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | [**SamlResponseSignatureAlgorithm**](SamlResponseSignatureAlgorithm.md) |  | [optional] 

## Example

```python
from okta.models.saml_response_algorithm import SamlResponseAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of SamlResponseAlgorithm from a JSON string
saml_response_algorithm_instance = SamlResponseAlgorithm.from_json(json)
# print the JSON string representation of the object
print(SamlResponseAlgorithm.to_json())

# convert the object into a dict
saml_response_algorithm_dict = saml_response_algorithm_instance.to_dict()
# create an instance of SamlResponseAlgorithm from a dict
saml_response_algorithm_from_dict = SamlResponseAlgorithm.from_dict(saml_response_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


