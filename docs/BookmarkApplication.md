# BookmarkApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ApplicationCredentials**](ApplicationCredentials.md) |  | [optional] 
**name** | **str** | &#x60;bookmark&#x60; is the key name for a Bookmark app | 
**settings** | [**BookmarkApplicationSettings**](BookmarkApplicationSettings.md) |  | 

## Example

```python
from okta.models.bookmark_application import BookmarkApplication

# TODO update the JSON string below
json = "{}"
# create an instance of BookmarkApplication from a JSON string
bookmark_application_instance = BookmarkApplication.from_json(json)
# print the JSON string representation of the object
print(BookmarkApplication.to_json())

# convert the object into a dict
bookmark_application_dict = bookmark_application_instance.to_dict()
# create an instance of BookmarkApplication from a dict
bookmark_application_from_dict = BookmarkApplication.from_dict(bookmark_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


