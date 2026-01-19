# SAMLPayLoadDataAssertionSubjectConfirmationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **str** | The token endpoint URL of the authorization server | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_subject_confirmation_data import SAMLPayLoadDataAssertionSubjectConfirmationData

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionSubjectConfirmationData from a JSON string
saml_pay_load_data_assertion_subject_confirmation_data_instance = SAMLPayLoadDataAssertionSubjectConfirmationData.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionSubjectConfirmationData.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_subject_confirmation_data_dict = saml_pay_load_data_assertion_subject_confirmation_data_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionSubjectConfirmationData from a dict
saml_pay_load_data_assertion_subject_confirmation_data_from_dict = SAMLPayLoadDataAssertionSubjectConfirmationData.from_dict(saml_pay_load_data_assertion_subject_confirmation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


