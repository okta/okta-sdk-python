# Office365ApplicationSettingsApplication

Office365 app instance properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain for your Office 365 account | 
**msft_tenant** | **str** | Microsoft tenant name | 

## Example

```python
from okta.models.office365_application_settings_application import Office365ApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of Office365ApplicationSettingsApplication from a JSON string
office365_application_settings_application_instance = Office365ApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(Office365ApplicationSettingsApplication.to_json())

# convert the object into a dict
office365_application_settings_application_dict = office365_application_settings_application_instance.to_dict()
# create an instance of Office365ApplicationSettingsApplication from a dict
office365_application_settings_application_from_dict = Office365ApplicationSettingsApplication.from_dict(office365_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


