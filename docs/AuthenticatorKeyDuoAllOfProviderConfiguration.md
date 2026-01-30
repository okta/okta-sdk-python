# AuthenticatorKeyDuoAllOfProviderConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The Duo Security API hostname | [optional] 
**integration_key** | **str** | The Duo Security integration key | [optional] 
**secret_key** | **str** | The Duo Security secret key | [optional] 
**user_name_template** | [**AuthenticatorKeyDuoAllOfProviderConfigurationUserNameTemplate**](AuthenticatorKeyDuoAllOfProviderConfigurationUserNameTemplate.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_key_duo_all_of_provider_configuration import AuthenticatorKeyDuoAllOfProviderConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyDuoAllOfProviderConfiguration from a JSON string
authenticator_key_duo_all_of_provider_configuration_instance = AuthenticatorKeyDuoAllOfProviderConfiguration.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyDuoAllOfProviderConfiguration.to_json())

# convert the object into a dict
authenticator_key_duo_all_of_provider_configuration_dict = authenticator_key_duo_all_of_provider_configuration_instance.to_dict()
# create an instance of AuthenticatorKeyDuoAllOfProviderConfiguration from a dict
authenticator_key_duo_all_of_provider_configuration_from_dict = AuthenticatorKeyDuoAllOfProviderConfiguration.from_dict(authenticator_key_duo_all_of_provider_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


