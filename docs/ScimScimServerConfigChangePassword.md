# ScimScimServerConfigChangePassword

Password change options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | Specifies if password change is supported | [optional] [default to False]

## Example

```python
from okta.models.scim_scim_server_config_change_password import ScimScimServerConfigChangePassword

# TODO update the JSON string below
json = "{}"
# create an instance of ScimScimServerConfigChangePassword from a JSON string
scim_scim_server_config_change_password_instance = ScimScimServerConfigChangePassword.from_json(json)
# print the JSON string representation of the object
print(ScimScimServerConfigChangePassword.to_json())

# convert the object into a dict
scim_scim_server_config_change_password_dict = scim_scim_server_config_change_password_instance.to_dict()
# create an instance of ScimScimServerConfigChangePassword from a dict
scim_scim_server_config_change_password_from_dict = ScimScimServerConfigChangePassword.from_dict(scim_scim_server_config_change_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


