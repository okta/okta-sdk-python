# AuthenticatorSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_for** | [**AllowedForEnum**](AllowedForEnum.md) |  | [optional] 
**app_instance_id** | **str** |  | [optional] 
**channel_binding** | [**ChannelBinding**](ChannelBinding.md) |  | [optional] 
**compliance** | [**Compliance**](Compliance.md) |  | [optional] 
**token_lifetime_in_minutes** | **int** |  | [optional] 
**user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_settings import AuthenticatorSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorSettings from a JSON string
authenticator_settings_instance = AuthenticatorSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorSettings.to_json())

# convert the object into a dict
authenticator_settings_dict = authenticator_settings_instance.to_dict()
# create an instance of AuthenticatorSettings from a dict
authenticator_settings_from_dict = AuthenticatorSettings.from_dict(authenticator_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


