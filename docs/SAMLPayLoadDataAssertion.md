# SAMLPayLoadDataAssertion

Details of the SAML assertion that was generated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**SAMLPayLoadDataAssertionSubject**](SAMLPayLoadDataAssertionSubject.md) |  | [optional] 
**authentication** | [**SAMLPayLoadDataAssertionAuthentication**](SAMLPayLoadDataAssertionAuthentication.md) |  | [optional] 
**conditions** | [**SAMLPayLoadDataAssertionConditions**](SAMLPayLoadDataAssertionConditions.md) |  | [optional] 
**claims** | [**Dict[str, SAMLPayLoadDataAssertionClaimsValue]**](SAMLPayLoadDataAssertionClaimsValue.md) | Provides a JSON representation of the &#x60;&lt;saml:AttributeStatement&gt;&#x60; element contained in the generated SAML assertion. Contains any optional SAML attribute statements that you have defined for the app using the Admin Console&#39;s **SAML Settings**. | [optional] 
**lifetime** | [**SAMLPayLoadDataAssertionLifetime**](SAMLPayLoadDataAssertionLifetime.md) |  | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion import SAMLPayLoadDataAssertion

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertion from a JSON string
saml_pay_load_data_assertion_instance = SAMLPayLoadDataAssertion.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertion.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_dict = saml_pay_load_data_assertion_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertion from a dict
saml_pay_load_data_assertion_from_dict = SAMLPayLoadDataAssertion.from_dict(saml_pay_load_data_assertion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


