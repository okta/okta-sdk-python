# Office365ProvisioningSettings

Settings required for the Microsoft Office 365 provisioning connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_password** | **str** | Microsoft Office 365 global administrator password | 
**admin_username** | **str** | Microsoft Office 365 global administrator username | 

## Example

```python
from okta.models.office365_provisioning_settings import Office365ProvisioningSettings

# TODO update the JSON string below
json = "{}"
# create an instance of Office365ProvisioningSettings from a JSON string
office365_provisioning_settings_instance = Office365ProvisioningSettings.from_json(json)
# print the JSON string representation of the object
print(Office365ProvisioningSettings.to_json())

# convert the object into a dict
office365_provisioning_settings_dict = office365_provisioning_settings_instance.to_dict()
# create an instance of Office365ProvisioningSettings from a dict
office365_provisioning_settings_from_dict = Office365ProvisioningSettings.from_dict(office365_provisioning_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


