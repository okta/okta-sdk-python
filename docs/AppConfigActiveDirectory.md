# AppConfigActiveDirectory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinguished_name** | **str** | The distinguished name of the group in Active Directory | 
**group_scope** | [**ActiveDirectoryGroupScope**](ActiveDirectoryGroupScope.md) |  | 
**group_type** | [**ActiveDirectoryGroupType**](ActiveDirectoryGroupType.md) |  | 
**sam_account_name** | **str** | The SAM account name of the group in Active Directory | 

## Example

```python
from okta.models.app_config_active_directory import AppConfigActiveDirectory

# TODO update the JSON string below
json = "{}"
# create an instance of AppConfigActiveDirectory from a JSON string
app_config_active_directory_instance = AppConfigActiveDirectory.from_json(json)
# print the JSON string representation of the object
print(AppConfigActiveDirectory.to_json())

# convert the object into a dict
app_config_active_directory_dict = app_config_active_directory_instance.to_dict()
# create an instance of AppConfigActiveDirectory from a dict
app_config_active_directory_from_dict = AppConfigActiveDirectory.from_dict(app_config_active_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


