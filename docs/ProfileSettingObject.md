# ProfileSettingObject

This setting determines whether a user in the application gets updated when they're updated in Okta.  If enabled, Okta updates a user's attributes in the application when the application is assigned. Future changes made to the Okta user's profile automatically overwrite the corresponding attribute value in the application. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**EnabledStatus**](EnabledStatus.md) |  | [optional] 

## Example

```python
from okta.models.profile_setting_object import ProfileSettingObject

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSettingObject from a JSON string
profile_setting_object_instance = ProfileSettingObject.from_json(json)
# print the JSON string representation of the object
print(ProfileSettingObject.to_json())

# convert the object into a dict
profile_setting_object_dict = profile_setting_object_instance.to_dict()
# create an instance of ProfileSettingObject from a dict
profile_setting_object_from_dict = ProfileSettingObject.from_dict(profile_setting_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


