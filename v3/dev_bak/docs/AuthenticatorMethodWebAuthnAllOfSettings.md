# AuthenticatorMethodWebAuthnAllOfSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) |  | [optional] 
**attachment** | [**WebAuthnAttachment**](WebAuthnAttachment.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticator_method_web_authn_all_of_settings import AuthenticatorMethodWebAuthnAllOfSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodWebAuthnAllOfSettings from a JSON string
authenticator_method_web_authn_all_of_settings_instance = AuthenticatorMethodWebAuthnAllOfSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodWebAuthnAllOfSettings.to_json())

# convert the object into a dict
authenticator_method_web_authn_all_of_settings_dict = authenticator_method_web_authn_all_of_settings_instance.to_dict()
# create an instance of AuthenticatorMethodWebAuthnAllOfSettings from a dict
authenticator_method_web_authn_all_of_settings_from_dict = AuthenticatorMethodWebAuthnAllOfSettings.from_dict(authenticator_method_web_authn_all_of_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


