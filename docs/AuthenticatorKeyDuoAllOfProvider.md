# AuthenticatorKeyDuoAllOfProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Provider type | [optional] 
**configuration** | [**AuthenticatorKeyDuoAllOfProviderConfiguration**](AuthenticatorKeyDuoAllOfProviderConfiguration.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_duo_all_of_provider import AuthenticatorKeyDuoAllOfProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyDuoAllOfProvider from a JSON string
authenticator_key_duo_all_of_provider_instance = AuthenticatorKeyDuoAllOfProvider.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyDuoAllOfProvider.to_json())

# convert the object into a dict
authenticator_key_duo_all_of_provider_dict = authenticator_key_duo_all_of_provider_instance.to_dict()
# create an instance of AuthenticatorKeyDuoAllOfProvider from a dict
authenticator_key_duo_all_of_provider_from_dict = AuthenticatorKeyDuoAllOfProvider.from_dict(authenticator_key_duo_all_of_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


