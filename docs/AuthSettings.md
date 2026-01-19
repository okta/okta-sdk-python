# AuthSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | [**AuthType**](AuthType.md) |  | 
**custom_settings** | [**CustomAuthSettings**](CustomAuthSettings.md) |  | [optional] 
**o_auth2_settings** | [**OAuth2Settings**](OAuth2Settings.md) |  | [optional] 

## Example

```python
from okta.models.auth_settings import AuthSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AuthSettings from a JSON string
auth_settings_instance = AuthSettings.from_json(json)
# print the JSON string representation of the object
print(AuthSettings.to_json())

# convert the object into a dict
auth_settings_dict = auth_settings_instance.to_dict()
# create an instance of AuthSettings from a dict
auth_settings_from_dict = AuthSettings.from_dict(auth_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


