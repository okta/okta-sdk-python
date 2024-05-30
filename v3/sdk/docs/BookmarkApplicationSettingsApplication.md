# BookmarkApplicationSettingsApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_integration** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bookmark_application_settings_application import BookmarkApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkApplicationSettingsApplication from a JSON string
bookmark_application_settings_application_instance = BookmarkApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(BookmarkApplicationSettingsApplication.to_json())

# convert the object into a dict
bookmark_application_settings_application_dict = bookmark_application_settings_application_instance.to_dict()
# create an instance of BookmarkApplicationSettingsApplication from a dict
bookmark_application_settings_application_form_dict = bookmark_application_settings_application.from_dict(bookmark_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


