# ApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_store_id** | **str** |  | [optional] 
**implicit_assignment** | **bool** |  | [optional] 
**inline_hook_id** | **str** |  | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_settings import ApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSettings from a JSON string
application_settings_instance = ApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(ApplicationSettings.to_json())

# convert the object into a dict
application_settings_dict = application_settings_instance.to_dict()
# create an instance of ApplicationSettings from a dict
application_settings_form_dict = application_settings.from_dict(application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


