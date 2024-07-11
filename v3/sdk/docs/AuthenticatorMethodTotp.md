# AuthenticatorMethodTotp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**AuthenticatorMethodTotpAllOfSettings**](AuthenticatorMethodTotpAllOfSettings.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_method_totp import AuthenticatorMethodTotp

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorMethodTotp from a JSON string
authenticator_method_totp_instance = AuthenticatorMethodTotp.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorMethodTotp.to_json())

# convert the object into a dict
authenticator_method_totp_dict = authenticator_method_totp_instance.to_dict()
# create an instance of AuthenticatorMethodTotp from a dict
authenticator_method_totp_from_dict = AuthenticatorMethodTotp.from_dict(authenticator_method_totp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


