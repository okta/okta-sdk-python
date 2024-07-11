# SamlApplicationSettingsApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_url** | **str** |  | [optional] 
**aud_restriction** | **str** |  | [optional] 
**base_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.saml_application_settings_application import SamlApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of SamlApplicationSettingsApplication from a JSON string
saml_application_settings_application_instance = SamlApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(SamlApplicationSettingsApplication.to_json())

# convert the object into a dict
saml_application_settings_application_dict = saml_application_settings_application_instance.to_dict()
# create an instance of SamlApplicationSettingsApplication from a dict
saml_application_settings_application_from_dict = SamlApplicationSettingsApplication.from_dict(saml_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


