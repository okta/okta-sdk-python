# SAMLPayLoadDataAssertionClaimsValueAttributeValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SAMLPayLoadDataAssertionClaimsValueAttributeValuesInnerAttributes**](SAMLPayLoadDataAssertionClaimsValueAttributeValuesInnerAttributes.md) |  | [optional] 
**value** | **str** | The actual value of the attribute | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_claims_value_attribute_values_inner import SAMLPayLoadDataAssertionClaimsValueAttributeValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionClaimsValueAttributeValuesInner from a JSON string
saml_pay_load_data_assertion_claims_value_attribute_values_inner_instance = SAMLPayLoadDataAssertionClaimsValueAttributeValuesInner.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionClaimsValueAttributeValuesInner.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_claims_value_attribute_values_inner_dict = saml_pay_load_data_assertion_claims_value_attribute_values_inner_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionClaimsValueAttributeValuesInner from a dict
saml_pay_load_data_assertion_claims_value_attribute_values_inner_from_dict = SAMLPayLoadDataAssertionClaimsValueAttributeValuesInner.from_dict(saml_pay_load_data_assertion_claims_value_attribute_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


