# AuthenticatorKeyOktaVerifyAllOfSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_binding** | [**ChannelBinding**](ChannelBinding.md) |  | [optional] 
**compliance** | [**Compliance**](Compliance.md) |  | [optional] 
**user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) |  | [optional] 
**app_instance_id** | **str** | The application instance ID | [optional] 

## Example

```python
from okta.models.authenticator_key_okta_verify_all_of_settings import AuthenticatorKeyOktaVerifyAllOfSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyOktaVerifyAllOfSettings from a JSON string
authenticator_key_okta_verify_all_of_settings_instance = AuthenticatorKeyOktaVerifyAllOfSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyOktaVerifyAllOfSettings.to_json())

# convert the object into a dict
authenticator_key_okta_verify_all_of_settings_dict = authenticator_key_okta_verify_all_of_settings_instance.to_dict()
# create an instance of AuthenticatorKeyOktaVerifyAllOfSettings from a dict
authenticator_key_okta_verify_all_of_settings_from_dict = AuthenticatorKeyOktaVerifyAllOfSettings.from_dict(authenticator_key_okta_verify_all_of_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


