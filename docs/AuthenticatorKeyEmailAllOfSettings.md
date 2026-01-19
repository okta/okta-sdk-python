# AuthenticatorKeyEmailAllOfSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_for** | [**AllowedForEnum**](AllowedForEnum.md) |  | [optional] 
**token_lifetime_in_minutes** | **float** | Specifies the lifetime of an email token. Default value is 5 minutes. | [optional] [default to 5]

## Example

```python
from okta.models.authenticator_key_email_all_of_settings import AuthenticatorKeyEmailAllOfSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyEmailAllOfSettings from a JSON string
authenticator_key_email_all_of_settings_instance = AuthenticatorKeyEmailAllOfSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyEmailAllOfSettings.to_json())

# convert the object into a dict
authenticator_key_email_all_of_settings_dict = authenticator_key_email_all_of_settings_instance.to_dict()
# create an instance of AuthenticatorKeyEmailAllOfSettings from a dict
authenticator_key_email_all_of_settings_from_dict = AuthenticatorKeyEmailAllOfSettings.from_dict(authenticator_key_email_all_of_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


