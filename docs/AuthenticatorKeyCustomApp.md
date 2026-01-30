# AuthenticatorKeyCustomApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agree_to_terms** | **bool** | A value of &#x60;true&#x60; indicates that the administrator accepts the [terms](https://www.okta.com/privacy-policy/) for creating a new authenticator. Okta requires that you accept the terms when creating a new &#x60;custom_app&#x60; authenticator. Other authenticators don&#39;t require this field. | [optional] 
**provider** | [**AuthenticatorKeyCustomAppAllOfProvider**](AuthenticatorKeyCustomAppAllOfProvider.md) |  | [optional] 
**settings** | [**AuthenticatorKeyCustomAppAllOfSettings**](AuthenticatorKeyCustomAppAllOfSettings.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_custom_app import AuthenticatorKeyCustomApp

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyCustomApp from a JSON string
authenticator_key_custom_app_instance = AuthenticatorKeyCustomApp.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyCustomApp.to_json())

# convert the object into a dict
authenticator_key_custom_app_dict = authenticator_key_custom_app_instance.to_dict()
# create an instance of AuthenticatorKeyCustomApp from a dict
authenticator_key_custom_app_from_dict = AuthenticatorKeyCustomApp.from_dict(authenticator_key_custom_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


