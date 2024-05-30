# AuthenticatorProviderConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_port** | **int** |  | [optional] 
**host_name** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**shared_secret** | **str** |  | [optional] 
**user_name_template** | [**AuthenticatorProviderConfigurationUserNameTemplate**](AuthenticatorProviderConfigurationUserNameTemplate.md) |  | [optional] 

## Example

```python
from openapi_client.models.authenticator_provider_configuration import AuthenticatorProviderConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorProviderConfiguration from a JSON string
authenticator_provider_configuration_instance = AuthenticatorProviderConfiguration.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorProviderConfiguration.to_json())

# convert the object into a dict
authenticator_provider_configuration_dict = authenticator_provider_configuration_instance.to_dict()
# create an instance of AuthenticatorProviderConfiguration from a dict
authenticator_provider_configuration_form_dict = authenticator_provider_configuration.from_dict(authenticator_provider_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


