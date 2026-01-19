# ApplicationVisibilityHide

Hides the app for specific end-user apps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_os** | **bool** | Okta Mobile for iOS or Android (pre-dates Android) | [optional] [default to False]
**web** | **bool** | Okta End-User Dashboard on a web browser | [optional] [default to False]

## Example

```python
from okta.models.application_visibility_hide import ApplicationVisibilityHide

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationVisibilityHide from a JSON string
application_visibility_hide_instance = ApplicationVisibilityHide.from_json(json)
# print the JSON string representation of the object
print(ApplicationVisibilityHide.to_json())

# convert the object into a dict
application_visibility_hide_dict = application_visibility_hide_instance.to_dict()
# create an instance of ApplicationVisibilityHide from a dict
application_visibility_hide_from_dict = ApplicationVisibilityHide.from_dict(application_visibility_hide_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


