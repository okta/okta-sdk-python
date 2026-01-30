# BasicApplicationSettingsApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_url** | **str** | The URL of the authenticating site for this app | 
**url** | **str** | The URL of the sign-in page for this app | 

## Example

```python
from okta.models.basic_application_settings_application import BasicApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of BasicApplicationSettingsApplication from a JSON string
basic_application_settings_application_instance = BasicApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(BasicApplicationSettingsApplication.to_json())

# convert the object into a dict
basic_application_settings_application_dict = basic_application_settings_application_instance.to_dict()
# create an instance of BasicApplicationSettingsApplication from a dict
basic_application_settings_application_from_dict = BasicApplicationSettingsApplication.from_dict(basic_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


