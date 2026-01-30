# GoogleApplicationSettingsApplication

Google app instance properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Your Google company domain | 
**rp_id** | **str** | RPID | [optional] 

## Example

```python
from okta.models.google_application_settings_application import GoogleApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleApplicationSettingsApplication from a JSON string
google_application_settings_application_instance = GoogleApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(GoogleApplicationSettingsApplication.to_json())

# convert the object into a dict
google_application_settings_application_dict = google_application_settings_application_instance.to_dict()
# create an instance of GoogleApplicationSettingsApplication from a dict
google_application_settings_application_from_dict = GoogleApplicationSettingsApplication.from_dict(google_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


