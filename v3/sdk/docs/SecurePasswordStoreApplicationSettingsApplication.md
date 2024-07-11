# SecurePasswordStoreApplicationSettingsApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**optional_field1** | **str** |  | [optional] 
**optional_field1_value** | **str** |  | [optional] 
**optional_field2** | **str** |  | [optional] 
**optional_field2_value** | **str** |  | [optional] 
**optional_field3** | **str** |  | [optional] 
**optional_field3_value** | **str** |  | [optional] 
**password_field** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**username_field** | **str** |  | [optional] 

## Example

```python
from okta.models.secure_password_store_application_settings_application import SecurePasswordStoreApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of SecurePasswordStoreApplicationSettingsApplication from a JSON string
secure_password_store_application_settings_application_instance = SecurePasswordStoreApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(SecurePasswordStoreApplicationSettingsApplication.to_json())

# convert the object into a dict
secure_password_store_application_settings_application_dict = secure_password_store_application_settings_application_instance.to_dict()
# create an instance of SecurePasswordStoreApplicationSettingsApplication from a dict
secure_password_store_application_settings_application_from_dict = SecurePasswordStoreApplicationSettingsApplication.from_dict(secure_password_store_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


