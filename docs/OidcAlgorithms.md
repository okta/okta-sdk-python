# OidcAlgorithms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**OidcRequestAlgorithm**](OidcRequestAlgorithm.md) |  | [optional] 

## Example

```python
from okta.models.oidc_algorithms import OidcAlgorithms

# TODO update the JSON string below
json = "{}"
# create an instance of OidcAlgorithms from a JSON string
oidc_algorithms_instance = OidcAlgorithms.from_json(json)
# print the JSON string representation of the object
print(OidcAlgorithms.to_json())

# convert the object into a dict
oidc_algorithms_dict = oidc_algorithms_instance.to_dict()
# create an instance of OidcAlgorithms from a dict
oidc_algorithms_from_dict = OidcAlgorithms.from_dict(oidc_algorithms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


