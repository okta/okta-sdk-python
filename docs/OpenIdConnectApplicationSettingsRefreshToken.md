# OpenIdConnectApplicationSettingsRefreshToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leeway** | **int** |  | [optional] 
**rotation_type** | [**OpenIdConnectRefreshTokenRotationType**](OpenIdConnectRefreshTokenRotationType.md) |  | [optional] 

## Example

```python
from okta.models.open_id_connect_application_settings_refresh_token import OpenIdConnectApplicationSettingsRefreshToken

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectApplicationSettingsRefreshToken from a JSON string
open_id_connect_application_settings_refresh_token_instance = OpenIdConnectApplicationSettingsRefreshToken.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectApplicationSettingsRefreshToken.to_json())

# convert the object into a dict
open_id_connect_application_settings_refresh_token_dict = open_id_connect_application_settings_refresh_token_instance.to_dict()
# create an instance of OpenIdConnectApplicationSettingsRefreshToken from a dict
open_id_connect_application_settings_refresh_token_from_dict = OpenIdConnectApplicationSettingsRefreshToken.from_dict(open_id_connect_application_settings_refresh_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


