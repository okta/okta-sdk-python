# STSVaultSecretConnectionCreatable

Create an STS connection for a vaulted secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | Type of connection authentication method | 
**protocol_type** | **str** | The authentication protocol type used for the connection | [optional] 
**resource_indicator** | **str** | Resource indicator used when requesting tokens. Defaults to the vaulted secret&#39;s ORN if not specified. | [optional] 
**secret** | [**STSVaultSecretConnectionCreatableSecret**](STSVaultSecretConnectionCreatableSecret.md) |  | 

## Example

```python
from okta.models.sts_vault_secret_connection_creatable import STSVaultSecretConnectionCreatable

# TODO update the JSON string below
json = "{}"
# create an instance of STSVaultSecretConnectionCreatable from a JSON string
sts_vault_secret_connection_creatable_instance = STSVaultSecretConnectionCreatable.from_json(json)
# print the JSON string representation of the object
print(STSVaultSecretConnectionCreatable.to_json())

# convert the object into a dict
sts_vault_secret_connection_creatable_dict = sts_vault_secret_connection_creatable_instance.to_dict()
# create an instance of STSVaultSecretConnectionCreatable from a dict
sts_vault_secret_connection_creatable_from_dict = STSVaultSecretConnectionCreatable.from_dict(sts_vault_secret_connection_creatable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


