# SAMLPayLoadDataAssertionAuthenticationAuthnContext

Details of the authentication methods used for the SAML assertion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authn_context_class_ref** | **str** | Describes the identity provider&#39;s supported authentication context classes | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_assertion_authentication_authn_context import SAMLPayLoadDataAssertionAuthenticationAuthnContext

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataAssertionAuthenticationAuthnContext from a JSON string
saml_pay_load_data_assertion_authentication_authn_context_instance = SAMLPayLoadDataAssertionAuthenticationAuthnContext.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataAssertionAuthenticationAuthnContext.to_json())

# convert the object into a dict
saml_pay_load_data_assertion_authentication_authn_context_dict = saml_pay_load_data_assertion_authentication_authn_context_instance.to_dict()
# create an instance of SAMLPayLoadDataAssertionAuthenticationAuthnContext from a dict
saml_pay_load_data_assertion_authentication_authn_context_from_dict = SAMLPayLoadDataAssertionAuthenticationAuthnContext.from_dict(saml_pay_load_data_assertion_authentication_authn_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


