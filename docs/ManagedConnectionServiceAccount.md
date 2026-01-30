# ManagedConnectionServiceAccount

Service account for the managed connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of the service account | 
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the service account | 
**links** | [**CustomAuthorizationServerLinks**](CustomAuthorizationServerLinks.md) |  | 

## Example

```python
from okta.models.managed_connection_service_account import ManagedConnectionServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedConnectionServiceAccount from a JSON string
managed_connection_service_account_instance = ManagedConnectionServiceAccount.from_json(json)
# print the JSON string representation of the object
print(ManagedConnectionServiceAccount.to_json())

# convert the object into a dict
managed_connection_service_account_dict = managed_connection_service_account_instance.to_dict()
# create an instance of ManagedConnectionServiceAccount from a dict
managed_connection_service_account_from_dict = ManagedConnectionServiceAccount.from_dict(managed_connection_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


