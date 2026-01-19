# AuthenticatorKeyPhone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**AuthenticatorKeyPhoneAllOfSettings**](AuthenticatorKeyPhoneAllOfSettings.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_phone import AuthenticatorKeyPhone

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyPhone from a JSON string
authenticator_key_phone_instance = AuthenticatorKeyPhone.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyPhone.to_json())

# convert the object into a dict
authenticator_key_phone_dict = authenticator_key_phone_instance.to_dict()
# create an instance of AuthenticatorKeyPhone from a dict
authenticator_key_phone_from_dict = AuthenticatorKeyPhone.from_dict(authenticator_key_phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


