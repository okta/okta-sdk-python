# AutoAssignAdminAppSetting

The org setting that automatically assigns the Okta Admin Console when an admin role is assigned

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_assign_admin_app_setting** | **bool** | Automatically assigns the Okta Admin Console to the user when an admin role is assigned | [optional] 

## Example

```python
from okta.models.auto_assign_admin_app_setting import AutoAssignAdminAppSetting

# TODO update the JSON string below
json = "{}"
# create an instance of AutoAssignAdminAppSetting from a JSON string
auto_assign_admin_app_setting_instance = AutoAssignAdminAppSetting.from_json(json)
# print the JSON string representation of the object
print(AutoAssignAdminAppSetting.to_json())

# convert the object into a dict
auto_assign_admin_app_setting_dict = auto_assign_admin_app_setting_instance.to_dict()
# create an instance of AutoAssignAdminAppSetting from a dict
auto_assign_admin_app_setting_from_dict = AutoAssignAdminAppSetting.from_dict(auto_assign_admin_app_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


