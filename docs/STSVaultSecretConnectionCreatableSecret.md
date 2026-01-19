# STSVaultSecretConnectionCreatableSecret

Reference to a vaulted secret in [ORN](/openapi/okta-management/guides/roles/#okta-resource-name-orn) format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the vaulted secret | 

## Example

```python
from okta.models.sts_vault_secret_connection_creatable_secret import STSVaultSecretConnectionCreatableSecret

# TODO update the JSON string below
json = "{}"
# create an instance of STSVaultSecretConnectionCreatableSecret from a JSON string
sts_vault_secret_connection_creatable_secret_instance = STSVaultSecretConnectionCreatableSecret.from_json(json)
# print the JSON string representation of the object
print(STSVaultSecretConnectionCreatableSecret.to_json())

# convert the object into a dict
sts_vault_secret_connection_creatable_secret_dict = sts_vault_secret_connection_creatable_secret_instance.to_dict()
# create an instance of STSVaultSecretConnectionCreatableSecret from a dict
sts_vault_secret_connection_creatable_secret_from_dict = STSVaultSecretConnectionCreatableSecret.from_dict(sts_vault_secret_connection_creatable_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


