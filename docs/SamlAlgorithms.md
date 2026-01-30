# SamlAlgorithms

Settings for signing and verifying SAML messages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SamlRequestAlgorithm**](SamlRequestAlgorithm.md) |  | [optional] 
**response** | [**SamlResponseAlgorithm**](SamlResponseAlgorithm.md) |  | [optional] 

## Example

```python
from okta.models.saml_algorithms import SamlAlgorithms

# TODO update the JSON string below
json = "{}"
# create an instance of SamlAlgorithms from a JSON string
saml_algorithms_instance = SamlAlgorithms.from_json(json)
# print the JSON string representation of the object
print(SamlAlgorithms.to_json())

# convert the object into a dict
saml_algorithms_dict = saml_algorithms_instance.to_dict()
# create an instance of SamlAlgorithms from a dict
saml_algorithms_from_dict = SamlAlgorithms.from_dict(saml_algorithms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


