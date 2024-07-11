# OpenIdConnectApplicationSettingsClientKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[JsonWebKey]**](JsonWebKey.md) |  | [optional] 

## Example

```python
from openapi_client.models.open_id_connect_application_settings_client_keys import OpenIdConnectApplicationSettingsClientKeys

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIdConnectApplicationSettingsClientKeys from a JSON string
open_id_connect_application_settings_client_keys_instance = OpenIdConnectApplicationSettingsClientKeys.from_json(json)
# print the JSON string representation of the object
print(OpenIdConnectApplicationSettingsClientKeys.to_json())

# convert the object into a dict
open_id_connect_application_settings_client_keys_dict = open_id_connect_application_settings_client_keys_instance.to_dict()
# create an instance of OpenIdConnectApplicationSettingsClientKeys from a dict
open_id_connect_application_settings_client_keys_from_dict = OpenIdConnectApplicationSettingsClientKeys.from_dict(open_id_connect_application_settings_client_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


