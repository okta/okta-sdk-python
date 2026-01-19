# AuthenticatorKeyCustomAppAllOfProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Provider type | [optional] 
**configuration** | [**AuthenticatorKeyCustomAppAllOfProviderConfiguration**](AuthenticatorKeyCustomAppAllOfProviderConfiguration.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_custom_app_all_of_provider import AuthenticatorKeyCustomAppAllOfProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyCustomAppAllOfProvider from a JSON string
authenticator_key_custom_app_all_of_provider_instance = AuthenticatorKeyCustomAppAllOfProvider.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyCustomAppAllOfProvider.to_json())

# convert the object into a dict
authenticator_key_custom_app_all_of_provider_dict = authenticator_key_custom_app_all_of_provider_instance.to_dict()
# create an instance of AuthenticatorKeyCustomAppAllOfProvider from a dict
authenticator_key_custom_app_all_of_provider_from_dict = AuthenticatorKeyCustomAppAllOfProvider.from_dict(authenticator_key_custom_app_all_of_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


