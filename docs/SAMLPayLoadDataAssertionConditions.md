# SAMLPayLoadDataAssertionConditions

Provides a JSON representation of the `<saml:Conditions>` element of the SAML assertion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_restriction** | **List[str]** | Describes which service providers the assertion is valid for | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_conditions import SAMLPayLoadDataAssertionConditions

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionConditions from a JSON string
saml_pay_load_data_assertion_conditions_instance = SAMLPayLoadDataAssertionConditions.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionConditions.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_conditions_dict = saml_pay_load_data_assertion_conditions_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionConditions from a dict
saml_pay_load_data_assertion_conditions_from_dict = SAMLPayLoadDataAssertionConditions.from_dict(saml_pay_load_data_assertion_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


