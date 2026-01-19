# ManagedConnectionAppInstance

App instance for the managed connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | **str** | Image URL for the app logo | [optional] 
**name** | **str** | Display name of the app | 
**orn** | **str** | The [ORN](https://developer.okta.com/docs/api/openapi/okta-management/guides/roles/#okta-resource-name-orn) of the app instance | 
**links** | [**CustomAuthorizationServerLinks**](CustomAuthorizationServerLinks.md) |  | 

## Example

```python
from okta.models.managed_connection_app_instance import ManagedConnectionAppInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedConnectionAppInstance from a JSON string
managed_connection_app_instance_instance = ManagedConnectionAppInstance.from_json(json)
# print the JSON string representation of the object
print(ManagedConnectionAppInstance.to_json())

# convert the object into a dict
managed_connection_app_instance_dict = managed_connection_app_instance_instance.to_dict()
# create an instance of ManagedConnectionAppInstance from a dict
managed_connection_app_instance_from_dict = ManagedConnectionAppInstance.from_dict(managed_connection_app_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


