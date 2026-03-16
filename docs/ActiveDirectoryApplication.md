# ActiveDirectoryApplication

Active Directory application for directory integrations. This application type has a null signOnMode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique key for the Active Directory app definition. Always &#39;active_directory&#39; for AD apps. | [optional] [readonly] 
**settings** | [**ActiveDirectoryApplicationSettings**](ActiveDirectoryApplicationSettings.md) |  | [optional] 

## Example

```python
from okta.models.active_directory_application import ActiveDirectoryApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryApplication from a JSON string
active_directory_application_instance = ActiveDirectoryApplication.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryApplication.to_json())

# convert the object into a dict
active_directory_application_dict = active_directory_application_instance.to_dict()
# create an instance of ActiveDirectoryApplication from a dict
active_directory_application_from_dict = ActiveDirectoryApplication.from_dict(active_directory_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


