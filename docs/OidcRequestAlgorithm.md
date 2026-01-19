# OidcRequestAlgorithm

Algorithm settings used to sign an authorization request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | [**OidcRequestSignatureAlgorithm**](OidcRequestSignatureAlgorithm.md) |  | [optional] 

## Example

```python
from okta.models.oidc_request_algorithm import OidcRequestAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of OidcRequestAlgorithm from a JSON string
oidc_request_algorithm_instance = OidcRequestAlgorithm.from_json(json)
# print the JSON string representation of the object
print(OidcRequestAlgorithm.to_json())

# convert the object into a dict
oidc_request_algorithm_dict = oidc_request_algorithm_instance.to_dict()
# create an instance of OidcRequestAlgorithm from a dict
oidc_request_algorithm_from_dict = OidcRequestAlgorithm.from_dict(oidc_request_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


