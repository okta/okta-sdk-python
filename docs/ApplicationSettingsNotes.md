# ApplicationSettingsNotes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **str** |  | [optional] 
**enduser** | **str** |  | [optional] 

## Example

```python
from okta.models.application_settings_notes import ApplicationSettingsNotes

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSettingsNotes from a JSON string
application_settings_notes_instance = ApplicationSettingsNotes.from_json(json)
# print the JSON string representation of the object
print(ApplicationSettingsNotes.to_json())

# convert the object into a dict
application_settings_notes_dict = application_settings_notes_instance.to_dict()
# create an instance of ApplicationSettingsNotes from a dict
application_settings_notes_from_dict = ApplicationSettingsNotes.from_dict(application_settings_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


