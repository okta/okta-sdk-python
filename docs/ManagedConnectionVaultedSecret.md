# ManagedConnectionVaultedSecret

Secret for the managed connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional description of the secret | [optional] 
**name** | **str** | Display name of the secret | 
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the vaulted secret | 
**path** | **str** | Secret path in Okta Privileged Access (OPA) | [optional] 
**links** | [**CustomAuthorizationServerLinks**](CustomAuthorizationServerLinks.md) |  | 

## Example

```python
from okta.models.managed_connection_vaulted_secret import ManagedConnectionVaultedSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedConnectionVaultedSecret from a JSON string
managed_connection_vaulted_secret_instance = ManagedConnectionVaultedSecret.from_json(json)
# print the JSON string representation of the object
print(ManagedConnectionVaultedSecret.to_json())

# convert the object into a dict
managed_connection_vaulted_secret_dict = managed_connection_vaulted_secret_instance.to_dict()
# create an instance of ManagedConnectionVaultedSecret from a dict
managed_connection_vaulted_secret_from_dict = ManagedConnectionVaultedSecret.from_dict(managed_connection_vaulted_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


