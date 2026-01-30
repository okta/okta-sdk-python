# ScimScimServerConfig

SCIM server schema configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch** | [**ScimScimServerConfigPatch**](ScimScimServerConfigPatch.md) |  | [optional] 
**change_password** | [**ScimScimServerConfigChangePassword**](ScimScimServerConfigChangePassword.md) |  | [optional] 

## Example

```python
from okta.models.scim_scim_server_config import ScimScimServerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ScimScimServerConfig from a JSON string
scim_scim_server_config_instance = ScimScimServerConfig.from_json(json)
# print the JSON string representation of the object
print(ScimScimServerConfig.to_json())

# convert the object into a dict
scim_scim_server_config_dict = scim_scim_server_config_instance.to_dict()
# create an instance of ScimScimServerConfig from a dict
scim_scim_server_config_from_dict = ScimScimServerConfig.from_dict(scim_scim_server_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


