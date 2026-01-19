# AuthenticatorKeyDuoAllOfProviderConfigurationUserNameTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** | The Duo Security user template name | [optional] 

## Example

```python
from okta.models.authenticator_key_duo_all_of_provider_configuration_user_name_template import AuthenticatorKeyDuoAllOfProviderConfigurationUserNameTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorKeyDuoAllOfProviderConfigurationUserNameTemplate from a JSON string
authenticator_key_duo_all_of_provider_configuration_user_name_template_instance = AuthenticatorKeyDuoAllOfProviderConfigurationUserNameTemplate.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorKeyDuoAllOfProviderConfigurationUserNameTemplate.to_json())

# convert the object into a dict
authenticator_key_duo_all_of_provider_configuration_user_name_template_dict = authenticator_key_duo_all_of_provider_configuration_user_name_template_instance.to_dict()
# create an instance of AuthenticatorKeyDuoAllOfProviderConfigurationUserNameTemplate from a dict
authenticator_key_duo_all_of_provider_configuration_user_name_template_from_dict = AuthenticatorKeyDuoAllOfProviderConfigurationUserNameTemplate.from_dict(authenticator_key_duo_all_of_provider_configuration_user_name_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


