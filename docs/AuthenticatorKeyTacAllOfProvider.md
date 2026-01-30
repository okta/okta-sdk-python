# AuthenticatorKeyTacAllOfProvider

<x-lifecycle-container><x-lifecycle class=\"oie\"></x-lifecycle></x-lifecycle-container>Settings for the TAC authenticator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Provider type | [optional] 
**configuration** | [**AuthenticatorKeyTacAllOfProviderConfiguration**](AuthenticatorKeyTacAllOfProviderConfiguration.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_tac_all_of_provider import AuthenticatorKeyTacAllOfProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyTacAllOfProvider from a JSON string
authenticator_key_tac_all_of_provider_instance = AuthenticatorKeyTacAllOfProvider.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyTacAllOfProvider.to_json())

# convert the object into a dict
authenticator_key_tac_all_of_provider_dict = authenticator_key_tac_all_of_provider_instance.to_dict()
# create an instance of AuthenticatorKeyTacAllOfProvider from a dict
authenticator_key_tac_all_of_provider_from_dict = AuthenticatorKeyTacAllOfProvider.from_dict(authenticator_key_tac_all_of_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


