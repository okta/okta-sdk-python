# AuthenticatorKeyTacAllOfProviderConfiguration

Define the configuration settings of the TAC

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_ttl** | **float** | Minimum time-to-live (TTL) of the TAC in minutes. The &#x60;minTtl&#x60; indicates the minimum amount of time that a TAC is valid. The &#x60;minTtl&#x60; must be less than the &#x60;maxTtl&#x60;. | 
**max_ttl** | **float** | Maximum TTL of the TAC in minutes. The &#x60;maxTtl&#x60; indicates the maximum amount of time that a TAC is valid. The &#x60;maxTtl&#x60; must be greater than the &#x60;minTtl&#x60;. | 
**default_ttl** | **float** | The default TTL in minutes when you create a TAC. The &#x60;defaultTtl&#x60; indicates the actual amount of time that a TAC is valid before it expires. The &#x60;defaultTtl&#x60; must be greater than the &#x60;minTtl&#x60; and less than the &#x60;maxTtl&#x60;. | [default to 120]
**length** | **float** | Defines the number of characters in a TAC. For example, a &#x60;length&#x60; of &#x60;16&#x60; means that the TAC is 16 characters. | 
**complexity** | [**AuthenticatorKeyTacAllOfProviderConfigurationComplexity**](AuthenticatorKeyTacAllOfProviderConfigurationComplexity.md) |  | 
**multi_use_allowed** | **bool** | Indicates whether a TAC can be used multiple times. If set to &#x60;true&#x60;, the TAC can be used multiple times until it expires. | [optional] 

## Example

```python
from okta.models.authenticator_key_tac_all_of_provider_configuration import AuthenticatorKeyTacAllOfProviderConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyTacAllOfProviderConfiguration from a JSON string
authenticator_key_tac_all_of_provider_configuration_instance = AuthenticatorKeyTacAllOfProviderConfiguration.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyTacAllOfProviderConfiguration.to_json())

# convert the object into a dict
authenticator_key_tac_all_of_provider_configuration_dict = authenticator_key_tac_all_of_provider_configuration_instance.to_dict()
# create an instance of AuthenticatorKeyTacAllOfProviderConfiguration from a dict
authenticator_key_tac_all_of_provider_configuration_from_dict = AuthenticatorKeyTacAllOfProviderConfiguration.from_dict(authenticator_key_tac_all_of_provider_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


