# AuthenticatorMethodWebAuthn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**AuthenticatorMethodWebAuthnAllOfSettings**](AuthenticatorMethodWebAuthnAllOfSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticator_method_web_authn import AuthenticatorMethodWebAuthn

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodWebAuthn from a JSON string
authenticator_method_web_authn_instance = AuthenticatorMethodWebAuthn.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodWebAuthn.to_json())

# convert the object into a dict
authenticator_method_web_authn_dict = authenticator_method_web_authn_instance.to_dict()
# create an instance of AuthenticatorMethodWebAuthn from a dict
authenticator_method_web_authn_from_dict = AuthenticatorMethodWebAuthn.from_dict(authenticator_method_web_authn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


