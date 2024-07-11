# BookmarkApplicationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_store_id** | **str** |  | [optional] 
**implicit_assignment** | **bool** |  | [optional] 
**inline_hook_id** | **str** |  | [optional] 
**notes** | [**ApplicationSettingsNotes**](ApplicationSettingsNotes.md) |  | [optional] 
**notifications** | [**ApplicationSettingsNotifications**](ApplicationSettingsNotifications.md) |  | [optional] 
**app** | [**BookmarkApplicationSettingsApplication**](BookmarkApplicationSettingsApplication.md) |  | [optional] 

## Example

```python
from okta.models.bookmark_application_settings import BookmarkApplicationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkApplicationSettings from a JSON string
bookmark_application_settings_instance = BookmarkApplicationSettings.from_json(json)
# print the JSON string representation of the object
print(BookmarkApplicationSettings.to_json())

# convert the object into a dict
bookmark_application_settings_dict = bookmark_application_settings_instance.to_dict()
# create an instance of BookmarkApplicationSettings from a dict
bookmark_application_settings_from_dict = BookmarkApplicationSettings.from_dict(bookmark_application_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


