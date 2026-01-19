# SAMLPayLoadDataAssertionAuthentication

Provides a JSON representation of the `<saml:AuthnStatement>` element of the SAML assertion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_index** | **str** | The unique identifier describing the assertion statement | [optional] 
**authn_context** | [**SAMLPayLoadDataAssertionAuthenticationAuthnContext**](SAMLPayLoadDataAssertionAuthenticationAuthnContext.md) |  | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_authentication import SAMLPayLoadDataAssertionAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionAuthentication from a JSON string
saml_pay_load_data_assertion_authentication_instance = SAMLPayLoadDataAssertionAuthentication.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionAuthentication.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_authentication_dict = saml_pay_load_data_assertion_authentication_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionAuthentication from a dict
saml_pay_load_data_assertion_authentication_from_dict = SAMLPayLoadDataAssertionAuthentication.from_dict(saml_pay_load_data_assertion_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


