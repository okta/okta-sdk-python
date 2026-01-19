# SAMLPayLoadDataAssertionClaimsValueAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_format** | **str** | Indicates how to interpret the attribute name | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_claims_value_attributes import SAMLPayLoadDataAssertionClaimsValueAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionClaimsValueAttributes from a JSON string
saml_pay_load_data_assertion_claims_value_attributes_instance = SAMLPayLoadDataAssertionClaimsValueAttributes.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionClaimsValueAttributes.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_claims_value_attributes_dict = saml_pay_load_data_assertion_claims_value_attributes_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionClaimsValueAttributes from a dict
saml_pay_load_data_assertion_claims_value_attributes_from_dict = SAMLPayLoadDataAssertionClaimsValueAttributes.from_dict(saml_pay_load_data_assertion_claims_value_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


