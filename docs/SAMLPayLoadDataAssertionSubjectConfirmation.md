# SAMLPayLoadDataAssertionSubjectConfirmation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Used to indicate how the authorization server confirmed the SAML assertion | [optional] 
**data** | [**SAMLPayLoadDataAssertionSubjectConfirmationData**](SAMLPayLoadDataAssertionSubjectConfirmationData.md) |  | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_subject_confirmation import SAMLPayLoadDataAssertionSubjectConfirmation

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionSubjectConfirmation from a JSON string
saml_pay_load_data_assertion_subject_confirmation_instance = SAMLPayLoadDataAssertionSubjectConfirmation.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionSubjectConfirmation.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_subject_confirmation_dict = saml_pay_load_data_assertion_subject_confirmation_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionSubjectConfirmation from a dict
saml_pay_load_data_assertion_subject_confirmation_from_dict = SAMLPayLoadDataAssertionSubjectConfirmation.from_dict(saml_pay_load_data_assertion_subject_confirmation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


