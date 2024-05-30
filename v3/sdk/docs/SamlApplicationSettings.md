# SamlApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_store_id** | **str** |  | [optional] 
**implicit_assignment** | **bool** |  | [optional] 
**inline_hook_id** | **str** |  | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 
**app** | [**SamlApplicationSettingsApplication**](SamlApplicationSettingsApplication.md) |  | [optional] 
**sign_on** | [**SamlApplicationSettingsSignOn**](SamlApplicationSettingsSignOn.md) |  | [optional] 

## Example

```python
from openapi_client.models.saml_application_settings import SamlApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SamlApplicationSettings from a JSON string
saml_application_settings_instance = SamlApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(SamlApplicationSettings.to_json())

# convert the object into a dict
saml_application_settings_dict = saml_application_settings_instance.to_dict()
# create an instance of SamlApplicationSettings from a dict
saml_application_settings_form_dict = saml_application_settings.from_dict(saml_application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


