# ClientPrivilegesSetting

The org setting that assigns the super admin role by default to a public client app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_privileges_setting** | **bool** | If true, assigns the super admin role by default to new public client apps | [optional] 

## Example

```python
from okta.models.client_privileges_setting import ClientPrivilegesSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPrivilegesSetting from a JSON string
client_privileges_setting_instance = ClientPrivilegesSetting.from_json(json)
# print the JSON string representation of the object
print(ClientPrivilegesSetting.to_json())

# convert the object into a dict
client_privileges_setting_dict = client_privileges_setting_instance.to_dict()
# create an instance of ClientPrivilegesSetting from a dict
client_privileges_setting_from_dict = ClientPrivilegesSetting.from_dict(client_privileges_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


