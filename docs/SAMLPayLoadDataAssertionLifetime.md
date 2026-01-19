# SAMLPayLoadDataAssertionLifetime

Specifies the expiration time, in seconds, of the SAML assertion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration** | **int** | The expiration time in seconds | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_lifetime import SAMLPayLoadDataAssertionLifetime

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionLifetime from a JSON string
saml_pay_load_data_assertion_lifetime_instance = SAMLPayLoadDataAssertionLifetime.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionLifetime.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_lifetime_dict = saml_pay_load_data_assertion_lifetime_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionLifetime from a dict
saml_pay_load_data_assertion_lifetime_from_dict = SAMLPayLoadDataAssertionLifetime.from_dict(saml_pay_load_data_assertion_lifetime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


