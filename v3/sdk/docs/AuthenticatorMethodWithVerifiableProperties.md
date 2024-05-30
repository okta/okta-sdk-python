# AuthenticatorMethodWithVerifiableProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verifiable_properties** | [**List[AuthenticatorMethodProperty]**](AuthenticatorMethodProperty.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticator_method_with_verifiable_properties import AuthenticatorMethodWithVerifiableProperties

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodWithVerifiableProperties from a JSON string
authenticator_method_with_verifiable_properties_instance = AuthenticatorMethodWithVerifiableProperties.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodWithVerifiableProperties.to_json())

# convert the object into a dict
authenticator_method_with_verifiable_properties_dict = authenticator_method_with_verifiable_properties_instance.to_dict()
# create an instance of AuthenticatorMethodWithVerifiableProperties from a dict
authenticator_method_with_verifiable_properties_form_dict = authenticator_method_with_verifiable_properties.from_dict(authenticator_method_with_verifiable_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


