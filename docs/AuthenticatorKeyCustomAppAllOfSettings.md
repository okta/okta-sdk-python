# AuthenticatorKeyCustomAppAllOfSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_verification** | [**CustomAppUserVerificationEnum**](CustomAppUserVerificationEnum.md) |  | [optional] 
**app_instance_id** | **str** | The application instance ID. For custom_app, you need to create an OIDC native app using the [Apps API](https://developer.okta.com/docs/reference/api/apps/) with &#x60;Authorization Code&#x60; and &#x60;Refresh Token&#x60; grant types. You can leave both &#x60;Sign-in redirect URIs&#x60; and &#x60;Sign-out redirect URIs&#x60; as the default values. | [optional] 

## Example

```python
from okta.models.authenticator_key_custom_app_all_of_settings import AuthenticatorKeyCustomAppAllOfSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyCustomAppAllOfSettings from a JSON string
authenticator_key_custom_app_all_of_settings_instance = AuthenticatorKeyCustomAppAllOfSettings.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyCustomAppAllOfSettings.to_json())

# convert the object into a dict
authenticator_key_custom_app_all_of_settings_dict = authenticator_key_custom_app_all_of_settings_instance.to_dict()
# create an instance of AuthenticatorKeyCustomAppAllOfSettings from a dict
authenticator_key_custom_app_all_of_settings_from_dict = AuthenticatorKeyCustomAppAllOfSettings.from_dict(authenticator_key_custom_app_all_of_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


