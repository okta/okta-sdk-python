# PasswordSettingObject

Determines whether Okta creates and pushes a password in the app for each assigned user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change** | [**ChangeEnum**](ChangeEnum.md) |  | [optional] [default to ChangeEnum.KEEP_EXISTING]
**seed** | [**SeedEnum**](SeedEnum.md) |  | [optional] [default to SeedEnum.RANDOM]
**status** | [**EnabledStatus**](EnabledStatus.md) |  | [optional] 

## Example

```python
from okta.models.password_setting_object import PasswordSettingObject

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordSettingObject from a JSON string
password_setting_object_instance = PasswordSettingObject.from_json(json)
# print the JSON string representation of the object
print(PasswordSettingObject.to_json())

# convert the object into a dict
password_setting_object_dict = password_setting_object_instance.to_dict()
# create an instance of PasswordSettingObject from a dict
password_setting_object_from_dict = PasswordSettingObject.from_dict(password_setting_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


