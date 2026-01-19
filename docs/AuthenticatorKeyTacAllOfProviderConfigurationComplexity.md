# AuthenticatorKeyTacAllOfProviderConfigurationComplexity

Define the complexity of the TAC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numbers** | **bool** | Use numbers in the TAC. &#x60;numbers&#x60; is always &#x60;true&#x60; for the TAC authenticator. | [optional] 
**letters** | **bool** | Use letters in the TAC | [optional] 
**special_characters** | **bool** | Use special characters in the TAC | [optional] 

## Example

```python
from okta.models.authenticator_key_tac_all_of_provider_configuration_complexity import AuthenticatorKeyTacAllOfProviderConfigurationComplexity

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyTacAllOfProviderConfigurationComplexity from a JSON string
authenticator_key_tac_all_of_provider_configuration_complexity_instance = AuthenticatorKeyTacAllOfProviderConfigurationComplexity.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyTacAllOfProviderConfigurationComplexity.to_json())

# convert the object into a dict
authenticator_key_tac_all_of_provider_configuration_complexity_dict = authenticator_key_tac_all_of_provider_configuration_complexity_instance.to_dict()
# create an instance of AuthenticatorKeyTacAllOfProviderConfigurationComplexity from a dict
authenticator_key_tac_all_of_provider_configuration_complexity_from_dict = AuthenticatorKeyTacAllOfProviderConfigurationComplexity.from_dict(authenticator_key_tac_all_of_provider_configuration_complexity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


