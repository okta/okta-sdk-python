# SecurePasswordStoreApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_store_id** | **str** |  | [optional] 
**implicit_assignment** | **bool** |  | [optional] 
**inline_hook_id** | **str** |  | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 
**app** | [**SecurePasswordStoreApplicationSettingsApplication**](SecurePasswordStoreApplicationSettingsApplication.md) |  | [optional] 

## Example

```python
from openapi_client.models.secure_password_store_application_settings import SecurePasswordStoreApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SecurePasswordStoreApplicationSettings from a JSON string
secure_password_store_application_settings_instance = SecurePasswordStoreApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(SecurePasswordStoreApplicationSettings.to_json())

# convert the object into a dict
secure_password_store_application_settings_dict = secure_password_store_application_settings_instance.to_dict()
# create an instance of SecurePasswordStoreApplicationSettings from a dict
secure_password_store_application_settings_from_dict = SecurePasswordStoreApplicationSettings.from_dict(secure_password_store_application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


