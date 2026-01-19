# CapabilitiesImportSettingsObject

Defines import settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**ImportScheduleObject**](ImportScheduleObject.md) |  | [optional] 
**username** | [**ImportUsernameObject**](ImportUsernameObject.md) |  | [optional] 

## Example

```python
from okta.models.capabilities_import_settings_object import CapabilitiesImportSettingsObject

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesImportSettingsObject from a JSON string
capabilities_import_settings_object_instance = CapabilitiesImportSettingsObject.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesImportSettingsObject.to_json())

# convert the object into a dict
capabilities_import_settings_object_dict = capabilities_import_settings_object_instance.to_dict()
# create an instance of CapabilitiesImportSettingsObject from a dict
capabilities_import_settings_object_from_dict = CapabilitiesImportSettingsObject.from_dict(capabilities_import_settings_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


