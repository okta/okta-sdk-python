# AuthenticatorKeyPhoneAllOfSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_for** | [**AllowedForEnum**](AllowedForEnum.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_phone_all_of_settings import AuthenticatorKeyPhoneAllOfSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyPhoneAllOfSettings from a JSON string
authenticator_key_phone_all_of_settings_instance = AuthenticatorKeyPhoneAllOfSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyPhoneAllOfSettings.to_json())

# convert the object into a dict
authenticator_key_phone_all_of_settings_dict = authenticator_key_phone_all_of_settings_instance.to_dict()
# create an instance of AuthenticatorKeyPhoneAllOfSettings from a dict
authenticator_key_phone_all_of_settings_from_dict = AuthenticatorKeyPhoneAllOfSettings.from_dict(authenticator_key_phone_all_of_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


