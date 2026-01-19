# SAMLPayLoadDataAssertionSubject

Provides a JSON representation of the `<saml:Subject>` element of the SAML assertion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_id** | **str** | The unique identifier of the user | [optional] 
**name_format** | **str** | Indicates how to interpret the attribute name | [optional] 
**confirmation** | [**SAMLPayLoadDataAssertionSubjectConfirmation**](SAMLPayLoadDataAssertionSubjectConfirmation.md) |  | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_subject import SAMLPayLoadDataAssertionSubject

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionSubject from a JSON string
saml_pay_load_data_assertion_subject_instance = SAMLPayLoadDataAssertionSubject.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionSubject.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_subject_dict = saml_pay_load_data_assertion_subject_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionSubject from a dict
saml_pay_load_data_assertion_subject_from_dict = SAMLPayLoadDataAssertionSubject.from_dict(saml_pay_load_data_assertion_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


