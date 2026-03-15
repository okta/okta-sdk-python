# ActiveDirectoryApplicationSettingsApplication

App-specific settings for Active Directory applications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_email** | **str** | Email address to send activation emails | [optional] 
**filter_groups_by_ou** | **bool** | Whether to filter groups by organizational unit | [optional] 
**jit_groups_across_domains** | **bool** | Whether to enable just-in-time provisioning of groups across domains | [optional] 
**login** | **str** | Login username for AD connection | [optional] 
**naming_context** | **str** | The AD domain naming context (e.g., &#39;corp.local&#39;) | [optional] 
**password** | **str** | Password for AD connection | [optional] 
**scan_rate** | **int** | Rate at which to scan the AD directory | [optional] 
**search_org_unit** | **str** | Organizational unit to search within | [optional] 

## Example

```python
from okta.models.active_directory_application_settings_application import ActiveDirectoryApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryApplicationSettingsApplication from a JSON string
active_directory_application_settings_application_instance = ActiveDirectoryApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryApplicationSettingsApplication.to_json())

# convert the object into a dict
active_directory_application_settings_application_dict = active_directory_application_settings_application_instance.to_dict()
# create an instance of ActiveDirectoryApplicationSettingsApplication from a dict
active_directory_application_settings_application_from_dict = ActiveDirectoryApplicationSettingsApplication.from_dict(active_directory_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


