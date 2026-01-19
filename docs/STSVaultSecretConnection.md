# STSVaultSecretConnection

STS connection to a vaulted secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | Type of connection authentication method | 
**id** | **str** | Unique identifier for the managed connection. Only present for managed connections. | [optional] 
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the managed connection | [optional] 
**protocol_type** | **str** | The authentication protocol type used for the connection | [optional] 
**resource_indicator** | **str** | Resource indicator used when requesting tokens. | 
**secret** | [**ManagedConnectionVaultedSecret**](ManagedConnectionVaultedSecret.md) |  | 
**status** | [**ManagedConnectionStatus**](ManagedConnectionStatus.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.sts_vault_secret_connection import STSVaultSecretConnection

# TODO update the JSON string below
json = "{}"
# create an instance of STSVaultSecretConnection from a JSON string
sts_vault_secret_connection_instance = STSVaultSecretConnection.from_json(json)
# print the JSON string representation of the object
print(STSVaultSecretConnection.to_json())

# convert the object into a dict
sts_vault_secret_connection_dict = sts_vault_secret_connection_instance.to_dict()
# create an instance of STSVaultSecretConnection from a dict
sts_vault_secret_connection_from_dict = STSVaultSecretConnection.from_dict(sts_vault_secret_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


