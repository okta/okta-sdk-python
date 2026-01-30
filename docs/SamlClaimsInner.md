# SamlClaimsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The attribute name | [optional] 
**values** | **List[str]** | The Okta values inserted in the attribute statement | [optional] 

## Example

```python
from okta.models.saml_claims_inner import SamlClaimsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SamlClaimsInner from a JSON string
saml_claims_inner_instance = SamlClaimsInner.from_json(json)
# print the JSON string representation of the object
print(SamlClaimsInner.to_json())

# convert the object into a dict
saml_claims_inner_dict = saml_claims_inner_instance.to_dict()
# create an instance of SamlClaimsInner from a dict
saml_claims_inner_from_dict = SamlClaimsInner.from_dict(saml_claims_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


