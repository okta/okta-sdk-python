# SAMLPayLoadDataAssertionClaimsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SAMLPayLoadDataAssertionClaimsValueAttributes**](SAMLPayLoadDataAssertionClaimsValueAttributes.md) |  | [optional] 
**attribute_values** | [**List[SAMLPayLoadDataAssertionClaimsValueAttributeValuesInner]**](SAMLPayLoadDataAssertionClaimsValueAttributeValuesInner.md) |  | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_claims_value import SAMLPayLoadDataAssertionClaimsValue

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionClaimsValue from a JSON string
saml_pay_load_data_assertion_claims_value_instance = SAMLPayLoadDataAssertionClaimsValue.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionClaimsValue.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_claims_value_dict = saml_pay_load_data_assertion_claims_value_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionClaimsValue from a dict
saml_pay_load_data_assertion_claims_value_from_dict = SAMLPayLoadDataAssertionClaimsValue.from_dict(saml_pay_load_data_assertion_claims_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


