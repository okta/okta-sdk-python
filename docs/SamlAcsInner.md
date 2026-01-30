# SamlAcsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** | Index of ACS URL. You can&#39;t reuse the same index in the ACS URL array. | [optional] 
**url** | **str** | Assertion Consumer Service (ACS) URL | [optional] 

## Example

```python
from okta.models.saml_acs_inner import SamlAcsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SamlAcsInner from a JSON string
saml_acs_inner_instance = SamlAcsInner.from_json(json)
# print the JSON string representation of the object
print(SamlAcsInner.to_json())

# convert the object into a dict
saml_acs_inner_dict = saml_acs_inner_instance.to_dict()
# create an instance of SamlAcsInner from a dict
saml_acs_inner_from_dict = SamlAcsInner.from_dict(saml_acs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


