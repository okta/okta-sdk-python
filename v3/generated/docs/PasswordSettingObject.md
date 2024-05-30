# PasswordSettingObject

Determines whether Okta creates and pushes a password in the application for each assigned user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change** | [**ChangeEnum**](ChangeEnum.md) |  | [optional] 
**seed** | [**SeedEnum**](SeedEnum.md) |  | [optional] 
**status** | [**EnabledStatus**](EnabledStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.password_setting_object import PasswordSettingObject

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordSettingObject from a JSON string
password_setting_object_instance = PasswordSettingObject.from_json(json)
# print the JSON string representation of the object
print(PasswordSettingObject.to_json())

# convert the object into a dict
password_setting_object_dict = password_setting_object_instance.to_dict()
# create an instance of PasswordSettingObject from a dict
password_setting_object_form_dict = password_setting_object.from_dict(password_setting_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


